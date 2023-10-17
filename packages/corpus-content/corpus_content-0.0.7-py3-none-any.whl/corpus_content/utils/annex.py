import re
from collections.abc import Iterator
from typing import NamedTuple, Self

NOTE_INDICATOR = re.compile(r"\n(?=\[\^[\w-]+\]:)", re.M)


class Footnote(NamedTuple):
    reference: str
    value: str

    @property
    def pointer(self):
        return f"[^{self.reference}]: "

    @property
    def as_markdown(self):
        """Each footnote's multiline value (after the first line)
        should begin with an additional four spaces for proper
        indention.
        """
        texts = self.value.split("\n")
        for idx, line in enumerate(texts):
            if line and idx != 0:  # line = not blank, != after first line
                texts[idx] = f"    {line}"  # 4 spaces = tab
        return self.pointer + "\n".join(texts)

    @classmethod
    def from_marker(cls, text: str):
        """Does the text start with a marker? If yes, extract
        the parts of a footnote so that multi-line processing
        can be done."""
        if match := re.search(r"(^\[\^(?P<marker>[\w-]+)\]:)", text):
            return cls(
                reference=match.group("marker"),
                value=text.removeprefix(match.group()).strip(),
            )

    @classmethod
    def gather(cls, text: str) -> Iterator[Self]:
        """Given annex text, generate a list of Footnote instances"""
        from .formatter import sp_at_start

        start_text = sp_at_start.sub("\n\n", text)
        notes = NOTE_INDICATOR.split(start_text)
        for note in notes:
            if matched := cls.from_marker(text=note):
                yield matched


class Annex(NamedTuple):
    footnotes: list[Footnote]

    @classmethod
    def detect_initial_footnote(cls, text: str, start: int = 1):
        try:
            return text.index(f"[^{start}]:")
        except ValueError:
            return None

    @property
    def as_markdown(self):
        return "\n\n".join([f.as_markdown for f in self.footnotes])


def clean_annex(text: str):
    detect = Annex.detect_initial_footnote
    index = detect(text, start=1) or detect(text, start=2)
    if not index:
        return text

    body = text[:index]
    raw_annex = text[index:].removesuffix("---")
    formatted_annex = Annex(footnotes=list(Footnote.gather(raw_annex))).as_markdown
    return body + formatted_annex + "\n"
