# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2023-10-14 23:05:35
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Database build methods.
"""


from typing import List, Optional

from .rdatabase_engine import REngine


class RBuild(object):
    """
    Rey's `database build` type.
    """


    def __init__(self, rengine: Optional[REngine]) -> None:
        """
        Build `database build` instance.

        Parameters
        ----------
        rengine : REngine object.
        """

        # Set attribute.
        self.rengine = rengine


    def create(self) -> None:
        """

        """


    def drop(self) -> None:
        """

        """


    def alter(self) -> None:
        """

        """


    def truncate(self) -> None:
        """

        """


    def exist(self, database: str, table: Optional[str] = None) -> bool:
        """
        Judge table or database exists.

        Parameters
        ----------
        database : Database name.
        table : Table name.
        """

        # # Handle parameter.
        # database, table = self.rengine.extract_path(path)

        # # Get parameter.
        # self.rengine.info(