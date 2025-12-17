
# Summaryofbundle Response

## Structure

`SummaryofbundleResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | Request Id of the API call |
| `payer_id` | `int` | Optional | Payer Id of the bundles and cards.<br>Example: 123456 |
| `payer_number` | `str` | Optional | Payer Number of the bundles and cards.<br>Example: GB000000123 |
| `account_id` | `int` | Optional | - |
| `account_number` | `str` | Optional | Account Number of the bundle.<br>Example: GB000000123 |
| `count_of_cards_not_in_bundle` | `int` | Optional | Count of cards that are not part of the bundle in a given account. |
| `card_bundles` | [`CardBundle`](../../doc/models/card-bundle.md) | Optional | - |
| `error` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |

## Example (as JSON)

```json
{
  "RequestId": "2ace3991-5d03-4a68-ac68-ca9119b25101",
  "PayerId": 70,
  "PayerNumber": "PayerNumber2",
  "AccountId": 130,
  "AccountNumber": "AccountNumber4"
}
```

