
# Real Gift Additional Details

Additional details of real gift card transaction.

## Structure

`RealGiftAdditionalDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization_source` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field indicates the point of authorization. |
| `call_type` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field indicates the type of call for authorization. |
| `gc_retrieval_reference_number` | `str` | Optional | Gift Card Retrieval Reference Number, a key to uniquely identify a card transaction based on the ISO 8583 standard. Appears for gift<br><br>**Constraints**: *Maximum Length*: `12` |
| `mail_phone_indicator` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Indicator of mail/phone for transactions. |
| `origin_type` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Type of origin for transactions. |
| `pos_cond_code` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field indicates the POS Condition Code for transactions. |
| `void_indicator` | `str` | Optional | A method of confirming that a terminal received a transaction. The terminal transmits the reference number of the last EFT transaction in each request. If the terminal and host are not in sync, the last EFT transaction is reversed.<br><br>**Constraints**: *Maximum Length*: `1` |
| `authorization_communication_type` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Authorization communication details. |
| `application_identifier` | `str` | Optional | An application identifier is a number at the beginning of a string of data that identifies the intended interpretation of the data.<br><br>**Constraints**: *Maximum Length*: `32` |
| `issuer_country_code` | `str` | Optional | This field indicates the country code of issuer<br><br>**Constraints**: *Maximum Length*: `3` |
| `unique_serial_device` | `str` | Optional | This field indicates the unique id of device.<br><br>**Constraints**: *Maximum Length*: `16` |
| `customer_id` | `str` | Optional | This field indicates the ecom customer identifier.<br><br>**Constraints**: *Maximum Length*: `25` |
| `merchant_order` | `str` | Optional | This field indicates the ecom merchant order identifier.<br><br>**Constraints**: *Maximum Length*: `25` |
| `campaign` | `str` | Optional | This field indicates the ecom campaign.<br><br>**Constraints**: *Maximum Length*: `25` |
| `affiliate` | `str` | Optional | This field indicates the ecom affiliate.<br><br>**Constraints**: *Maximum Length*: `25` |
| `merchant_grouping_id` | `str` | Optional | This field indicates the ecom merchant grouping identifier<br><br>**Constraints**: *Maximum Length*: `25` |
| `report_group` | `str` | Optional | This field indicates the ecom report group<br><br>**Constraints**: *Maximum Length*: `25` |
| `charge_id` | `str` | Optional | This field indicates the returns on a successful pay transaction. It must be returned on reversal/refund to restore PAN for routing.<br><br>**Constraints**: *Maximum Length*: `27` |

## Example (as JSON)

```json
{
  "authorizationSource": {
    "code": "5",
    "shortDescription": "Issuer Approval",
    "longDescription": "Issuer Approval"
  },
  "posCondCode": {
    "code": "59",
    "shortDescription": "E-Commerce",
    "longDescription": "E-COMMERCE"
  },
  "voidIndicator": "A",
  "authorizationCommunicationType": {
    "code": "0",
    "shortDescription": "STANDARD RAFT",
    "longDescription": "STANDARD RAFT"
  },
  "applicationIdentifier": "E",
  "issuerCountryCode": "ADF",
  "uniqueSerialDevice": "B8973827348H43",
  "customerId": "G768",
  "merchantOrder": "A453",
  "campaign": "D453",
  "affiliate": "G123",
  "merchantGroupingId": "S673",
  "reportGroup": "E874",
  "chargeId": "G453",
  "callType": {
    "code": "code4",
    "shortDescription": "shortDescription8",
    "longDescription": "longDescription6"
  },
  "gcRetrievalReferenceNumber": "gcRetrievalReferenceNumber8",
  "mailPhoneIndicator": {
    "code": "code8",
    "shortDescription": "shortDescription6",
    "longDescription": "longDescription0"
  },
  "originType": {
    "code": "code2",
    "shortDescription": "shortDescription0",
    "longDescription": "longDescription4"
  }
}
```

