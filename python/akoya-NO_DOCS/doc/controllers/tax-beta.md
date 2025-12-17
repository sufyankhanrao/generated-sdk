# Tax Beta

```python
tax_beta_api = client.tax_beta
```

## Class Name

`TaxBetaApi`

## Methods

* [Tax Forms Search](../../doc/controllers/tax-beta.md#tax-forms-search)
* [Get Tax Form](../../doc/controllers/tax-beta.md#get-tax-form)


# Tax Forms Search

Get the full lists of tax document data and tax form images available for a specific year for the current authorized customer.

```python
def tax_forms_search(self,
                    version,
                    provider_id,
                    x_akoya_interaction_id=None,
                    x_akoya_interaction_type=None,
                    accept=None,
                    tax_year=None,
                    tax_forms=None,
                    account_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | [`Version`](../../doc/models/version.md) | Template, Required | Endpoint version. |
| `provider_id` | `str` | Template, Required | Provider to query for Tax data. |
| `x_akoya_interaction_id` | `str` | Header, Optional | Unique identifier to associate with this request. No specific format required. |
| `x_akoya_interaction_type` | [`InteractionType`](../../doc/models/interaction-type.md) | Header, Optional | Identifies whether the customer is present (USER) or it is a BATCH operation. Case-insensitive. |
| `accept` | [`List[MediaType]`](../../doc/models/media-type.md) | Header, Optional | Use the [Accept HTTP request header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept) to indicate one or more content types to request for the search result response. Use `application/json` to request data or `application/pdf to request images in comma-separated array format.         Use in combination with TaxDataTypeQuery parameter to request `application/json` responses in ''JSON'' or ''BASE64_PDF'' format for tax form data' |
| `tax_year` | `str` | Query, Optional | Tax year in which to search for tax forms. |
| `tax_forms` | [`List[TypeFormType]`](../../doc/models/type-form-type.md) | Query, Optional | One or more tax form type enums for the specific documents being requested. Comma separated |
| `account_id` | `str` | Query, Optional | Unique account identifier (not the account number) |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TaxStatementList`](../../doc/models/tax-statement-list.md).

## Example Usage

```python
version = Version.V2

provider_id = 'providerId6'

x_akoya_interaction_id = 'unique-request-id-001'

x_akoya_interaction_type = InteractionType.USER

accept = [
    MediaType.ENUM_APPLICATIONJSON
]

tax_year = '2024'

tax_forms = [
    TypeFormType.TAX1099DIV,
    TypeFormType.TAX1099INT
]

result = tax_beta_api.tax_forms_search(
    version,
    provider_id,
    x_akoya_interaction_id=x_akoya_interaction_id,
    x_akoya_interaction_type=x_akoya_interaction_type,
    accept=accept,
    tax_year=tax_year,
    tax_forms=tax_forms
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "statements": [
    {
      "taxYear": 2020,
      "taxStatementId": "9876987698769876",
      "attributes": [
        {
          "name": "federalTaxWithheld",
          "value": "4014.00"
        }
      ],
      "taxDataType": "JSON",
      "forms": [
        {
          "tax1099Div": {
            "taxYear": 2020,
            "taxFormId": "9876987698769876",
            "taxFormDate": "2021-03-30",
            "additionalInformation": "FDX v6.0",
            "taxFormType": "Tax1099Div"
          }
        }
      ]
    },
    {
      "taxYear": 2020,
      "taxStatementId": "6543654365436543",
      "attributes": [
        {
          "name": "federalTaxWithheld",
          "value": "4011.00"
        }
      ],
      "taxDataType": "JSON",
      "forms": [
        {
          "tax1099Int": {
            "taxYear": 2020,
            "taxFormId": "6543654365436543",
            "taxFormDate": "2021-03-30",
            "additionalInformation": "FDX v6.0",
            "taxFormType": "Tax1099Int"
          }
        }
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 404 | Not Found | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 405 | Method Not Allowed | `ApiException` |
| 406 | Content Type not Supported | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 408 | Request timed out (round trip call took >10 seconds). | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 409 | Conflict | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 500 | Catch-all exception where request was not processed due to an internal outage/issue. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 501 | FdxVersion in header is not implemented. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 503 | System is down for maintenance. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Get Tax Form

Get the Tax Statement as JSON or PDF for a single tax document for the customer. Use [HTTP Accept request-header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html) to specify desired content types. See `AcceptHeader` definition for typical values.

Not all providers support PDF payloads. See [this article](https://recipient.ddp.akoya.com/support/article/kA0Uw00000026VxKAI) in the Data Recipent Hub for a list of providers that support document PDFs.

```python
def get_tax_form(self,
                version,
                provider_id,
                tax_form_id,
                x_akoya_interaction_id=None,
                x_akoya_interaction_type=None,
                tax_data_type=None,
                accept=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | [`Version`](../../doc/models/version.md) | Template, Required | Endpoint version. |
| `provider_id` | `str` | Template, Required | Provider to query for Tax data. |
| `tax_form_id` | `str` | Template, Required | Unique identifier of the tax form to request. |
| `x_akoya_interaction_id` | `str` | Header, Optional | Unique identifier to associate with this request. No specific format required. |
| `x_akoya_interaction_type` | [`InteractionType`](../../doc/models/interaction-type.md) | Header, Optional | Identifies whether the customer is present (USER) or it is a BATCH operation. Case-insensitive. |
| `tax_data_type` | [`TypeDataType`](../../doc/models/type-data-type.md) | Query, Optional | Use taxDataType to request `application/json` tax form data response in 'JSON' or 'BASE64_PDF' format. Omit if either format is acceptable. Used in combination with AcceptHeader requesting `application/json` response |
| `accept` | [`List[MediaType]`](../../doc/models/media-type.md) | Header, Optional | Use the [Accept HTTP request header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept) to indicate one or more content types to request for the search result response. Use `application/json` to request data or `application/pdf`to request images. In comma-separated array format.         Use in combination with TaxDataTypeQuery parameter to request `application/json` responses in ''JSON'' or ''BASE64_PDF'' format for tax form data' |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TaxStatement`](../../doc/models/tax-statement.md).

## Example Usage

```python
version = Version.V2

provider_id = 'providerId6'

tax_form_id = 'taxFormId2'

x_akoya_interaction_id = 'unique-request-id-001'

x_akoya_interaction_type = InteractionType.USER

tax_data_type = TypeDataType.JSON

accept = [
    MediaType.ENUM_APPLICATIONJSON
]

result = tax_beta_api.get_tax_form(
    version,
    provider_id,
    tax_form_id,
    x_akoya_interaction_id=x_akoya_interaction_id,
    x_akoya_interaction_type=x_akoya_interaction_type,
    tax_data_type=tax_data_type,
    accept=accept
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "taxYear": 2020,
  "taxStatementId": "1234123412341234",
  "attributes": [
    {
      "name": "Total tax withheld",
      "value": "8025.00"
    }
  ],
  "issuer": {
    "tin": "12-3456789",
    "partyType": "BUSINESS",
    "businessName": {
      "name1": "Financial Data Exchange"
    },
    "address": {
      "line1": "12020 Sunrise Valley Dr",
      "line2": "Suite 230",
      "city": "Reston",
      "region": "VA",
      "postalCode": "20191",
      "country": "US"
    },
    "phone": {
      "number": "8885551212"
    }
  },
  "recipient": {
    "tin": "xxx-xx-1234",
    "partyType": "INDIVIDUAL",
    "individualName": {
      "first": "Kris",
      "middle": "Q",
      "last": "Public"
    },
    "address": {
      "line1": "1 Main St",
      "city": "Melrose",
      "region": "NY",
      "postalCode": "12121",
      "country": "US"
    }
  },
  "taxDataType": "JSON",
  "forms": [
    {
      "tax1099Div": {
        "taxYear": 2020,
        "taxFormId": "9876987698769876",
        "taxFormDate": "2021-03-30",
        "additionalInformation": "FDX v6.0",
        "taxFormType": "Tax1099Div",
        "foreignAccountTaxCompliance": false,
        "accountNumber": "111-5555555",
        "ordinaryDividends": 1107,
        "qualifiedDividends": 1208,
        "totalCapitalGain": 2109,
        "unrecaptured1250Gain": 2210,
        "section1202Gain": 2311,
        "collectiblesGain": 2412,
        "nonTaxableDistribution": 3013,
        "federalTaxWithheld": 4014,
        "section199ADividends": 5015,
        "investmentExpenses": 6016,
        "foreignTaxPaid": 7017,
        "foreignCountry": "Mexico",
        "cashLiquidation": 9019,
        "nonCashLiquidation": 10020,
        "taxExemptInterestDividend": 11021,
        "specifiedPabInterestDividend": 12022,
        "stateAndLocal": [
          {
            "stateCode": "NY",
            "state": {
              "taxWithheld": 15023,
              "taxId": "14-000023"
            }
          }
        ]
      }
    },
    {
      "tax1099Int": {
        "taxYear": 2020,
        "taxFormId": "6543654365436543",
        "taxFormDate": "2021-03-30",
        "additionalInformation": "FDX v6.0",
        "taxFormType": "Tax1099Int",
        "foreignAccountTaxCompliance": false,
        "accountNumber": "111-5555555",
        "payerRtn": "007007007",
        "interestIncome": 1008,
        "earlyWithdrawalPenalty": 2009,
        "usBondInterest": 3010,
        "federalTaxWithheld": 4011,
        "investmentExpenses": 5012,
        "foreignTaxPaid": 6013,
        "foreignCountry": "Canada",
        "taxExemptInterest": 8015,
        "specifiedPabInterest": 9016,
        "marketDiscount": 10017,
        "bondPremium": 11018,
        "usBondPremium": 12019,
        "taxExemptBondPremium": 13020,
        "cusipNumber": "CUSIP",
        "stateAndLocal": [
          {
            "stateCode": "NY",
            "state": {
              "taxWithheld": 17022,
              "taxId": "15-000022"
            }
          }
        ]
      }
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Account ID is required for searching or validating authorization | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 404 | Tax Form for provided Tax Form ID was not found | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 405 | Method Not Allowed | `ApiException` |
| 406 | Content Type not Supported | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 408 | Request timed out (round trip call took >10 seconds). | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 409 | Tax forms are not currently available for this account or this year | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 500 | Catch-all exception where request was not processed due to an internal outage/issue. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 501 | FdxVersion in header is not implemented. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 503 | System is down for maintenance. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |

