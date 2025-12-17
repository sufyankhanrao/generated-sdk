
# Add Client Request

## Structure

`AddClientRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_balance` | `float` | Optional | The client’s current [account balance](https://mindbody-online-support.force.com/support/s/article/203262013-Adding-account-payments-video-tutorial?language=en_US). |
| `action` | [`Action1Enum`](../../doc/models/action-1-enum.md) | Optional | The action taken. |
| `active` | `bool` | Optional | When `true`, indicates that the client is active at the site.<br /><br>When `false`, indicates that the client is not active at the site. |
| `address_line_1` | `str` | Optional | The first line of the client’s street address. |
| `address_line_2` | `str` | Optional | The second line of the client’s street address, if needed. |
| `appt_gender_pref_male` | `bool` | Optional | When `true`, indicates that the client prefers services to be provided by a male service provider.<br /><br>When `false`, indicates that the client prefers services to be provided by a female service provider.<br /><br>When `null`, indicates that the client has no preference.<br>Default: **null** |
| `birth_date` | `datetime` | Optional | The client’s date of birth. |
| `city` | `str` | Optional | The client’s city. |
| `client_credit_card` | [`ClientCreditCard`](../../doc/models/client-credit-card.md) | Optional | A client credit card. |
| `client_indexes` | [`List[AssignedClientIndex]`](../../doc/models/assigned-client-index.md) | Optional | Contains a list of the indexes and client index values to be assigned to the client.<br><br>If an index is already assigned to the client, it is overwritten with the passed index value. You cannot currently remove client indexes using the Public API. Only the indexes passed in the request are returned in the response. |
| `client_relationships` | [`List[ClientRelationship]`](../../doc/models/client-relationship.md) | Optional | Contains information about client relationships that were added or updated for the client. This parameter does not include all of the relationships assigned to the client, only the ones passed in the request. |
| `country` | `str` | Optional | The country in which the client is located. |
| `creation_date` | `datetime` | Optional | The date when the client was added to the business, either by the client from the online store or by a staff member at the subscriber’s business. This value always returns in the format yyyy-mm-ddThh:mm:ss:ms. |
| `custom_client_fields` | [`List[CustomClientFieldValue]`](../../doc/models/custom-client-field-value.md) | Optional | Contains information about the custom fields used for clients in the business. |
| `email` | `str` | Optional | The client’s email address. |
| `emergency_contact_info_email` | `str` | Optional | The email address of the client’s emergency contact.<br /><br>For more information, see [Children’s program features(emergency contact information)](https://support.mindbodyonline.com/s/article/203259283-Children-s-program-features-emergency-contact-information?language=en_US). |
| `emergency_contact_info_name` | `str` | Optional | The name of the client’s emergency contact. |
| `emergency_contact_info_phone` | `str` | Optional | The phone number of the client’s emergency contact. |
| `emergency_contact_info_relationship` | `str` | Optional | The client’s relationship with the emergency contact, for example, mother or spouse. |
| `first_appointment_date` | `datetime` | Optional | The date of the client’s first booked appointment at the business. |
| `first_name` | `str` | Required | The client’s first name. You must specify a first name when you add a client. |
| `gender` | `str` | Optional | The client’s gender. |
| `home_location` | [`Location`](../../doc/models/location.md) | Optional | - |
| `home_phone` | `str` | Optional | The client’s home phone number. |
| `is_company` | `bool` | Optional | When `true`, indicates that the client should be marked as a company at the business.<br /><br>When `false`, indicates the client is an individual and does not represent a company. |
| `is_prospect` | `bool` | Optional | This value is set only if the business owner allows individuals to be prospects.<br /><br>If the business owner has enabled the setting to default new client as a Prospect, the isProspect value will always be true. Otherwise,<br /><br>When `true`, indicates that the client should be marked as a prospect for the business.<br /><br>When `false`, indicates that the client should not be marked as a prospect for the business. |
| `last_formula_notes` | `str` | Optional | The last [formula note](https://support.mindbodyonline.com/s/article/203259903-Appointments-Formula-notes?language=en_US) entered for the client. |
| `last_modified_date_time` | `datetime` | Optional | The UTC date and time when the client’s information was last modified. |
| `last_name` | `str` | Required | The client’s last name. You must specify a last name when you add a client. |
| `liability` | [`Liability`](../../doc/models/liability.md) | Optional | - |
| `liability_release` | `bool` | Optional | When `true`, sets the client’s liability information as follows:<br><br>* `IsReleased` is set to true.<br>* `AgreementDate` is set to the time zone of the business when the call was processed.<br>* `ReleasedBy` is set to `null` if the call is made by the client, `0` if the call was made by the business owner, or to a specific staff member’s ID if a staff member made the call.<br>  When `false`, sets the client’s liability information as follows:<br>* `IsReleased` is set to `false`.<br>* `AgreementDate` is set to `null`.<br>* `ReleasedBy` is set to `null`. |
| `membership_icon` | `int` | Optional | The ID of the membership icon displayed next to the client’s name, if the client has a membership on their account. |
| `middle_name` | `str` | Optional | The client’s middle name. |
| `mobile_phone` | `str` | Optional | The client’s mobile phone number. |
| `mobile_provider` | `int` | Optional | The client's mobile provider. |
| `new_id` | `str` | Optional | The new RSSID to be used for the client. Use `NewId` to assign a specific alphanumeric value to be a client’s ID. This RSSID must be unique within the subscriber’s site. If this is a cross-regional update, the RSSID must be unique across the region. If the requested value is already in use, the call returns an error. |
| `notes` | `str` | Optional | Any notes entered on the client’s account by staff members. This value should never be shown to clients unless the business owner has a specific reason for showing them. |
| `photo_url` | `str` | Optional | The URL for the client’s photo, if one has been uploaded. |
| `postal_code` | `str` | Optional | The client’s postal code. |
| `prospect_stage` | [`ProspectStage`](../../doc/models/prospect-stage.md) | Optional | - |
| `red_alert` | `str` | Optional | Contains any red alert information entered by the business owner for the client. |
| `referred_by` | `str` | Optional | Specifies how the client was referred to the business. You can get a list of possible strings using the `GET ClientReferralTypes` endpoint.<br /><br>For more information, see [Referral types and referral subtypes](https://support.mindbodyonline.com/s/article/203259393-Referral-types-and-referral-subtypes?language=en_US). |
| `sales_reps` | [`List[SalesRep]`](../../doc/models/sales-rep.md) | Optional | Contains information about the sales representatives to be assigned to the new client. |
| `site_id` | `int` | Optional | The ID of the site. |
| `state` | `str` | Optional | The client’s state. |
| `status` | `str` | Optional | The client’s status. |
| `test` | `bool` | Optional | When `true`, indicates that test mode is enabled. The method is validated, but no client data is added or updated.<br /><br>Default: **false** |
| `unique_id` | `int` | Optional | The client’s system-generated ID at the business. This value cannot be changed by business owners and is always unique across all clients at the business. This ID is not widely used in the Public API, but can be used by your application to uniquely identify clients. |
| `work_extension` | `str` | Optional | The client’s work phone extension number. |
| `work_phone` | `str` | Optional | The client’s work phone number. |
| `yellow_alert` | `str` | Optional | Contains any yellow alert information entered by the business owner for the client. |
| `send_schedule_emails` | `bool` | Optional | When `true`, indicates that the client opts to receive schedule emails.<br>Default : **false** |
| `send_account_emails` | `bool` | Optional | When `true`, indicates that the client opts to receive account emails.<br>Default : **false** |
| `send_promotional_emails` | `bool` | Optional | When `true`, indicates that the client opts to receive promotional emails.<br>Default : **false** |
| `send_schedule_texts` | `bool` | Optional | When `true`, indicates that the client opts to receive schedule texts. |
| `send_account_texts` | `bool` | Optional | When `true`, indicates that the client opts to receive account texts. |
| `send_promotional_texts` | `bool` | Optional | When `true`, indicates that the client opts to receive promotional texts. |
| `locker_number` | `str` | Optional | The clients locker number. |
| `reactivate_inactive_client` | `bool` | Optional | When `true`, indicates that the client opts to reactive existing Inactive client. |
| `lead_channel_id` | `int` | Optional | The ID of the LeadChannel from LeadManagement. This parameter is required by LeadManagement to track the LeadChannel from where the new client is added.<br>If this value is not supplied then it won't save anything. |

## Example (as JSON)

```json
{
  "AccountBalance": 250.98,
  "Action": "Removed",
  "Active": false,
  "AddressLine1": "AddressLine10",
  "AddressLine2": "AddressLine24",
  "FirstName": "FirstName0",
  "LastName": "LastName0"
}
```

