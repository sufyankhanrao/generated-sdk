from fortisapi.configuration import Environment
from fortisapi.exceptions.api_exception import APIException
from fortisapi.exceptions.response_401_token_exception import Response401tokenException
from fortisapi.exceptions.response_412_exception import Response412Exception
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials
from fortisapi.models.interval_type_enum import IntervalTypeEnum
from fortisapi.models.payment_method_1_enum import PaymentMethod1Enum
from fortisapi.models.status_enum import StatusEnum
from fortisapi.models.v_1_recurrings_request_1 import V1RecurringsRequest1

client = FortisapiClient(
    user_id_credentials=UserIdCredentials(
        user_id='user-id'
    ),
    user_api_key_credentials=UserApiKeyCredentials(
        user_api_key='user-api-key'
    ),
    developer_id_credentials=DeveloperIdCredentials(
        developer_id='developer-id'
    ),
    environment=Environment.SANDBOX
)

recurring_controller = client.recurring
recurring_id = '11e95f8ec39de8fbdb0a4f1a'

body = V1RecurringsRequest1(
    next_run_date='2021-12-01',
    account_vault_id='11e95f8ec39de8fbdb0a4f1a',
    token_id='11e95f8ec39de8fbdb0a4f1a',
    active=True,
    description='Description',
    end_date='2021-12-01',
    installment_total_count=20,
    interval=1,
    interval_type=IntervalTypeEnum.D,
    location_id='11e95f8ec39de8fbdb0a4f1a',
    notification_days=2,
    payment_method=PaymentMethod1Enum.CC,
    product_transaction_id='11e95f8ec39de8fbdb0a4f1a',
    recurring_id='11e95f8ec39de8fbdb0a4f1a',
    recurring_api_id='recurring1234abcd',
    start_date='2021-12-01',
    status=StatusEnum.ACTIVE,
    transaction_amount=300,
    terms_agree=True,
    terms_agree_ip='192.168.0.10',
    recurring_c_1='recurring custom data 1',
    recurring_c_2='recurring custom data 2',
    recurring_c_3='recurring custom data 3',
    send_to_proc_as_recur=True,
    contact_id='11e95f8ec39de8fbdb0a4f1a'
)

try:
    result = recurring_controller.update_recurring_payment(
        recurring_id,
        body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except Response401tokenException as e: 
    print(e)
except Response412Exception as e: 
    print(e)
except APIException as e: 
    print(e)

