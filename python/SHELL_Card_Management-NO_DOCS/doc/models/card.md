
# Card

## Structure

`Card`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `int` | Optional | Account ID |
| `account_name` | `str` | Optional | Account Name |
| `account_number` | `str` | Optional | Account Number |
| `account_short_name` | `str` | Optional | Account Short Name |
| `bundle_id` | `str` | Optional | Bundle Id associated with card in the Gateway.<br /><br><br>This field will have null value if the card is not associated with any bundle in Gateway or the value of IncludeBundleDetails in request is false. |
| `card_block_schedules` | [`List[CardBlockSchedule]`](../../doc/models/card-block-schedule.md) | Optional | List of Scheduled Card Blocks details<br /><br>Entity: CardBlockSchedule |
| `card_group_id` | `int` | Optional | Card group ID |
| `card_group_name` | `str` | Optional | Card group name |
| `card_id` | `int` | Optional | Unique Card Id |
| `card_type_code` | `str` | Optional | ISO code of the card i.e. first 7 digits of the PAN |
| `card_type_id` | `int` | Optional | Card Type ID Example Id and Description: 1 -Philippines CRT 7077861 2-Philippines<br /><br>Fleet 7002861 5-SHELL FLEET-HONG KONG 7002821 6-SHELL NHF- HONG KONG 7002821 7-SHELL CRT- HONG KONG 7077821 |
| `card_type_name` | `str` | Optional | Card Type Name Example Id and Description: 1-Philippines CRT 7077861 2-Philippines <br /><br>Fleet 7002861 5-SHELL FLEET- HONG KONG 7002821 6-SHELL NHF- HONG KONG 7002821 7-SHELL  CRT- HONG KONG 7077821 |
| `col_co_country_code` | `str` | Optional | The 2 character ISO Code for the customer and card owning country. <br /><br>If default card type is not set then the first two alphabets of the account ID is returned. |
| `creation_date` | `str` | Optional | Card Creation datetime.<br /><br>Format: yyyyMMdd HH:mm:ss<br /><br>Note: Clients to convert this to appropriate DateTime type. |
| `driver_name` | `str` | Optional | Driver name |
| `effective_date` | `str` | Optional | Effective date for the Card<br /><br>Format: yyyyMMdd<br /><br>Note: Clients to convert this to appropriate DateTime type. |
| `expiry_date` | `str` | Optional | Expiry date of the card.<br /><br>Format: yyyyMMdd<br /><br>Note: Clients to convert this to appropriate DateTime type. |
| `fleet_id_input` | `bool` | Optional | True/False True if fleet id input is enabled, else false |
| `is_crt` | `bool` | Optional | True/False True if it is a CRT type card, else false |
| `is_fleet` | `bool` | Optional | True/False True if it is a Fleet type card, else false |
| `is_international` | `bool` | Optional | True/False True if it is an international card, else false |
| `is_national` | `bool` | Optional | True/False True if it is a national card, else false |
| `is_partner_sites_included` | `bool` | Optional | True/False True if it is allowed at all partner sites, else false |
| `is_shell_sites_only` | `bool` | Optional | True/False True if it is only allowed at Shell sites, else false |
| `issue_date` | `str` | Optional | Issue date<br /><br>Format: yyyyMMdd<br /><br>Note: Clients to convert this to appropriate DateTime type. |
| `is_superseded` | `bool` | Optional | True/False True if a new card is issued with the same PAN, else false. |
| `is_virtual_card` | `bool` | Optional | True/False True if it is a virtual card, else false |
| `last_modified_date` | `str` | Optional | Card last modified date and time<br /><br>Format: yyyyMMdd HH:mm:ss<br /><br>Note: Clients to convert this to appropriate DateTime type. |
| `last_used_date` | `str` | Optional | Card last used date .<br /><br>Note: last used date of a card will be calculated based on billed/unbilled sales items<br><br>      of a given card.The query that extracts the last used dates will be applied on the<br>    <br>      subset of the cards being returned to the client.Unbilled sales items is checked<br>    <br>      first and for those not found in the unbilled table, sales items will be checked<br>    <br>      (only when the last used date is not found in unbilled table for at least a single<br>    <br>      card from the result). The transactions in last 48 hours are not expected to be<br><br>Therefore this field gives the correct information up to 48 hours early.<br /><br>Format: yyyyMMdd HH:mm:ss<br /><br>Note: Clients to convert this to appropriate DateTime type |
| `local_currency_code` | `str` | Optional | ISO code of the local currency. <br /> |
| `local_currency_symbol` | `str` | Optional | Local currency symbol. <br /> |
| `odometer_input` | `bool` | Optional | True/False True if odometer input is enabled on the card, else false |
| `pan` | `str` | Optional | Card PAN Mask PAN (Mask all digits except the Last 6 digits of the PAN) |
| `purchase_category_code` | `str` | Optional | Purchase category code |
| `purchase_category_id` | `int` | Optional | Purchase category Id <br /><br>Note: Not Purchase code. |
| `purchase_category_name` | `str` | Optional | Purchase category name |
| `reason` | `str` | Optional | Card Status reason Example: Lost Stolen Card no longer required |
| `reissue_setting` | `str` | Optional | Reissue setting of the card. If the card is superseded (i.e. a replacement/new card is issued) then reissue setting of the latest card issued. <br /><br>Values<br /><br>•True –Card will be Reissued when nearing its expiry date <br /><br>•False –Card will not be Reissued |
| `status_description` | `str` | Optional | Status Description (Active, Temporarily Blocked, etc.,)<br /><br>Possible Ids and description: 1 Active 7 Blocked Card 8 Expired 9 Cancelled 10 New 23 Pending Renewal 31 Replaced 41<br /><br>Temporary Block(Customer) 42 Temporary Block(Shell) 43 Fraud 101 Active(Block in progress)<br /><br><br>* 102 Blocked Card(Unblock in progress) <br /><br>* 103 Active(Cancel in progress) <br /><br>* 104 Active(Marked as damaged)<br /><br>* 105 New(Cancel in progress) <br /><br>* 106 { Status}(Scheduled for block)<br /><br>* 107 { Status}(Scheduled for unblock) <br /><br>  *# Note: Items marked with* are intermediate statuses  to indicate that there are pending requests in progress.<br /><br>  The response can contain these intermediate statuses only if the<br /><br>  IncludeIntermediateStatus flag is true. The placeholder { Status} in the items<br /><br>  marked with # will be replaced with the  status description. E.g., Active (Scheduled for block) |
| `status_id` | `int` | Optional | Card Status id Possible Ids and description: 1 Active 7 Blocked Card 8 Expired 9 Cancelled 10 New 23 Pending Renewal 31 Replaced 41 Temporary Block(Customer) 42 <br /><br>Temporary Block(Shell) 43 Fraud 101 Active(Block in progress) <br /><br><br>* 102 Blocked Card(Unblock in progress)<br /><br>* 103 Active(Cancel in progress) <br /><br>* 104 Active(Marked as damaged) <br /><br>* 105 New(Cancel in progress)<br /><br>* 106 { Status}(Scheduled for block) <br /><br><br># 107 {Status}(Scheduled for unblock)<br /><br><br>*# Note: Items marked with* are intermediate statuses to indicate that there are pending requests in progress.<br /><br>The response can contain these intermediate statuses only if the IncludeIntermediateStatus flag is true.<br /><br>The placeholder { Status} in the items marked with # will be replaced with<br /><br>the status description. E.g., Active (Scheduled for block) |
| `token_type_id` | `int` | Optional | Token Type ID configured for the Card E.g. 107 |
| `token_type_name` | `str` | Optional | Token Type Name configured for the Card |
| `vrn` | `str` | Optional | Vehicle registration number |
| `client_reference_id` | `str` | Optional | Customer reference number of the card. |
| `is_emv_contact` | `bool` | Optional | Is Europay, MasterCard, and Visa Contact enabled or not. |
| `is_emv_contactless` | `bool` | Optional | Is Europay, MasterCard, and Visa Contactless enabled or not. |
| `is_rfid` | `bool` | Optional | Whether the card type is enabled for RFID (Radio Frequency Identification) |
| `rfiduid` | `str` | Optional | RFIDUID |
| `emaid` | `str` | Optional | EMAID |
| `ev_printed_number` | `str` | Optional | EV Printed Number |
| `card_media_code` | `str` | Optional | Card Media Code. |

## Example (as JSON)

```json
{
  "AccountId": 140,
  "AccountName": "AccountName0",
  "AccountNumber": "AccountNumber4",
  "AccountShortName": "AccountShortName6",
  "BundleId": "BundleId2"
}
```

