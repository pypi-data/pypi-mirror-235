# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2023-10-08 21:26:43
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Log methods.
"""


from __future__ import annotations
from typing import Any, Tuple, Dict, Optional, Union, Literal, Final, Callable, ClassVar, NoReturn, overload
from queue import Queue
from os.path import abspath as os_abspath, basename as os_basename
from logging import getLogger, Handler, StreamHandler, FileHandler, Formatter, Filter, LogRecord, DEBUG, INFO, WARNING, ERROR, CRITICAL
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler, QueueHandler
from re import sub as re_sub

from .rdata import objs_in
from .rprint import rprint, abspath_rprint
from .rregular import search
from .rsystem import get_first_notnull, rexc, rstack
from .rtext import to_text
from .rwrap import start_thread


__all__ = (
    "RLog",
)


abspath_rlog = os_abspath(__file__)


class RLog(object):
    """
    Rey's `log` type.
    """

    # State
    print_replaced: ClassVar[bool] = False

    # Default value.
    default_format: ClassVar[str] = (
        "%(asctime)s.%(msecs)s | "
        "%(levelname)s | "
        "%(stack_filename)s:%(stack_lineno)s | "
        "%(message)s"
    )
    default_format_date: ClassVar[str] = "%Y-%m-%d %H:%M:%S"
    default_format_width: ClassVar[int] = 100


    def __init__(
        self,
        name: str = "Log"
    ) -> None:
        """
        Build `log` instance.

        Parameters
        ----------
        name : Log name. When log name existed, then direct return, otherwise build.
        """

        # Set parameter.
        self.name: Final[str] = name
        self.stoped = False

        # Get logger.
        self.logger = getLogger(name)

        # Set level.
        self.logger.setLevel(DEBUG)


    def _get_message_stack(self) -> Dict:
        """
        Get message stack parameters.

        Returns
        -------
        Stack parameters.
        """

        # Get parameter.
        stack_params = rstack.get_stack_param("full", 11)
        stack_param = stack_params[-1]

        # Compatible.

        ## Compatible "__call__".
        if (
            stack_param["filename"] == abspath_rlog
            and stack_param["name"] in ("debug", "info", "warning", "error", "critical")
        ):
            stack_param = stack_params[-2]

        ## Compatible "print".
        if (
            stack_param["filename"] == abspath_rlog
            and stack_param["name"] == "preprocess"
        ):
            stack_param = stack_params[-3]

        ## Compatible "rprint".
        if (
            stack_param["filename"] == abspath_rprint
            and stack_param["name"] == "rprint"
        ):
            stack_param = stack_params[-4]

        # Convert.
        params = {
            "stack_filename": stack_param["filename"],
            "stack_lineno": stack_param["lineno"],
            "stack_name": stack_param["name"],
            "stack_line": stack_param["line"]
        }

        return params


    def _supply_format_stack(
        self,
        format_: str,
        record: LogRecord
    ) -> None:
        """
        Supply format `stack` information.

        Parameters
        ----------
        format_ : Record format.
        record : Log record instance.
        """

        # Break.
        if not objs_in(
            format_,
            "%(stack_filename)",
            "%(stack_lineno)",
            "%(stack_name)",
            "%(stack_line)"
        ):
            return

        # Supply.
        message_stack = self._get_message_stack()
        record.stack_filename: str = message_stack["stack_filename"]
        record.stack_lineno: int = message_stack["stack_lineno"]
        record.stack_name: str = message_stack["stack_name"]
        record.stack_line: str = message_stack["stack_line"]


    def _get_level_color_ansi(
        self,
        level: int
    ) -> str:
        """
        Get level color `ANSI` code.

        Parameters
        ----------
        level : Record level.

        Returns
        -------
        Level color ansi code.
        """

        # Set parameters.
        color_code_dict = {
            10: "\033[1;34m",
            20: "\033[1;37m",
            30: "\033[1;33m",
            40: "\033[1;31m",
            50: "\033[1;37;41m"
        }

        # Index.
        color_code = color_code_dict.get(level, "")

        return color_code


    def _supply_format_color(
        self,
        format_: str,
        record: LogRecord
    ) -> None:
        """
        Supply format `ANSI` color code.

        Parameters
        ----------
        format_ : Record format.
        record : Log record instance.
        """

        # Break.
        result = search("\033\[[\d;]+?m", format_)
        if result is not None:
            return

        # Format "asctime".
        if "%(asctime)s" in format_:
            record.asctime = "\033[32m%s\033[0m" % record.asctime

        # Format "msecs".
        if "%(msecs)s" in format_:
            msecs = str(int(record.msecs))
            msecs = msecs.ljust(3)
            record.msecs = "\033[32m%s\033[0m" % msecs

        # Format "levelname".
        if "%(levelname)s" in format_:
            level_color_code = self._get_level_color_ansi(record.levelno)
            levelname = record.levelname.ljust(8)
            record.levelname = "%s%s\033[0m" % (
                level_color_code,
                levelname
            )

        # Format "stack_filename".
        if "%(stack_filename)s" in format_:
            record.stack_filename = "\033[36m%s\033[0m" % record.stack_filename

        # Format "stack_lineno".
        if "%(stack_lineno)s" in format_:
            record.stack_lineno = "\033[36m%s\033[0m" % record.stack_lineno

        # Format "message".
        if (
            "%(message)s" in format_
            and (
                record.msg.__class__ != str
                or search("\033\[[\d;]+?m", record.msg) is None
            )
        ):
            level_color_code = self._get_level_color_ansi(record.levelno)
            record.msg = "%s%s\033[0m" % (
                level_color_code,
                record.msg
            )


    def get_default_filter_method(
        self,
        handler: Handler,
        type_ : Optional[Literal["print", "file"]] = None
    ) -> Callable[[LogRecord], Literal[True]]:
        """
        Get default `filter` method of handler.

        Parameters
        ----------
        handler : Handler.
        type_ : Handler type.
            - `None` : Standard filter method.
            - `Literal['print'] : Print handler filter method.
            - `Literal['file'] : File handler filter method.

        Returns
        -------
        Filter method.
        """

        # Get parameter.
        if (
            handler.formatter is None
            or handler.formatter._fmt is None
        ):
            format_ = ""
        else:
            format_ = handler.formatter._fmt


        def default_filter_method(
            record: LogRecord
        ) -> Literal[True]:
            """
            Default `filter` method of handler.

            Parameters
            ----------
            record : Log record instance.

            Returns
            -------
            Whether pass.
            """

            # Supply message parameter.
            self._supply_format_stack(format_, record)

            # Print handler.
            if type_ == "print":

                # Format color.
                self._supply_format_color(format_, record)

            # File handler.
            elif type_ == "file":

                ## Delete ANSI code.
                pattern = "\033\[[\d;]+?m"
                record.msg = re_sub(pattern, "", record.msg)

            return True


        return default_filter_method


    def add_print(
        self,
        level: int = DEBUG,
        format_: Optional[str] = None,
        filter_: Optional[Callable[[LogRecord], bool]] = None
    ) -> StreamHandler:
        """
        Add `print output` handler.

        Parameters
        ----------
        level : Handler level.
        format_ : Record format.
            - `None` : Use attribute `default_format`.
            - `str` : Use this value.
                * `Contain 'stack_filename'` : Code stack file path.
                * `Contain 'stack_lineno'` : Code stack file line number.
                * `Contain 'stack_name'` : Code stack module name.
                * `Contain 'stack_line'` : Code stack line content.

        filter_ : Filter method. The parameter is the `LogRecord` instance, return is `bool`.
            - `None` : Use default filter method.
            - `Callable` : Use this method.

        Returns
        -------
        Handler.
        """

        # Get parameter.
        format_ = get_first_notnull(format_, self.default_format, default="exception")

        # Create handler.
        handler = StreamHandler()

        # Set handler.
        formatter = Formatter(format_, self.default_format_date)
        handler.setFormatter(formatter)
        handler.setLevel(level)
        handler_filter = Filter()
        if filter_ is None:
            default_filter_method = self.get_default_filter_method(handler, "print")
            handler_filter.filter = default_filter_method
        else:
            handler_filter = filter_
        handler.addFilter(handler_filter)

        # Add.
        self.logger.addHandler(handler)

        return handler


    @overload
    def add_file(
        self,
        path: Optional[str] = None,
        mb: None = None,
        time: None = None,
        level: int = DEBUG,
        format_: Optional[str] = None,
        filter_: Optional[Callable[[LogRecord], bool]] = None
    ) -> FileHandler: ...

    @overload
    def add_file(
        self,
        path: Optional[str] = None,
        mb: float = None,
        time: None = None,
        level: int = DEBUG,
        format_: Optional[str] = None,
        filter_: Optional[Callable[[LogRecord], bool]] = None
    ) -> RotatingFileHandler: ...

    @overload
    def add_file(
        self,
        path: Optional[str] = None,
        mb: None = None,
        time: Union[float, Literal["m", "w0", "w1", "w2", "w3", "w4", "w5", "w6"]] = None,
        level: int = DEBUG,
        format_: Optional[str] = None,
        filter_: Optional[Callable[[LogRecord], bool]] = None
    ) -> TimedRotatingFileHandler: ...

    @overload
    def add_file(
        self,
        path: Optional[str] = None,
        mb: None = None,
        time: Any = None,
        level: int = DEBUG,
        format_: Optional[str] = None,
        filter_: Optional[Callable[[LogRecord], bool]] = None
    ) -> NoReturn: ...

    @overload
    def add_file(
        self,
        path: Optional[str] = None,
        mb: float = None,
        time: Union[float, Literal["m", "w0", "w1", "w2", "w3", "w4", "w5", "w6"]] = None,
        level: int = DEBUG,
        format_: Optional[str] = None,
        filter_: Optional[Callable[[LogRecord], bool]] = None
    ) -> NoReturn: ...

    def add_file(
        self,
        path: Optional[str] = None,
        mb: Optional[float] = None,
        time: Optional[Union[float, Literal["m", "w0", "w1", "w2", "w3", "w4", "w5", "w6"]]] = None,
        level: int = DEBUG,
        format_: Optional[str] = None,
        filter_: Optional[Callable[[LogRecord], bool]] = None
    ) -> Union[FileHandler, RotatingFileHandler, TimedRotatingFileHandler]:
        """
        Add `file output` handler, can split files based on size or time.

        Parameters
        ----------
        path : File path.
            - `None` : Use '%s.log' %s self.name.
            - `str` : Use this value.

        mb : File split condition, max megabyte. Conflict with parameter `time`. Cannot be less than 1, prevent infinite split file.
        time : File split condition, interval time. Conflict with parameter `mb`.
            - `float` : Interval hours.
            - `Literal['m']` : Everyday midnight.
            - `Literal['w0', 'w1', 'w2', 'w3', 'w4', 'w5', 'w6']` : Weekly midnight, 'w0' is monday, 'w6' is sunday, and so on.

        level : Handler level.
        format_ : Record format.
            - `None` : Use attribute `default_format`.
            - `str` : Use this value.
                * `Contain 'stack_filename'` : Code stack file path.
                * `Contain 'stack_lineno'` : Code stack file line number.
                * `Contain 'stack_name'` : Code stack module name.
                * `Contain 'stack_line'` : Code stack line content.

        filter_ : Filter method. The parameter is the `LogRecord` instance, return is `bool`.
            - `None` : Use default filter method.
            - `Callable` : Use this method.

        Returns
        -------
        Handler.
        """

        # Get parameter.
        format_ = get_first_notnull(format_, self.default_format, default="exception")
        if path is None:
            path = "%s.log" % self.name

        # Create handler.

        ## Raise.
        if (
            mb is not None
            and time is not None
        ):
            raise AssertionError("parameter 'mb' and 'time' cannot be used together")

        ## By size split.
        elif mb is not None:

            ### Check.
            if mb < 1:
                rexc(ValueError, mb)

            byte = int(mb * 1024 * 1024)
            handler = RotatingFileHandler(
                path,
                "a",
                byte,
                1_0000_0000
            )

        ## By time split.
        elif time is not None:

            ### Interval hours.
            if time.__class__ in (int, float):
                second = int(time * 60 * 60)
                handler = TimedRotatingFileHandler(
                    path,
                    "S",
                    second,
                    1_0000_0000
                )

            ### Everyday midnight.
            elif time == "m":
                handler = TimedRotatingFileHandler(
                    path,
                    "MIDNIGHT",
                    backupCount=1_0000_0000
                )

            ### Weekly midnight
            elif time in ("w0", "w1", "w2", "w3", "w4", "w5", "w6"):
                handler = TimedRotatingFileHandler(
                    path,
                    time,
                    backupCount=1_0000_0000
                )

            ### Raise.
            else:
                rexc(ValueError, time)

        ## Not split.
        else:
            handler = FileHandler(
                path,
                "a"
            )

        # Set handler.
        formatter = Formatter(format_, self.default_format_date)
        handler.setFormatter(formatter)
        handler.setLevel(level)
        handler_filter = Filter()
        if filter_ is None:
            default_filter_method = self.get_default_filter_method(handler, "file")
            handler_filter.filter = default_filter_method
        else:
            handler_filter = filter_
        handler.addFilter(handler_filter)

        # Add.
        self.logger.addHandler(handler)

        return handler


    def add_queue(
        self,
        queue: Optional[Queue] = None,
        level: int = DEBUG,
        filter_: Optional[Callable[[LogRecord], bool]] = None
    ) -> Tuple[QueueHandler, Queue[LogRecord]]:
        """
        Add `queue output` handler.

        Parameters
        ----------
        queue : Queue instance.
            - `None` : Create queue and use.
            - `Queue` : Use this queue.

        level : Handler level.
        filter_ : Filter method. The parameter is the `LogRecord` instance, return is `bool`.
            - `None` : Use default filter method.
            - `Callable` : Use this method.

        Returns
        -------
        Handler and queue.
        """

        ## Create queue.
        if queue is None:
            queue = Queue()

        # Create handler.
        handler = QueueHandler(queue)

        # Set handler.
        handler.setLevel(level)
        handler_filter = Filter()
        if filter_ is None:
            default_filter_method = self.get_default_filter_method(handler)
            handler_filter.filter = default_filter_method
        else:
            handler_filter = filter_
        handler.addFilter(handler_filter)

        # Add.
        self.logger.addHandler(handler)

        return handler, queue


    @start_thread
    def add_method(
        self,
        method: Callable[[LogRecord], Any],
        level: int = DEBUG,
        filter_: Optional[Callable[[LogRecord], bool]] = None
    ) -> None:
        """
        Add `method` handler.

        Parameters
        ----------
        method : Handler method. The parameter is the `LogRecord` instance.
        level : Handler level.
        filter_ : Filter method. The parameter is the `LogRecord` instance, return is `bool`.
            - `None` : Use default filter method.
            - `Callable` : Use this method.
        """

        # Add queue out.
        _, queue = self.add_queue(level, filter_)

        # Execute.
        while True:
            record = queue.get()
            method(record)


    def delete_handler(self, handler: Optional[Handler] = None) -> None:
        """
        Delete handler.

        Parameters
        ----------
        handler : Handler.
            - `None` : Delete all handler.
            - `Handler` : Delete this handler.
        """

        # Delete.

        ## This.
        if handler is None:
            for handle in self.logger.handlers:
                self.logger.removeHandler(handle)

        ## All.
        else:
            self.logger.removeHandler(handler)


    def catch_print(self, printing: bool = True) -> None:
        """
        Catch print to log.

        Parameters
        ----------
        printing : Whether to still print.
        """


        # Define.
        def preprocess(__s: str) -> str:
            """
            Preprocess function.

            Parameters
            ----------
            __s : Standard ouput text.

            Returns
            -------
            Preprocessed text.
            """

            # Break.
            if __s in ("\n", "[0m"): return

            # Log.
            self(__s)

            # Print.
            if printing:
                return __s


        # Modify.
        rprint.modify(preprocess)

        # Update state.
        self.print_replaced = True


    def reset_print(self) -> None:
        """
        Reset log `replace` print.
        """

        # Break.
        if not self.print_replaced: return

        # Reset.
        rprint.reset()

        # Update state.
        self.print_replaced = False


    def log(
        self,
        *messages: Optional[Any],
        level: Optional[int] = None
    ) -> None:
        """
        `Record` log.

        Parameters
        ----------
        messages : Record content.
        level : Record level.
            - `None` : Automatic judge.
                * `in 'except' syntax` : Use 'ERROR' level.
                * `Other` : Use 'INFO' level.
            - `int` : Use this value.
        """

        # Get parameter.

        ## Messages.
        messages_len = len(messages)
        if messages_len == 0:
            messages = [None]

        ## Level.
        _, exc_type, _, _ = rexc.catch()
        if level is None:
            if exc_type is None:
                level = INFO
            else:
                level = ERROR

        # Convert.

        ## Join.
        messages = "\n".join(
            [
                to_text(message, self.default_format_width)
                for message in messages
            ]
        )
        if "\n" in messages:
            messages = "\n" + messages

        ## Exception.
        exc_stack, exc_type, _, _ = rexc.catch()
        if exc_type is not None:
            messages = "%s\n%s" % (
                messages,
                exc_stack
            )

        # Record.
        self.logger.log(level, messages)


    def debug(
        self,
        *messages: Optional[Any]
    ) -> None:
        """
        Record `debug` level log.

        Parameters
        ----------
        messages : Record content.
        """

        # Record.
        self.log(*messages, level=DEBUG)


    def info(
        self,
        *messages: Optional[Any]
    ) -> None:
        """
        Record `info` level log.

        Parameters
        ----------
        messages : Record content.
        """

        # Record.
        self.log(*messages, level=INFO)


    def warning(
        self,
        *messages: Optional[Any]
    ) -> None:
        """
        Record `warning` level log.

        Parameters
        ----------
        messages : Record content.
        """

        # Record.
        self.log(*messages, level=WARNING)


    def error(
        self,
        *messages: Optional[Any]
    ) -> None:
        """
        Record `error` level log.

        Parameters
        ----------
        messages : Record content.
        """

        # Record.
        self.log(*messages, level=ERROR)


    def critical(
        self,
        *messages: Optional[Any]
    ) -> None:
        """
        Record `critical` level log.

        Parameters
        ----------
        messages : Record content.
        """

        # Record.
        self.log(*messages, level=CRITICAL)


    def stop(self) -> None:
        """
        `Stop` record.
        """

        # Set level.
        self.logger.setLevel(100)

        # Update state.
        self.stoped = True


    def start(self) -> None:
        """
        `Start` record.
        """

        # Set level.
        self.logger.setLevel(DEBUG)

        # Update state.
        self.stoped = False


    def __del__(self) -> None:
        """
        Delete handle.
        """

        # Reset.
        self.reset_print()

        # Delete handler.
        self.delete_handler()


    __call__ = log