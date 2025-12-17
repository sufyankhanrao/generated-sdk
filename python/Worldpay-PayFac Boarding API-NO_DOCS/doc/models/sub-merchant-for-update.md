
# Sub Merchant for Update

## Structure

`SubMerchantForUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dba_name` | `str` | Required | Required. Doing Business As Name of the Sub-Merchant. Valid special characters are space , ' & ; - _<br><br>**Constraints**: *Maximum Length*: `40`, *Pattern*: `^[0-9A-Za-z ,'.&amp;-_]{1,40}$` |
| `billing_descriptor` | `str` | Required | Billing Descriptor for the Sub-Merchant.<br><br>**Constraints**: *Maximum Length*: `25` |
| `business_type` | [`BusinessType1Enum`](../../doc/models/business-type-1-enum.md) | Required | Required. Business Type of the Sub-Merchant |
| `business_established_date` | `date` | Required | Format yyyy-mm-dd. Date on which Sub-Merchant business was established |
| `transaction_type` | [`TransactionTypeEnum`](../../doc/models/transaction-type-enum.md) | Required | Required. Transaction Type for the Sub-Merchant to indicate whether they do any percentage of business online. OnlineStore or NoOnlineStore |
| `website_url` | `str` | Optional | Website URL of the Sub-Merchant.<br><br>**Constraints**: *Maximum Length*: `80`, *Pattern*: `^(http:\/\/www\.\|https:\/\/www\.\|http:\/\/\|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$` |

## Example (as JSON)

```json
{
  "dbaName": "PayFac Submerchant 01",
  "billingDescriptor": "PFA*SM",
  "businessType": "Lodging",
  "businessEstablishedDate": "2016-03-13",
  "transactionType": "OnlineStore",
  "websiteUrl": "https://payfacsm.com"
}
```

