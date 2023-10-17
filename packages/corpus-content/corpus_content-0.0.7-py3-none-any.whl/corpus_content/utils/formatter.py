import re
from collections.abc import Iterator
from pathlib import Path

import frontmatter

from .annex import clean_annex
from .dumper import SafeDumper
from .fallo import add_fallo_comment
from .phrase import Phrase

xao = re.compile(r"\xa0")

xad = re.compile(r"\xad")

sp_at_start = re.compile(r"^\s+(?=.*)", re.M)
"""New line starting with at least one space."""

sp_empty_bq = re.compile(r"(?<=^>)\n{2}(?=>)")
"""Blockquote terminating with double line breaks and followed by another blockquote"""

start_bq = re.compile(r"\n{2}(>\n){2}", re.M)
"""Blockquotes that start with double line breaks and followed by double blockquotes"""

end_bq = re.compile(r"(\n[>\s]+){2}\n{2}", re.M)
"""Blockquotes that terminate with double blockquotes and double line breaks"""

lone_bq = re.compile(r"\n{2}[>\s]+\n{2}", re.M)
"""Blockquotes that appear as a lone symbol, surrounded by double link breaks"""


x_placeholder = r"\s*[x][\sx]+\n{2}"
xxx = "x x x"
xxx_bq_ideal = " " + xxx + "\n"
xxx_bq1 = re.compile(rf"(?<=^>){x_placeholder}", re.M)
xxx_bq2 = re.compile(rf"(?<=^>\s>){x_placeholder}", re.M)
xxx_bq3 = re.compile(rf"(?<=^>\s>\s>){x_placeholder}", re.M)


phrases = Phrase.generate_regex_unnamed()


def clean_headings(text: str):
    for phrase in re.finditer(rf"\*+(?P<heading>{phrases}):?\*+\s+", text):
        matched_text = phrase.group()
        if heading := phrase.group("heading"):
            text = text.replace(matched_text, f"\n## {heading}\n\n")
    return text


candidate = re.compile(
    r"""^\*+ # starts with open asterisk
    \s* # optional space
    (?P<candidate>
        [\w\s:,'\-\–\.\(\)\*;\/\"&%\^’]{15,65} # first line, must contain at least 15 characters
        (
            \n # can be an empty line
            ([\w\s:,'\-\–\.\(\)\*;\/\"&%\^’]{5,65})? # non-empty line may contain shorter string (5)
        )+ # subsequent lines
        \?? # may end with a question mark
    )
    \*+ # ends with closing asterisk
    (\.?)? # ending punctuation can follow asterisk
    (\[\^\d+\])? # footnote can follow asterisk
    \n{2} # terminates in two new lines
    """,  # noqa: E501
    re.M | re.X,
)


def clean_candidates(text: str):
    for phrase in candidate.finditer(text):
        matched_text = phrase.group()
        if heading := phrase.group("candidate"):
            revised = re.sub(r"\n+", " ", heading).strip("* ")
            text = text.replace(matched_text, f"\n### {revised}\n\n")
    return text


def formatter(text: str, is_main: bool = False):
    text = text.replace("`", "'h")
    text = xao.sub(" ", text)
    text = xad.sub("", text)
    text = sp_at_start.sub("\n", text)
    text = xxx_bq1.sub(xxx_bq_ideal, text)
    text = xxx_bq2.sub(xxx_bq_ideal, text)
    text = xxx_bq3.sub(xxx_bq_ideal, text)
    text = start_bq.sub("\n\n", text)
    text = end_bq.sub("\n\n", text)
    text = lone_bq.sub("\n\n", text)
    text = sp_empty_bq.sub("\n", text)
    text = clean_headings(text)
    text = clean_candidates(text)
    if is_main:
        text = add_fallo_comment(text)
    text = clean_annex(text)
    return text


possibles = re.compile(
    r"""
    \n
    ^\*+
    (?P<possible>.+)
    \*+$\n
    """,
    re.X | re.M,
)


def is_ok_endnote_format(text: str) -> str | None:
    for i in [1, 2]:
        base = rf"\[\^{i}\]"
        if len(re.findall(rf"{base}", text)) == 2:
            if re.search(rf"^{base}:", text, flags=re.M):
                return str(i)
    return None


def detect_possibles(text: str) -> list[str]:
    texts = []
    for matched in possibles.finditer(text):
        text = matched.group("possible").strip("* ")
        evaluated = text.lower()
        if "so ordered" in evaluated:
            continue
        if evaluated.startswith("wherefore"):
            continue
        texts.append(text)

    return texts


def update_content(file: Path) -> list[str]:
    is_main = "main" in file.stem
    meta = frontmatter.load(file)
    content = formatter(text=meta.content, is_main=is_main)
    post = frontmatter.Post(content, **meta.metadata)
    frontmatter.dump(post=post, fd=file, Dumper=SafeDumper)
    return detect_possibles(post.content)
