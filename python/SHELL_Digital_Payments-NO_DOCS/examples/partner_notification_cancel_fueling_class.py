from shelldigitalpayments.configuration import Environment
from shelldigitalpayments.exceptions.api_exception import APIException
from shelldigitalpayments.models.cancel_fueling_request import CancelFuelingRequest
from shelldigitalpayments.shell_digital_payments_client import ShellDigitalPaymentsClient

client = ShellDigitalPaymentsClient(
    environment=Environment.PRODUCTION
)

partner_notification_controller = client.partner_notification
body = CancelFuelingRequest(
    mpp_transaction_id='000000001E5M',
    reason_code='CANCELLED'
)

try:
    result = partner_notification_controller.cancel_fueling(
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

