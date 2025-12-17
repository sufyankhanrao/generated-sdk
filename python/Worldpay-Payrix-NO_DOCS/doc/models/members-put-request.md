
# Members Put Request

## Structure

`MembersPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant` | `str` | Optional | The identifier of the Merchant associated with this Member. |
| `title` | `str` | Optional | The title that this Member holds in relation to the associated Merchant.<br>This field is stored as a text string and must be between 0 and 100 characters long.<br>For example, 'CEO', 'Owner' or 'Director of Finance'. |
| `first` | `str` | Optional | The first name associated with this Member.<br>This field is stored as a text string and must be between 1 and 100 characters long. |
| `middle` | `str` | Optional | The middle name associated with this Member.<br>This field is stored as a text string and must be between 0 and 100 characters long. |
| `last` | `str` | Optional | The last name associated with this Member.<br>This field is stored as a text string and must be between 1 and 100 characters long. |
| `ssn` | `str` | Optional | The social security number of this Member. This field is required if the Merchant associated with the Member is a sole trader.<br>This field is stored as a text string and must be 9 characters long and numeric characters only. |
| `citizenship` | [`CitizenshipEnum`](../../doc/models/citizenship-enum.md) | Optional | The country of which the owner is a citizen.<br>Valid values for this field is the 3-letter ISO code for the country. |
| `dob` | `int` | Optional | The date of birth of this Member.  The date is specified as an eight digit string in YYYYMMDD format, for example, '20160120' for January 20, 2016. |
| `gender` | [`GenderEnum`](../../doc/models/gender-enum.md) | Optional | The gender of this Member.<br><br><details><br><summary>Valid Values</summary><br>- `male` - **Male**<br>- `female` - **Female**<br><br></details><br> |
| `dl` | `str` | Optional | The driver's license number of this Member.<br>This field is stored as a text string and must be between 0 and 15 characters long. |
| `dlstate` | `str` | Optional | The U.S. state or Canadian province relevant to the address provided here. If the location is within the U.S. and Canada, specify the 2-character postal abbreviation for the state. If the location is outside of the U.S. and Canada, provide the full state name. This field is stored as a text string and must be between 2 and 100 characters long.<br><br><details><br><summary>U.S. States</summary><br> <br> - `AK` - **Alaska (US)**<br> <br> - `AR` - **Arkansas (US)**<br> <br> - `AL` - **Alabama (US)**<br> <br> - `AZ` - **Arizona (US)**<br> <br> - `CA` - **California (US)**<br> <br> - `CO` - **Colorado (US)**<br> <br> - `CT` - **Connecticut (US)**<br> <br> - `DE` - **Delaware (US)**<br> <br> - `FL` - **Florida (US)**<br> <br> - `GA` - **Georgia (US)**<br> <br> - `HI` - **Hawaii (US)**<br> <br> - `IA` - **Iowa (US)**<br> <br> - `ID` - **Idaho (US)**<br> <br> - `IL` - **Illinois (US)**<br> <br> - `IN` - **Indiana (US)**<br> <br> - `KY` - **Kentucky (US)**<br> <br> - `KS` - **Kansas (US)**<br> <br> - `LA` - **Louisiana (US)**<br> <br> - `MA` - **Massachusetts (US)**<br> <br> - `MD` - **Maryland (US)**<br> <br> - `ME` - **Maine (US)**<br> <br> - `MI` - **Michigan (US)**<br> <br> - `MN` - **Minnesota (US)**<br> <br> - `MO` - **Missouri (US)**<br> <br> - `MS` - **Mississippi (US)**<br> <br> - `MT` - **Montana (US)**<br> <br> - `NC` - **North Carolina (US)**<br> <br> - `ND` - **North Dakota (US)**<br> <br> - `NE` - **Nebraska (US)**<br> <br> - `NH` - **New Hampshire (US)**<br> <br> - `NJ` - **New Jersey (US)**<br> <br> - `NM` - **New Mexico (US)**<br> <br> - `NV` - **Nevada (US)**<br> <br> - `NY` - **New York (US)**<br> <br> - `OH` - **Ohio (US)**<br> <br> - `OK`- **Oklahoma (US)**<br> <br> - `OR` - **Oregon (US)**<br> <br> - `PA` - **Pennsylvania (US)**<br> <br> - `RI` - **Rhode Island (US)**<br> <br> - `SC`- **South Carolina (US)**<br> <br> - `SD` - **South Dakota (US)**<br> <br> - `TN` - **Tennessee (US)**<br> <br> - `TX` - **Texas (US)**<br> <br> - `UT` - **Utah (US)**<br> <br> - `VA` - **Virginia (US)**<br> <br> - `VT` - **Vermont (US)**<br> <br> - `WA` - **Washington (US)**<br> <br> - `WI` - **Wisconsin (US)**<br> <br> - `WV` - **West Virginia (US)**<br> <br> - `WY` - **Wyoming (US)**<br> </details><br> <details><br><summary>Canada Provinces and Territories</summary><br> <br> - `AB` - **Alberta (CAN)**<br> <br> - `BC` - **British Columbia (CAN)**<br> <br> - `MB` - **Manitoba (CAN)**<br> <br> - `ON` - **Ontario (CAN)**<br> <br> - `NS` - **Nova Scotia (CAN)**<br> <br> - `NB` - **New Brunswick (CAN)**<br> <br> - `NL` - **Newfoundland and Labrador (CAN)**<br> <br> - `NT` - **Northwest Territories (CAN)**<br> <br> - `NU` - **Nunavut (CAN)**<br> <br> - `PE` - **Prince Edward Island (CAN)**<br> <br> - `QC` - **Quebec (CAN)**<br> <br> - `SK` - **Saskatchewan (CAN)**<br> <br> - `YT` - **Yukon (CAN)**<br> </details><br> |
| `email` | `str` | Optional | The email address of this Member.<br>This field is stored as a text string and must be between 1 and 100 characters long. |
| `ownership` | `int` | Optional | The share of the Member's ownership of the associated Merchant, expressed in basis points.<br>For example, 25.3% is expressed as '2530'.<br>This field is stored as an integer and must be between 1 and 10000 characters long. |
| `primary` | [`MembersPrimaryEnum`](../../doc/models/members-primary-enum.md) | Optional | Indicates whether the Member is the 'primary' contact for the associated Merchant. Only one Member associated with each Merchant can be the 'primary' Member.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Primary contact.**<br>- `1` - **Primary contact.**<br><br></details><br>**Default**: `0`<br> |
| `credit_score` | `int` | Optional | A credit score is a three-digit number that rates your creditworthiness. scores range from 334 to 818. |
| `credit_score_date` | `str` | Optional | Date for Credit Score. |
| `significant_responsibility` | [`SignificantResponsibilityEnum`](../../doc/models/significant-responsibility-enum.md) | Optional | 'A controlling authority', or 'Control Prong'. Includes, but is not limited to:<br><br>* Chief Executive Officer,<br><br>* Chief Financial Officer,<br><br>* Chief Operating Officer,<br><br>* Managing Member,<br><br>* General Partner,<br><br>* President,<br><br>* Vice Presidents, or<br><br>* An individual with significant legal authority to enter the Legal Entity into a commercial relationship.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **No significant responsibility.**<br>- `1` - **Significant reponsibility.**<br><br></details><br> |
| `politically_exposed` | [`PoliticallyExposedEnum`](../../doc/models/politically-exposed-enum.md) | Optional | This person is politically exposed, defined as: "persons whom through their prominent position or influence, is more susceptible to being involved in bribery or corruption."<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not politically exposed.**<br>- `1` - **Politically exposed.**<br><br></details><br> |
| `mailing_address_1` | `str` | Optional | The mailing first line of the address associated with this Member.<br>This field is stored as a text string and must be between 1 and 500 characters long. |
| `mailing_address_2` | `str` | Optional | The mailing second line of the address associated with this Member.<br>This field is stored as a text string and must be between 1 and 500 characters long. |
| `mailing_city` | `str` | Optional | The mailing name of the city in the address associated with this Member.<br>This field is stored as a text string and must be between 1 and 500 characters long. |
| `mailing_state` | `str` | Optional | The U.S. state or Canadian province relevant to the address provided here. If the location is within the U.S. and Canada, specify the 2-character postal abbreviation for the state. If the location is outside of the U.S. and Canada, provide the full state name. This field is stored as a text string and must be between 2 and 100 characters long.<br><br><details><br><summary>U.S. States</summary><br> <br> - `AK` - **Alaska (US)**<br> <br> - `AR` - **Arkansas (US)**<br> <br> - `AL` - **Alabama (US)**<br> <br> - `AZ` - **Arizona (US)**<br> <br> - `CA` - **California (US)**<br> <br> - `CO` - **Colorado (US)**<br> <br> - `CT` - **Connecticut (US)**<br> <br> - `DE` - **Delaware (US)**<br> <br> - `FL` - **Florida (US)**<br> <br> - `GA` - **Georgia (US)**<br> <br> - `HI` - **Hawaii (US)**<br> <br> - `IA` - **Iowa (US)**<br> <br> - `ID` - **Idaho (US)**<br> <br> - `IL` - **Illinois (US)**<br> <br> - `IN` - **Indiana (US)**<br> <br> - `KY` - **Kentucky (US)**<br> <br> - `KS` - **Kansas (US)**<br> <br> - `LA` - **Louisiana (US)**<br> <br> - `MA` - **Massachusetts (US)**<br> <br> - `MD` - **Maryland (US)**<br> <br> - `ME` - **Maine (US)**<br> <br> - `MI` - **Michigan (US)**<br> <br> - `MN` - **Minnesota (US)**<br> <br> - `MO` - **Missouri (US)**<br> <br> - `MS` - **Mississippi (US)**<br> <br> - `MT` - **Montana (US)**<br> <br> - `NC` - **North Carolina (US)**<br> <br> - `ND` - **North Dakota (US)**<br> <br> - `NE` - **Nebraska (US)**<br> <br> - `NH` - **New Hampshire (US)**<br> <br> - `NJ` - **New Jersey (US)**<br> <br> - `NM` - **New Mexico (US)**<br> <br> - `NV` - **Nevada (US)**<br> <br> - `NY` - **New York (US)**<br> <br> - `OH` - **Ohio (US)**<br> <br> - `OK`- **Oklahoma (US)**<br> <br> - `OR` - **Oregon (US)**<br> <br> - `PA` - **Pennsylvania (US)**<br> <br> - `RI` - **Rhode Island (US)**<br> <br> - `SC`- **South Carolina (US)**<br> <br> - `SD` - **South Dakota (US)**<br> <br> - `TN` - **Tennessee (US)**<br> <br> - `TX` - **Texas (US)**<br> <br> - `UT` - **Utah (US)**<br> <br> - `VA` - **Virginia (US)**<br> <br> - `VT` - **Vermont (US)**<br> <br> - `WA` - **Washington (US)**<br> <br> - `WI` - **Wisconsin (US)**<br> <br> - `WV` - **West Virginia (US)**<br> <br> - `WY` - **Wyoming (US)**<br> </details><br> <details><br><summary>Canada Provinces and Territories</summary><br> <br> - `AB` - **Alberta (CAN)**<br> <br> - `BC` - **British Columbia (CAN)**<br> <br> - `MB` - **Manitoba (CAN)**<br> <br> - `ON` - **Ontario (CAN)**<br> <br> - `NS` - **Nova Scotia (CAN)**<br> <br> - `NB` - **New Brunswick (CAN)**<br> <br> - `NL` - **Newfoundland and Labrador (CAN)**<br> <br> - `NT` - **Northwest Territories (CAN)**<br> <br> - `NU` - **Nunavut (CAN)**<br> <br> - `PE` - **Prince Edward Island (CAN)**<br> <br> - `QC` - **Quebec (CAN)**<br> <br> - `SK` - **Saskatchewan (CAN)**<br> <br> - `YT` - **Yukon (CAN)**<br> </details><br> |
| `mailing_country` | [`MailingCountryEnum`](../../doc/models/mailing-country-enum.md) | Optional | The country of which the owner is a citizen.<br>Valid values for this field is the 3-letter ISO code for the country. |
| `mailing_postal_code` | `str` | Optional | The mailing postal code in the address associated with this Member.<br>This field is stored as a text string and must be between 1 and 20 characters long. |
| `treasury_prime_roles` | `Any` | Optional | - |
| `timezone` | [`TimezoneEnum`](../../doc/models/timezone-enum.md) | Optional | The timezone for the address associated with the terminal's location.<br><br><details><br><summary>Valid Values</summary><br>- `est` - **Eastern Standard Time**<br>- `cst` - **Central Standard Time**<br><br>- `pst` - **Pacific Standard Time**<br><br>- `mst` - **Mountain Daylight Time**<br><br>- `akst` - **Alaska Standard Time**<br><br>- `hst` - **Hawaii Standard Time**<br><br>- `sst` - **Samoa Standard Time**<br><br>- `chst` - **Chamorro Standard Time**<br><br>- `ast` - **Atlantic Standard Time**<br><br>- `pwt` - **Palau Time**<br><br>- `mht` - **Marshall Islands Time**<br><br>- `chut` - **Chuuk Time**<br><br>- `nst` - **Newfoundland Standard Time**<br><br></details><br> |
| `address_1` | `str` | Optional | The first line of the address associated with this Member.<br>This field is stored as a text string and must be between 1 and 500 characters long. |
| `address_2` | `str` | Optional | The second line of the address associated with this Member.<br>This field is stored as a text string and must be between 1 and 500 characters long. |
| `city` | `str` | Optional | The name of the city in the address associated with this Member.<br>This field is stored as a text string and must be between 1 and 500 characters long. |
| `state` | `str` | Optional | The U.S. state or Canadian province relevant to the address provided here. If the location is within the U.S. and Canada, specify the 2-character postal abbreviation for the state. If the location is outside of the U.S. and Canada, provide the full state name. This field is stored as a text string and must be between 2 and 100 characters long.<br><br><details><br><summary>U.S. States</summary><br> <br> - `AK` - **Alaska (US)**<br> <br> - `AR` - **Arkansas (US)**<br> <br> - `AL` - **Alabama (US)**<br> <br> - `AZ` - **Arizona (US)**<br> <br> - `CA` - **California (US)**<br> <br> - `CO` - **Colorado (US)**<br> <br> - `CT` - **Connecticut (US)**<br> <br> - `DE` - **Delaware (US)**<br> <br> - `FL` - **Florida (US)**<br> <br> - `GA` - **Georgia (US)**<br> <br> - `HI` - **Hawaii (US)**<br> <br> - `IA` - **Iowa (US)**<br> <br> - `ID` - **Idaho (US)**<br> <br> - `IL` - **Illinois (US)**<br> <br> - `IN` - **Indiana (US)**<br> <br> - `KY` - **Kentucky (US)**<br> <br> - `KS` - **Kansas (US)**<br> <br> - `LA` - **Louisiana (US)**<br> <br> - `MA` - **Massachusetts (US)**<br> <br> - `MD` - **Maryland (US)**<br> <br> - `ME` - **Maine (US)**<br> <br> - `MI` - **Michigan (US)**<br> <br> - `MN` - **Minnesota (US)**<br> <br> - `MO` - **Missouri (US)**<br> <br> - `MS` - **Mississippi (US)**<br> <br> - `MT` - **Montana (US)**<br> <br> - `NC` - **North Carolina (US)**<br> <br> - `ND` - **North Dakota (US)**<br> <br> - `NE` - **Nebraska (US)**<br> <br> - `NH` - **New Hampshire (US)**<br> <br> - `NJ` - **New Jersey (US)**<br> <br> - `NM` - **New Mexico (US)**<br> <br> - `NV` - **Nevada (US)**<br> <br> - `NY` - **New York (US)**<br> <br> - `OH` - **Ohio (US)**<br> <br> - `OK`- **Oklahoma (US)**<br> <br> - `OR` - **Oregon (US)**<br> <br> - `PA` - **Pennsylvania (US)**<br> <br> - `RI` - **Rhode Island (US)**<br> <br> - `SC`- **South Carolina (US)**<br> <br> - `SD` - **South Dakota (US)**<br> <br> - `TN` - **Tennessee (US)**<br> <br> - `TX` - **Texas (US)**<br> <br> - `UT` - **Utah (US)**<br> <br> - `VA` - **Virginia (US)**<br> <br> - `VT` - **Vermont (US)**<br> <br> - `WA` - **Washington (US)**<br> <br> - `WI` - **Wisconsin (US)**<br> <br> - `WV` - **West Virginia (US)**<br> <br> - `WY` - **Wyoming (US)**<br> </details><br> <details><br><summary>Canada Provinces and Territories</summary><br> <br> - `AB` - **Alberta (CAN)**<br> <br> - `BC` - **British Columbia (CAN)**<br> <br> - `MB` - **Manitoba (CAN)**<br> <br> - `ON` - **Ontario (CAN)**<br> <br> - `NS` - **Nova Scotia (CAN)**<br> <br> - `NB` - **New Brunswick (CAN)**<br> <br> - `NL` - **Newfoundland and Labrador (CAN)**<br> <br> - `NT` - **Northwest Territories (CAN)**<br> <br> - `NU` - **Nunavut (CAN)**<br> <br> - `PE` - **Prince Edward Island (CAN)**<br> <br> - `QC` - **Quebec (CAN)**<br> <br> - `SK` - **Saskatchewan (CAN)**<br> <br> - `YT` - **Yukon (CAN)**<br> </details><br> |
| `zip` | `str` | Optional | The ZIP code in the address associated with this Member.<br>This field is stored as a text string and must be between 1 and 20 characters long. |
| `country` | [`CountryEnum`](../../doc/models/country-enum.md) | Optional | The country of which the owner is a citizen.<br>Valid values for this field is the 3-letter ISO code for the country. |
| `phone` | `str` | Optional | The phone number associated with this Member.<br>This field is stored as a text string and must be between 5 and 15 characters long. |
| `fax` | `str` | Optional | The fax number associated with this Member.<br>This field is stored as a text string and must be between 5 and 15 characters long. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "merchant": "t1_mer_67d033698c234e74c399ddd",
  "first": "Chad",
  "last": "Foster",
  "dob": 20160120,
  "email": "Jerrod_Glover@hotmail.com",
  "ownership": 10000,
  "primary": 1,
  "significantResponsibility": 0,
  "politicallyExposed": 0,
  "timezone": "est",
  "title": "CEO",
  "middle": "middle name",
  "ssn": "1924",
  "citizenship": "MAR",
  "gender": "male",
  "dl": "6679",
  "dlstate": "MD",
  "creditScore": 334,
  "creditScoreDate": "2025-03-11 08:58:20",
  "mailingAddress1": "mailing first line of address",
  "mailingAddress2": "mailing second line of address",
  "mailingCity": "mailing name of the city",
  "mailingState": "MD",
  "mailingCountry": "MAR",
  "mailingPostalCode": "mailing postal code",
  "address1": "first line of address",
  "address2": "second line of address",
  "city": "name of city",
  "state": "MD",
  "zip": "ZIP code",
  "country": "MAR",
  "phone": "5106406000",
  "fax": "5106406000",
  "inactive": 0,
  "frozen": 0
}
```

