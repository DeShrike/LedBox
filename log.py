import logging
import logging.config

# DEBUG, INFO, WARNING, ERROR, and CRITICAL
#    Default = WARNING ----------->>>>>>

logging.config.fileConfig('logging.ini', disable_existing_loggers = False)
logger = logging.getLogger(__name__) # 'root' Logger

# console = logging.StreamHandler()

# format_str = '%(asctime)s\t%(levelname)s -- %(processName)s %(filename)s:%(lineno)s -- %(message)s'
# console.setFormatter(logging.Formatter(format_str))

# log.addHandler(console) # prints to console.
# log.setLevel(logging.ERROR) # anything ERROR or above

# logger.debug(__name__)
# logger.info("Hello World")
# logger.warning('Citizens of Earth, be warned!')
# logger.error("This is an error")
# logger.critical("CRIT Citizens of Earth, be warned!")
