from sty import fg as Clr
import datetime
import logging
import os


os.system('')  # System call to enable coloring in the terminal.


class Logger:
    """ Static representation of a simple terminal logger. """

    LOG_LEVELS = {
        'info' : ('[i]', Clr.li_blue),
        'ok' : ('[o]', Clr.li_green),
        'warning' : ('[!]', Clr.li_yellow),
        'error' : ('[X]', Clr.li_red)
    }


    @staticmethod
    def _log(level: str, title: str, message: str) -> None:
        """
        Helper function for printing log messages.

        ------

        Log levels: info, ok, warning, error, default.

        ------

        Arguments:
            level: The log level.
            title: Title of the log message.
            message: The log message.
        """

        time = datetime.datetime.now().replace(microsecond = 0).astimezone().strftime('%H:%M:%S')
        code, color = Logger.LOG_LEVELS.get(level.lower(), ('[_]', Clr.white))

        lines = message.split('\n')

        header = f'{color}{code} {Clr.li_cyan}[{time}]{Clr.li_magenta}[{title.center(25)}]'
        entry = f'{header} {color}{lines[0]}'

        for line in lines[1:]:
            entry += f'\n{" " * 41} {color}{line}'

        print(entry)


    @staticmethod
    def info(title: str, message: str) -> None:
        """ Log an informational message. """

        Logger._log('info', title, message)


    @staticmethod
    def ok(title: str, message: str) -> None:
        """ Log an informational message. """

        Logger._log('ok', title, message)


    @staticmethod
    def warning(title: str, message: str) -> None:
        """ Log an informational message. """

        Logger._log('warning', title, message)


    @staticmethod
    def error(title: str, message: str) -> None:
        """ Log an informational message. """

        Logger._log('error', title, message)


    @staticmethod
    def log(title: str, message: str) -> None:
        """ Log an informational message. """

        Logger._log('default', title, message)


class LogsHandler(logging.Handler):
    """ Handling Discord logs through the custom logger. """

    LOG_LEVELS = {
        logging.DEBUG : Logger.log,
        logging.INFO : Logger.info,
        logging.WARNING : Logger.warning,
        logging.ERROR : Logger.error,
        logging.CRITICAL : Logger.error
    }


    def emit(self, record: logging.LogRecord) -> None:
        """ Redirect log records to the custom logger. """

        message = self.format(record)
        log_func = self.LOG_LEVELS.get(record.levelno, Logger.log)
        log_func(record.name, message)


def setup_logs_handler() -> None:
    """ Set up the LogsHandler to redirect Discord logs to the custom logger. """

    logs_handler = LogsHandler()
    formatter = logging.Formatter('%(message)s')
    logs_handler.setFormatter(formatter)

    discord_loggers = [
        'discord',
        'discord.client',
        'discord.gateway',
        'discord.http',
        'discord.state',
        'discord.voice_state',
        'discord.gateway',
        'discard.ext.commands'
    ]

    for logger_name in discord_loggers:
        logger = logging.getLogger(logger_name)

        for handler in logger.handlers[:]:
            logger.removeHandler(handler)

        logger.addHandler(logs_handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False

    Logger.ok('Logger', 'Successfully set up the Discord logs handler.')


__all__ = ['Logger', 'setup_logs_handler']
