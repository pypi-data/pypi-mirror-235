from __future__ import annotations

import argparse
import json
import pathlib
import re
from collections.abc import Sequence

import bibtexparser  # type: ignore
import toml  # type: ignore
import yaml  # type: ignore

from texcliques import color


def extract_citations_from_bib(bib: str) -> Sequence[dict[str, str]]:
    with open(bib, encoding='utf-8') as f:
        bib_database = bibtexparser.load(f)
    return bib_database.entries


def extract_citations_from_tex(
    tex: str,
    section_title: str | None,
    id_pattern: re.Pattern
) -> set[str] | None:
    """Extract citations from a LaTeX file."""
    with open(tex, encoding='utf-8') as f:
        content = f.read()

    if section_title is not None:
        # Assuming the section is clearly defined like this:
        # \section{<Specified section>}
        # [...]
        # \section{Another section}
        section = re.search(
            fr'\\section{{{section_title}}}(.*?)\\section',
            content, flags=re.I | re.DOTALL | re.M
        )

        if section:
            section_content = section.group(1)
            cits = re.findall(id_pattern, section_content)
        else:
            color.step('SKIP', start=f"Section {section_title!r} not in {tex}.",
                       color='turquoise')
            return None
    else:
        cits = re.findall(id_pattern, content)

    if cits:
        cits_split = [cit.split(',') for cit in cits]
        cits_unique = {cit for cits in cits_split for cit in cits}
        return cits_unique
    else:
        return set()


def clean_bibtex_fields(
    bib_ref: dict[str, str],
    fields: Sequence[str]
) -> dict[str, str]:
    """Remove unnecessary characters from BibTeX fields."""
    cleaned_fields = {}
    for field in fields:
        if field in bib_ref:
            cleaned_field = bib_ref[field]
            cleaned_field = re.sub(r'\\.', '', cleaned_field)
            cleaned_field = re.sub(r'[{}]', '', cleaned_field)
            cleaned_field = re.sub(r'\s+', ' ', cleaned_field)
            cleaned_fields[field] = cleaned_field
    return cleaned_fields


def save_output(
    all_citations: Sequence[dict[str, str]],
    *,
    output: str,
    formats: Sequence[str],
    fields: Sequence[str],
    sort: bool = False
) -> None:
    """Save the output in the specified formats.
    If `toml` is specified and `sort` is `True`, the citations will be sorted in
    natural order based on their key."""

    for format in formats:
        if format not in ('toml', 'yaml', 'yml', 'json'):
            color.step('SKIP', start=f"Unsupported format {format!r}",
                       color='yellow')
            continue
        else:
            cleaned_cits = {}
            for bib_entry in all_citations:
                cleaned_fields = clean_bibtex_fields(bib_entry, fields)
                cleaned_cits[bib_entry['ID']] = cleaned_fields

        if format == 'json':
            with open(f'{output}.json', 'w', encoding='utf-8') as json_file:
                json.dump(cleaned_cits, json_file,
                          indent=4, ensure_ascii=False, sort_keys=sort)
        elif format in ('yaml', 'yml'):
            with open(f'{output}.{format}', 'w', encoding='utf-8') as yaml_file:
                yaml.dump(cleaned_cits, yaml_file,
                          allow_unicode=True, line_break='\n\n', sort_keys=sort)
        elif format == 'toml':
            with open(f'{output}.toml', 'w', encoding='utf-8') as toml_file:
                # sort is not supported by toml, so we naturally sort them
                if sort:
                    sorted_cits = sorted(
                        cleaned_cits,
                        key=lambda x: [int(c) if c.isdigit() else c
                                       for c in re.split(r'(\d+)', x)]
                    )
                    toml.dump(sorted_cits, toml_file)
                else:
                    toml.dump(cleaned_cits, toml_file)


def extract_citations(args: argparse.Namespace) -> int:

    file = args.file
    section_title = args.section
    pattern = re.compile(args.pattern)
    bib = args.bib
    sort = args.sort
    output = args.output
    fields = args.fields
    formats = args.formats

    for arg in (file, bib):
        if not pathlib.Path(arg).exists() or not pathlib.Path(arg).is_file():
            print(f"'{arg}' does not exist (or is not a file).")
            return 1

    if not pathlib.Path(file).suffix == '.tex':
        print(f"'{file}' is not a LaTeX file.")
        return 1

    if not pathlib.Path(bib).suffix == '.bib':
        print(f"'{bib}' is not a BibTeX file.")
        return 1

    citations = extract_citations_from_tex(file, section_title, pattern)

    if citations:
        suffix = 's' if len(citations) > 1 else ''
        ending = f'in {section_title}' if section_title else f'in {file}'
        msg = f'Found {len(citations)} reference{suffix} {ending}'
        color.step('Done', start=msg, color='green')

        all_citations = []
        bib_citations = extract_citations_from_bib(bib)

        for bib_entry in bib_citations:
            if bib_entry['ID'] in citations:
                all_citations.append(bib_entry)

        save_output(all_citations,
                    output=output, formats=formats, fields=fields, sort=sort)

        return 0

    elif citations == set():
        color.step('Done', start='No citations found', color='green')
        return 0
    else:
        color.step('Error', start='Could not find any citations', color='red')
        return 1
