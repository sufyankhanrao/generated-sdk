# VAS Efe Offers

```python
vas_efe_offers_controller = client.vas_efe_offers
```

## Class Name

`VASEfeOffersController`

## Methods

* [Get Vas Efe Offers Id](../../doc/controllers/vas-efe-offers.md#get-vas-efe-offers-id)
* [Get Vas Efe Offers](../../doc/controllers/vas-efe-offers.md#get-vas-efe-offers)


# Get Vas Efe Offers Id

Query a vasEfeOffers.

```python
def get_vas_efe_offers_id(self,
                         id,
                         request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`VasEfeOffersResponseResult`](../../doc/models/vas-efe-offers-response-result.md).

## Example Usage

```python
id = '000000000000002'

request_token = '20250423-yourmerchant-refunds-001'

result = vas_efe_offers_controller.get_vas_efe_offers_id(
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
        "id": "000000000000002",
        "created": "2025-06-05 16:36:15.9522",
        "modified": "2025-06-05 16:36:15.9522",
        "creator": "000000000000001",
        "modifier": "000000000000001",
        "offerId": "c00ef79c-f024-4254-ae17-c67a2e691d00",
        "expiry": "2029-12-03 00:00:00",
        "entity": "000000000000001",
        "mid": "4445061757076",
        "primaryContactEmail": "jorge@fisglobal.com",
        "merchantLenderId": "M67890",
        "vendorName": "Parafin",
        "offerDate": "2024-12-03 22:35:18.3837",
        "totalApprovedAmount": "10000.000",
        "feeAmount": "1250.000",
        "originationFee": "",
        "offerUrl": "efos-test-merchant-portal.nonprod.nb01.local/offers/c00ef79c-f024-4254-ae17-c67a2e691d00",
        "productName": "flex loan",
        "productLongDescription": "Loan1",
        "acquirePlatform": "",
        "prequalificationSentDate": "2024-12-03 22:35:18.3837",
        "prequalificationReceivedDate": "2024-12-03 22:35:18.3837",
        "isMerchantPrequalified": 0,
        "appliedDate": "2024-12-03 22:35:18.3837",
        "offerStatus": "ACTIVE",
        "productCode": "",
        "startDate": "2024-12-03 22:35:18.3837",
        "endDate": "2024-12-03 22:35:18.3837",
        "splitFundingCap": "",
        "splitFundingRate": "",
        "dailyFundingMaxLimit": "",
        "splitFundingAmount": "",
        "optInDate": "2024-12-03 22:35:18.3837",
        "splitSettlementEnabled": 0
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


# Get Vas Efe Offers

Query a vasEfeOffers.

```python
def get_vas_efe_offers(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`VasEfeOffersResponseResult`](../../doc/models/vas-efe-offers-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = vas_efe_offers_controller.get_vas_efe_offers(
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
        "id": "000000000000002",
        "created": "2025-06-05 16:36:15.9522",
        "modified": "2025-06-05 16:36:15.9522",
        "creator": "000000000000001",
        "modifier": "000000000000001",
        "offerId": "c00ef79c-f024-4254-ae17-c67a2e691d00",
        "expiry": "2029-12-03 00:00:00",
        "entity": "000000000000001",
        "mid": "4445061757076",
        "primaryContactEmail": "jorge@fisglobal.com",
        "merchantLenderId": "M67890",
        "vendorName": "Parafin",
        "offerDate": "2024-12-03 22:35:18.3837",
        "totalApprovedAmount": "10000.000",
        "feeAmount": "1250.000",
        "originationFee": "",
        "offerUrl": "efos-test-merchant-portal.nonprod.nb01.local/offers/c00ef79c-f024-4254-ae17-c67a2e691d00",
        "productName": "flex loan",
        "productLongDescription": "Loan1",
        "acquirePlatform": "",
        "prequalificationSentDate": "2024-12-03 22:35:18.3837",
        "prequalificationReceivedDate": "2024-12-03 22:35:18.3837",
        "isMerchantPrequalified": 0,
        "appliedDate": "2024-12-03 22:35:18.3837",
        "offerStatus": "ACTIVE",
        "productCode": "",
        "startDate": "2024-12-03 22:35:18.3837",
        "endDate": "2024-12-03 22:35:18.3837",
        "splitFundingCap": "",
        "splitFundingRate": "",
        "dailyFundingMaxLimit": "",
        "splitFundingAmount": "",
        "optInDate": "2024-12-03 22:35:18.3837",
        "splitSettlementEnabled": 0
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

