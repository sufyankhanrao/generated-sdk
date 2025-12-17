
# Customer Detail Response

## Structure

`CustomerDetailResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `int` | Optional | Account Id of the selected account. |
| `account_name` | `str` | Optional | Account Name of the selected account. |
| `account_number` | `str` | Optional | Account Number of the selected account. |
| `account_short_name` | `str` | Optional | Short name of the customer. |
| `account_trading_name` | `str` | Optional | Trading name of the customer |
| `allow_fleet_id_input` | `bool` | Optional | True/False.<br>When false, users should not be allowed to enable Fleet Id prompt option while ordering cards under this account. |
| `band` | `str` | Optional | Band Id and Description of the Payer in Card Platform<br>e.g. (Id – Description):<br>1-Platinum<br>2-Gold<br>3-Silver<br>4-Bronze |
| `billing_address` | [`Address`](../../doc/models/address.md) | Optional | - |
| `card_group_position` | `str` | Optional | Card group position at –<br>•	Payer – Payer level<br>•	Account – Account level |
| `correspondence_address` | [`Address`](../../doc/models/address.md) | Optional | - |
| `delivery_addresses` | [`List[DeliveryAddresses]`](../../doc/models/delivery-addresses.md) | Optional | - |
| `fleet_pin` | `bool` | Optional | Is Fleet Pin optional enabled for the selected account |
| `full_name` | `str` | Optional | Full Name of the customer |
| `invoice_customer_id` | `int` | Optional | Customer Id of the Invoice Point of the account |
| `invoice_customer_short_name` | `str` | Optional | Short Name of the Invoice Point of the account |
| `is_invoice_point` | `bool` | Optional | Whether the account is an invoice point. |
| `marketing_segmentation` | `str` | Optional | Marketing Segmentation id and description<br>e.g. (Id – Description):<br>1-National CRT<br>2-International CRT & IKAs<br>3-Small Customers<br>4-National/International Fleet/IKA |
| `vat_number` | `str` | Optional | VAT Registration Number of Customer |
| `payer_id` | `int` | Optional | Payer Id of the selected account. |
| `payer_name` | `str` | Optional | Payer Name of the selected account. |
| `payer_number` | `str` | Optional | Payer Number of the selected account. |
| `self_selected_pin` | `bool` | Optional | Is Self-selected Pin enabled for the account |
| `status` | `str` | Optional | Payer current status id and description<br>e.g. (Id – Description):<br>1-Active<br>2-Requested from UTA<br>3-Awaiting embossing<br>4-Manufactured<br>5-Awaiting despatch |
| `default_pin_advice_type` | `int` | Optional | Default PIN AdviceType of the customer.<br>Possible Values:<br><br>1. Paper<br>2. Email<br>3. SMS<br>4. None |
| `pin_advice_types` | [`List[PINAdviceTypes]`](../../doc/models/pin-advice-types.md) | Optional | - |
| `error` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |
| `request_id` | `str` | Optional | API Request id |
| `pin_change_allowed_by_cardholder` | `bool` | Optional | PIN change allowed for card holder or not. |
| `pin_change_allowed_from_fleet_pin` | `bool` | Optional | PIN change allowed from fleetpin or not. |

## Example (as JSON)

```json
{
  "AccountId": 1227,
  "AccountName": "5.11.3 DE",
  "AccountNumber": "DE00001067",
  "AccountShortName": "5.11.3 DE",
  "AccountTradingName": "5.11.3 DE",
  "Band": "2 - Gold",
  "FullName": "5.11.3 DE",
  "InvoiceCustomerId": 1227,
  "InvoiceCustomerShortName": "5.11.3 DE",
  "MarketingSegmentation": "4 - National/International Fleet/IKA",
  "VATNumber": "PH6578900900",
  "PayerId": 1227,
  "PayerName": "5.11.3 DE",
  "PayerNumber": "DE00001067",
  "Status": "1 - Active",
  "DefaultPINAdviceType": 1,
  "RequestId": "908358e3-03ca-4aef-93b2-37586b859171"
}
```

