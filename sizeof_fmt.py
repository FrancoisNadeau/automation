#!/bin/usr/env python3

from argparse import ArgumentParser


def sizeof_fmt(num: int) -> str:
    """
    Returns the size of the input formatted to be human-readable.

    Args:
        num: int
            Integer representing the number of bytes to format.

    Returns: str
        String representing the formatted input size.
    """

    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, 'B')
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', 'B')


def main():
    init_dict = dict(prog=sizeof_fmt,
                     usage=sizeof_fmt.__doc__,
                     description=__name__.__doc__.splitlines()[0])

    _parser = ArgumentParser(**init_dict)
    _parser.add_argument('num', type=int,
                         help='Total number of bytes', nargs=1)
    args = _parser.parse_args()
    sizeof_fmt(args.num[0])


if __name__ == '__main__':
    main()
