
# Sub Merchant for Patch

## Structure

`SubMerchantForPatch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dba_name` | `str` | Optional | Doing Business As Name of the Sub-Merchant. Valid special characters are space , ' & ; - _<br><br>**Constraints**: *Maximum Length*: `40`, *Pattern*: `^[0-9A-Za-z ,'.&amp;-_]{1,40}$` |
| `billing_descriptor` | `str` | Optional | An asterik is required. The asterik has to be in the 4th, 8th, or 13th position of the string<br><br>**Constraints**: *Maximum Length*: `25` |
| `business_type` | [`BusinessType4Enum`](../../doc/models/business-type-4-enum.md) | Optional | Business Type of the Sub-Merchant |
| `mcc_code` | `int` | Optional | - |
| `business_established_date` | `date` | Optional | Format yyyy-mm-dd. Date on which Sub-Merchant business was established |
| `transaction_type` | [`TransactionTypeEnum`](../../doc/models/transaction-type-enum.md) | Optional | Required. Transaction Type for the Sub-Merchant to indicate whether they do any percentage of business online. OnlineStore or NoOnlineStore |
| `website_url` | [`WebsiteUrlEnum`](../../doc/models/website-url-enum.md) | Optional | Website URL of the Sub-Merchant.<br><br>**Constraints**: *Maximum Length*: `80`, *Pattern*: `^(http:\/\/www\.\|https:\/\/www\.\|http:\/\/\|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$` |
| `division_code` | `str` | Optional | Optional, only send if the divisionCode needs to be updated for a submerchant. |
| `owners` | [`List[Owner]`](../../doc/models/owner.md) | Optional | - |
| `contacts` | [`List[Contact]`](../../doc/models/contact.md) | Optional | * CustomerService Contact is mandatory. It could be same as any Owner Contact information.<br>* For Customer Service Contact, firstName, lastName, phoneNumber, and email are mandatory.<br>* For any other contactTtype, firstName and lastName are mandatory. |
| `addresses` | [`List[Address]`](../../doc/models/address.md) | Optional | * Physical address is mandatory.<br>* For any addressType, streetAddress1, city, state, postalCode, and countryCode are mandatory. |
| `accepted_cards` | [`List[AcceptedCard]`](../../doc/models/accepted-card.md) | Optional | Method of Payment or Card Type related attributes. Only the attributes specific to the Card type needs to be included.<br><br>* Visa and Mastercard are mandatory |
| `default_bank_account` | [`BankAccount`](../../doc/models/bank-account.md) | Optional | - |
| `advanced_settlement_accounts` | [`List[AdvancedSettlementAccount]`](../../doc/models/advanced-settlement-account.md) | Optional | - |

## Example (as JSON)

```json
{
  "dbaName": "PayFac Submerchant 01",
  "billingDescriptor": "PFA*SM",
  "mccCode": 7372,
  "transactionType": "OnlineStore",
  "divisionCode": "001",
  "businessType": "AutoRental",
  "businessEstablishedDate": "2016-03-13"
}
```

