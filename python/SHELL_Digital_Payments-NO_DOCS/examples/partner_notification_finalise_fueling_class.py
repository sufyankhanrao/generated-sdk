from shelldigitalpayments.configuration import Environment
from shelldigitalpayments.exceptions.api_exception import APIException
from shelldigitalpayments.models.finalise_fueling_request import FinaliseFuelingRequest
from shelldigitalpayments.shell_digital_payments_client import ShellDigitalPaymentsClient

client = ShellDigitalPaymentsClient(
    environment=Environment.PRODUCTION
)

partner_notification_controller = client.partner_notification
body = FinaliseFuelingRequest(
    site_name='Pentahof Site B 9997',
    timestamp=1548429960631,
    volume_quantity=10.4,
    volume_unit='LTR',
    final_price=23.3,
    currency='GBP',
    status='FINISHED',
    site_address='Test Geman Address',
    original_price=23.3,
    discount=0,
    mpp_transaction_id='000000006KCC'
)

try:
    result = partner_notification_controller.finalise_fueling(
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

