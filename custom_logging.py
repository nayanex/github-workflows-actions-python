import logging
from datetime import datetime


# https://www.datacamp.com/community/tutorials/decorators-python
# https://www.python.org/dev/peps/pep-0318/#design-goals
def logging_message(app):
    def func_wrapper(func):
        ## stream logs to app.log file
        logging.basicConfig(filename="app.log", level=logging.DEBUG)

        timestamp = datetime.now()
        function_name = func.__name__

        app.logger.info(
            "{{{timestamp}}}, {{{endpoint}}} endpoint request was reached successfully".format(
                timestamp=timestamp, endpoint=function_name
            )
        )
        return func

    return func_wrapper
