
# Sub Merchants Find Vas

## Structure

`SubMerchantsFindVas`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | ResourceId. ReadOnly. Returned by GET, not used in POST/PUT |
| `mid` | `int` | Optional | Merchant Identifier. ReadOnly. Returned by GET, not used in POST/PUT |
| `uuid` | `uuid\|str` | Optional | Required. PayFac generated Sub-Merchant unique id |
| `chain_code` | `str` | Optional | Required. Existing PayFac Chain code.<br><br>**Constraints**: *Pattern*: `^[0-9A-Z]{6}$` |
| `division_code` | `str` | Optional | Required for PayFacs that are using division codes |
| `store_number` | `str` | Optional | Optional. For PayFacs that want to specify a Store Number for a submerchant. |
| `federal_tax_id` | `str` | Optional | a) Required. For US Sub-merchants Federal Tax ID is the Tax Identification Number (TIN). If Sub-Merchant Ownership type is SolePropietor, then use SSN.<br>example: '123456789'<br><br>b) Required. For Canadian Sub-merchants provide EIN (Employer Identification Nummber). If Sub-Merchant Ownership type is SolePropietor, then use SIN.<br><br>**Constraints**: *Pattern*: `^\d{9}$` |
| `legal_name` | `str` | Optional | Required. Legal Name of the Sub Merchant.Valid special characters are space , ' & ; - _<br><br>**Constraints**: *Maximum Length*: `40`, *Pattern*: `^[0-9A-Za-z ,'.&amp;-_]{1,40}$` |
| `dba_name` | `str` | Optional | Required. Doing Business As Name of the Sub-Merchant. Valid special characters are space , ' & ; - _<br><br>**Constraints**: *Maximum Length*: `40`, *Pattern*: `^[0-9A-Za-z ,'.&amp;-_]{1,40}$` |
| `billing_descriptor` | `str` | Optional | Required. An asterik is required. The asterik has to be in the 4th, 8th, or 13th position of the string<br><br>**Constraints**: *Maximum Length*: `25` |
| `ownership_type` | [`OwnershipTypeEnum`](../../doc/models/ownership-type-enum.md) | Optional | Required. Type of the Sub-Merchant organization |
| `business_type` | [`BusinessType1Enum`](../../doc/models/business-type-1-enum.md) | Optional | Required. Business Type of the Sub-Merchant |
| `mcc_code` | `str` | Optional | Required. SIC Code / MCC Code (Sub-Merchant Category Code)<br><br>**Constraints**: *Pattern*: `^\d{4}$` |
| `business_established_date` | `date` | Optional | Required. Format yyyy-mm-dd. Date on which Sub-Merchant business was established |
| `website_url` | `str` | Optional | Required. Website URL of the Sub-Merchant.<br><br>**Constraints**: *Maximum Length*: `80`, *Pattern*: `^(http:\/\/www\.\|https:\/\/www\.\|http:\/\/\|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$` |
| `vas_enrolled` | `str` | Optional | Name of the value added service |

## Example (as JSON)

```json
{
  "chainCode": "0A1B2C",
  "divisionCode": "001",
  "storeNumber": "000000001",
  "legalName": "PayFac_Submerchant 01",
  "dbaName": "PayFac Submerchant 01",
  "billingDescriptor": "PFA*SM",
  "ownershipType": "PublicCorporation",
  "mccCode": "1520",
  "websiteUrl": "https://payfacsm.com",
  "vasEnrolled": "OmniToken",
  "id": 196,
  "mid": 152,
  "uuid": "00001cd2-0000-0000-0000-000000000000"
}
```

