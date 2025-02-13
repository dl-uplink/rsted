# -----------------------------------------------------------------------------
# rsted
# (C) 2022 A. Shavykin <0.delameter@gmail.com>
# -----------------------------------------------------------------------------
import logging as lg
import logging.handlers
import os

from application import app

LOG_FILEPATH = "/logs/rsted_app.log"


def init():
    log_level = os.getenv("APP_LOG_LEVEL", "INFO")

    formatter = lg.Formatter("%(asctime)s [%(levelname)-5.5s] [%(name)s] %(message)s")

    handler_file = lg.handlers.TimedRotatingFileHandler(
        LOG_FILEPATH, "d", interval=1, backupCount=1
    )
    handler_file.setFormatter(formatter)
    handler_file.setLevel(log_level)
    app.logger.addHandler(handler_file)
