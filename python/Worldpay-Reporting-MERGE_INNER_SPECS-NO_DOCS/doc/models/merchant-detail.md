
# Merchant Detail

## Structure

`MerchantDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_name` | `str` | Optional | Merchant ID (card acceptor identification code)<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `16` |
| `merchant_id` | `str` | Optional | Merchant ID (card acceptor identification code)<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `16` |
| `bank_number` | `int` | Optional | the acquiring institution identification code (Bank ID) |
| `merchant_category_code` | `int` | Optional | Merchant category code is a four-digit number assigned to businesses by payment card networks. It helps identify the nature of merchant's business and the industry in which they operate.<br><br>**Constraints**: `<= 4` |

## Example (as JSON)

```json
{
  "merchantName": "PRODDEV 122218",
  "merchantId": "1000910955961234",
  "bankNumber": 1444,
  "merchantCategoryCode": 4
}
```

