#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Sequence


def flatten(nested: Sequence) -> list:
    """
    Return vectorized (1D) list from nested Sequence ``nested``.

    Args:
        nested: Sequence
           Iterable sequence containing multiple other nested sequences.

    Returns: list
        Vectorized (unidimensional) version of ``nested``.
    """

    return [lowest for sublist in nested for lowest
            in (flatten(sublist)
                if bool(isinstance(sublist, Sequence)
                        and not isinstance(sublist, str))
                else [sublist])]


def main():
    parser = ArgumentParser(prog='flatten',
                            description=flatten.__doc__.splitlines()[0],
                            usage=flatten.__doc__)
    parser.add_argument('nested', nargs=1)
    args = parser.parse_args()
    flatten(args.nested[0])


if __name__ == '__main__':
    main()
