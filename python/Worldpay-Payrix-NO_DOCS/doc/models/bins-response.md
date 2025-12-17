
# Bins Response

## Structure

`BinsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `bin` | `str` | Optional | The first 6 digits of the card used in a Transaction. |
| `method` | [`BinMethodEnum`](../../doc/models/bin-method-enum.md) | Optional | The type of payment method used for this transaction.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Unknown Payment Method**<br>- `1` - **American Express**<br>- `2` - **Visa**<br>- `3` - **MasterCard**<br>- `4` - **Diners Club**<br>- `5` - **Discover**<br>- `6` - **PayPal**<br>- `7` - **Debit Card**<br>- `8` - **Checking Account**<br>- `9` - **Savings Account**<br>- `10` - **Corporate Checking Account**<br>- `11` - **Corporate Savings Account**<br>- `12` - **Gift Card**<br>- `13` - **EBT (Electronic Benefits Transfer) Card**<br>- `14` - **WIC (Women, Infants and Children) Card**<br>- `15` - **Accel**<br>- `16` - **ATH**<br>- `17` - **AFFN**<br>- `18` - **Culiance**<br>- `19` - **Interlink**<br>- `20` - **Jeanie**<br>- `21` - **Maestro**<br>- `22` - **NYCE**<br>- `23` - **Pulse**<br>- `24` - **Shazam**<br>- `25` - **Star**<br>- `26` - **Interac**<br>- `27` - **OmniToken**<br></details><br> |
| `mtype` | [`BinsTypeEnum`](../../doc/models/bins-type-enum.md) | Optional | The type of the card used in the Transaction.<br><br><details><br><summary>Valid Values</summary><br>- `credit` - **Credit Card**<br>- `debit` - **Debit Card**<br>- `debitCredit` - **Debit or Credit Card**<br>- `charge` - **Charge Card**<br>- `prepaid` - **Prepaid Debit Card**<br>- `bankAccount` - **Bank Account Card**<br></details><br> |
| `category` | [`CategoryEnum`](../../doc/models/category-enum.md) | Optional | The category of the account product.<br><br><details><br><summary>Valid Values</summary><br>- `classic` - **Classic credit or debit card.**<br>- `business` - **Business credit or debit card.**<br>- `corporate` - **Corporate credit or debit card.**<br>- `fleet` - **Fleet card for transportation-related expenses.**<br>- `hsaFsa` - **HSA (Health Savings Account) or FSA (Flexible Spending Account) card.**<br>- `platinum` - **Platinum credit card.**<br>- `prepaid` - **Prepaid card.**<br>- `coreCard` - **Core card.**<br>- `personal` - **Personal account.**<br>- `standard` - **Standard account.**<br>- `other` - **Other type of account.**<br>- `international` - **International account.**<br></details><br> |
| `name` | `str` | Optional | The name of the bank that issued the card used in the Transaction. |
| `address` | `str` | Optional | Street address of the bank. |
| `city` | `str` | Optional | City of the bank. |
| `state` | `str` | Optional | The U.S. state or Canadian province relevant to the address provided here. If the location is within the U.S. and Canada, specify the 2-character postal abbreviation for the state. If the location is outside of the U.S. and Canada, provide the full state name. This field is stored as a text string and must be between 2 and 100 characters long.<br><br><details><br><summary>U.S. States</summary><br> <br> - `AK` - **Alaska (US)**<br> <br> - `AR` - **Arkansas (US)**<br> <br> - `AL` - **Alabama (US)**<br> <br> - `AZ` - **Arizona (US)**<br> <br> - `CA` - **California (US)**<br> <br> - `CO` - **Colorado (US)**<br> <br> - `CT` - **Connecticut (US)**<br> <br> - `DE` - **Delaware (US)**<br> <br> - `FL` - **Florida (US)**<br> <br> - `GA` - **Georgia (US)**<br> <br> - `HI` - **Hawaii (US)**<br> <br> - `IA` - **Iowa (US)**<br> <br> - `ID` - **Idaho (US)**<br> <br> - `IL` - **Illinois (US)**<br> <br> - `IN` - **Indiana (US)**<br> <br> - `KY` - **Kentucky (US)**<br> <br> - `KS` - **Kansas (US)**<br> <br> - `LA` - **Louisiana (US)**<br> <br> - `MA` - **Massachusetts (US)**<br> <br> - `MD` - **Maryland (US)**<br> <br> - `ME` - **Maine (US)**<br> <br> - `MI` - **Michigan (US)**<br> <br> - `MN` - **Minnesota (US)**<br> <br> - `MO` - **Missouri (US)**<br> <br> - `MS` - **Mississippi (US)**<br> <br> - `MT` - **Montana (US)**<br> <br> - `NC` - **North Carolina (US)**<br> <br> - `ND` - **North Dakota (US)**<br> <br> - `NE` - **Nebraska (US)**<br> <br> - `NH` - **New Hampshire (US)**<br> <br> - `NJ` - **New Jersey (US)**<br> <br> - `NM` - **New Mexico (US)**<br> <br> - `NV` - **Nevada (US)**<br> <br> - `NY` - **New York (US)**<br> <br> - `OH` - **Ohio (US)**<br> <br> - `OK`- **Oklahoma (US)**<br> <br> - `OR` - **Oregon (US)**<br> <br> - `PA` - **Pennsylvania (US)**<br> <br> - `RI` - **Rhode Island (US)**<br> <br> - `SC`- **South Carolina (US)**<br> <br> - `SD` - **South Dakota (US)**<br> <br> - `TN` - **Tennessee (US)**<br> <br> - `TX` - **Texas (US)**<br> <br> - `UT` - **Utah (US)**<br> <br> - `VA` - **Virginia (US)**<br> <br> - `VT` - **Vermont (US)**<br> <br> - `WA` - **Washington (US)**<br> <br> - `WI` - **Wisconsin (US)**<br> <br> - `WV` - **West Virginia (US)**<br> <br> - `WY` - **Wyoming (US)**<br> </details><br> <details><br><summary>Canada Provinces and Territories</summary><br> <br> - `AB` - **Alberta (CAN)**<br> <br> - `BC` - **British Columbia (CAN)**<br> <br> - `MB` - **Manitoba (CAN)**<br> <br> - `ON` - **Ontario (CAN)**<br> <br> - `NS` - **Nova Scotia (CAN)**<br> <br> - `NB` - **New Brunswick (CAN)**<br> <br> - `NL` - **Newfoundland and Labrador (CAN)**<br> <br> - `NT` - **Northwest Territories (CAN)**<br> <br> - `NU` - **Nunavut (CAN)**<br> <br> - `PE` - **Prince Edward Island (CAN)**<br> <br> - `QC` - **Quebec (CAN)**<br> <br> - `SK` - **Saskatchewan (CAN)**<br> <br> - `YT` - **Yukon (CAN)**<br> </details><br> |
| `country` | [`CountryEnum`](../../doc/models/country-enum.md) | Optional | The country of the bank that issued the card used in the Transaction. |
| `zip` | `str` | Optional | Zip code of the banking institution. |
| `location_type` | [`BinLocationTypeEnum`](../../doc/models/bin-location-type-enum.md) | Optional | The type of location of this banking institution. Used in `bankAccount` type bins.<br><br><details><br><summary>Valid Values</summary><br>- `branch` - **Branch location.**<br>- `main` - **Main headquarters.**<br></details><br> |
| `new_bin` | `str` | Optional | The BIN (Bank Issuer Number) or routing number that replaces or supersedes this bin. |
| `website` | `str` | Optional | The website of the bank that issued the card used in the Transaction. |
| `phone` | `str` | Optional | The phone of the bank that issued the card used in the Transaction. |
| `transfer_enabled` | [`TransferEnabledEnum`](../../doc/models/transfer-enabled-enum.md) | Optional | Whether funds may be “pushed” to this debit card (with push-to-card).<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Push-to-card transfer disabled.**<br>- `1` - **Push-to-card transfer enabled.**<br></details><br> |
| `number_length` | `int` | Optional | The amount of digits expected for account numbers with this bin. |
| `debit_over_credit_enabled` | [`DebitOverCreditEnabledEnum`](../../doc/models/debit-over-credit-enabled-enum.md) | Optional | Whether this debit card may be charged as credit over the credit networks.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Debit charge as 'credit' disabled.**<br>- `1` - **Debit charge as 'credit' enabled.**<br></details><br> |
| `bill_pay_enabled` | [`BillPayEnabledEnum`](../../doc/models/bill-pay-enabled-enum.md) | Optional | Whether this card may be used for bill pay features.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Bill pay capability disabled.**<br>- `1` - **Bill pay capability enabled.**<br></details><br> |
| `pinless_support` | [`PinlessSupportEnum`](../../doc/models/pinless-support-enum.md) | Optional | What type of pinless charging is allowed on this debit card.<br><br><details><br><summary>Valid Values</summary><br>- `none` - **No pinless support, PIN (Personal Identification Number) must always be provided.**<br>- `restricted` - **Some pinless support, PIN (Personal Identification Number) may not always be necessary.**<br>- `full` - **Full pinless support, PIN (Personal Identification Number) may be omitted for pinless payments.**<br></details><br> |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "inactive": 0,
  "frozen": 0,
  "id": "id8",
  "created": "created8",
  "modified": "modified6",
  "creator": "String7",
  "modifier": "modifier2"
}
```

