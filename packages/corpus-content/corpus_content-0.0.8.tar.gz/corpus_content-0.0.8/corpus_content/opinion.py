from typing import NamedTuple

from citation_utils import CountedCitation  # type: ignore
from statute_utils import CountedStatute  # type: ignore

from .utils import Annex, Block


class Opinion(NamedTuple):
    """Whether the opinion is the main opinion of the decision
    or a separate one, it will contain common fields and associated
    records based on the content.
    """

    id: str
    decision_id: str
    content: str
    justice_id: int | None = None
    is_main: bool = True
    label: str = "Opinion"
    file_statutes: str | None = None
    file_citations: str | None = None

    def __repr__(self) -> str:
        return f"<Opinion {self.id}>"

    @property
    def row(self):
        return {"opinion_id": self.id, "decision_id": self.decision_id}

    @property
    def index(self):
        return Annex.detect_initial_footnote(self.content)

    @property
    def body(self) -> str:
        return self.content[: self.index] if self.index else self.content

    @property
    def annex(self) -> str | None:
        return self.content[self.index :] if self.index else None

    @property
    def blocks(self) -> list[Block]:
        return list(Block(body=self.body).blocks)

    @property
    def headings(self):
        res = []
        for blk in self.blocks:
            if blk.title:
                data = {}
                data["id"] = f"{self.id}-{blk.material_path}"
                data |= blk._asdict()
                data |= self.row
                data["category"] = data.pop("inherited_category")
                data.pop("body")
                res.append(data)
        return res

    @property
    def segments(self):
        res = []
        for blk in self.blocks:
            for chunk in blk.chunks:
                data = {}
                data["id"] = f"{self.id}-{chunk.material_path}"
                data |= self.row
                data |= chunk.as_row
                res.append(data)
        return res

    @property
    def statutes(self):
        res = []
        if self.file_statutes:
            objs = CountedStatute.from_repr_format(self.file_statutes.split("; "))
            for obj in objs:
                data = {"cat": obj.cat, "num": obj.num, "mentions": obj.mentions}
                data |= self.row
                res.append(data)
        return res

    @property
    def citations(self):
        res = []
        if self.file_citations:
            objs = CountedCitation.from_repr_format(self.file_citations.split("; "))
            for obj in objs:
                data = obj.model_dump()
                data |= self.row
                res.append(data)
        return res
