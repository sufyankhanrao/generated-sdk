
# Entities Response 1

The details of the Entity associated with this Merchant.

## Structure

`EntitiesResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `ip_created` | `str` | Optional | The incoming IP address from which this Entity was created. |
| `ip_modified` | `str` | Optional | The incoming IP address from which this Entity was last modified. |
| `client_ip` | `str` | Optional | The client IP address from which the Entity was created.<br>Valid values are any IPv4 or IPv6 address. |
| `login` | str \| [loginsResponse2](../../doc/models/logins-response-2.md) \| None | Optional | This is a container for any-of cases. |
| `parameter` | `str` | Optional | The parameter associated with this Entity. |
| `total_credit_disbursements` | `int` | Optional | The sum of all negative disbursements, in cents, associated to this Entity. |
| `mtype` | [`EntityTypeEnum`](../../doc/models/entity-type-enum.md) | Optional | The type of Entity.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Sole Proprietorship**<br>- `1` - **Corporation**<br>- `2` - **Limited Liability Company**<br>- `3` - **Partnership**<br>- `4` - **Association**<br>- `5` - **Non-Profit Organization**<br>- `6` - **Government Organization**<br>- `7` - **C Corporation**<br>- `8` - **S Corporation**<br></details><br> |
| `name` | `str` | Optional | The name of this Entity.<br>This field is stored as a text string and must be between 1 and 100 characters long. |
| `display_name` | `str` | Optional | The display name of this Entity.<br>This field is stored as a text string and must be between 1 and 1,000 characters long. |
| `address_1` | `str` | Optional | The first line of the address associated with this Entity.<br>This field is stored as a text string and must be between 1 and 500 characters long. |
| `address_2` | `str` | Optional | The second line of the address associated with this Entity.<br>This field is stored as a text string and must be between 1 and 500 characters long. |
| `city` | `str` | Optional | The name of the city in the address associated with this Entity.<br>This field is stored as a text string and must be between 1 and 500 characters long. |
| `state` | `str` | Optional | The U.S. state or Canadian province relevant to the address provided here. If the location is within the U.S. and Canada, specify the 2-character postal abbreviation for the state. If the location is outside of the U.S. and Canada, provide the full state name. This field is stored as a text string and must be between 2 and 100 characters long.<br><br><details><br><summary>U.S. States</summary><br> <br> - `AK` - **Alaska (US)**<br> <br> - `AR` - **Arkansas (US)**<br> <br> - `AL` - **Alabama (US)**<br> <br> - `AZ` - **Arizona (US)**<br> <br> - `CA` - **California (US)**<br> <br> - `CO` - **Colorado (US)**<br> <br> - `CT` - **Connecticut (US)**<br> <br> - `DE` - **Delaware (US)**<br> <br> - `FL` - **Florida (US)**<br> <br> - `GA` - **Georgia (US)**<br> <br> - `HI` - **Hawaii (US)**<br> <br> - `IA` - **Iowa (US)**<br> <br> - `ID` - **Idaho (US)**<br> <br> - `IL` - **Illinois (US)**<br> <br> - `IN` - **Indiana (US)**<br> <br> - `KY` - **Kentucky (US)**<br> <br> - `KS` - **Kansas (US)**<br> <br> - `LA` - **Louisiana (US)**<br> <br> - `MA` - **Massachusetts (US)**<br> <br> - `MD` - **Maryland (US)**<br> <br> - `ME` - **Maine (US)**<br> <br> - `MI` - **Michigan (US)**<br> <br> - `MN` - **Minnesota (US)**<br> <br> - `MO` - **Missouri (US)**<br> <br> - `MS` - **Mississippi (US)**<br> <br> - `MT` - **Montana (US)**<br> <br> - `NC` - **North Carolina (US)**<br> <br> - `ND` - **North Dakota (US)**<br> <br> - `NE` - **Nebraska (US)**<br> <br> - `NH` - **New Hampshire (US)**<br> <br> - `NJ` - **New Jersey (US)**<br> <br> - `NM` - **New Mexico (US)**<br> <br> - `NV` - **Nevada (US)**<br> <br> - `NY` - **New York (US)**<br> <br> - `OH` - **Ohio (US)**<br> <br> - `OK`- **Oklahoma (US)**<br> <br> - `OR` - **Oregon (US)**<br> <br> - `PA` - **Pennsylvania (US)**<br> <br> - `RI` - **Rhode Island (US)**<br> <br> - `SC`- **South Carolina (US)**<br> <br> - `SD` - **South Dakota (US)**<br> <br> - `TN` - **Tennessee (US)**<br> <br> - `TX` - **Texas (US)**<br> <br> - `UT` - **Utah (US)**<br> <br> - `VA` - **Virginia (US)**<br> <br> - `VT` - **Vermont (US)**<br> <br> - `WA` - **Washington (US)**<br> <br> - `WI` - **Wisconsin (US)**<br> <br> - `WV` - **West Virginia (US)**<br> <br> - `WY` - **Wyoming (US)**<br> </details><br> <details><br><summary>Canada Provinces and Territories</summary><br> <br> - `AB` - **Alberta (CAN)**<br> <br> - `BC` - **British Columbia (CAN)**<br> <br> - `MB` - **Manitoba (CAN)**<br> <br> - `ON` - **Ontario (CAN)**<br> <br> - `NS` - **Nova Scotia (CAN)**<br> <br> - `NB` - **New Brunswick (CAN)**<br> <br> - `NL` - **Newfoundland and Labrador (CAN)**<br> <br> - `NT` - **Northwest Territories (CAN)**<br> <br> - `NU` - **Nunavut (CAN)**<br> <br> - `PE` - **Prince Edward Island (CAN)**<br> <br> - `QC` - **Quebec (CAN)**<br> <br> - `SK` - **Saskatchewan (CAN)**<br> <br> - `YT` - **Yukon (CAN)**<br> </details><br> |
| `website` | `str` | Optional | The website URL associated with this Entity.<br>This field is stored as a text string and must be between 0 and 500 characters long. |
| `zip` | `str` | Optional | The ZIP code in the address associated with this Entity.<br>This field is stored as a text string and must be between 1 and 20 characters long. |
| `country` | [`EntityCountryEnum`](../../doc/models/entity-country-enum.md) | Optional | The country in the address associated with the Entity, currently accepting values including `USA` and `CAN`. |
| `timezone` | [`TimezoneEnum`](../../doc/models/timezone-enum.md) | Optional | The time zone for the address associated with the terminal's location.<br><br><details><br><summary>Valid Values</summary> <br>- `est` - **Eastern Standard Time**<br>- `pst` - **Pacific Standard Time**<br><br>- `cst` - **Central Standard Time**<br><br>- `mst` - **Mountain Daylight Time**<br><br>- `akst` - **Alaska Standard Time**<br><br>- `hst` - **Hawaii Standard Time**<br><br>- `sst` - **Samoa Standard Time**<br><br>- `chst` - **Chamorro Standard Time**<br><br>- `ast`  - **Atlantic Standard Time**<br><br>- `pwt` - **Palau Time**<br><br>- `mht` - **Marshall Islands Time**<br><br>- `chut` - **Chuuk Time**<br><br>- `nst` - **Newfoundland Standard Time**<br><br> </details><br> |
| `phone` | `str` | Optional | The phone number associated with this Entity.<br>This field is stored as a text string and must be between 5 and 15 characters long. |
| `customer_phone` | `str` | Optional | The customer service phone number associated with this Entity. For Merchants, this number will be displayed on the customer's credit card statement.<br>This field is stored as a text string and must be between 5 and 15 characters long. |
| `fax` | `str` | Optional | The fax number associated with this Entity.<br>This field is stored as a text string and must be between 5 and 15 characters long. |
| `email` | `str` | Optional | The email address associated with this Entity.<br>This field is stored as a text string and must be between 1 and 100 characters long. |
| `ein` | `str` | Optional | The IRS Employer Identification Number (EIN) for the Entity.<br>This field is stored as an integer and must be 9 characters long. |
| `ein_type` | [`EinTypeEnum`](../../doc/models/ein-type-enum.md) | Optional | Indicates if the TIN being used is an EIN, SSN, or other/unknown number.<br><br><details><br><summary>Valid Values</summary><br>- `ssn` - **Social Security Number.**<br>- `tin` - **Employer Identification Number.**<br>- `other` - **Other/Unknown TIN.**<br></details><br> |
| `global_business_id` | `str` | Optional | The business registration number for the entity.<br>This field is stored as an alphanumeric and must be between 9 to 10 characters long. |
| `global_business_type` | [`GlobalBusinessTypeEnum`](../../doc/models/global-business-type-enum.md) | Optional | The business registration type for the entity<br><br><details><br><summary>Valid Values for country USA</summary><br>- `ssn` - **Social Security Number.**<br>- `tin` - **Employer Identification Number.**<br>- `other` - **Other/Unknown TIN.**<br></details><br><details><br><summary>Valid Values for country Canada</summary><br>- `CD` - **Federal**<br>- `AB` - **Alberta**<br>- `BC` - **British Columbia**<br>- `MB` - **Manitoba**<br>- `NB` - **New Brunswick**<br>- `NL` - **Newfoundland and Labrador**<br>- `NT` - **Northwest Territories**<br>- `NS` - **Nova Scotia**<br>- `NU` - **Nunavut**<br>- `ON` - **Ontario**<br>- `PE` - **Prince Edward Island**<br>- `QC` - **Quebec**<br>- `SK` - **Saskatchewan**<br>- `YT` - **Yukon**<br></details><br> |
| `irs_filing_name` | `str` | Optional | The IRS Legal Filing Name. This must match what has been provided to the IRS when filing taxes. |
| `locations` | `int` | Optional | The number of locations at which this Entity does business.<br>This field is stored as an integer and must be between 1 and 1,000,000 characters long. |
| `tc_version` | `str` | Optional | An indicator showing the version of the terms and conditions that this Entity has accepted. The API indicates the version as a string.<br>This field is stored as a text string and must be between 0 and 20 characters long. |
| `tc_date` | `str` | Optional | Date the `tcVersion` was last updated. The format should be YYYY-MM-DD HH:MM:SS.<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}` |
| `tc_ip` | `str` | Optional | IP address of client from last `tcVersion` update. |
| `tc_accept_date` | `str` | Optional | Date and time on which this Entity accepted the Terms and Conditions, if different than tcDate.<br>The date is specified as a 12-digit string in YYYYMMDDHHII format, for example, `201601201528` for January 20, 2016, at 15:28 (3:28 PM). |
| `tc_accept_ip` | `str` | Optional | IP address from which this Entity accepted the Terms and Conditions, if different than `tcIp`. |
| `custom` | `str` | Optional | Custom, free-form field for client-supplied text; must be between 0 and 1,000 characters long. |
| `tin_status` | [`TinStatusEnum`](../../doc/models/tin-status-enum.md) | Optional | The Tax Identification Number (TIN) status of the entity.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Pending**<br>- `1` - **Valid**<br>- `2` - **Invalid**<br>- `3` - **Not required**<br></details><br> |
| `public` | [`EntitiesPublicEnum`](../../doc/models/entities-public-enum.md) | Optional | Indicates whether this is a publicly held entity.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Private entity**<br>- `1` - **Public entity**<br></details><br>**Default**: `0`<br> |
| `reserved` | [`ReservedEnum`](../../doc/models/reserved-enum.md) | Optional | Indicates the reserve status of the entity.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **No reserve.**<br>- `1` - **Block transaction, will never be processed. The Entity is sent to the manual review queue..**<br>- `3` - **Hold transaction, will not be captured.**<br>- `4` - **Reserve transaction, funds should be reserved.**<br>- `5` - **Block current activity, no change for merchant.**<br>- `6` - **Passed decision(s). Will not be set anywhere, will only be used for integration purposes.**<br>- `7` - **We did not have policies to process.**<br>- `8` - **We onboard the merchant and wait for manual check later.**<br>- `9` - **Schedule the automatic release of the reserve.**<br>- `10` - **Hold transaction, will not be captured. Automatic release when the associated sale is done.**<br></details><br> |
| `pending_risk_check` | [`PendingRiskCheckEnum`](../../doc/models/pending-risk-check-enum.md) | Optional | Whether it is pending a risk check.<br><br><details><br><summary>Valid Values</summary><br>- `pending` - **Pending**<br>- `successful` - **Successful**<br>- `failed` - **Failed**<br>- `manual` - **Manual**<br></details><br> |
| `check_stage` | [`EntityCheckStageEnum`](../../doc/models/entity-check-stage-enum.md) | Optional | The last stage completed for risk underwriting review.<br><br><details><br><summary>Valid Values</summary><br>- `createEntity` - **Merchant created.** No Signup Form submitted.<br>- `underwriting` - **Risk/Underwriting Review.** Merchant Signup Form submitted.<br>- `preboard` - **Preboard.** Check the Merchant before they are boarded.<br>- `postboard` - **Check the Merchant after they are boarded.**<br>- `txn` - **Check the Merchant when they process a Transaction.**<br>- `txnVolume` - **Check the Merchant when their transaction volume hits a certain amount.**<br>- `payout` - **Check the Merchant when a Payout occurs.**<br>- `payoutVolume` - **Check the Merchant when the volume of Payouts to the Merchant hits a certain amount.**<br></details><br> |
| `industry` | `str` | Optional | This field is stored as a text string and must be between 0 and 1,000 characters long. |
| `payout_secondary_descriptor` | `str` | Optional | The secondary billing descriptor to appear on the bank statements for funds transfer for the entity. |
| `currency` | [`CurrencyEnum`](../../doc/models/currency-enum.md) | Optional | The currency of this Entity. See <a href="https://www.iban.com/currency-codes" target="_blank">Currency codes</a>  for all valid values. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |
| `accounts` | [`List[AccountsResponse]`](../../doc/models/accounts-response.md) | Optional | - |
| `adjustments` | [`List[AdjustmentsResponse]`](../../doc/models/adjustments-response.md) | Optional | - |
| `adjustments_fromentity` | [`List[AdjustmentsResponse]`](../../doc/models/adjustments-response.md) | Optional | - |
| `adjustments_onentity` | [`List[AdjustmentsResponse]`](../../doc/models/adjustments-response.md) | Optional | - |
| `aggregations` | [`List[AggregationsResponse]`](../../doc/models/aggregations-response.md) | Optional | - |
| `owned_apple_domains` | [`List[AppleDomainsResponse]`](../../doc/models/apple-domains-response.md) | Optional | - |
| `assessments_onentity` | [`List[AssessmentsResponse]`](../../doc/models/assessments-response.md) | Optional | - |
| `billing_modifiers` | [`List[BillingModifiersResponse]`](../../doc/models/billing-modifiers-response.md) | Optional | - |
| `billings` | [`List[BillingsResponse]`](../../doc/models/billings-response.md) | Optional | - |
| `billings_forentity` | [`List[BillingsResponse]`](../../doc/models/billings-response.md) | Optional | - |
| `change_requests` | [`List[ChangeRequest]`](../../doc/models/change-request.md) | Optional | - |
| `contacts` | [`List[ContactsResponse]`](../../doc/models/contacts-response.md) | Optional | - |
| `credentials` | [`List[CredentialsResponse]`](../../doc/models/credentials-response.md) | Optional | - |
| `disbursements` | [`List[DisbursementsResponse]`](../../doc/models/disbursements-response.md) | Optional | - |
| `decisions` | [`List[DecisionsResponse]`](../../doc/models/decisions-response.md) | Optional | - |
| `embedded_finance` | [`List[DivisionsResponse2]`](../../doc/models/divisions-response-2.md) | Optional | - |
| `entity_custom_fields` | [`List[EntityCustomFieldsResponse]`](../../doc/models/entity-custom-fields-response.md) | Optional | - |
| `entity_data` | [`List[EntityDataResponse]`](../../doc/models/entity-data-response.md) | Optional | - |
| `entity_debts` | [`List[EntityDebtsResponse]`](../../doc/models/entity-debts-response.md) | Optional | - |
| `entity_debts_toentity` | [`List[EntityDebtsResponse]`](../../doc/models/entity-debts-response.md) | Optional | - |
| `entity_refs` | [`List[EntityRefsResponse]`](../../doc/models/entity-refs-response.md) | Optional | - |
| `entity_returns` | [`List[EntityReturnsResponse]`](../../doc/models/entity-returns-response.md) | Optional | - |
| `entity_terms` | [`List[EntityTermsResponse]`](../../doc/models/entity-terms-response.md) | Optional | - |
| `entries_onentity` | [`List[EntriesResponse]`](../../doc/models/entries-response.md) | Optional | - |
| `fees` | [`List[FeesResponse]`](../../doc/models/fees-response.md) | Optional | - |
| `forentity_fees` | [`List[FeesResponse]`](../../doc/models/fees-response.md) | Optional | - |
| `forentity_profit_shares` | [`List[ProfitSharesResponse]`](../../doc/models/profit-shares-response.md) | Optional | - |
| `funds` | [`List[FundsResponse]`](../../doc/models/funds-response.md) | Optional | - |
| `holds` | [`List[HoldsResponse]`](../../doc/models/holds-response.md) | Optional | - |
| `invoice_parameters` | [`List[InvoiceParametersResponse]`](../../doc/models/invoice-parameters-response.md) | Optional | - |
| `notes` | [`List[NotesResponse]`](../../doc/models/notes-response.md) | Optional | - |
| `org_entities` | [`List[OrgEntitiesResponse]`](../../doc/models/org-entities-response.md) | Optional | - |
| `omni_tokens` | [`List[OmniTokensResponse]`](../../doc/models/omni-tokens-response.md) | Optional | - |
| `payment_update_groups` | [`List[PaymentUpdateGroupsResponse]`](../../doc/models/payment-update-groups-response.md) | Optional | - |
| `payout_flows` | [`List[PayoutFlowsResponse]`](../../doc/models/payout-flows-response.md) | Optional | - |
| `payouts` | [`List[PayoutsResponse]`](../../doc/models/payouts-response.md) | Optional | - |
| `pending_entries_onentity` | [`List[PendingEntriesResponse]`](../../doc/models/pending-entries-response.md) | Optional | - |
| `pinless_debit_conversions` | [`List[PinlessDebitConversionsResponse]`](../../doc/models/pinless-debit-conversions-response.md) | Optional | - |
| `profit_shares` | [`List[ProfitSharesResponse]`](../../doc/models/profit-shares-response.md) | Optional | - |
| `reserve_entries_onentity` | [`List[ReserveEntriesResponse]`](../../doc/models/reserve-entries-response.md) | Optional | - |
| `reserves` | [`List[ReservesResponse]`](../../doc/models/reserves-response.md) | Optional | - |
| `revenue_boosts` | [`List[RevenueBoostsResponse]`](../../doc/models/revenue-boosts-response.md) | Optional | - |
| `rev_share_schedules_entity` | [`List[RevShareSchedulesResponse]`](../../doc/models/rev-share-schedules-response.md) | Optional | - |
| `rev_share_schedules_forentity` | [`List[RevShareSchedulesResponse]`](../../doc/models/rev-share-schedules-response.md) | Optional | - |
| `rev_share_statements_entity` | [`List[RevShareStatmentsResponse]`](../../doc/models/rev-share-statments-response.md) | Optional | - |
| `rev_share_statements_forentity` | [`List[RevShareStatmentsResponse]`](../../doc/models/rev-share-statments-response.md) | Optional | - |
| `secrets` | [`List[SecretsResponse]`](../../doc/models/secrets-response.md) | Optional | - |
| `statement_entries` | [`List[StatementEntriesResponse]`](../../doc/models/statement-entries-response.md) | Optional | - |
| `statement_entries_onentity` | [`List[StatementEntriesResponse]`](../../doc/models/statement-entries-response.md) | Optional | - |
| `statement_entries_forentity` | [`List[StatementEntriesResponse]`](../../doc/models/statement-entries-response.md) | Optional | - |
| `subscriptions` | [`List[SubscriptionsResponse]`](../../doc/models/subscriptions-response.md) | Optional | - |
| `statements_entity` | [`List[StatementsResponse]`](../../doc/models/statements-response.md) | Optional | - |
| `statements_forentity` | [`List[StatementsResponse]`](../../doc/models/statements-response.md) | Optional | - |
| `safer_payments` | [`List[SaferPaymentsResponse]`](../../doc/models/safer-payments-response.md) | Optional | - |
| `vendor` | [`List[VendorsResponse]`](../../doc/models/vendors-response.md) | Optional | - |
| `merchant` | [`MerchantsResponse`](../../doc/models/merchants-response.md) | Optional | - |

## Example (as JSON)

```json
{
  "public": 0,
  "currency": "USD",
  "inactive": 0,
  "frozen": 0,
  "id": "id0",
  "created": "created0",
  "modified": "modified2",
  "creator": "String9",
  "modifier": "modifier6"
}
```

