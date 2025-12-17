
# Vas Efe Offers Response

## Structure

`VasEfeOffersResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `offer_id` | `str` | Optional | Id of the offer |
| `expiry` | `str` | Optional | Expire date of offer<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}` |
| `entity` | `str` | Optional | EntityId for merchant |
| `mid` | `str` | Optional | MID |
| `primary_contact_email` | `str` | Optional | Primary point of contacts email |
| `merchant_lender_id` | `str` | Optional | This refers to the partner product association |
| `vendor_name` | `str` | Optional | Vendor associated with the product |
| `offer_date` | `str` | Optional | Date of provided offer<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `total_approved_amount` | `str` | Optional | Amount approved for |
| `fee_amount` | `str` | Optional | Fee amount charged |
| `origination_fee` | `str` | Optional | Refers to fee charged by a lender to process a new loan application. |
| `offer_url` | `str` | Optional | Url of corresponding offer |
| `product_name` | `str` | Optional | Name associated with the product |
| `product_long_description` | `str` | Optional | Long description of the product. |
| `acquire_platform` | `str` | Optional | To identify whether a partner belongs to Core or VAP platforms. |
| `prequalification_sent_date` | `str` | Optional | The date when preliminary information is submitted for vendor assessment to determine merchant eligibility to receive the cash advance.<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `prequalification_received_date` | `str` | Optional | Date when the vendor provides the preQualification status of a given sub-merchant.<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `is_merchant_prequalified` | [`IsMerchantPrequalifiedEnum`](../../doc/models/is-merchant-prequalified-enum.md) | Optional | A flag that indicates if a merchant meets predetermined vendor criteria to receive cash advance funding. |
| `applied_date` | `str` | Optional | Date when merchant submitted an application to receive cash advance from a vendor. Date should be past or present in the format YYYY-MM-DD.<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `offer_status` | [`OfferStatusEnum`](../../doc/models/offer-status-enum.md) | Optional | Indicates the status of a cash advance application submitted by the sub-merchant |
| `product_code` | `str` | Optional | Type of product which partner has enrolled into. |
| `start_date` | `str` | Optional | Date when sub merchant started re-paying cash advance.<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `end_date` | `str` | Optional | Date when sub merchant is expected to complete the repayment of cash advance.<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `split_funding_cap` | `str` | Optional | Maximum amount to be repaid by sub merchant. |
| `split_funding_rate` | `str` | Optional | Repayment percentage as defined by lender. |
| `daily_funding_max_limit` | `str` | Optional | Maximum daily repayment limit as defined by lender. |
| `split_funding_amount` | `str` | Optional | Split Funding Amount refers to the cash advance provided to the merchant. |
| `opt_in_date` | `str` | Optional | The date when the merchant has opted in.<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `split_settlement_enabled` | [`SplitSettlementEnabledEnum`](../../doc/models/split-settlement-enabled-enum.md) | Optional | Indicates if split funding settlement allowed for merchant. |

## Example (as JSON)

```json
{
  "id": "id0",
  "created": "created0",
  "modified": "modified8",
  "creator": "String9",
  "modifier": "modifier4"
}
```

