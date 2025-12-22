from webhooksandcallbacksapi.configuration import Environment
from webhooksandcallbacksapi.exceptions.api_exception import APIException
from webhooksandcallbacksapi.exceptions.error_exception import ErrorException
from webhooksandcallbacksapi.http.auth.api_key import ApiKeyCredentials
from webhooksandcallbacksapi.http.auth.bearer_auth import BearerAuthCredentials
from webhooksandcallbacksapi.models.create_order_request import CreateOrderRequest
from webhooksandcallbacksapi.models.order_item import OrderItem
from webhooksandcallbacksapi.webhooksandcallbacksapi_client import WebhooksandcallbacksapiClient

client = WebhooksandcallbacksapiClient(
    api_key_credentials=ApiKeyCredentials(
        x_api_key='X-API-Key'
    ),
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.PRODUCTION
)

orders_controller = client.orders
body = CreateOrderRequest(
    customer_id='cust_12345',
    items=[
        OrderItem(
            product_id='prod_001',
            quantity=2,
            price=29.99
        )
    ],
    callback_url='https://merchant.example.com/callbacks/payment'
)

try:
    result = orders_controller.create_order(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

