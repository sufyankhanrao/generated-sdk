
# Logins Response 2

The details of Login that owns this resource.

## Structure

`LoginsResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `login` | str \| [loginsResponse1](../../doc/models/logins-response-1.md) \| None | Optional | This is a container for any-of cases. |
| `last_login` | `str` | Optional | The timestamp when this Login last logged in to the API. The format should be YYYY-MM-DD HH:MM:SS.<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}` |
| `username` | `str` | Optional | The username associated with this Login.<br>This field is stored as a text string, all lowercase, and must be between 0 and 50 characters long. |
| `password` | `str` | Optional | The password associated with this Login.<br>This field is stored as a text string and must be between 0 and 100 characters long. |
| `sso_id` | `str` | Optional | The SSO (Single Sign On) ID setup for the login.<br>This field is stored as a text string and must be between 1 and 100 characters long. |
| `first` | `str` | Optional | The first name associated with this Login. |
| `middle` | `str` | Optional | The middle name associated with this Login. |
| `last` | `str` | Optional | The last name associated with this Login. |
| `email` | `str` | Optional | The email address associated with this Login. |
| `fax` | `str` | Optional | The fax number associated with this Login.<br>This field is stored as a text string and must be between 10 and 15 characters long. |
| `phone` | `str` | Optional | The phone number associated with this Login.<br>This field is stored as a text string and must be between 10 and 15 characters long. |
| `country` | [`CountryEnum`](../../doc/models/country-enum.md) | Optional | The country associated with this Customer.<br>Valid values for this field is the 3-letter ISO code for the country. |
| `zip` | `str` | Optional | The ZIP code in the address associated with this Login.<br>This field is stored as a text string and must be between 1 and 20 characters long. |
| `state` | `str` | Optional | The U.S. state or Canadian province relevant to the address provided here. If the location is within the U.S. and Canada, specify the 2-character postal abbreviation for the state. If the location is outside of the U.S. and Canada, provide the full state name. This field is stored as a text string and must be between 2 and 100 characters long.<br><br><details><br><summary>U.S. States</summary><br> <br> - `AK` - **Alaska (US)**<br> <br> - `AR` - **Arkansas (US)**<br> <br> - `AL` - **Alabama (US)**<br> <br> - `AZ` - **Arizona (US)**<br> <br> - `CA` - **California (US)**<br> <br> - `CO` - **Colorado (US)**<br> <br> - `CT` - **Connecticut (US)**<br> <br> - `DE` - **Delaware (US)**<br> <br> - `FL` - **Florida (US)**<br> <br> - `GA` - **Georgia (US)**<br> <br> - `HI` - **Hawaii (US)**<br> <br> - `IA` - **Iowa (US)**<br> <br> - `ID` - **Idaho (US)**<br> <br> - `IL` - **Illinois (US)**<br> <br> - `IN` - **Indiana (US)**<br> <br> - `KY` - **Kentucky (US)**<br> <br> - `KS` - **Kansas (US)**<br> <br> - `LA` - **Louisiana (US)**<br> <br> - `MA` - **Massachusetts (US)**<br> <br> - `MD` - **Maryland (US)**<br> <br> - `ME` - **Maine (US)**<br> <br> - `MI` - **Michigan (US)**<br> <br> - `MN` - **Minnesota (US)**<br> <br> - `MO` - **Missouri (US)**<br> <br> - `MS` - **Mississippi (US)**<br> <br> - `MT` - **Montana (US)**<br> <br> - `NC` - **North Carolina (US)**<br> <br> - `ND` - **North Dakota (US)**<br> <br> - `NE` - **Nebraska (US)**<br> <br> - `NH` - **New Hampshire (US)**<br> <br> - `NJ` - **New Jersey (US)**<br> <br> - `NM` - **New Mexico (US)**<br> <br> - `NV` - **Nevada (US)**<br> <br> - `NY` - **New York (US)**<br> <br> - `OH` - **Ohio (US)**<br> <br> - `OK`- **Oklahoma (US)**<br> <br> - `OR` - **Oregon (US)**<br> <br> - `PA` - **Pennsylvania (US)**<br> <br> - `RI` - **Rhode Island (US)**<br> <br> - `SC`- **South Carolina (US)**<br> <br> - `SD` - **South Dakota (US)**<br> <br> - `TN` - **Tennessee (US)**<br> <br> - `TX` - **Texas (US)**<br> <br> - `UT` - **Utah (US)**<br> <br> - `VA` - **Virginia (US)**<br> <br> - `VT` - **Vermont (US)**<br> <br> - `WA` - **Washington (US)**<br> <br> - `WI` - **Wisconsin (US)**<br> <br> - `WV` - **West Virginia (US)**<br> <br> - `WY` - **Wyoming (US)**<br> </details><br> <details><br><summary>Canada Provinces and Territories</summary><br> <br> - `AB` - **Alberta (CAN)**<br> <br> - `BC` - **British Columbia (CAN)**<br> <br> - `MB` - **Manitoba (CAN)**<br> <br> - `ON` - **Ontario (CAN)**<br> <br> - `NS` - **Nova Scotia (CAN)**<br> <br> - `NB` - **New Brunswick (CAN)**<br> <br> - `NL` - **Newfoundland and Labrador (CAN)**<br> <br> - `NT` - **Northwest Territories (CAN)**<br> <br> - `NU` - **Nunavut (CAN)**<br> <br> - `PE` - **Prince Edward Island (CAN)**<br> <br> - `QC` - **Quebec (CAN)**<br> <br> - `SK` - **Saskatchewan (CAN)**<br> <br> - `YT` - **Yukon (CAN)**<br> </details><br> |
| `city` | `str` | Optional | The name of the city in the address associated with this Login.<br>This field is stored as a text string and must be between 1 and 500 characters long. |
| `address_2` | `str` | Optional | The second line of the address associated with this Login.<br>This field is stored as a text string and must be between 1 and 500 characters long. |
| `address_1` | `str` | Optional | The first line of the address associated with this Login.<br>This field is stored as a text string and must be between 1 and 500 characters long. |
| `confirmed` | [`ConfirmedEnum`](../../doc/models/confirmed-enum.md) | Optional | Whether the email associated with this Login was confirmed. This field is stored as an integer and will be set to '1' when the email is confirmed.<br><br><details> <summary>Valid Values</summary><br>- `0`  - **Not confirmed.**<br>- `1`  - **Confirmed.**<br><br> </details><br> |
| `roles` | `int` | Optional | The roles associated with this Login, specified as an integer. |
| `partition` | `str` | Optional | The partition that this Login is associated with. |
| `division` | str \| [divisionsResponse](../../doc/models/divisions-response.md) \| None | Optional | This is a container for any-of cases. |
| `parent_division` | `str` | Optional | The parent division that this Login belongs to. Children of this Login will inherit its parent division. |
| `allowed_resources` | `str` | Optional | The allowedResources field specifies the actions and resources a user can access. The JSON structure includes action keys (create, update, read, delete, totals) and lists of resources (e.g., logins, apikeys, sessions). Omitted action keys indicate no access for those actions. |
| `restricted_resources` | `str` | Optional | The restrictedResources field defines the actions and resources a user is restricted from accessing. The JSON structure includes action keys (create, update, read, delete, totals) and lists of resources (e.g., logins, apikeys, sessions). Omitted action keys indicate no restrictions for those actions. |
| `portal_access` | [`PortalAccessEnum`](../../doc/models/portal-access-enum.md) | Optional | Whether or not this user should have access to portal functionality.<br><br><details><br><summary>Valid Values</summary> <br>- `0` - **No access to the portal**<br>- `1` - **Has access to the portal**<br><br> </details><br> |
| `mfa_enabled` | [`MfaEnabledEnum`](../../doc/models/mfa-enabled-enum.md) | Optional | Whether or not this user should have multi factor authentication (MFA) feature.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Disabled**<br>- `1` - **Enabled**<br></details><br> |
| `mfa_secret` | `str` | Optional | The MFA secret key used to link the MFA device with this Login.<br>This field is stored as a text string and must be between 1 and 128 characters long. |
| `mfa_enrolled_date` | `str` | Optional | The datetimestamp  when this Login was enabled for MFA. |
| `mfa_type` | `str` | Optional | The Type of the MFA enrolled.<br>This field is stored as a text string and must be between 1 and 50 characters long. |
| `effective_roles` | `int` | Optional | EffectiveRoles is included in the response when a user record is returned via API indicating the full effective roles of the user (as an integer), broken down by role, for roles that include other roles automatically. |
| `mfa_sms_codes_count` | `int` | Optional | The end time of the current MFA SMS window which is a sliding window limitinig how many codes can be generated during a given window |
| `mfa_sms_window` | `int` | Optional | The most recent SMS Code which has been texted to the user |
| `login_as_enabled` | `int` | Optional | Whether the associated login can use loginAs or not |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |
| `aggregations` | [`List[AggregationsResponse]`](../../doc/models/aggregations-response.md) | Optional | - |
| `analyzed_change_requests` | [`List[ChangeRequest]`](../../doc/models/change-request.md) | Optional | - |
| `change_requests` | [`List[ChangeRequest]`](../../doc/models/change-request.md) | Optional | - |
| `confirm_codes` | [`List[ConfirmCodesResponse]`](../../doc/models/confirm-codes-response.md) | Optional | - |
| `customers` | [`List[CustomersResponse]`](../../doc/models/customers-response.md) | Optional | - |
| `billings` | [`List[BillingsResponse]`](../../doc/models/billings-response.md) | Optional | - |
| `divisions` | [`List[DivisionsResponse1]`](../../doc/models/divisions-response-1.md) | Optional | - |
| `entities` | [`List[EntitiesResponse]`](../../doc/models/entities-response.md) | Optional | - |
| `entity_returns` | [`List[EntityReturnsResponse]`](../../doc/models/entity-returns-response.md) | Optional | - |
| `invoices` | [`List[InvoicesResponse]`](../../doc/models/invoices-response.md) | Optional | - |
| `invoice_parameters` | [`List[InvoiceParametersResponse]`](../../doc/models/invoice-parameters-response.md) | Optional | - |
| `logins` | [`List[LoginsResponse3]`](../../doc/models/logins-response-3.md) | Optional | - |
| `logins_helpers` | [`List[LoginHelpersResponse]`](../../doc/models/login-helpers-response.md) | Optional | - |
| `notes` | [`List[NotesResponse]`](../../doc/models/notes-response.md) | Optional | - |
| `message_threads` | [`List[MessageThreadsResponse]`](../../doc/models/message-threads-response.md) | Optional | - |
| `org_flows` | [`List[OrgFlowsResponse]`](../../doc/models/org-flows-response.md) | Optional | - |
| `org_flowsforlogin` | [`List[OrgFlowsResponse]`](../../doc/models/org-flows-response.md) | Optional | - |
| `profit_shares` | [`List[ProfitSharesResponse]`](../../doc/models/profit-shares-response.md) | Optional | - |
| `secrets` | [`List[SecretsResponse]`](../../doc/models/secrets-response.md) | Optional | - |
| `team_logins` | [`List[TeamLoginResponse]`](../../doc/models/team-login-response.md) | Optional | - |
| `teams` | [`List[TeamsResponse]`](../../doc/models/teams-response.md) | Optional | - |

## Example (as JSON)

```json
{
  "inactive": 0,
  "frozen": 0,
  "id": "id2",
  "created": "created2",
  "modified": "modified0",
  "creator": "String1",
  "modifier": "modifier6"
}
```

