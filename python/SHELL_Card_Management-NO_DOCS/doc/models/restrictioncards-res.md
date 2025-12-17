
# Restrictioncards Res

## Structure

`RestrictioncardsRes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `int` | Optional | Account Id of the customer.<br>Example: 123456 |
| `account_number` | `str` | Optional | Account Number of the customer.<br>Example: GB000000123 |
| `card_id` | `str` | Optional | Unique Card Id<br>Example: 275549 |
| `pan` | `str` | Optional | Card PAN.<br>Example: 7002051006629890645 |
| `usage_restriction_status` | `str` | Optional | Status of the card usage restriction submitted. Based on the response the value will be set as either “Success” or “Failed”. |
| `usage_restriction_description` | `str` | Optional | Response for the usage restriction in case of an error. This field will have a value only when “UsageRestrictionStatus” is “Failed”. |
| `day_time_restriction_status` | `str` | Optional | Status of the card day/time restriction submitted. Based on the response from Gateway value will be set as either “Success” or “Failed”. |
| `day_time_restriction_description` | `str` | Optional | Response for the day/time restriction in case of an error. This field will have a value only when “DayTimeRestrictionStatus” is “Failed”. |
| `product_restriction_status` | `str` | Optional | Status of the card product restriction submitted. Based on the response  the value will be set  either as “Success” or “Failed”. |
| `product_restriction_description` | `str` | Optional | Response for the product restriction in case of an error. This field will have a value only when “ProductRestrictionStatus” is “Failed”. |
| `location_restriction_status` | `str` | Optional | Card Location restriction submitted, based on response value set as “Success” or “Failed”. |
| `location_restriction_status_description` | `str` | Optional | Response for the location restriction in case of an error. This field will have a value only when “LocationRestrictionStatus” is “Failed”. |
| `validation_error_code` | `str` | Optional | Error code for validation failure. |
| `validation_error_description` | `str` | Optional | Description of validation failure. |

## Example (as JSON)

```json
{
  "AccountId": 148,
  "AccountNumber": "AccountNumber0",
  "CardId": "CardId0",
  "PAN": "PAN2",
  "UsageRestrictionStatus": "UsageRestrictionStatus0"
}
```

