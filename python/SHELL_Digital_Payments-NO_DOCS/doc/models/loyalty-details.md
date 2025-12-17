
# Loyalty Details

## Structure

`LoyaltyDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loyalty_id` | `str` | Required | The user’s Loyalty card number. Although this is optional the expectation is that if this is specified then loyaltyType must also be specified |
| `loyalty_type` | `str` | Required | Loyalty type being used, associated to the loyalty ID being passed. Possible values are 'Shell' |

## Example (as JSON)

```json
{
  "loyaltyId": "70043201060148830",
  "loyaltyType": "Shell"
}
```

