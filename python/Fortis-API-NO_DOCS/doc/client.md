
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| environment | `Environment` | The API environment. <br> **Default: `Environment.SANDBOX`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 60** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](../doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| user_id_credentials | [`UserIdCredentials`](auth/custom-header-signature.md) | The credential object for Custom Header Signature |
| user_api_key_credentials | [`UserApiKeyCredentials`](auth/custom-header-signature-1.md) | The credential object for Custom Header Signature |
| developer_id_credentials | [`DeveloperIdCredentials`](auth/custom-header-signature-2.md) | The credential object for Custom Header Signature |
| access_token_credentials | [`AccessTokenCredentials`](auth/custom-header-signature-3.md) | The credential object for Custom Header Signature |

The API client can be initialized as follows:

## Code-Based Client Initialization

```python
from fortisapi.configuration import Environment
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.access_token import AccessTokenCredentials
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials

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
    access_token_credentials=AccessTokenCredentials(
        access_token='access-token'
    ),
    environment=Environment.SANDBOX
)
```

## Environment-Based Client Initialization

```python
from fortisapi.fortisapi_client import FortisapiClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = FortisapiClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](../doc/environment-based-client-initialization.md) section for details.

## Fortis API Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| async_processing | Gets AsyncProcessingController |
| batches | Gets BatchesController |
| contacts | Gets ContactsController |
| declined_recurring_transactions | Gets DeclinedRecurringTransactionsController |
| device_terms | Gets DeviceTermsController |
| elements | Gets ElementsController |
| full_boarding | Gets FullBoardingController |
| locations | Gets LocationsController |
| on_boarding | Gets OnBoardingController |
| paylinks | Gets PaylinksController |
| quick_invoices | Gets QuickInvoicesController |
| recurring | Gets RecurringController |
| signatures | Gets SignaturesController |
| tags | Gets TagsController |
| terminals | Gets TerminalsController |
| tickets | Gets TicketsController |
| tokens | Gets TokensController |
| transactions_ach | Gets TransactionsACHController |
| transactions_cash | Gets TransactionsCashController |
| transactions_credit_card | Gets TransactionsCreditCardController |
| transactions_read | Gets TransactionsReadController |
| level_3_data | Gets Level3DataController |
| transactions_updates | Gets TransactionsUpdatesController |
| user_verifications | Gets UserVerificationsController |
| users | Gets UsersController |
| merchant_details | Gets MerchantDetailsController |
| apple_pay_validate_merchant | Gets ApplePayValidateMerchantController |
| webhooks | Gets WebhooksController |

