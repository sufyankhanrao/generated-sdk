
# Entities Put Request

## Structure

`EntitiesPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_ip` | `str` | Optional | The client IP address from which the Entity was created. Valid values are any IPv4 or IPv6 address. |
| `login` | `str` | Optional | The Login that owns this resource. |
| `mtype` | [`EntityTypeEnum`](../../doc/models/entity-type-enum.md) | Optional | The type of Entity.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Sole Proprietorship**<br>- `1` - **Corporation**<br>- `2` - **Limited Liability Company**<br>- `3` - **Partnership**<br>- `4` - **Association**<br>- `5` - **Non-Profit Organization**<br>- `6` - **Government Organization**<br>- `7` - **C Corporation**<br>- `8` - **S Corporation**<br></details><br> |
| `name` | `str` | Optional | The name of this Entity.<br>This field is stored as a string string and must be between 1 and 100 characters long. |
| `display_name` | `str` | Optional | The display name of this Entity.<br>This field is stored as a string and must be between 1 and 1,000 characters long. |
| `address_1` | `str` | Optional | The first line of the address associated with this Entity.<br>This field is stored as a string and must be between 1 and 500 characters long. |
| `address_2` | `str` | Optional | The second line of the address associated with this Entity.<br>This field is stored as a string and must be between 1 and 500 characters long. |
| `city` | `str` | Optional | The name of the city in the address associated with this Entity.<br>This field is stored as a string and must be between 1 and 500 characters long. |
| `state` | `str` | Optional | The U.S. state or Canadian province relevant to the address provided here. If the location is within the U.S. and Canada, specify the 2-character postal abbreviation for the state. If the location is outside of the U.S. and Canada, provide the full state name. This field is stored as a text string and must be between 2 and 100 characters long.<br><br><details><br><summary>U.S. States</summary><br> <br> - `AK` - **Alaska (US)**<br> <br> - `AR` - **Arkansas (US)**<br> <br> - `AL` - **Alabama (US)**<br> <br> - `AZ` - **Arizona (US)**<br> <br> - `CA` - **California (US)**<br> <br> - `CO` - **Colorado (US)**<br> <br> - `CT` - **Connecticut (US)**<br> <br> - `DE` - **Delaware (US)**<br> <br> - `FL` - **Florida (US)**<br> <br> - `GA` - **Georgia (US)**<br> <br> - `HI` - **Hawaii (US)**<br> <br> - `IA` - **Iowa (US)**<br> <br> - `ID` - **Idaho (US)**<br> <br> - `IL` - **Illinois (US)**<br> <br> - `IN` - **Indiana (US)**<br> <br> - `KY` - **Kentucky (US)**<br> <br> - `KS` - **Kansas (US)**<br> <br> - `LA` - **Louisiana (US)**<br> <br> - `MA` - **Massachusetts (US)**<br> <br> - `MD` - **Maryland (US)**<br> <br> - `ME` - **Maine (US)**<br> <br> - `MI` - **Michigan (US)**<br> <br> - `MN` - **Minnesota (US)**<br> <br> - `MO` - **Missouri (US)**<br> <br> - `MS` - **Mississippi (US)**<br> <br> - `MT` - **Montana (US)**<br> <br> - `NC` - **North Carolina (US)**<br> <br> - `ND` - **North Dakota (US)**<br> <br> - `NE` - **Nebraska (US)**<br> <br> - `NH` - **New Hampshire (US)**<br> <br> - `NJ` - **New Jersey (US)**<br> <br> - `NM` - **New Mexico (US)**<br> <br> - `NV` - **Nevada (US)**<br> <br> - `NY` - **New York (US)**<br> <br> - `OH` - **Ohio (US)**<br> <br> - `OK`- **Oklahoma (US)**<br> <br> - `OR` - **Oregon (US)**<br> <br> - `PA` - **Pennsylvania (US)**<br> <br> - `RI` - **Rhode Island (US)**<br> <br> - `SC`- **South Carolina (US)**<br> <br> - `SD` - **South Dakota (US)**<br> <br> - `TN` - **Tennessee (US)**<br> <br> - `TX` - **Texas (US)**<br> <br> - `UT` - **Utah (US)**<br> <br> - `VA` - **Virginia (US)**<br> <br> - `VT` - **Vermont (US)**<br> <br> - `WA` - **Washington (US)**<br> <br> - `WI` - **Wisconsin (US)**<br> <br> - `WV` - **West Virginia (US)**<br> <br> - `WY` - **Wyoming (US)**<br> </details><br> <details><br><summary>Canada Provinces and Territories</summary><br> <br> - `AB` - **Alberta (CAN)**<br> <br> - `BC` - **British Columbia (CAN)**<br> <br> - `MB` - **Manitoba (CAN)**<br> <br> - `ON` - **Ontario (CAN)**<br> <br> - `NS` - **Nova Scotia (CAN)**<br> <br> - `NB` - **New Brunswick (CAN)**<br> <br> - `NL` - **Newfoundland and Labrador (CAN)**<br> <br> - `NT` - **Northwest Territories (CAN)**<br> <br> - `NU` - **Nunavut (CAN)**<br> <br> - `PE` - **Prince Edward Island (CAN)**<br> <br> - `QC` - **Quebec (CAN)**<br> <br> - `SK` - **Saskatchewan (CAN)**<br> <br> - `YT` - **Yukon (CAN)**<br> </details><br> |
| `zip` | `str` | Optional | The ZIP code in the address associated with this Entity.<br>This field is stored as a text string and must be between 1 and 20 characters long. |
| `country` | [`EntityCountryEnum`](../../doc/models/entity-country-enum.md) | Optional | The country in the address associated with the Entity, currently accepting values including `USA` and `CAN`. |
| `timezone` | [`TimezoneEnum`](../../doc/models/timezone-enum.md) | Optional | The timezone for the address associated with the terminal's location.<br><br><details><br><summary>Valid Values</summary> <br>- `est` - **Eastern Standard Time**<br>- `pst` - **Pacific Standard Time**<br><br>- `cst` - **Central Standard Time**<br><br>- `mst` - **Mountain Daylight Time**<br><br>- `akst` - **Alaska Standard Time**<br><br>- `hst` - **Hawaii Standard Time**<br><br>- `sst` - **Samoa Standard Time**<br><br>- `chst` - **Chamorro Standard Time**<br><br>- `ast`  - **Atlantic Standard Time**<br><br>- `pwt` - **Palau Time**<br><br>- `mht` - **Marshall Islands Time**<br><br>- `chut` - **Chuuk Time**<br><br>- `nst` - **Newfoundland Standard Time**<br><br> </details><br> |
| `phone` | `str` | Optional | The phone number associated with this Entity.<br>This field is stored as a text string and must be between 5 and 15 characters long. |
| `customer_phone` | `str` | Optional | The customer service phone number associated with this Entity. For Merchants, this number will be displayed on the customer's credit card statement.<br>This field is stored as a text string and must be between 5 and 15 characters long. |
| `fax` | `str` | Optional | The fax number associated with this Entity.<br>This field is stored as a text string and must be between 5 and 15 characters long. |
| `email` | `str` | Optional | The email address associated with this Entity.<br>This field is stored as a text string and must be between 1 and 100 characters long. |
| `website` | `str` | Optional | The web site URL associated with this Entity.<br>This field is stored as a text string and must be between 0 and 500 characters long. |
| `apple_domain` | `str` | Optional | The web sites URL associated with this Entity.<br>This field is stored as a text string; must be between 0 and 1,000 characters long and separated by comma. |
| `ein_type` | [`EinTypeEnum`](../../doc/models/ein-type-enum.md) | Optional | Indicates if the TIN being used is an EIN, SSN, or other/unknown number.<br><br><details><br><summary>Valid Values</summary><br>- `ssn` - **Social Security Number.**<br>- `tin` - **Employer Identification Number.**<br>- `other` - **Other/Unknown TIN.**<br></details><br> |
| `irs_filing_name` | `str` | Optional | The IRS Legal Filing Name. This must match what has been provided to the IRS when filing taxes. |
| `ein` | `str` | Optional | The IRS Employer Identification Number (EIN) for the Entity.<br>This field is stored as an integer and must be 9 characters long. |
| `locations` | `int` | Optional | The number of locations at which this Entity does business.<br>This field is stored as an integer and must be between 1 and 1,000,000 characters long. |
| `public` | [`EntitiesPublicEnum`](../../doc/models/entities-public-enum.md) | Optional | Indicates whether this is a publicly held entity.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Private entity**<br>- `1` - **Public entity**<br></details><br>**Default**: `0`<br> |
| `tc_version` | `str` | Optional | An indicator showing the version of the terms and conditions that this Entity has accepted. The API indicates the version as a string.<br>This field is stored as a text string and must be between 0 and 20 characters long. |
| `tc_accept_date` | `str` | Optional | Date and time on which this Entity accepted the Terms and Conditions, if different than `tcDate`.<br>The date is specified as a 12-digit string in YYYYMMDDHHII format, for example, `201601201528` for January 20, 2016, at 15:28 (3:28 PM). |
| `tc_accept_ip` | `str` | Optional | IP address from which this Entity accepted the Terms and Conditions, if different than `tcIp`. |
| `custom` | `str` | Optional | Custom, free-form field for client-supplied text; must be between 0 and 1,000 characters long. |
| `payout_secondary_descriptor` | `str` | Optional | The secondary billing descriptor to appear on the bank statements for funds transfer for the entity. |
| `industry` | `str` | Optional | This field is stored as a text string and must be between 0 and 1,000 characters long. |
| `global_business_type` | [`GlobalBusinessTypeEnum`](../../doc/models/global-business-type-enum.md) | Optional | The business registration type for the entity<br><br><details><br><summary>Valid Values for country USA</summary><br>- `ssn` - **Social Security Number.**<br>- `tin` - **Employer Identification Number.**<br>- `other` - **Other/Unknown TIN.**<br></details><br><details><br><summary>Valid Values for country Canada</summary><br>- `CD` - **Federal**<br>- `AB` - **Alberta**<br>- `BC` - **British Columbia**<br>- `MB` - **Manitoba**<br>- `NB` - **New Brunswick**<br>- `NL` - **Newfoundland and Labrador**<br>- `NT` - **Northwest Territories**<br>- `NS` - **Nova Scotia**<br>- `NU` - **Nunavut**<br>- `ON` - **Ontario**<br>- `PE` - **Prince Edward Island**<br>- `QC` - **Quebec**<br>- `SK` - **Saskatchewan**<br>- `YT` - **Yukon**<br></details><br> |
| `global_business_id` | `str` | Optional | The business registration number for the entity.<br>This field is stored as an alphanumeric and must be between 9 to 10 characters long. |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "clientIp": "152.58.83.44",
  "login": "t1_log_6733015a79f48410904564b",
  "type": 6,
  "name": "Splash LLC",
  "address1": "1234 Rivver Lane",
  "address2": "San house Fremont",
  "city": "Frisco",
  "state": "TX",
  "zip": "75034",
  "country": "USA",
  "timezone": "cst",
  "phone": "995685662566",
  "fax": "995685662566",
  "email": "rawatankit0911@gmail.com",
  "website": "http://payrix.com",
  "ein": "678912345",
  "tcVersion": "1.0",
  "tcDate": "2024-11-12 02:18:50",
  "tcIp": "134.238.16.164",
  "tcAcceptDate": "202204281403",
  "tcAcceptIp": "162.250.123.158",
  "custom": "voluptatibus et accusamus",
  "inactive": 0,
  "frozen": 0,
  "tinStatus": 0,
  "public": 1,
  "customerPhone": "995685662566",
  "locations": 1,
  "industry": "Residential Painting",
  "displayName": "John",
  "payoutSecondaryDescriptor": "Apex Leadership",
  "einType": "ssn",
  "irsFilingName": "Integration Test 2025-02-21T09:12:15.332",
  "currency": "USD",
  "globalBusinessId": "678912345",
  "globalBusinessType": "ssn"
}
```

