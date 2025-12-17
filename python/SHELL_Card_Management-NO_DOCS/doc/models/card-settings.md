
# Card Settings

## Structure

`CardSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `self_selected_encrypted_pin` | `str` | Optional | The encrypted value of self-selected PIN.<br /><br>Optional – When not provided, the PIN will be auto generated(if the card token type supports PIN) and delivered based on the given PIN delivery option.<br /><br>Max Length: 256<br><br>**Constraints**: *Maximum Length*: `256` |
| `self_selected_pin_key_id` | `str` | Optional | KeyId of the PIN encrypted value.<br /><br>Mandatory, if opted for self-selected PIN else optional.<br /><br>Max Length: 30<br><br>**Constraints**: *Maximum Length*: `30` |
| `self_selected_pin_session_key` | `str` | Optional | Encoded message of the TCS form which is used for encrypting the PIN of this card.<br /><br>The encode message forms are provided to clients by another API (“TCS”).<br /><br>Instructions to encrypt the PIN is covered in the related API specifications document.<br /><br>Mandatory –If opted for self-selected PIN else optional.<br>Max Length: 1024<br><br>**Constraints**: *Maximum Length*: `1024` |
| `validate_fleet_id` | `bool` | Optional | True/False.<br /><br>Optional <br /><br>Default: False<br /><br>For cards ordered with Validate Fleet Id parameter set to true, CFGW will be notified to enable this validation for the card.<br /><br>Note: When “FleetIdInputRequired” is not set on the card, validate fleet id will be considered false regardless of the value passed on this parameter. |
| `card_group_id` | `int` | Optional | Existing Card Group ID, under which the replacement card is to be created.<br /><br>Pass “-1” if the replacement card should not be assigned to any card group.<br /><br>Optional <br /><br>If not provided, the replacement card will be created under the same card group as the current card. |
| `card_delivery_type` | `int` | Required | Card delivery type.<br /><br>Mandatory <br /><br>Allowed Value: <br /><br><br>1. Customer Address(Default) <br /><br>2. New Delivery Address <br /><br>3. Old Card Address |
| `delivery_contact_title` | `str` | Optional | Title of the contact person. <br /><br>Optional<br /><br>Max field length: 10<br><br>**Constraints**: *Maximum Length*: `10` |
| `delivery_contact_name` | `str` | Optional | Name of the contact person <br /><br>Mandatory - If CardDeliveryType  is 2 and OrderCardReplacement is passed as true.<br /><br>Max field length: 50<br><br>**Constraints**: *Maximum Length*: `50` |
| `delivery_company_name` | `str` | Optional | Company name <br /><br>Mandatory - If CardDeliveryType  is 2 and OrderCardReplacement is passed as true.<br>Max field length: 50<br><br>**Constraints**: *Maximum Length*: `50` |
| `delivery_address_line_1` | `str` | Optional | Address line 1 <br /><br>Mandatory - If CardDeliveryType  is 2 and OrderCardReplacement is passed as true.<br /><br>Max field length: 40<br><br>**Constraints**: *Maximum Length*: `40` |
| `delivery_address_line_2` | `str` | Optional | Address line 2 <br /><br>Optional <br /><br>Max field length: 40<br><br>**Constraints**: *Maximum Length*: `40` |
| `delivery_address_line_3` | `str` | Optional | Address line 3 <br /><br>Optional<br /><br>Max field length: 40<br><br>**Constraints**: *Maximum Length*: `40` |
| `delivery_zip_code` | `str` | Optional | ZIP code <br /><br>Mandatory - If CardDeliveryType  is 2 and OrderCardReplacement is passed as true.<br /><br>Max field length: 10<br><br>**Constraints**: *Maximum Length*: `10` |
| `delivery_city` | `str` | Optional | City  <br /><br>Mandatory - If CardDeliveryType  is 2 and OrderCardReplacement is passed as true.<br /><br>Max field length: 40<br><br>**Constraints**: *Maximum Length*: `40` |
| `delivery_region_id` | `int` | Optional | Region Id  <br /><br>Optional |
| `delivery_region` | `str` | Optional | Region  <br /><br>Optional<br /><br>When region is passed |
| `delivery_country` | `str` | Optional | The ISO code of the country.<br /><br>Mandatory - If CardDeliveryType  is 2 and OrderCardReplacement is passed as true |
| `delivery_country_id` | `int` | Optional | The countryId of gicen country.<br /> |
| `phone_number` | `str` | Optional | Phone number for to send SMS. <br /><br>Optional<br /><br>Max field length: 20<br><br>**Constraints**: *Maximum Length*: `16` |
| `email_address` | `str` | Optional | Email address for to send email.<br /><br>Mandatory if PINAdviceType is email else optional.<br /><br>Max field length: 90<br><br>**Constraints**: *Maximum Length*: `90` |
| `pin_delivery_address_type` | `int` | Optional | PIN delivery address type selection.<br /><br>Optional<br /><br>Allowed Values:<br /><br><br>1. Customer Address(Default)<br /><br>2. Card Address<br /><br>3. New Delivery Address |
| `pin_advice_type` | `int` | Optional | PIN delivery method.<br /><br>Mandatory when OrderReplacement Is true.<br /><br>Allowed Values:<br /><br><br>1. Paper<br /><br>2. Email<br /><br>3. SMS<br /><br>4. None |
| `pin_delivery_contact_title` | `str` | Optional | Title of the contact person.<br /><br>Optional <br /><br>Max field length: 10<br><br>**Constraints**: *Maximum Length*: `10` |
| `pin_delivery_contact_name` | `str` | Optional | Name of the contact person.<br /><br>Mandatory - If PINAdviceType is paper else optional.<br /><br>Max field length: 50<br><br>**Constraints**: *Maximum Length*: `50` |
| `pin_delivery_company_name` | `str` | Optional | Company name.<br /><br>Mandatory - If PINAdviceType is paper else optional.<br /><br>Max field length: 50<br><br>**Constraints**: *Maximum Length*: `50` |
| `pin_delivery_address_line_1` | `str` | Optional | Address line 1.<br /><br>Mandatory - If PINAdviceType is paper else optional.<br /><br>Max field length: 40<br><br>**Constraints**: *Maximum Length*: `40` |
| `pin_delivery_address_line_2` | `str` | Optional | Address line 2.<br /><br>Optional <br /><br>Max field length: 40<br><br>**Constraints**: *Maximum Length*: `40` |
| `pin_delivery_address_line_3` | `str` | Optional | Address line 3.<br /><br>Optional <br /><br>Max field length: 40<br><br>**Constraints**: *Maximum Length*: `40` |
| `pin_delivery_zip_code` | `str` | Optional | ZIP code.<br /><br>Mandatory - if PINAdviceType is paper else optional. <br /><br>Max field length: 10<br><br>**Constraints**: *Maximum Length*: `10` |
| `pin_delivery_city` | `str` | Optional | City.<br /><br>Mandatory - If PINAdviceType is paper else optional. <br /><br>Max field length: 40<br><br>**Constraints**: *Maximum Length*: `40` |
| `pin_delivery_region_id` | `int` | Optional | Region Id.<br /><br>Optional |
| `pin_delivery_region` | `str` | Optional | Region.<br /><br>When region is passed |
| `pin_delivery_country` | `str` | Optional | The ISO code of the country.<br /><br>Mappings for ISO code <br /><br>Mandatory if PINAdviceType is paper else optional. |
| `pin_delivery_country_id` | `int` | Optional | The countryId of the country.<br /><br>Mappings for ISO code<br /><br>This is not an input parameter. |
| `pin_phone_number` | `str` | Optional | Phone number for to send SMS of the PIN in case PINAdviceType is SMS.<br /><br>Mandatory if PINAdviceType is SMS else optional.<br /><br>Max field length: 20<br><br>**Constraints**: *Maximum Length*: `16` |
| `pin_email_address` | `str` | Optional | Email address for to send email of the PIN in case PINAdviceType is Email.<br /><br>Mandatory if PINAdviceType is email else optional.<br /><br>Max field length: 90<br><br>**Constraints**: *Maximum Length*: `90` |
| `save_for_pin_reminder` | `bool` | Optional | The given address will be used for sending PIN reminders in future when requested.<br /><br>PIN Advice type should be Paper<br>Optional |
| `save_for_card_reissue` | `bool` | Optional | If this is specified, the contact address will be saved in cards platform for card reissue processing.<br /><br>Optional |
| `expiry_date` | `str` | Optional | Expiry Date for newly created card to be update in cards plot form.<br /><br>Optional <br /><br>Format: MMyy <br /><br>Eg:1221 <br /><br>If not apply the default Expiry Date.<br /><br>Note:<br /><br>There is a limit to the ExpiryDate which the user can choose for the Card.<br>If the user chooses a later ExpiryDate than the allowed value for the CardType of the OU,<br>the background service logs the respective error code and description<br><br>**Constraints**: *Maximum Length*: `4` |

## Example (as JSON)

```json
{
  "SelfSelectedEncryptedPIN": "SelfSelectedEncryptedPIN8",
  "SelfSelectedPINKeyID": "SelfSelectedPINKeyID2",
  "SelfSelectedPINSessionKey": "SelfSelectedPINSessionKey4",
  "ValidateFleetId": false,
  "CardGroupId": 118,
  "CardDeliveryType": 2
}
```

