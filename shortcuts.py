#!/usr/bin/env python3

import os
import re
from functools import reduce
from io import StringIO, IOBase
from os import PathLike
from pathlib import Path, PosixPath
from typing import Generator, Iterable
from typing import NewType, Sequence, Union

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

    Useful to pass as an the ``ignore`` parameter from
    ``shutil.copytree``. Allows to recursively copy a
    directory tree without the files.
    """

    return sorted(filter(os.path.isfile, sorted(Path(src).rglob('*'))))


def factorGenerator(n: int) -> Generator:
    """
    Returns a generator for an integer's factors.
    """

    from functools import reduce
    yield from sorted(set(reduce(list.__add__,
                                 ([i, n // i] for i in
                                  range(1, int(n ** 0.5) + 1)
                                  if n % i == 0))))[1:-1].__iter__()


def eveseq(it: Iterable) -> tuple:
    return tuple(i[1] for i in enumerate(it) if i[0] % 2 == 0)


def oddseq(it: Iterable) -> tuple:
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


def lst_exc(exc: Sequence, seq: Sequence) -> Sequence:
    return [i for i in seq if i not in exc]


def lst_inc(inc: Sequence, l1: Sequence) -> Sequence:
    """
    Return the intersection (non-unique common items) from ``l1`` & ``l2``.

    Similar to ``set.intersection``, but duplicate items are not discarded.
    """

    return [i for i in l1 if i in inc]


def prntonly(txt: str, ensure_ascii: bool = True) -> str:
    """
    Return str containing only UTF-8 printable characters in ``txt``.
    """

    import string
    from unidecode import unidecode

    outpt = ''.join([c for c in list(txt) if c in string.printable])
    if ensure_ascii is True:
        outpt = unidecode(outpt)
    return outpt


def unibuff(d: Union[bytes, bytearray], enc: str) -> IOBase:
    return StringIO(unidecode(d.decode(enc)))


def str_exc(exc: Sequence, lst: Sequence) -> list:
    return [i for i in lst if all(s not in i for s in exc)]


def str_inc(inc: Sequence, lst: Sequence) -> list:
    return [i for i in lst if any(s in i for s in inc)]


def s2sq(txt: str) -> list:
    return [[txt] if isinstance(txt, str) else list(txt)][0]


def upath(src: Union[str, os.PathLike]) -> str:
    return unidecode(re.sub('\\s+', '_', str(src)))
