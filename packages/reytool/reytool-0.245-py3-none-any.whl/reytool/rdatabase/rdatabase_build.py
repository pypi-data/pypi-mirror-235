# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2023-10-14 23:05:35
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Database build methods.
"""


from typing import Any, List, Tuple, Dict, Optional, Union, Literal, NoReturn, overload

from .rdatabase_engine import REngine
from ..rsystem import rexc


class RBuild(object):
    """
    Rey's `database build` type.
    """


    def __init__(self, rengine: REngine) -> None:
        """
        Build `database build` instance.

        Parameters
        ----------
        rengine : REngine object.
        """

        # Set attribute.
        self.rengine = rengine


    def create_database(
        self,
        database: str,
        character: str = "utf8mb3",
        collate: str = "utf8_general_ci",
        execute: bool = True
    ) -> str:
        """
        Create `database`.

        Parameters
        ----------
        database : Database name.
        character : Character set.
        collate : Collate rule.
        execute : Whether directly execute.

        Returns
        -------
        Execute SQL.
        """

        # Generate.
        sql = f"CREATE DATABASE `{database}` CHARACTER SET {character} COLLATE {collate}"

        # Execute.
        if execute:
            self.rengine(sql)

        return sql


    def _get_field_sql(
        self,
        name: str,
        type_: str,
        constraint: str = "DEFAULT NULL",
        comment: Optional[str] = None
    ) -> str:
        """
        Get a field set SQL.

        Parameters
        ----------
        name : Field name.
        type_ : Field type.
        constraint : Field constraint.
        comment : Field comment.

        Returns
        -------
        Field set SQL.
        """

        # Get parameter.

        ## Constraint.
        if constraint[:1] != " ":
            constraint = " " + constraint

        ## Comment.
        if comment is None:
            comment = ""
        else:
            comment = f" COMMENT '{comment}'"

        # Generate.
        sql = f"`{name}` {type_}{constraint}{comment}"

        return sql


    @overload
    def _get_index_sql(
        self,
        name: str,
        fields: Union[str, List[str]],
        type_: Literal["noraml", "unique", "fulltext", "spatial"] = "noraml",
        comment: Optional[str] = None
    ) -> str: ...

    @overload
    def _get_index_sql(
        self,
        name: str,
        fields: Union[str, List[str]],
        type_: str = "noraml",
        comment: Optional[str] = None
    ) -> NoReturn: ...

    def _get_index_sql(
        self,
        name: str,
        fields: Union[str, List[str]],
        type_: Literal["noraml", "unique", "fulltext", "spatial"] = "noraml",
        comment: Optional[str] = None
    ) -> str:
        """
        Get a index set SQL.

        Parameters
        ----------
        name : Index name.
        fields : Index fileds.
        type_ : Index type.
        comment : Index comment.

        Returns
        -------
        Index set SQL.
        """

        # Get parameter.
        if fields.__class__ == str:
            fields = [fields]
        if type_ == "noraml":
            type_ = "KEY"
            method = " USING BTREE"
        elif type_ == "unique":
            type_ = "UNIQUE KEY"
            method = " USING BTREE"
        elif type_ == "fulltext":
            type_ = "FULLTEXT KEY"
            method = ""
        elif type_ == "spatial":
            type_ = "SPATIAL KEY"
            method = ""
        else:
            rexc(ValueError, type_)
        if comment in (None, ""):
            comment = ""
        else:
            comment = f" COMMENT '{comment}'"

        # Generate.

        ## Fields.
        sql_fields = ", ".join(
            [
                f"`{field}`"
                for field in fields
            ]
        )

        ## Join.
        sql = f"{type_} `{name}` ({sql_fields}){method}{comment}"

        return sql


    def create_table(
        self,
        database: str,
        table: str,
        fields: Union[Dict, List[Dict]],
        primary: Optional[Union[str, List[str]]] = None,
        indexes: Optional[Union[Dict, List[Dict]]] = None,
        engine: str = "InnoDB",
        increment: int = 1,
        charset: str = "utf8mb3",
        execute: bool = True
    ) -> str:
        """
        Create `table`.

        Parameters
        ----------
        database : Database name.
        table : Table name.
        fields : Fields set table.
            - `Key 'name'` : Field name.
            - `Key 'type_'` : Field type.
            - `Key 'constraint'` : Field constraint.
                * `Empty or None` : Use 'DEFAULT NULL'.
                * `str` : Use this value.
            - `Key `comment` : Field comment.
                * `Empty or None` : Not comment.
                * `str` : Use this value.

        primary : Primary key fields.
            - `str` : One field.
            - `List[str]` : Multiple fileds.

        indexes : Index set table.
            - `Key 'name'` : Index name.
            - `Key 'fields'` : Index fields.
                * `str` : One field.
                * `List[str]` : Multiple fileds.
            - `Key 'type_'` : Index type.
                * `Literal['noraml']` : Noraml key.
                * `Literal['unique']` : Unique key.
                * `Literal['fulltext']` : Full text key.
                * `Literal['spatial']` : Spatial key.
            - `Key `comment` : Field comment.
                * `Empty or None` : Not comment.
                * `str` : Use this value.

        engine : Engine type.
        increment : Automatic Increment start value.
        charset : Character type.
        execute : Whether directly execute.

        Returns
        -------
        Execute SQL.
        """

        # Get parameter.
        if fields.__class__ == dict:
            fields = [fields]
        if primary.__class__ == str:
            primary = [primary]
        if primary in ([], [""]):
            primary = None
        if indexes.__class__ == dict:
            indexes = [indexes]

        # Generate.

        ## Fields.
        sql_fields = [
            self._get_field_sql(**field)
            for field in fields
        ]

        ## Primary.
        if primary is not None:
            keys = ", ".join(
                [
                    f"`{key}`"
                    for key in primary
                ]
            )
            sql_primary = f"PRIMARY KEY ({keys}) USING BTREE"
            sql_fields.append(sql_primary)

        ## Indexes.
        sql_indexes = [
            self._get_index_sql(**index)
            for index in indexes
        ]
        sql_fields.extend(sql_indexes)

        ## Join.
        sql_fields = ",\n    ".join(sql_fields)
        sql = (
            f"CREATE TABLE `{database}`.`{table}`(\n"
            f"    {sql_fields}\n"
            f") ENGINE={engine} AUTO_INCREMENT={increment} DEFAULT CHARSET={charset}"
        )

        # Execute.
        if execute:
            self.rengine(sql)

        return sql


    def drop_database(
        self,
        database: str,
        execute: bool = True
    ) -> str:
        """
        Drop `database`.

        Parameters
        ----------
        database : Database name.
        execute : Whether directly execute.

        Returns
        -------
        Execute SQL.
        """

        # Generate.
        sql = f"DROP DATABASE `{database}`"

        # Execute.
        if execute:
            self.rengine(sql)

        return sql


    def drop_table(
        self,
        database: str,
        table: str,
        execute: bool = True
    ) -> str:
        """
        Drop `table`.

        Parameters
        ----------
        database : Database name.
        table : Table name.
        execute : Whether directly execute.

        Returns
        -------
        Execute SQL.
        """

        # Generate.
        sql = f"DROP TABLE `{database}`.`{table}`"

        # Execute.
        if execute:
            self.rengine(sql)

        return sql


    def alter(self) -> str: ...


    def truncate(self) -> str: ...


    def exist(
        self,
        path: Union[str, Tuple[str, Optional[str], Optional[str]]]
    ) -> bool:
        """
        Judge database or table or column exists.

        Parameters
        ----------
        path : Database name and table name and column name.
            - `str` : Automatic extract.
            - `Tuple[str, Optional[str], Optional[str]]` : Database name and table name, column name is optional.

        Returns
        -------
        Judge result.
        """

        # Handle parameter.
        if path.__class__ == str:
            database, table, column = self.rengine.extract_path(path, "database")
        else:
            database, table, column = path

        # Judge.
        if table is None:
            rinfo = self.rengine.info(database)
        elif column is None:
            rinfo = self.rengine.info(database)(table)
        else:
            rinfo = self.rengine.info(database)(table)(column)
        try:
            rinfo["*"]
        except AssertionError:
            judge = False
        else:
            judge = True

        return judge