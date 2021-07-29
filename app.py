from flask import Flask, json

import settings
from custom_logging import logging_message

app = Flask(__name__)


@app.route("/")
def hello():
    app.logger.info("Main request successfull")
    return "Hello World!"


@app.route("/healthcheck", endpoint="healthcheck")
@logging_message(app)
def healthcheck():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype="application/json",
    )
    return response

# https://stackoverflow.com/questions/17256602/assertionerror-view-function-mapping-is-overwriting-an-existing-endpoint-functi
@app.route("/metrics", endpoint="metrics")
@logging_message(app)
def metrics():
    response = app.response_class(
        response=json.dumps(
            {
                "status": "success",
                "code": 0,
                "data": {"UserCount": 140, "UserCountActive": 23},
            }
        ),
        status=200,
        mimetype="application/json",
    )
    return response


if __name__ == "__main__":
    
    app.run(
        host=settings.SERVER_HOST, port=settings.SERVER_PORT, debug=settings.FLASK_DEBUG
    )
