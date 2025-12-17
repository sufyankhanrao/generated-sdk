
# Merchants Response

## Structure

`MerchantsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `last_activity` | `str` | Optional | The date and time on which this Merchant last processed a Transaction. The format should be YYYY-MM-DD HH:MM:SS.<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}` |
| `total_approved_sales` | `int` | Optional | Show the total approved amount to this merchant. |
| `entity` | str \| [entitiesResponse1](../../doc/models/entities-response-1.md) \| None | Optional | This is a container for any-of cases. |
| `dba` | `str` | Optional | The name under which the Merchant is doing business, if applicable. This field is stored as a text string and must be between 0 and 50 characters long. |
| `new` | [`NewEnum`](../../doc/models/new-enum.md) | Optional | An indicator that specifies whether the Merchant is new to credit card processing, where merchants are considered to be new by default and can have a valid value of either '0' (Not new) or '1' (New).<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not new**<br>- `1` - **New**<br></details><br> |
| `incremental_auth_supported` | [`IncrementalAuthSupportedEnum`](../../doc/models/incremental-auth-supported-enum.md) | Optional | This field allows the ability to submit merchant registration files with a MasterCard (MC) Auth Integrity value.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Incremental Auth Not Supported**<br>- `1` - **Incremental Auth Supported**<br></details><br> |
| `seasonal` | [`SeasonalEnum`](../../doc/models/seasonal-enum.md) | Optional | Indicates if the merchant is a seasonal merchant or operates year-round.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Year-Round Merchant**<br>- `1` - **Seasonal Merchant**<br></details><br> |
| `advanced_billing` | [`AdvancedBillingEnum`](../../doc/models/advanced-billing-enum.md) | Optional | Indicates whether the merchant accepts pre-purchase for products that are shipped at a later date or not currently available, specifying advanced billing as either disabled (0) or enabled (1).<br><br><details><br><summary>Valid Values</summary><br>- `0` - **AdvancedBilling is disabled.**<br>- `1` - **AdvancedBilling is enabled.**<br></details><br> |
| `established` | `int` | Optional | The date on which the Merchant was established. The date is specified as an eight digit string in YYYYMMDD format, for example, '20160120' for January 20, 2016.<br><br>**Note:** Include the `established` date value to ensure successful underwriting and new Merchant onboarding to the VCore platform. |
| `annual_cc_sales` | `int` | Optional | The value of the annual credit card sales of this Merchant.<br>This field is specified as an integer in cents. For example, $25.30 is expressed as '2530'. |
| `annual_cc_sale_volume` | `int` | Optional | The value of the annual credit card sale volume of this Merchant.<br>This field is specified as an integer in cents. For example, $25.30 is expressed as '2530'. |
| `annual_ach_sale_volume` | `int` | Optional | The value of the annual direct deposit sale volume of this Merchant.<br>This field is specified as an integer in cents. For example, $25.30 is expressed as '2530'. |
| `amex_volume` | `int` | Optional | Indicates the Annual AMEX Sales Volume for the outlet. |
| `avg_ticket` | `int` | Optional | The value of the average credit card sales of this Merchant.<br>This field is specified as an integer in cents. For example, $25.30 is expressed as '2530'. |
| `amex` | `str` | Optional | The American Express merchant identifier for this Merchant, if applicable.<br>This field is stored as a text string and must be between 1 and 15 characters long. |
| `discover` | `str` | Optional | The Discover merchant identifier for this Merchant, if applicable.<br>This field is stored as a text string and must be between 1 and 15 characters long. |
| `mcc` | `str` | Optional | The Merchant Category Code (MCC) for this Merchant. This code is not required to create a Merchant, but it is required to successfully board a Merchant. |
| `visa_mvv` | `str` | Optional | Merchant Verification Value. A value assigned by Visa to identify participation in select merchant programs. |
| `visa_disclosure` | [`VisaDisclosureEnum`](../../doc/models/visa-disclosure-enum.md) | Optional | Whether or not the merchant has acknowledged and accepted the Visa Disclosure.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Accepted**<br>- `1` - **Accepted**<br></details><br> |
| `disclosure_ip` | `str` | Optional | The IP address where the Merchant platform disclosure is hosted. |
| `disclosure_date` | `int` | Optional | The date the Merchant platform disclosure is reviewed by the Merchant. |
| `environment` | [`MerchantEnvironmentEnum`](../../doc/models/merchant-environment-enum.md) | Optional | The environment which the Merchant is in, if applicable.<br><br><details><br><summary>Valid Values</summary><br>- `supermarket` - **Supermarkets / Grocery**<br>- `moto` - **Mail Order / Telephone Order**<br>- `cardPresent` - **Card Present Environment**<br>- `fuel` - **Fuel / Gas Stations**<br>- `serviceStation` - **Service Stations**<br>- `restaurant` - **Restaurants**<br>- `ecommerce` - **eCommerce / Online Sales**<br></details><br> |
| `status` | [`MerchantStatusEnum`](../../doc/models/merchant-status-enum.md) | Optional | The status of the Merchant.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not ready**. Occurs when a new Merchant is created. Unable to process payments.<br>- `1` - **Ready**. New Merchant submitted for underwriting approval after submitting a signup form.<br>- `2` - **Boarded**. Merchant has been approved and boarded to the platform. Payment processing now available.<br>- `3` - **Manual**. Set internally by platform underwriting. New Merchant is pending manual verification.<br>- `4` - **Closed**. Set internally by platform underwriting. New Merchant was declined and cannot access the platform.<br>- `5` - **Incomplete**. Set by user boarding the merchant. Can be manually set to "save" an incomplete Merchant boarding request for a later time.<br>- `6` - **Pending**. New Merchant was submitted for boarding, platform access pending review.<br></details><br>**Default**: `0`<br> |
| `auto_boarded` | [`AutoBoardedEnum`](../../doc/models/auto-boarded-enum.md) | Optional | Whether the merchant auto-boarded.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Auto-Boarded**<br>- `1` - **Auto-Boarded**<br></details><br> |
| `status_reason` | `str` | Optional | The reason for manual or closed status. |
| `account_closure_reason_code` | `str` | Optional | The denial or account closure reason code. |
| `account_closure_reason_date` | `int` | Optional | The date the account closure reason code was provided. It should be in YYYYMMDD format |
| `risk_level` | [`RiskLevelEnum`](../../doc/models/risk-level-enum.md) | Optional | The risk level which the Merchant is in, if applicable.<br><br><details><br><summary>Valid Values</summary><br>- `restricted` - **Restricted from processing transactions.**<br>- `prohibited` - **Prohibited business use category.**<br>- `high` - **High merchant risk score.**<br>- `medium` - **Medium merchant risk score.**<br>- `low` - **Low merchant risk score.**<br></details><br> |
| `credit_ratio` | `int` | Optional | The credit ratio to use while calculating risk factors for credit, if applicable. |
| `credit_timeliness` | `int` | Optional | The credit timeliness for the Merchant, if applicable. |
| `chargeback_ratio` | `int` | Optional | Chargeback Ratio. |
| `ndx_days` | `int` | Optional | The ndx (Non Delivery Exposure) days which the Merchant is in, if applicable. |
| `ndx_percentage` | `int` | Optional | The ndx (Non Delivery Exposure) percentage to be used for the merchant, if applicable. |
| `boarded` | `int` | Optional | The date and time on which this Merchant was successfully boarded. |
| `saq_type` | [`SaqTypeEnum`](../../doc/models/saq-type-enum.md) | Optional | Payment Card Industry Data Security Standard (PCI DSS) Self-assessment questionnaire (SAQ). Details about a merchant's business and the way they currently accept payments or plan to in the future.<br><br><details><br><summary>Valid Values</summary><br>- `SAQ-A` - **Card-not-present merchants (e-commerce or mail/telephone-order) with PCI DSS-validated third-party payments service provider(s) and does not store cardholder data.**<br>- `SAQ-A-EP` - **E-commerce merchants with PCI DSS-validated third-party payments service provider(s) with a website that doesn't directly collect cardholder data, but may impact it in some way, and does not store cardholder data.**<br>- `SAQ-B` - **Merchants with imprint machines or standalone, dial-out terminals that do not store cardholder data.**<br>- `SAQ-B-IP` - **Merchants with standalone, PTS-approved payment terminals that have an IP connection to the payment processor, but do not store cardholder data.**<br>- `SAQ-C-VT` - **Merchants that enter single transactions manually into an internet-based terminal hosted by PCI DSS-validated third-party payments service provider(s) and does not store cardholder data.**<br>- `SAQ-C` - **Merchants with payment application systems connected to the internet that do not store cardholder data.**<br>- `SAQ-P2PE-HW` - **Merchants with hardware-only payment terminals managed by a PCI SSC-listed P2PE solution, and does not store cardholder data.**<br>- `SAQ-D` - **Generic field for all Merchants that do not fall under the requirements for any above SAQ types.**<br></details><br> |
| `saq_date` | `int` | Optional | The date of the PCI SAQ assessment. The format should be YYYYMMDD. |
| `qsa` | `str` | Optional | Qualified Security Assessor (QSA) companies are independent security organizations that have been qualified by the PCI Security Standards Council to validate an entity's adherence to PCI DSS. This is a free-text field for inputting the QSA's business name.<br>The name of the Qualified Security Assessor (QSA) used by the Merchant to assess, verify and prove their PCI DSS compliance. |
| `letter_status` | [`LetterStatusEnum`](../../doc/models/letter-status-enum.md) | Optional | Indicates whether the letter status is ON or OFF.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **OFF**<br>- `1` - **ON**<br></details><br> |
| `letter_date` | `int` | Optional | The date associated with the letter status. The format should be YYYYMMDD. |
| `tc_attestation` | [`TcAttestationEnum`](../../doc/models/tc-attestation-enum.md) | Optional | Whether or not the merchant has acknowledged and accepted the Terms and Conditions.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Accepted**<br>- `1` - **Accepted**<br></details><br> |
| `tmx_session_id` | `str` | Optional | Transaction Session Id. |
| `chargeback_notification_email` | `str` | Optional | Notification Email for chargebacks. |
| `location_type` | [`MerchantLocationTypeEnum`](../../doc/models/merchant-location-type-enum.md) | Optional | Description of the type of address that the business operates at.<br><br><details><br><summary>Valid Values</summary><br>- `77` - **Retail Storefront**<br>- `78` - **Warehouse**<br>- `79` - **Private Residence**<br>- `80` - **Others**<br>- `81` - **P. RES-PROF/Construction**<br></details><br> |
| `percent_keyed` | `int` | Optional | The merchant percentage of transactions that are Card Not Present (Includes MOTO and eCommerce). |
| `total_volume` | `int` | Optional | The expected total volume for all credit card and ACH payments that the merchant will process for the current year. |
| `percent_ecomm` | `int` | Optional | This field indicates what percentage are internet originated transactions. |
| `percent_business` | `int` | Optional | This field indicates what percentage of the transactions are Business to Business. |
| `apple_pay_active` | [`ApplePayActiveEnum`](../../doc/models/apple-pay-active-enum.md) | Optional | This field indicates if Apple Pay is active for this merchant.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Inactive**<br>- `1` - **Active**<br></details><br> |
| `apple_pay_status` | `str` | Optional | The status of Apple Pay for this merchant. |
| `google_pay_active` | [`GooglePayActiveEnum`](../../doc/models/google-pay-active-enum.md) | Optional | This field indicates if Google Pay is active for this merchant.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Inactive**<br>- `1` - **Active**<br></details><br> |
| `naics` | [`NaicsEnum`](../../doc/models/naics-enum.md) | Optional | The NAICS sector code that accurately describes the industry the business operates in.<br><br>For more information, see the [NAICS Manual provided by the US Census Bureau's North American Industry Classification System.](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf)<br><br><details><br><summary>Valid Values</summary><br>- `11` - **Agriculture, Forestry, Fishing and Hunting**<br>- `21` - **Mining, Quarrying, and Oil and Gas Extraction**<br>- `22` - **Utilities**<br>- `23` - **Construction**<br>- `31` / `33` - **Manufacturing**<br>- `41` - **Wholesale Trade**<br>- `44` / `45` - **Retail Trade**<br>- `48` / `49` - **Transportation and Warehousing**<br>- `51` - **Information**<br>- `52` - **Finance and Insurance**<br>- `53` - **Real Estate and Property Rental / Leasing**<br>- `54` - **Professional, Scientific, and Technical Services**<br>- `55` - **Management of Companies and Enterprises**<br>- `56` - **Administrative and Support and Waste Management and Remediation Services**<br>- `61` - **Educational Services**<br>- `62` - **Health Care and Social Assistance**<br>- `71` - **Arts, Entertainment, and Recreation**<br>- `72` - **Accommodation and Food Services**<br>- `81` - **Other Services (except Public Administration)**<br>- `91` / `92` - **Public Administration**<br></details><br> |
| `naics_description` | `str` | Optional | The NAICS sector description matching the above NAICS sector code. If "Other", industry description is prefixed with "Other: ". |
| `express_batch_close_method` | [`ExpressBatchCloseMethodEnum`](../../doc/models/express-batch-close-method-enum.md) | Optional | This field indicates the batch close method for this merchant applicable to Express platform.<br><br><details><br><summary>Valid Values</summary><br>- `TimeInitiated` - **Batch close occurs at specific time intervals (Automated).**<br>- `MerchantInitiated` - **Batch close occurs when initiated by the Merchant (Manual).**<br></details><br> |
| `express_batch_close_time` | `str` | Optional | This field indicates the batch close time for this merchant applicable to Express platform. |
| `pass_token_enabled` | [`PassTokenEnabledEnum`](../../doc/models/pass-token-enabled-enum.md) | Optional | This field indicates if Pass Token is enabled for this merchant.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Disabled**<br>- `1` - **Enabled**<br></details><br> |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |
| `assessments` | [`List[AssessmentsResponse]`](../../doc/models/assessments-response.md) | Optional | - |
| `apple_domains` | [`List[AppleDomainsResponse]`](../../doc/models/apple-domains-response.md) | Optional | - |
| `batches` | [`List[BatchesResponse]`](../../doc/models/batches-response.md) | Optional | - |
| `chargebacks` | [`List[ChargebacksResponse]`](../../doc/models/chargebacks-response.md) | Optional | - |
| `customers` | [`List[CustomersResponse]`](../../doc/models/customers-response.md) | Optional | - |
| `invoices` | [`List[InvoicesResponse]`](../../doc/models/invoices-response.md) | Optional | - |
| `members` | [`List[MembersResponse]`](../../doc/models/members-response.md) | Optional | - |
| `merchant_platform_statuses` | [`List[MerchantPlatformStatusesResponse]`](../../doc/models/merchant-platform-statuses-response.md) | Optional | - |
| `merchant_results` | [`List[MerchantResultsResponse]`](../../doc/models/merchant-results-response.md) | Optional | - |
| `plans` | [`List[PlansResponse]`](../../doc/models/plans-response.md) | Optional | - |
| `terminals` | [`List[TerminalsResponse]`](../../doc/models/terminals-response.md) | Optional | - |
| `terminal_txns` | [`List[TerminalTxnsResponse]`](../../doc/models/terminal-txns-response.md) | Optional | - |
| `txns` | [`List[TxnsResponse]`](../../doc/models/txns-response.md) | Optional | - |

## Example (as JSON)

```json
{
  "status": 0,
  "inactive": 0,
  "frozen": 0,
  "id": "id8",
  "created": "created8",
  "modified": "modified6",
  "creator": "String7",
  "modifier": "modifier2"
}
```

