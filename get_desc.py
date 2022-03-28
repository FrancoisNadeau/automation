#!/usr/bin/env python3

from argparse import ArgumentParser
from docstring_parser import parse as ds_parse

def get_desc(function_name: str) -> tuple:
    """
    Parse a function's docstring automatically
    
    Args:
        function_name: str
            Name of the function for which to get documentation from.

    Returns: tuple(desc, help_msgs)
        desc: str
            Concatenation of short and long function descriptions
        help_msgs: tuple(str)
            Tuple of strings representing each parameter's help message
    """

    parsed = ds_parse(function_name.__doc__)
    help_msgs = tuple(prm.description for prm
                      in parsed.params)
    desc = '\n'.join([parsed.short_description,
                      parsed.long_description])
    return desc, help_msgs


def main():
    parser = ArgumentParser(prog='get_desc',
                            description=get_desc.__doc__.splitlines()[0],
                            usage=get_desc.__doc__)
    parser.add_argument('function_name', nargs=1)
    args = parser.parse_args()
    get_desc(args.function_name[0])


if __name__ == '__main__':
    main()
