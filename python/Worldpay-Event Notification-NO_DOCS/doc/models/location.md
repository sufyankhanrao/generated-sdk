
# Location

This aggregate field includes location details

## Structure

`Location`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `store_number` | `str` | Optional | Store identifier, you can store alphanumber value when creating the store<br><br>**Constraints**: *Maximum Length*: `9` |
| `store_name` | `str` | Optional | Name of the store<br><br>**Constraints**: *Maximum Length*: `40` |
| `merchant_id` | `str` | Optional | Unique identifier assigned for a processing location<br><br>**Constraints**: *Maximum Length*: `10` |
| `host_merchant_number` | `str` | Optional | Merchant number associated with host<br><br>**Constraints**: *Maximum Length*: `30` |
| `billing_descriptor` | `str` | Optional | Name of the Merchant<br><br>**Constraints**: *Maximum Length*: `30` |
| `mcc` | `str` | Optional | Merchant Category Code<br><br>**Constraints**: *Maximum Length*: `4` |
| `mcc_description` | `str` | Optional | Description of the merchant category code<br><br>**Constraints**: *Maximum Length*: `15` |
| `seasonal_merchant` | `bool` | Optional | Identifier for the merchant business being seasonal or not |
| `active_months` | [`List[ActiveMonthEnum]`](../../doc/models/active-month-enum.md) | Optional | List of Active Months for merchant business |
| `last_batch_activity_date` | `date` | Optional | Date of last batch activity at merchant level |
| `status` | `str` | Optional | Status of the merchant<br><br>**Constraints**: *Maximum Length*: `255` |
| `alternate_merchant_id` | `str` | Optional | Alternate identifier for the merchant<br><br>**Constraints**: *Maximum Length*: `30` |
| `card_swiped_indicator` | `bool` | Optional | Indicator for card swiping |
| `ecom_indicator` | `bool` | Optional | Indicator for ecom business |
| `emv_indicator` | `bool` | Optional | Indicator for EMV acceptance |
| `mastercard_ica` | `str` | Optional | Master Card Inter Bank Association Number<br><br>**Constraints**: *Maximum Length*: `6` |
| `moto_indicator` | `bool` | Optional | Indicator for card not present transations |
| `p_2_pe_indicator` | `bool` | Optional | Indicator for Point to Point Encryption |
| `p_2_pe_service_level` | `bool` | Optional | Indicator for Service level Point to Point Encryption |
| `third_party_merchant_id` | `str` | Optional | Third Party Merchant ID<br><br>**Constraints**: *Maximum Length*: `30` |
| `primary_contact` | [`AdditionalContact`](../../doc/models/additional-contact.md) | Optional | This aggregate field includes primary contact data |
| `physical_address` | [`AdditionalAddress`](../../doc/models/additional-address.md) | Optional | This aggregate field includes physical address data |
| `deployment_contact` | [`AdditionalContact`](../../doc/models/additional-contact.md) | Optional | This aggregate  field includes deployment contact data |
| `deployment_address` | [`AdditionalAddress`](../../doc/models/additional-address.md) | Optional | This aggregate field includes deployment address data |
| `payment_methods` | [`PaymentMethods`](../../doc/models/payment-methods.md) | Optional | This aggregate field includes payment methods data |
| `products` | [`Products`](../../doc/models/products.md) | Optional | This aggregate field includes products data |
| `accelerated_funding` | [`AcceleratedProducts`](../../doc/models/accelerated-products.md) | Optional | This aggregate field includes accelerated funding data |

## Example (as JSON)

```json
{
  "storeNumber": "000000001",
  "storeName": "My Store Name",
  "merchantId": "1234567890",
  "hostMerchantNumber": "123456789",
  "billingDescriptor": "Merchant at Stonegate",
  "mcc": "5812",
  "mccDescription": "Lodging",
  "seasonalMerchant": true,
  "activeMonths": [
    "AUG",
    "SEP",
    "NOV"
  ],
  "lastBatchActivityDate": "2021-08-30",
  "status": "Open",
  "alternateMerchantId": "123456789",
  "cardSwipedIndicator": true,
  "ecomIndicator": true,
  "emvIndicator": false,
  "mastercardIca": "127684",
  "motoIndicator": true,
  "p2peIndicator": false,
  "p2peServiceLevel": true,
  "thirdPartyMerchantId": "123456789"
}
```

