# corpus-content

![Github CI](https://github.com/justmars/corpus-content/actions/workflows/main.yml/badge.svg)

Using opinion text from frontmatter-formatted markdown files, chunk the same into segments and itemize Philippine statutes, citations within the text.

```py
from corpus_content import Decision

file = next(Path().home().joinpath("corpus-decisions").glob("gr/**/2023*/main*"))
metadata = Decision.from_file(file)
meta.main_opinion.segments
meta.separate_opinions
```

## Hierarchy

1. `Decision` - at least consisting of a single main opinion with optional separate opinions
   1. `Writer`- a justice who may pen an opinion (anonymoys _per curiam_ opinions are marked as such)
   2. `Voteline` - how the other justices voted in a decision re: each opinion
   3. `Opinion` - authored by a writer, can consist of a _body_ (with or without an _annex_)
      1. `Body` - content of the opinion
         1. `Block` - a body division based on a natural or commented header in the body
            1. `Chunk` - an algorithmic division of a block
      2. `Annex` - if the body contains footnotes, the annex is the reference area of an opinion containing the value of footnotes; it can can be subdivided into the area of each footnote
         1. `Footnote`

Based on block-chunk setups, it may be possible to use FTS only on `ruling` `issue` `preface` `fallo` chunks as searchable segments that can also have embeddings.

## Todo

1. `^\*+[^\*]{1,60}(?!\*)\n` detect short strings that ought to be converted into headings
2. The `formatter()` needs to exclude indented enumerations in removing pre-line spaces

## Limitations

### Blocks

At present blocks only include headers. It might be useful to introduce html comments `<!-- Example -->` as a means of adding metadata within markdown content

- [x] Heading includes footnote

      ## Regional Trial Court[^1]

- [ ] Heading may be prefixed by a Roman Numeral, Number, and/or Letter

      ## I. Facts

- [ ] Heading includes parenthesis

      ## Regional Trial Court (Sample Text)

### Chunks

1. Blocks can only create proper chunks if the block is formatted properly
2. For instance if an ` xxx ` is in between blockquotes and not preceded by a `>` indicator, this will result in multiple chunks rather than a single one.

    >

    xxx xxx xxx

    > As we outlined above, **a temporary total disability only becomes permanent when so declared by the company physician within the periods he is allowed to do so, or upon the expiration of the maximum 240-day medical treatment period without a declaration of either fitness

