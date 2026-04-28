import logging

class WarningLevelFilter(logging.Filter):
    def filter(self, record):
        return record.levelno >= logging.WARNING

class ContainsWordsFilter(logging.Filter):
    # ??? TODO implement a filter that checks for the presence of the word "SECURITY"
    def filter(self, record): # pyright: ignore[reportIncompatibleMethodOverride]
        if 'SECURITY' in record.getMessage():
            print(record.getMessage())


logger = logging.getLogger("FilterChainExample")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()

console_handler.addFilter(WarningLevelFilter())
console_handler.addFilter(ContainsWordsFilter())

formatter = logging.Formatter("%(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


logger.debug("This is a debug message")            # Filtered: below WARNING
logger.warning("SECURITY: This is a warning")                # Passed
logger.error("SECURITY: This should be logged")              # Passed
logger.error("Ignore this message")                # Filtered: contains 'ignore'