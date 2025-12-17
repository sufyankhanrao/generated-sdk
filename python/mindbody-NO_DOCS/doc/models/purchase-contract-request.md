
# Purchase Contract Request

## Structure

`PurchaseContractRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `test` | `bool` | Optional | When `true`, the Public API validates input information, but does not commit it, so no client data is affected.<br /><br>When `false` or omitted, the transaction is committed, and client data is affected.<br /><br>Default: **false** |
| `location_id` | `int` | Optional | The ID of the location where the client is purchasing the contract; used for AutoPays. |
| `client_id` | `str` | Required | The ID of the client. Note that this is not the same as the client’s unique ID. |
| `contract_id` | `int` | Required | The ID of the contract being purchased. |
| `start_date` | `datetime` | Optional | The date that the contract starts.<br /><br>Default: **today’s date** |
| `first_payment_occurs` | `str` | Optional | The date on which the first payment is to occur. Possible values:<br><br>* Instant<br>* `StartDate` |
| `client_signature` | `str` | Optional | A representation of the client’s signature. This value can take the form of Base64-encoded byte array. The file type should be PNG. The picture of the client’s signature is uploaded and viewable from the Client Documents page in the Core Business Mode software. The title of the document is:<br /><br>clientContractSignature-{uniquePurchasedClientContractID}-{contractName}-{contractStartDate}.{fileType} |
| `promotion_code` | `str` | Optional | A promotion code, if one applies. Promotion codes are applied to items that are both marked as pay now in a contract and are discounted by the promotion code. If a pay now item is an autopay item, its autopay price is the price at the time of checkout, so, if a promotion code was applied, all autopays are scheduled using that discounted price. |
| `promotion_codes` | `List[str]` | Optional | Promotion codes, if they apply. Promotion codes are applied to items that are both marked as pay now in a contract and are discounted by the promotion code. If a pay now item is an autopay item, its autopay price is the price at the time of checkout, so, if a promotion code was applied, all autopays are scheduled using that discounted price. |
| `credit_card_info` | [`CreditCardInfo`](../../doc/models/credit-card-info.md) | Optional | INformation about an individual credit card |
| `stored_card_info` | [`StoredCardInfo`](../../doc/models/stored-card-info.md) | Optional | - |
| `send_notifications` | `bool` | Optional | When `true`, indicates that email and SMS notifications should be sent to the client after purchase.<br /><br>Default: **true** |
| `sales_rep_id` | `int` | Optional | The ID of the staff member to be marked as the sales rep for this contract sale. |
| `use_direct_debit` | `bool` | Optional | When `true`, indicates that the direct debit information stored on the client's account is to be used to pay for the contract.<br /><br>This is only required if both `CreditCardInfo` and `StoredCardInfo` are not passed.<br /><br>Default: **false** |
| `consumer_present` | `bool` | Optional | When `true`, indicates that the consumer is present or otherwise able to successfully negotiate an SCA challenge. It is not a good idea to have this always be false as that could very likely lead to a bank declining all transactions for the merchant.<br>Defaults to **false**. |
| `payment_authentication_callback_url` | `str` | Optional | The URL consumer is redirected to if the bank requests SCA. This field is only needed if ConsumerPresent is true. |
| `prorate_date` | `datetime` | Optional | Optional, date to prorate contract |

## Example (as JSON)

```json
{
  "Test": false,
  "LocationId": 24,
  "ClientId": "ClientId4",
  "ContractId": 210,
  "StartDate": "2016-03-13T12:52:32.123Z",
  "FirstPaymentOccurs": "FirstPaymentOccurs4",
  "ClientSignature": "ClientSignature8"
}
```

