
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 60** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](../doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| custom_header_authentication_credentials | [`CustomHeaderAuthenticationCredentials`](auth/custom-header-signature.md) | The credential object for Custom Header Signature |

The API client can be initialized as follows:

## Code-Based Client Initialization

```python
from payfacsubmerchantprovisioningapi.configuration import Environment
from payfacsubmerchantprovisioningapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from payfacsubmerchantprovisioningapi.payfacsubmerchantprovisioningapi_client import PayfacsubmerchantprovisioningapiClient

client = PayfacsubmerchantprovisioningapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)
```

## Environment-Based Client Initialization

```python
from payfacsubmerchantprovisioningapi.payfacsubmerchantprovisioningapi_client import PayfacsubmerchantprovisioningapiClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = PayfacsubmerchantprovisioningapiClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](../doc/environment-based-client-initialization.md) section for details.

## PayFac: Submerchant Provisioning API Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| health | Gets HealthController |
| divisions | Gets DivisionsController |
| chains | Gets ChainsController |
| sub_merchant | Gets SubMerchantController |
| owners | Gets OwnersController |
| resource_id | Gets ResourceIDController |
| issued_i_ds | Gets IssuedIDsController |
| contacts | Gets ContactsController |
| addresses | Gets AddressesController |
| accepted_cards | Gets AcceptedCardsController |
| default_bank_account | Gets DefaultBankAccountController |
| advanced_settlement_account | Gets AdvancedSettlementAccountController |
| underwriting_status | Gets UnderwritingStatusController |
| terminals | Gets TerminalsController |
| express_sub_account | Gets ExpressSubAccountController |
| vas_omni_token | Gets VASOmniTokenController |
| vas_pass_token | Gets VASPASSTokenController |
| vas_recurring_billing | Gets VASRecurringBillingController |
| vas_account_updater | Gets VASAccountUpdaterController |
| vas_pi_nless_debit | Gets VASPINlessDebitController |
| vas_pin_debit | Gets VASPINDebitController |
| vas_e_check | Gets VASECheckController |
| vas_fraud_sight | Gets VASFraudSightController |
| vas_review_trackers | Gets VASReviewTrackersController |
| vas_apple_pay | Gets VASApplePayController |
| vas_google_pay | Gets VASGooglePayController |
| vas_hpp | Gets VASHPPController |

