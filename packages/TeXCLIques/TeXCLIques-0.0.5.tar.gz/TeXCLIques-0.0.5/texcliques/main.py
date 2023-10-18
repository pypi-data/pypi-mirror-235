from __future__ import annotations

import argparse
from collections.abc import Sequence

import texcliques.constants as C
from texcliques.commands.extract_citations import extract_citations


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=C.DESCRIPTION, formatter_class=argparse.RawTextHelpFormatter
    )

    # https://stackoverflow.com/a/8521644/812183
    parser.add_argument(
        '-V', '--version', action='version',
        version=f"{C.COLORS['subtle']}%(prog)s {C.VERSION}{C.COLORS['normal']}",
    )

    def add_cmd(name: str, *, help: str) -> argparse.ArgumentParser:
        parser = subparsers.add_parser(name, help=help)
        return parser

    subparsers = parser.add_subparsers(dest='command')

    # 'extract-citations' command
    extract_citations_parser = add_cmd(
        'extract-citations',
        help="Extract the citations from a LaTeX file \n"
        "and save them in various formats. You can specify:\n"
        " - a --section to extract the citations from\n"
        " - the --fields that you want to extrct from the citations.\n"
        " - the output --formats."
    )
    extract_citations_parser.add_argument(
        'file',
        metavar='TEXFILE',
        help='The LaTeX file to extract citations from.'
    )
    extract_citations_parser.add_argument(
        'bib',
        metavar='BIBFILE',
        help='The BibTeX file to extract citations from.'
    )
    extract_citations_parser.add_argument(
        '-s', '--section',
        metavar='SECTION',
        help='The section to extract citations from.'
    )
    extract_citations_parser.add_argument(
        '-p', '--pattern',
        metavar='PATTERN',
        default=r'\\cite[tp]?{([^}]+)}',
        help='The pattern to use for identifying citations in the LaTeX file. '
        'The pattern must contain a single capturing group that matches the '
        'reference ID. Defaults to: `%(default)s`.'
    )
    extract_citations_parser.add_argument(
        '--sort',
        action='store_true',
        help='Sort the citations in natural order based on their key.'
    )
    extract_citations_parser.add_argument(
        '-o', '--output',
        metavar='OUTPUT',
        default='citations',
        help='The base name of the output files.'
    )
    extract_citations_parser.add_argument(
        '--fields',
        metavar='FIELDS',
        nargs='+',
        default=['id', 'title', 'author'],
        help='The fields to extract from the BibTeX file.'
    )
    extract_citations_parser.add_argument(
        '--formats',
        metavar='FORMATS',
        nargs='+',
        default=['toml', 'yaml', 'json'],
        help='The output formats to save the citations into. '
        'Supported formats: `toml`, `yaml`, `json`.'
    )

    args = parser.parse_args(argv)

    if args.command == 'extract-citations':
        return extract_citations(args)
    else:
        raise NotImplementedError(f"Command '{args.command}' not implemented.")


if __name__ == '__main__':
    raise SystemExit(main())
