
# Business

This aggregate field includes business data

## Structure

`Business`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chain_code` | `str` | Optional | The identifier code that represents the entity value of the chain<br><br>**Constraints**: *Maximum Length*: `6` |
| `chain_acro` | `str` | Optional | Acronym used for billing purpose<br><br>**Constraints**: *Maximum Length*: `4` |
| `created_date` | `date` | Optional | Merchant created date. Using ISO 8601 'yyyy-mm-dd' |
| `legal_name` | `str` | Optional | The official name of the person or entity that owns the business.<br><br>**Constraints**: *Maximum Length*: `50` |
| `dba_name` | `str` | Required | A pseudonym used by companies that do not operate under their registered company name.<br><br>**Constraints**: *Maximum Length*: `50` |
| `partners` | [`List[PartnersDetails]`](../../doc/models/partners-details.md) | Optional | Information about the partner |
| `federal_tax_id` | `str` | Optional | AKA Employer Identification Number (EIN). An identifying number used for tax purposes.<br><br>**Constraints**: *Minimum Length*: `9`, *Maximum Length*: `9`, *Pattern*: `^\d{9}$` |
| `ownership_type` | [`OwnershipTypeEnum`](../../doc/models/ownership-type-enum.md) | Optional | Type of Ownership<br><br>**Constraints**: *Maximum Length*: `15` |
| `product_service_sold` | `str` | Optional | Type of goods or services sold.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `40`, *Pattern*: `^[a-zA-Z0-9 \p{P}\p{S}]+$` |
| `industry_type` | [`IndustryTypeEnum`](../../doc/models/industry-type-enum.md) | Optional | Type of the industry<br><br>**Constraints**: *Maximum Length*: `7` |
| `established_date` | `date` | Optional | Date of business establishment. Using ISO 8601 'yyyy-mm-dd' |
| `website` | `str` | Optional | Website URL link<br><br>**Constraints**: *Maximum Length*: `80` |
| `contract_term_in_months` | `int` | Optional | Length of the contract<br><br>**Constraints**: `>= 1`, `<= 99` |
| `number_of_locations` | `int` | Optional | Total number of location under this business<br><br>**Constraints**: `>= 1`, `<= 9999` |
| `currently_processing` | `bool` | Optional | Current processing status |
| `closed_date` | `date` | Optional | Using ISO 8601 'yyyy-mm-dd' |
| `billing_account_type` | [`CodeAndDescription`](../../doc/models/code-and-description.md) | Optional | This aggregate field includes billing code and its description. |
| `emv_enabled_date` | `date` | Optional | Using ISO 8601 'yyyy-mm-dd' |
| `merchant_partner_acct_id` | `str` | Optional | Partner account ID<br><br>**Constraints**: *Maximum Length*: `5` |
| `pci_vendor_setup` | [`BusinessPciVendorSetup`](../../doc/models/business-pci-vendor-setup.md) | Optional | This aggregate field includes PCI Vendor Setup data |
| `security_products` | [`BusinessSecurityProducts`](../../doc/models/business-security-products.md) | Optional | This aggregate field includes security products data |
| `sales_person` | [`SalesPerson`](../../doc/models/sales-person.md) | Optional | This aggregate field includes sales person data |
| `customer_service_contact` | [`AdditionalContact`](../../doc/models/additional-contact.md) | Optional | This aggregate field includes customer service contact data |
| `primary_contact` | [`AdditionalContact`](../../doc/models/additional-contact.md) | Optional | This aggregate field includes primary contact data |
| `chargeback_contact` | [`AdditionalContact`](../../doc/models/additional-contact.md) | Optional | This aggregate field includes charge back contact data |
| `pci_contact` | [`AdditionalContact`](../../doc/models/additional-contact.md) | Optional | This aggregate field includes PCI contact data |
| `physical_address` | [`AdditionalAddress`](../../doc/models/additional-address.md) | Optional | This aggregate field includes physical address data |
| `mailing_address` | [`AdditionalAddress`](../../doc/models/additional-address.md) | Optional | This aggregate field includes mailing address data |
| `billing_debit_address` | [`AdditionalAddress`](../../doc/models/additional-address.md) | Optional | This aggregate field includes billing debit address data |
| `owners` | [`List[ReadOwner]`](../../doc/models/read-owner.md) | Optional | Information on the Owners |
| `guarantors` | [`List[ReadGuarantor]`](../../doc/models/read-guarantor.md) | Optional | Information on the Guarantors |

## Example (as JSON)

```json
{
  "chainCode": "0X1234",
  "chainAcro": "ABCD",
  "createdDate": "2021-07-24",
  "legalName": "Your Company Legal Name",
  "dbaName": "Your Company DBA Name",
  "ownershipType": "SOLE PROPRIETOR",
  "productServiceSold": "SHOES",
  "industryType": "LODGING",
  "establishedDate": "1990-10-24",
  "website": "https://www.website.com",
  "contractTermInMonths": 60,
  "numberOfLocations": 5,
  "currentlyProcessing": false,
  "closedDate": "2021-08-24",
  "emvEnabledDate": "2021-08-24",
  "merchantPartnerAcctId": "12345",
  "partners": [
    [
      {
        "type": "type2",
        "id": "id2",
        "name": "name2"
      }
    ]
  ]
}
```

