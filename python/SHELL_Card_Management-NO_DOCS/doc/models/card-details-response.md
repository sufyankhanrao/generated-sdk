
# Card Details Response

## Structure

`CardDetailsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payer_id` | `int` | Optional | Payer Id (i.e. Customer Id of the Payment Customer in the Shell Card Platform) of the selected payer. |
| `payer_number` | `str` | Optional | Payer Number of the selected payer. |
| `account_id` | `int` | Optional | Account Id (i.e. Customer Id of the Customer in the Shell Card Platform) of the customer. |
| `account_number` | `str` | Optional | Account Number of the customer. |
| `account_short_name` | `str` | Optional | Account short name. |
| `col_co_country_code` | `str` | Optional | ISO 3166 Alpha-2 Country Code for the customer and card owning country. |
| `local_currency_code` | `str` | Optional | ISO 4217 Curreny Code of the local currency. |
| `local_currency_symbol` | `str` | Optional | Currency symbol of local currency. |
| `card_id` | `int` | Optional | Unique Card Id in Cards platform. |
| `pan` | `str` | Optional | Card PAN. In the response body the PAN will be masked if the option is enabled in the Shell Card Platform. |
| `status_id` | [`CardDetailsResponseStatusIdEnum`](../../doc/models/card-details-response-status-id-enum.md) | Optional | - |
| `status` | `str` | Optional | Possible Id’s and description:<br><br>* 1  Active<br>* 7  Blocked Card<br>* 8  Expired<br>* 9  Cancelled<br>* 10  New<br>* 23  Pending Renewal<br>* 31  Replaced<br>* 41  Temporary Block (Customer)<br>* 42  Temporary Block (Shell)<br>* 43  Fraud<br>* 101 Active (Block in progress) *<br>* 102 Blocked Card (Unblock in progress) *<br>* 103 Active (Cancel in progress) *<br>* 104 Active (Marked as damaged) *<br>* 105 New (Cancel as damaged) *<br>* 106 Active(Scheduled for block) ”#<br>* 107 Blocked Card(Scheduled for unblock) *#<br>* 108 Blocked Card (Cancel in progress) *<br><br>> Note:<br>> •  Items marked with * are intermediate statuses  to indicate that there are pending requests in progress. , The response can contain these intermediate statuses only if the IncludeIntermediateStatus flag is true.<br>> •  The placeholder “<Shell Card Platform Status>” in the items marked with # will be replaced with the Shell Card Platform status description. E.g., “Active (Scheduled for block)” |
| `odometer_prompt` | `bool` | Optional | True if odometer input is enabled on the card, else false |
| `fleet_id_prompt` | `bool` | Optional | True if fleet id input is enabled, else false |
| `pin_type` | [`CardDetailsResponsePINTypeEnum`](../../doc/models/card-details-response-pin-type-enum.md) | Optional | - |
| `has_pin` | `bool` | Optional | True if card has PIN, else false |
| `is_self_selected_pin` | `bool` | Optional | True if card has Self Selected PIN, else false |
| `temporary_block_allowed` | `bool` | Optional | True if card can be blocked temporarily, else false |
| `unblock_allowed` | `bool` | Optional | True/False True if card can be Unblocked, else false |
| `permanent_block_allowed` | `bool` | Optional | True if card can be blocked permanently, else false |
| `issue_number` | `int` | Optional | Issue number of the card |
| `reissue_setting` | `Any` | Optional | - |
| `international_pos_language_id` | [`CardDetailsResponseInternationalPOSLanguageIDEnum`](../../doc/models/card-details-response-international-pos-language-id-enum.md) | Optional | - |
| `international_pos_language_code` | [`CardDetailsResponseInternationalPOSLanguageCodeEnum`](../../doc/models/card-details-response-international-pos-language-code-enum.md) | Optional | - |
| `local_pos_language_id` | [`CardDetailsResponseInternationalPOSLanguageIDEnum`](../../doc/models/card-details-response-international-pos-language-id-enum.md) | Optional | - |
| `local_pos_language_code` | [`CardDetailsResponseInternationalPOSLanguageCodeEnum`](../../doc/models/card-details-response-international-pos-language-code-enum.md) | Optional | - |
| `card_type_code` | `str` | Optional | ISO code of the card i.e. first 7 digits of the PAN. |
| `card_type_id` | `int` | Optional | Card Type ID |
| `card_type_name` | `str` | Optional | Card Type Name |
| `token_type_id` | `int` | Optional | Token Type ID configured for the Card |
| `token_type_name` | `str` | Optional | Token Type Name configured for the Card |
| `is_chip_card` | `bool` | Optional | True if a chip card, else false |
| `is_mag_strip_card` | `bool` | Optional | True if it is a magnetic stripe card, else false |
| `is_virtual_card` | `bool` | Optional | True if it is a virtual card, else false |
| `purchase_category_code` | `str` | Optional | Purchase category code of the card.<br><br>**Constraints**: *Maximum Length*: `1` |
| `purchase_category_id` | `int` | Optional | Purchase category identifier in the Shell Card Platform. |
| `purchase_category_name` | `str` | Optional | Purchase category name |
| `is_crt` | `bool` | Optional | True if it is a Commercial Road Transport (CRT) card, else false |
| `is_fleet` | `bool` | Optional | True if it is a Fleet card, else false |
| `is_international` | `bool` | Optional | True if it is an international card, else false |
| `is_national` | `bool` | Optional | True if it is a national card, else false |
| `is_partner_sites_included` | `bool` | Optional | True if it is allowed at all partner sites, else false |
| `is_shell_sites_only` | `bool` | Optional | True if it is only allowed at Shell sites, else false |
| `fuel_sets` | [`List[CardDetailsResponseFuelSetsItems]`](../../doc/models/card-details-response-fuel-sets-items.md) | Optional | List of active fuel type product restrictions applied on the card.<br><br>**Constraints**: *Unique Items Required* |
| `non_fuel_sets` | [`List[CardDetailsResponseNonFuelSetsItems]`](../../doc/models/card-details-response-non-fuel-sets-items.md) | Optional | List of active non-fuel type product restrictions applied on the card.<br><br>**Constraints**: *Unique Items Required* |
| `issued_date` | `str` | Optional | Card issue date. |
| `expiry_date` | `str` | Optional | Expiry date of the card. |
| `last_used_date` | `str` | Optional | Card last used date. |
| `misuse_date` | `str` | Optional | Last misused date of the card. |
| `temperature` | `str` | Optional | Hot-list status |
| `driver_name` | `str` | Optional | Driver name of the card. Note- While ordering card, optional when VRN is passed else mandatory.<br><br>**Constraints**: *Maximum Length*: `27` |
| `vrn` | `str` | Optional | Vehicle registration number of the card. Note- While ordering card, optional when DriverName is passed else mandatory.<br><br>**Constraints**: *Maximum Length*: `16` |
| `emboss_text` | `str` | Optional | Text printed on the card as account name.<br><br>**Constraints**: *Maximum Length*: `25` |
| `card_group_id` | `int` | Optional | Existing Card Group ID, under which the replacement card is to be created.<br>Pass “-1” if the replacement card should not be assigned to any card group.<br>Optional.<br>If not provided, the replacement card will be created under the same card group as the current card.<br>Example- 156 |
| `card_group_name` | `str` | Optional | Card group name. Note- 1. While ordering card this field is mandatory when IsNewCardGroup is true.<br><br>**Constraints**: *Maximum Length*: `30` |
| `renewal_date` | `str` | Optional | Renewal date of the card. Applicable if ReissueSetting is set to True. |
| `renewed_card_id` | `int` | Optional | Renewed card id. |
| `renewed_card_status_id` | `int` | Optional | Renewed card status id. |
| `renewed_card_status` | `str` | Optional | Renewed card status description. |
| `renewed_card_expiry_date` | `str` | Optional | Renewed card expiry date. |
| `renewed_card_issue_number` | `int` | Optional | Renewed card issue number. |
| `renewed_card_reissue_setting` | [`CardDetailsResponseRenewedCardReissueSettingEnum`](../../doc/models/card-details-response-renewed-card-reissue-setting-enum.md) | Optional | - |
| `creation_date` | `str` | Optional | Card Creation Date time |
| `effective_date` | `str` | Optional | Effective date for the Card |
| `last_modified_date` | `str` | Optional | Card last modified date |
| `bundle_id` | `str` | Optional | Bundle Id associated with card in the Gateway. This field will have a null value if the card is not associated with any bundle in Gateway or the value of IncludeBundleDetails in request is false. |
| `card_delivery_address` | [`CardDeliveryAddress`](../../doc/models/card-delivery-address.md) | Optional | - |
| `pin_delivery_address` | [`PINDeliveryAddress`](../../doc/models/pin-delivery-address.md) | Optional | - |
| `card_block_schedules` | [`List[CardDetailsResponseCardBlockSchedulesItemsAllOf0]`](../../doc/models/card-details-response-card-block-schedules-items-all-of-0.md) | Optional | **Constraints**: *Unique Items Required* |
| `error` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |
| `request_id` | `str` | Optional | API Request |

## Example (as JSON)

```json
{
  "PayerId": 853,
  "PayerNumber": "PH50000843",
  "AccountId": 854,
  "AccountNumber": "PH50000844",
  "AccountShortName": "PARKLEY",
  "ColCoCountryCode": "PH",
  "LocalCurrencyCode": "EUR",
  "LocalCurrencySymbol": "€",
  "CardId": 125,
  "PAN": "7002861007636000020",
  "OdometerPrompt": true,
  "FleetIdPrompt": true,
  "HasPIN": true,
  "IsSelfSelectedPIN": true,
  "TemporaryBlockAllowed": true,
  "UnblockAllowed": true,
  "PermanentBlockAllowed": true,
  "IssueNumber": 1,
  "CardTypeCode": "7077861",
  "CardTypeId": 1,
  "CardTypeName": "Philippines CRT 7077861",
  "TokenTypeId": 107,
  "TokenTypeName": "PH FLE NAT SIN R1",
  "IsChipCard": false,
  "IsMagStripCard": true,
  "IsVirtualCard": true,
  "PurchaseCategoryCode": "6",
  "PurchaseCategoryId": 54,
  "PurchaseCategoryName": "2 - FuelSave and Lubricants",
  "IsCRT": true,
  "IsFleet": true,
  "IsInternational": true,
  "IsNational": true,
  "IsPartnerSitesIncluded": true,
  "IsShellSitesOnly": true,
  "IssuedDate": "20181001",
  "ExpiryDate": "20181031",
  "LastUsedDate": "20181001 13:23:55",
  "MisuseDate": "20181001 13:23:55",
  "Temperature": "10-Warm",
  "DriverName": "ROBERT",
  "VRN": "MV65YLH",
  "EmbossText": "PARKLEY",
  "CardGroupId": 5,
  "CardGroupName": "GROUP1",
  "RenewalDate": "20181001",
  "RenewedCardId": 1325,
  "RenewedCardStatusId": 10,
  "RenewedCardStatus": "New",
  "RenewedCardExpiryDate": "20181031",
  "RenewedCardIssueNumber": 2,
  "CreationDate": "20181001",
  "EffectiveDate": "20181001",
  "LastModifiedDate": "20181001 13:23:55",
  "RequestId": "ed557f02-c7d7-4c01-b3e5-11bf3239c8ed"
}
```

