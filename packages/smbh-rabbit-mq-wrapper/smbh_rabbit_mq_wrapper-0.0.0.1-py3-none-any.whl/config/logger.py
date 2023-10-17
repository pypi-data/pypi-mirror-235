from loguru import logger

from config.config import PROJECT_PATH

log_format = "{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message}"

logger.configure(extra={"action": ""})
logger.add(f"{PROJECT_PATH}/logs/info.log", filter=lambda record: record["level"].name == "INFO", format=log_format)
logger.add(f"{PROJECT_PATH}/logs/debug.log", filter=lambda record: record["level"].name == "DEBUG", format=log_format)
logger.add(f"{PROJECT_PATH}/logs/errors.log", filter=lambda record: record["level"].name == "ERROR", format=log_format)

logger.add(
    f"{PROJECT_PATH}/logs/listener.log",
    filter=lambda record: record["extra"].get('action') == "listener",
    format=log_format
)
logger.add(
    f"{PROJECT_PATH}/logs/writer.log",
    filter=lambda record: record["extra"].get('action') == "writer",
    format=log_format
)

logger_writer = logger.bind(action="writer")
logger_listener = logger.bind(action="listener")
