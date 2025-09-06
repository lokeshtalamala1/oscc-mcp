from loguru import logger

logger.add("oscc.log", rotation="1 MB", level="INFO")
