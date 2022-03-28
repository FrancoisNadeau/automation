#!/usr/bin/env python3

import os
import re
from functools import reduce
from io import StringIO, IOBase
from os import PathLike
from pathlib import Path, PosixPath
from typing import Generator, Iterable
from typing import List, Sequence, Union

from unidecode import unidecode


def chunks(lst, n):
    """
    Yield successive n-sized chunks from lst.
    """

    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def ig_f(src: Union[str, PathLike, PosixPath]) -> list:
    """
    Returns only file paths within a directory.

    Useful to pass as the ``ignore`` parameter to the
    ``shutil.copytree`` function.
    Allows to recursively copy a directory tree without the files.
    """

    return sorted(filter(os.path.isfile, sorted(Path(src).rglob('*'))))


def iter_files(src: Union[str, PathLike]) -> Generator:
    """
    Returns a generator of ``PathLike`` objects.

    Recursively yields the absolute path of files
    within directory ``src``.

    Args:
        src: str or PathLike
            Path to the directory to traverse.

    Returns: Generator[PathLike]
    """

    src = src if isinstance(src, type(Path(src))) else Path(src)
    FilesGen = iter(filter(os.path.isfile, src.rglob('*')))
    while True:
        for _ in len(tuple(FilesGen)): yield from FilesGen


def factorGenerator(n: int) -> Generator:
    """
    Returns a generator for an integer's factors.
    """

    from functools import reduce
    yield from sorted(set(reduce(list.__add__,
                                 ([i, n // i] for i in
                                  range(1, int(n ** 0.5) + 1)
                                  if n % i == 0))))[1:-1].__iter__()


def even_seq(it: Iterable) -> tuple:
    return tuple(i[1] for i in enumerate(it) if i[0] % 2 == 0)


def odd_seq(it: Iterable) -> tuple:
    return tuple(i[1] for i in enumerate(it) if i[0] % 2 != 0)


def by_value(dc: dict, val) -> list:
    """
    Return key from ``dc`` if its value is equal to ``val``.
    """

    return list(dc.keys())[list(dc.values()).index(val)]


def rev_dict(dc: dict) -> dict:
    """
    Return dict inversely mapping key-value pairs in ``dc``.
    """

    return dict(tuple((i[1], i[0]) for i in tuple(dc.items())))


def chain_pipe(funcs: Sequence[callable], val: object) -> object:
    """
    Apply functions in ``funcs`` one by one to ``val``.
    """

    return reduce(lambda res, f: f(res), funcs, val)


def lst_exc(exc: Sequence, seq: Sequence) -> List:
    """
    Returns the difference between two sequences.

    Similar to the built-in method ``set.difference``,
    but duplicate (non-unique) items are not discarded.

    Args:
        exc: Sequence
            Elements to be excluded from ``seq``.
        seq: Sequence
            The sequence to be filtered.

    Returns: List
    """

    return [i for i in seq if i not in exc]


def lst_inc(inc: Sequence, seq: Sequence) -> List:
    """
    Returns the intersection of two sequences.

    Similar to the built-in method ``set.intersection``,
    but duplicate (non-unique) items are not discarded.

    Args:
        inc: Sequence
            Elements to be included from ``seq``.
        seq: Sequence
            The sequence to be filtered.

    Returns: List
    """

    return [i for i in seq if i in inc]


def printable_only(txt: str, ensure_ascii: bool = True) -> str:
    """
    Returns a string containing only printable characters in ``txt``.

    Args:
        txt: str
            The string to format.
        ensure_ascii: bool (Default = True)
            Indicates if printable characters in
            local variable ``new_string`` should be
            converted to their Unicode (UTF-8) equivalent.

    Returns: str
    """

    from unidecode import unidecode

    new_string = ''.join(filter(str.isprintable, iter(txt)))
    if ensure_ascii is True:
        new_string = unidecode(new_string)
    return new_string

# def unibuff(d: Union[bytes, bytearray], enc: str) -> IOBase:
#     return StringIO(unidecode(d.decode(enc)))
#
#
# def str_exc(exc: Sequence, lst: Sequence) -> list:
#     return [i for i in lst if all(s not in i for s in exc)]
#
#
# def str_inc(inc: Sequence, lst: Sequence) -> list:
#     return [i for i in lst if any(s in i for s in inc)]
#
#
# def s2sq(txt: str) -> list:
#     return [[txt] if isinstance(txt, str) else list(txt)][0]
#
#
# def upath(src: Union[str, os.PathLike]) -> str:
#     return unidecode(re.sub('\\s+', '_', str(src)))
