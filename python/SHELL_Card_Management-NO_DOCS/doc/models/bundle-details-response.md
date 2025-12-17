
# Bundle Details Response

## Structure

`BundleDetailsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payer_id` | `int` | Optional | Payer Id of the bundles and cards.<br>Example: 123456 |
| `payer_number` | `str` | Optional | Payer Number of the bundles and cards.<br>Example: GB000000123 |
| `account_id` | `int` | Optional | Account ID of the bundle.<br>Example: 123456 |
| `account_number` | `str` | Optional | Account Number of the bundle.<br>Example: GB000000123 |
| `bundle_id` | `str` | Optional | unique identifier for the Card Bundle |
| `external_bundle_id` | `str` | Optional | External system allocated Card Bundle identifier for Card Bundle. |
| `description` | `str` | Optional | Card Bundle Description. |
| `pans` | `List[str]` | Optional | List of Card Pans added to the card bundle. |
| `restriction_currency_code` | `str` | Optional | ISO currency code of the country.<br>Example: GBP |
| `restriction_currency_symbol` | `str` | Optional | Currency symbol of the country.<br>Example: £, $ |
| `restrictions` | [`BundledRestrictionsList`](../../doc/models/bundled-restrictions-list.md) | Optional | - |
| `error` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |
| `request_id` | `str` | Optional | API Request Id |

## Example (as JSON)

```json
{
  "PayerId": 172,
  "PayerNumber": "PayerNumber4",
  "AccountId": 232,
  "AccountNumber": "AccountNumber6",
  "BundleId": "BundleId4"
}
```

