
# Sub Merchant

## Structure

`SubMerchant`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | ResourceId. ReadOnly. Returned by GET, not used in POST/PUT |
| `mid` | `int` | Optional | Merchant Identifier. ReadOnly. Returned by GET, not used in POST/PUT |
| `uuid` | `uuid\|str` | Required | Required. PayFac generated Sub-Merchant unique id. UUID stands for Universally Unique Identifier. |
| `chain_code` | `str` | Required | Required. Existing PayFac Chain code.<br><br>**Constraints**: *Pattern*: `^[0-9A-Z]{6}$` |
| `division_code` | `str` | Optional | Required for PayFacs that are using division codes |
| `store_number` | `str` | Optional | Optional. For PayFacs that want to specify a Store Number for a submerchant. |
| `federal_tax_id` | `str` | Required | a) Required. For US Sub-merchants Federal Tax ID is the Tax Identification Number (TIN). If Sub-Merchant Ownership type is SolePropietor, then use SSN.<br><br>b) Required. For Canadian Sub-merchants provide EIN (Employer Identification Number). If Sub-Merchant Ownership type is SolePropietor, then use SIN.<br><br>**Constraints**: *Pattern*: `^\d{9}$` |
| `legal_name` | `str` | Required | Required. Legal Name of the Sub Merchant.Valid special characters are space , ' & ; - _<br><br>**Constraints**: *Maximum Length*: `40`, *Pattern*: `^[0-9A-Za-z ,'.&amp;-_]{1,40}$` |
| `dba_name` | `str` | Required | Required. Doing Business As Name of the Sub-Merchant. Valid special characters are space , ' & ; - _<br><br>**Constraints**: *Maximum Length*: `40`, *Pattern*: `^[0-9A-Za-z ,'.&amp;-_]{1,40}$` |
| `billing_descriptor` | `str` | Required | Required. An asterik is required. The asterik has to be in the 4th, 8th, or 13th position of the string<br><br>**Constraints**: *Maximum Length*: `25` |
| `ownership_type` | [`OwnershipTypeEnum`](../../doc/models/ownership-type-enum.md) | Required | Required. Type of the Sub-Merchant organization |
| `business_type` | [`BusinessTypeEnum`](../../doc/models/business-type-enum.md) | Required | Required. Business Type of the Sub-Merchant. MOTO - Mail Order Telephone Order |
| `mcc_code` | `str` | Required | Required. SIC Code / MCC Code (Sub-Merchant Category Code)<br><br>**Constraints**: *Pattern*: `^\d{4}$` |
| `business_established_date` | `date` | Required | Required. Format yyyy-mm-dd. Date on which Sub-Merchant business was established |
| `transaction_type` | [`TransactionTypeEnum`](../../doc/models/transaction-type-enum.md) | Required | Required. Transaction Type for the Sub-Merchant to indicate whether they do any percentage of business online. OnlineStore or NoOnlineStore |
| `website_url` | `str` | Optional | Website URL of the Sub-Merchant. Website URL is required if merchant selects OnlineStore as transactionType<br><br>**Constraints**: *Maximum Length*: `80`, *Pattern*: `^(http:\/\/www\.\|https:\/\/www\.\|http:\/\/\|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$` |
| `add_terminals` | [`AddTerminalsEnum`](../../doc/models/add-terminals-enum.md) | Optional | The addTerminal field indicates whether or not all the terminals that exist on the template mid will be created for the submerchant. This is an optional field. If it is omitted, the value will default to “Yes”. If the value is “Yes”, all terminals on the template mid will be created for the submerchant. If “No”, no terminals will be created for the submerchant using this call. Terminals can be created using the Create Terminal endpoint. |
| `terminals` | [`TerminalsPost`](../../doc/models/terminals-post.md) | Optional | - |
| `express_sub_account` | [`ExpressSubAccount`](../../doc/models/express-sub-account.md) | Optional | Express gateway information |
| `owners` | [`List[Owner]`](../../doc/models/owner.md) | Optional | - |
| `contacts` | [`List[Contact]`](../../doc/models/contact.md) | Required | * CustomerService Contact is mandatory. It could be same as any Owner Contact information.<br>* For Customer Service Contact, firstName, lastName, phoneNumber, and email are mandatory.<br>* For any other contactTtype, firstName and lastName are mandatory. |
| `addresses` | [`List[Address]`](../../doc/models/address.md) | Required | * Physical address is mandatory.<br>* For any addressType, streetAddress1, city, state, postalCode, and countryCode are mandatory. |
| `accepted_cards` | [`List[AcceptedCard]`](../../doc/models/accepted-card.md) | Required | Method of Payment or Card Type related attributes. Only the attributes specific to the Card type needs to be included.<br><br>* Visa and Mastercard are mandatory |
| `default_bank_account` | [`BankAccount`](../../doc/models/bank-account.md) | Required | - |
| `advanced_settlement_accounts` | [`List[AdvancedSettlementAccount]`](../../doc/models/advanced-settlement-account.md) | Optional | - |

## Example (as JSON)

```json
{
  "uuid": "000014e0-0000-0000-0000-000000000000",
  "chainCode": "0A1B2C",
  "divisionCode": "001",
  "storeNumber": "000000001",
  "federalTaxId": "123456789",
  "legalName": "PayFac_Submerchant 01",
  "dbaName": "PayFac Submerchant 01",
  "billingDescriptor": "PFA*SM",
  "ownershipType": "PublicCorporation",
  "businessType": "AutoRental",
  "mccCode": "1520",
  "businessEstablishedDate": "2016-03-13",
  "transactionType": "OnlineStore",
  "websiteUrl": "https://payfacsm.com",
  "contacts": [
    {
      "title": "Relationship Manager",
      "firstName": "Jane",
      "middleInitial": "S",
      "lastName": "Smith",
      "phoneNumber": "5135559876",
      "phoneNumberExt": "5432",
      "email": "jasmith@payfacsm.com",
      "faxNumber": "5135559876",
      "type": "Primary"
    }
  ],
  "addresses": [
    {
      "addressLine1": "100 West St",
      "addressLine2": "Suite 200",
      "city": "Anchorage",
      "state": "GA",
      "country": "US",
      "postalCode": "99501",
      "postalCodeExtension": "5555",
      "type": "Mailing"
    }
  ],
  "acceptedCards": [
    {
      "type": "AmericanExpress",
      "attributes": [
        {
          "name": "name4",
          "value": "value6"
        },
        {
          "name": "name4",
          "value": "value6"
        },
        {
          "name": "name4",
          "value": "value6"
        }
      ]
    }
  ],
  "defaultBankAccount": {
    "ddaType": "Checking",
    "accountNumber": "12345678910",
    "routingNumber": "123456789",
    "achType": "CommercialChequing"
  },
  "id": 34,
  "mid": 246
}
```

