# Merchants

Merchant details for transaction processing entities. Together with the entities table, this table defines a merchant. A merchant is primarily an entity that accepts payments and transacts with customers in Payrix Pro.

```python
merchants_controller = client.merchants
```

## Class Name

`MerchantsController`

## Methods

* [Get Merchants](../../doc/controllers/merchants.md#get-merchants)
* [Post Merchants](../../doc/controllers/merchants.md#post-merchants)
* [Get Merchants Id](../../doc/controllers/merchants.md#get-merchants-id)
* [Put Merchants Id](../../doc/controllers/merchants.md#put-merchants-id)
* [Delete Merchants Id](../../doc/controllers/merchants.md#delete-merchants-id)


# Get Merchants

Query a Merchant, an organization that processes credit card payments, each associated with an Entity.

```python
def get_merchants(self,
                 request_token=None,
                 search=None,
                 totals=None,
                 page_number=None,
                 page_limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |
| `search` | `str` | Header, Optional | Set this header to filter or sort the list of resources that the method returns.<br>See [Searches](page:welcome#searches) for detailed information and examples on how to use search header. |
| `totals` | `str` | Header, Optional | To configure a request to return a total for all instances of a field in a result set,  use the totals header in the format `totals={operator}[]={key}`.  This will calculate the desired total and return it in the `details > totals` object of the response.  For instance, if you want to sum the `total` field of all transactions,  you would use the `sum` operator. The response will include the result set,  along with the calculated total in the `details` section. See [Collection Operators](page:welcome#collection-operators) for detailed information and examples on how to use totals header. |
| `page_number` | `int` | Query, Optional | Set this path parameter to request a specific page of records.<br>For example, set `?page[number]=2` to retrieve the second page of records for this request. |
| `page_limit` | `int` | Query, Optional | Set this path parameter to request up to a specific amount of records. By default 30 records are retrieved per page. The maximum limit that can be set is 100.<br>For example, set `?page[limit]=50` to retrieve up to 50 records for this request. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MerchantsResponseResult`](../../doc/models/merchants-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = merchants_controller.get_merchants(
    request_token=request_token,
    search=search,
    totals=totals,
    page_number=page_number,
    page_limit=page_limit
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "response": {
    "data": [
      {
        "id": "p1_mer_00c66ace58ad2d376bb0067",
        "created": "2025-03-03 21:51:58.4016",
        "modified": "2025-03-03 22:56:04.3579",
        "creator": "p1_log_0067be40688861230a79682",
        "modifier": "p1_log_00c66acd69830f6a0d4718b",
        "lastActivity": "2025-03-03 21:51:58",
        "entity": "p1_ent_00c66acd8154446fc5567a3",
        "dba": "Colorado Blitz",
        "new": 0,
        "established": 20250226,
        "annualCCSales": 750000,
        "avgTicket": 15000,
        "amex": "",
        "discover": "",
        "mcc": "7997",
        "status": 2,
        "boarded": 20250303,
        "inactive": 0,
        "frozen": 0,
        "environment": "ecommerce",
        "visaMvv": "",
        "chargebackNotificationEmail": "",
        "statusReason": "",
        "totalApprovedSales": 0,
        "autoBoarded": 1,
        "saqType": "SAQ-A",
        "saqDate": 20250303,
        "qsa": "",
        "letterStatus": 0,
        "letterDate": 20250303,
        "tcAttestation": 1,
        "visaDisclosure": 1,
        "disclosureIP": "67.174.101.19",
        "disclosureDate": 20250303,
        "accountClosureReasonCode": "",
        "accountClosureReasonDate": 20250303,
        "annualCCSaleVolume": 0,
        "annualACHSaleVolume": 0,
        "riskLevel": "restricted",
        "creditRatio": 0,
        "creditTimeliness": 0,
        "chargebackRatio": 0,
        "ndxDays": 0,
        "ndxPercentage": 0,
        "advancedBilling": 0,
        "locationType": 77,
        "percentKeyed": 0,
        "totalVolume": 0,
        "percentEcomm": 0,
        "seasonal": 0,
        "amexVolume": 0,
        "incrementalAuthSupported": 0,
        "tmxSessionId": "6395015c-b0cc-45ba-abdc-aaf17123a4db",
        "percentBusiness": 0,
        "applePayActive": 0,
        "applePayStatus": "",
        "googlePayActive": 1,
        "passTokenEnabled": 0,
        "naics": "11",
        "naicsDescription": "",
        "expressBatchCloseMethod": "TimeInitiated",
        "expressBatchCloseTime": ""
      }
    ],
    "details": {
      "requestId": "1",
      "totals": [],
      "page": {
        "current": 1,
        "last": 1,
        "hasMore": false
      }
    },
    "errors": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ErrorFourHundredException`](../../doc/models/error-four-hundred-exception.md) |


# Post Merchants

Create a new Merchant. Details for creating one will be available soon.

```python
def post_merchants(self,
                  body,
                  request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`MerchantsPostRequest`](../../doc/models/merchants-post-request.md) | Body, Required | - |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MerchantsResponseResult`](../../doc/models/merchants-response-result.md).

## Example Usage

```python
body = MerchantsPostRequest(
    entity='p1_ent_00c94cb712c4cb8ecbe4c88',
    new=NewEnum.NOTNEW,
    annual_cc_sales=2530,
    avg_ticket=56000,
    environment=MerchantEnvironmentEnum.CARDPRESENT,
    status=MerchantStatusEnum.BOARDED,
    total_approved_sales=0,
    dba='DISPOSAL LLC',
    advanced_billing=AdvancedBillingEnum.DISABLED,
    seasonal=SeasonalEnum.YEARROUND,
    established=20210916,
    annual_cc_sale_volume=2530,
    annual_ach_sale_volume=2530,
    amex_volume=0,
    amex='American Express merchant identifier',
    discover='Discover merchant identifier',
    mcc='1799',
    visa_mvv='Merchant Verification Value',
    visa_disclosure=VisaDisclosureEnum.NOTACCEPTED,
    disclosure_ip='11.11.11.111',
    disclosure_date=20250307,
    incremental_auth_supported=IncrementalAuthSupportedEnum.NOTSUPPORTED,
    auto_boarded=AutoBoardedEnum.AUTOBOARDED,
    status_reason=StatusReasonEnum.FRAUD,
    location_type=MerchantLocationTypeEnum.RETAILSTOREFRONT,
    percent_ecomm=70,
    percent_keyed=30,
    percent_business=0,
    total_volume=1000000,
    account_closure_reason_code='reason code',
    account_closure_reason_date=20250307,
    risk_level=RiskLevelEnum.RESTRICTED,
    credit_ratio=0,
    credit_timeliness=0,
    chargeback_ratio=0,
    ndx_days=1,
    ndx_percentage=0,
    saq_type=SaqTypeEnum.SAQA,
    saq_date=20250307,
    qsa='0',
    letter_status=LetterStatusEnum.OFF,
    letter_date=20250307,
    chargeback_notification_email='Notification Email',
    tc_attestation=TcAttestationEnum.NOTACCEPTED,
    apple_pay_active=ApplePayActiveEnum.INACTIVE,
    google_pay_active=GooglePayActiveEnum.ACTIVE,
    naics=NaicsEnum.AGRICULTURE,
    naics_description='other',
    tmx_session_id='007462d6-a1df-40f4-b998-35bfa5539562',
    pass_token_enabled=PassTokenEnabledEnum.DISABLED,
    express_batch_close_method=ExpressBatchCloseMethodEnum.TIMEINITIATED,
    express_batch_close_time='03:00:00',
    omni_token_enabled=OmniTokenEnabledEnum.DISABLED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = merchants_controller.post_merchants(
    body,
    request_token=request_token
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "response": {
    "data": [
      {
        "id": "p1_mer_00c66ace58ad2d376bb0067",
        "created": "2025-03-03 21:51:58.4016",
        "modified": "2025-03-03 22:56:04.3579",
        "creator": "p1_log_0067be40688861230a79682",
        "modifier": "p1_log_00c66acd69830f6a0d4718b",
        "lastActivity": "2025-03-03 21:51:58",
        "entity": "p1_ent_00c66acd8154446fc5567a3",
        "dba": "Colorado Blitz",
        "new": 0,
        "established": 20250226,
        "annualCCSales": 750000,
        "avgTicket": 15000,
        "amex": "",
        "discover": "",
        "mcc": "7997",
        "status": 2,
        "boarded": 20250303,
        "inactive": 0,
        "frozen": 0,
        "environment": "ecommerce",
        "visaMvv": "",
        "chargebackNotificationEmail": "",
        "statusReason": "",
        "totalApprovedSales": 0,
        "autoBoarded": 1,
        "saqType": "SAQ-A",
        "saqDate": 20250303,
        "qsa": "",
        "letterStatus": 0,
        "letterDate": 20250303,
        "tcAttestation": 1,
        "visaDisclosure": 1,
        "disclosureIP": "67.174.101.19",
        "disclosureDate": 20250303,
        "accountClosureReasonCode": "",
        "accountClosureReasonDate": 20250303,
        "annualCCSaleVolume": 0,
        "annualACHSaleVolume": 0,
        "riskLevel": "restricted",
        "creditRatio": 0,
        "creditTimeliness": 0,
        "chargebackRatio": 0,
        "ndxDays": 0,
        "ndxPercentage": 0,
        "advancedBilling": 0,
        "locationType": 77,
        "percentKeyed": 0,
        "totalVolume": 0,
        "percentEcomm": 0,
        "seasonal": 0,
        "amexVolume": 0,
        "incrementalAuthSupported": 0,
        "tmxSessionId": "6395015c-b0cc-45ba-abdc-aaf17123a4db",
        "percentBusiness": 0,
        "applePayActive": 0,
        "applePayStatus": "",
        "googlePayActive": 1,
        "passTokenEnabled": 0,
        "naics": "11",
        "naicsDescription": "",
        "expressBatchCloseMethod": "TimeInitiated",
        "expressBatchCloseTime": ""
      }
    ],
    "details": {
      "requestId": "1",
      "totals": [],
      "page": {
        "current": 1,
        "last": 1,
        "hasMore": false
      }
    },
    "errors": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ErrorFourHundredException`](../../doc/models/error-four-hundred-exception.md) |


# Get Merchants Id

Query a Merchant, which is an organization that processes credit card payments and each is associated with an Entity.

```python
def get_merchants_id(self,
                    id,
                    request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource, also known as the Merchant ID (MID). |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MerchantsResponseResult`](../../doc/models/merchants-response-result.md).

## Example Usage

```python
id = 'p1_mer_00c6b12d04ac280ed694323'

request_token = '20250423-yourmerchant-refunds-001'

result = merchants_controller.get_merchants_id(
    id,
    request_token=request_token
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "response": {
    "data": [
      {
        "id": "p1_mer_00c66ace58ad2d376bb0067",
        "created": "2025-03-03 21:51:58.4016",
        "modified": "2025-03-03 22:56:04.3579",
        "creator": "p1_log_0067be40688861230a79682",
        "modifier": "p1_log_00c66acd69830f6a0d4718b",
        "lastActivity": "2025-03-03 21:51:58",
        "entity": "p1_ent_00c66acd8154446fc5567a3",
        "dba": "Colorado Blitz",
        "new": 0,
        "established": 20250226,
        "annualCCSales": 750000,
        "avgTicket": 15000,
        "amex": "",
        "discover": "",
        "mcc": "7997",
        "status": 2,
        "boarded": 20250303,
        "inactive": 0,
        "frozen": 0,
        "environment": "ecommerce",
        "visaMvv": "",
        "chargebackNotificationEmail": "",
        "statusReason": "",
        "totalApprovedSales": 0,
        "autoBoarded": 1,
        "saqType": "SAQ-A",
        "saqDate": 20250303,
        "qsa": "",
        "letterStatus": 0,
        "letterDate": 20250303,
        "tcAttestation": 1,
        "visaDisclosure": 1,
        "disclosureIP": "67.174.101.19",
        "disclosureDate": 20250303,
        "accountClosureReasonCode": "",
        "accountClosureReasonDate": 20250303,
        "annualCCSaleVolume": 0,
        "annualACHSaleVolume": 0,
        "riskLevel": "restricted",
        "creditRatio": 0,
        "creditTimeliness": 0,
        "chargebackRatio": 0,
        "ndxDays": 0,
        "ndxPercentage": 0,
        "advancedBilling": 0,
        "locationType": 77,
        "percentKeyed": 0,
        "totalVolume": 0,
        "percentEcomm": 0,
        "seasonal": 0,
        "amexVolume": 0,
        "incrementalAuthSupported": 0,
        "tmxSessionId": "6395015c-b0cc-45ba-abdc-aaf17123a4db",
        "percentBusiness": 0,
        "applePayActive": 0,
        "applePayStatus": "",
        "googlePayActive": 1,
        "passTokenEnabled": 0,
        "naics": "11",
        "naicsDescription": "",
        "expressBatchCloseMethod": "TimeInitiated",
        "expressBatchCloseTime": ""
      }
    ],
    "details": {
      "requestId": "1",
      "totals": [],
      "page": {
        "current": 1,
        "last": 1,
        "hasMore": false
      }
    },
    "errors": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ErrorFourHundredException`](../../doc/models/error-four-hundred-exception.md) |


# Put Merchants Id

Update a Merchant, A Merchant is an organization that processes credit card payments. Each Merchant is associated with an Entity.

```python
def put_merchants_id(self,
                    id,
                    body,
                    request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource, also known as the Merchant ID (MID). |
| `body` | [`MerchantsPutRequest`](../../doc/models/merchants-put-request.md) | Body, Required | Update Merchant Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MerchantsResponseResult`](../../doc/models/merchants-response-result.md).

## Example Usage

```python
id = 'p1_mer_00c6b12d04ac280ed694323'

body = MerchantsPutRequest(
    total_approved_sales=0,
    entity='p1_ent_00c94cb712c4cb8ecbe4c88',
    dba='DISPOSAL LLC',
    new=NewEnum.NOTNEW,
    advanced_billing=AdvancedBillingEnum.DISABLED,
    seasonal=SeasonalEnum.YEARROUND,
    established=20210916,
    annual_cc_sales=2530,
    annual_cc_sale_volume=2530,
    annual_ach_sale_volume=2530,
    amex_volume=0,
    avg_ticket=56000,
    amex='American Express merchant identifier',
    discover='Discover merchant identifier',
    mcc='1799',
    visa_mvv='Merchant Verification Value',
    visa_disclosure=VisaDisclosureEnum.NOTACCEPTED,
    disclosure_ip='11.11.11.111',
    disclosure_date=20250307,
    environment=MerchantEnvironmentEnum.CARDPRESENT,
    status=MerchantStatusEnum.BOARDED,
    incremental_auth_supported=IncrementalAuthSupportedEnum.NOTSUPPORTED,
    auto_boarded=AutoBoardedEnum.AUTOBOARDED,
    status_reason=StatusReasonEnum.FRAUD,
    location_type=MerchantLocationTypeEnum.RETAILSTOREFRONT,
    percent_ecomm=70,
    percent_keyed=30,
    percent_business=0,
    total_volume=1000000,
    account_closure_reason_code='reason code',
    account_closure_reason_date=20250307,
    risk_level=RiskLevelEnum.RESTRICTED,
    credit_ratio=0,
    credit_timeliness=0,
    chargeback_ratio=0,
    ndx_days=1,
    ndx_percentage=0,
    saq_type=SaqTypeEnum.SAQA,
    saq_date=20250307,
    qsa='0',
    letter_status=LetterStatusEnum.OFF,
    letter_date=20250307,
    chargeback_notification_email='Notification Email',
    tc_attestation=TcAttestationEnum.NOTACCEPTED,
    apple_pay_active=ApplePayActiveEnum.INACTIVE,
    google_pay_active=GooglePayActiveEnum.ACTIVE,
    naics=NaicsEnum.AGRICULTURE,
    naics_description='other',
    tmx_session_id='007462d6-a1df-40f4-b998-35bfa5539562',
    pass_token_enabled=PassTokenEnabledEnum.DISABLED,
    express_batch_close_method=ExpressBatchCloseMethodEnum.TIMEINITIATED,
    express_batch_close_time='03:00:00',
    tin_status=0,
    omni_token_enabled=OmniTokenEnabledEnum.DISABLED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = merchants_controller.put_merchants_id(
    id,
    body,
    request_token=request_token
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "response": {
    "data": [
      {
        "id": "p1_mer_00c66ace58ad2d376bb0067",
        "created": "2025-03-03 21:51:58.4016",
        "modified": "2025-03-03 22:56:04.3579",
        "creator": "p1_log_0067be40688861230a79682",
        "modifier": "p1_log_00c66acd69830f6a0d4718b",
        "lastActivity": "2025-03-03 21:51:58",
        "entity": "p1_ent_00c66acd8154446fc5567a3",
        "dba": "Colorado Blitz",
        "new": 0,
        "established": 20250226,
        "annualCCSales": 750000,
        "avgTicket": 15000,
        "amex": "",
        "discover": "",
        "mcc": "7997",
        "status": 2,
        "boarded": 20250303,
        "inactive": 0,
        "frozen": 0,
        "environment": "ecommerce",
        "visaMvv": "",
        "chargebackNotificationEmail": "",
        "statusReason": "",
        "totalApprovedSales": 0,
        "autoBoarded": 1,
        "saqType": "SAQ-A",
        "saqDate": 20250303,
        "qsa": "",
        "letterStatus": 0,
        "letterDate": 20250303,
        "tcAttestation": 1,
        "visaDisclosure": 1,
        "disclosureIP": "67.174.101.19",
        "disclosureDate": 20250303,
        "accountClosureReasonCode": "",
        "accountClosureReasonDate": 20250303,
        "annualCCSaleVolume": 0,
        "annualACHSaleVolume": 0,
        "riskLevel": "restricted",
        "creditRatio": 0,
        "creditTimeliness": 0,
        "chargebackRatio": 0,
        "ndxDays": 0,
        "ndxPercentage": 0,
        "advancedBilling": 0,
        "locationType": 77,
        "percentKeyed": 0,
        "totalVolume": 0,
        "percentEcomm": 0,
        "seasonal": 0,
        "amexVolume": 0,
        "incrementalAuthSupported": 0,
        "tmxSessionId": "6395015c-b0cc-45ba-abdc-aaf17123a4db",
        "percentBusiness": 0,
        "applePayActive": 0,
        "applePayStatus": "",
        "googlePayActive": 1,
        "passTokenEnabled": 0,
        "naics": "11",
        "naicsDescription": "",
        "expressBatchCloseMethod": "TimeInitiated",
        "expressBatchCloseTime": ""
      }
    ],
    "details": {
      "requestId": "1",
      "totals": [],
      "page": {
        "current": 1,
        "last": 1,
        "hasMore": false
      }
    },
    "errors": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ErrorFourHundredException`](../../doc/models/error-four-hundred-exception.md) |


# Delete Merchants Id

Delete a Merchant. A Merchant is an organization that processes credit card payments. Each Merchant is associated with an Entity.

```python
def delete_merchants_id(self,
                       id,
                       request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource, also known as the Merchant ID (MID). |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MerchantsResponseResult`](../../doc/models/merchants-response-result.md).

## Example Usage

```python
id = 'p1_mer_00c6b12d04ac280ed694323'

request_token = '20250423-yourmerchant-refunds-001'

result = merchants_controller.delete_merchants_id(
    id,
    request_token=request_token
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "response": {
    "data": [
      {
        "id": "p1_mer_00c66ace58ad2d376bb0067",
        "created": "2025-03-03 21:51:58.4016",
        "modified": "2025-03-03 22:56:04.3579",
        "creator": "p1_log_0067be40688861230a79682",
        "modifier": "p1_log_00c66acd69830f6a0d4718b",
        "lastActivity": "2025-03-03 21:51:58",
        "entity": "p1_ent_00c66acd8154446fc5567a3",
        "dba": "Colorado Blitz",
        "new": 0,
        "established": 20250226,
        "annualCCSales": 750000,
        "avgTicket": 15000,
        "amex": "",
        "discover": "",
        "mcc": "7997",
        "status": 2,
        "boarded": 20250303,
        "inactive": 0,
        "frozen": 0,
        "environment": "ecommerce",
        "visaMvv": "",
        "chargebackNotificationEmail": "",
        "statusReason": "",
        "totalApprovedSales": 0,
        "autoBoarded": 1,
        "saqType": "SAQ-A",
        "saqDate": 20250303,
        "qsa": "",
        "letterStatus": 0,
        "letterDate": 20250303,
        "tcAttestation": 1,
        "visaDisclosure": 1,
        "disclosureIP": "67.174.101.19",
        "disclosureDate": 20250303,
        "accountClosureReasonCode": "",
        "accountClosureReasonDate": 20250303,
        "annualCCSaleVolume": 0,
        "annualACHSaleVolume": 0,
        "riskLevel": "restricted",
        "creditRatio": 0,
        "creditTimeliness": 0,
        "chargebackRatio": 0,
        "ndxDays": 0,
        "ndxPercentage": 0,
        "advancedBilling": 0,
        "locationType": 77,
        "percentKeyed": 0,
        "totalVolume": 0,
        "percentEcomm": 0,
        "seasonal": 0,
        "amexVolume": 0,
        "incrementalAuthSupported": 0,
        "tmxSessionId": "6395015c-b0cc-45ba-abdc-aaf17123a4db",
        "percentBusiness": 0,
        "applePayActive": 0,
        "applePayStatus": "",
        "googlePayActive": 1,
        "passTokenEnabled": 0,
        "naics": "11",
        "naicsDescription": "",
        "expressBatchCloseMethod": "TimeInitiated",
        "expressBatchCloseTime": ""
      }
    ],
    "details": {
      "requestId": "1",
      "totals": [],
      "page": {
        "current": 1,
        "last": 1,
        "hasMore": false
      }
    },
    "errors": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ErrorFourHundredException`](../../doc/models/error-four-hundred-exception.md) |

