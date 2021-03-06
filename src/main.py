import os
import json

from aws_lambda_powertools.tracing import Tracer
from aws_lambda_powertools.logging import Logger

import vericall

tracer = Tracer()
logger = Logger()

host = os.environ["API_ENDPOINT"]
username = os.environ["USERNAME"]
password = os.environ["PASSWORD"]

VeriCall = vericall.VeriCall(host=host, username=username, password=password)


@tracer.capture_lambda_handler
def handler(event, context):
    contact_data = event["Details"].get("ContactData", {})
    parameters = event["Details"].get("Parameters", {})

    contact_id = contact_data["ContactId"]
    sip_data = {
        "P-Charge-Info": parameters.get("P-Charge-Info", None),
        "From": parameters.get("From", None),
        "P-Asserted-Identity": parameters.get("P-Asserted-Identity", None),
        "To": parameters.get("To", None),
        "X-Info-Dig": parameters.get("I-SUP-OLI", None),
    }
    meta = {"ContactId": contact_id}
    ani = contact_data["CustomerEndpoint"]["Address"]
    dnis = contact_data["SystemEndpoint"]["Address"]

    payload = {"ani": ani, "dnis": dnis, "headers": sip_data, "meta": meta}
    logger.info(f"ContactId: contact_id")
    data = vericall.score(VeriCall, payload)

    # https://docs.aws.amazon.com/connect/latest/adminguide/connect-lambda-functions.html
    # The output returned from the function must be a flat object of key/value
    # pairs, with values that include only alphanumeric, dash, and underscore
    # characters. Nested and complex objects are not supported.
    # The size of the returned data must be less than 32 Kb of UTF-8 data.
    logger.debug(data)
    if "reason_codes" in data:
        reason_codes = data.pop("reason_codes")
        data["reason_codes"] = "|".join(reason_codes)
    data["data_source"] = "vericall"

    return data
