
# Client With Suspension Info

A Client DTO with Suspension Informatoin

## Structure

`ClientWithSuspensionInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `suspension_info` | [`ClientSuspensionInfo`](../../doc/models/client-suspension-info.md) | Optional | A Client DTO with Suspension Informatoin |
| `appointment_gender_preference` | [`AppointmentGenderPreference1Enum`](../../doc/models/appointment-gender-preference-1-enum.md) | Optional | The gender of staff member with whom the client prefers to book appointments. |
| `birth_date` | `datetime` | Optional | The client’s date of birth. |
| `country` | `str` | Optional | The client’s country. |
| `creation_date` | `datetime` | Optional | The date the client’s profile was created and added to the business, either by the client from the online store, or by a staff member. This value always returns in the format `yyyy-mm-ddThh:mm:ss:ms`. |
| `custom_client_fields` | [`List[CustomClientFieldValue]`](../../doc/models/custom-client-field-value.md) | Optional | Contains information about the custom fields used for clients in the business. |
| `client_credit_card` | [`ClientCreditCard`](../../doc/models/client-credit-card.md) | Optional | A client credit card. |
| `client_indexes` | [`List[AssignedClientIndex]`](../../doc/models/assigned-client-index.md) | Optional | Contains the IDs of the client’s assigned ClientIndexes and ClientIndexValues.<br><br>If an index is already assigned to the client, it is overwritten with the passed index value. You cannot currently remove client indexes using the Public API. Only the indexes passed in the request are returned in the response. |
| `client_relationships` | [`List[ClientRelationship]`](../../doc/models/client-relationship.md) | Optional | Contains information about the relationship between two clients.<br><br>This parameter does not include all of the relationships assigned to the client, only the ones passed in the request. |
| `first_appointment_date` | `datetime` | Optional | The date of the client’s first booked appointment at the business. |
| `first_class_date` | `datetime` | Optional | The date of the clients first booked class at the business. |
| `first_name` | `str` | Optional | The client’s first name. |
| `id` | `str` | Optional | The client’s ID, as configured by the business owner. This is the client’s barcode ID if the business owner assigns barcodes to clients. This ID is used throughout the Public API for client-related Public API calls. When used in a POST `UpdateClient` request, the `Id` is used to identify the client for the update. |
| `is_company` | `bool` | Optional | When `true`, indicates that the client should be marked as a company at the business.<br /><br>When `false`, indicates the client is an individual and does not represent a company. |
| `is_prospect` | `bool` | Optional | This value is set only if the business owner allows individuals to be prospects.<br /><br>When `true`, indicates that the client should be marked as a prospect for the business.<br /><br>When `false`, indicates that the client should not be marked as a prospect for the business. |
| `last_name` | `str` | Optional | The client’s last name. |
| `liability` | [`Liability`](../../doc/models/liability.md) | Optional | - |
| `liability_release` | `bool` | Optional | Passing `true` sets the client’s liability information as follows:<br><br>* `IsReleased` is set to `true`.<br>* `AgreementDate` is set to the time zone of the business when the call was processed.<br>* `ReleasedBy` is set to `null` if the call is made by the client, `0` if the call was made by the business owner, or to a specific staff member’s ID if a staff member made the call.<br>  Passing `false` sets the client’s liability information as follows:<br>* `IsReleased` is set to `false`.<br>* `AgreementDate` is set to `null`.<br>* `ReleasedBy` is set to `null`. |
| `membership_icon` | `int` | Optional | The ID of the [membership icon](https://support.mindbodyonline.com/s/article/203259703-Membership-Setup-screen?language=en_US) displayed next to the client’s name, if the client has a membership on their account. |
| `mobile_provider` | `int` | Optional | The client’s mobile provider. |
| `notes` | `str` | Optional | Any notes entered on the client’s account by staff members. This value should never be shown to clients unless the business owner has a specific reason for showing them. |
| `state` | `str` | Optional | The client’s state. |
| `unique_id` | `int` | Optional | The client’s system-generated ID at the business. This value cannot be changed by business owners and is always unique across all clients at the business. This ID is not widely used in the Public API, but can be used by your application to uniquely identify clients. |
| `last_modified_date_time` | `datetime` | Optional | The UTC date and time when the client’s information was last modified. |
| `red_alert` | `str` | Optional | Contains any red alert information entered by the business owner for the client. |
| `yellow_alert` | `str` | Optional | Contains any yellow alert information entered by the business owner for the client. |
| `middle_name` | `str` | Optional | The client’s middle name. |
| `prospect_stage` | [`ProspectStage`](../../doc/models/prospect-stage.md) | Optional | - |
| `email` | `str` | Optional | The client’s email address. |
| `mobile_phone` | `str` | Optional | The client’s mobile phone number. |
| `home_phone` | `str` | Optional | The client’s home phone number. |
| `work_phone` | `str` | Optional | The client’s work phone number. |
| `account_balance` | `float` | Optional | The client’s current [account balance](https://mindbody-online-support.force.com/support/s/article/203262013-Adding-account-payments-video-tutorial?language=en_US). |
| `address_line_1` | `str` | Optional | The first line of the client’s street address. |
| `address_line_2` | `str` | Optional | The second line of the client’s street address, if needed. |
| `city` | `str` | Optional | The client’s city. |
| `postal_code` | `str` | Optional | The client’s postal code. |
| `work_extension` | `str` | Optional | The client’s work phone extension number. |
| `referred_by` | `str` | Optional | Specifies how the client was referred to the business. You can get a list of possible strings using the `GetClientReferralTypes` endpoint. |
| `photo_url` | `str` | Optional | The URL of the client’s photo for the client profile. |
| `emergency_contact_info_name` | `str` | Optional | The name of the client’s emergency contact. |
| `emergency_contact_info_email` | `str` | Optional | The email address of the client’s emergency contact. |
| `emergency_contact_info_phone` | `str` | Optional | The phone number of the client’s emergency contact. |
| `emergency_contact_info_relationship` | `str` | Optional | The client’s relationship with the emergency contact. |
| `gender` | `str` | Optional | The gender of the client. |
| `last_formula_notes` | `str` | Optional | The last [formula note](https://support.mindbodyonline.com/s/article/203259903-Appointments-Formula-notes?language=en_US) entered for the client. |
| `active` | `bool` | Optional | When `true`, indicates that the client’s profile is marked as active on the site.<br /><br>When `false`, the client’s profile is inactive.<br>Defaults to `true` based on the assumption that if a client is currently inactive OR is to be marked inactive, this property will explicitly be mapped/set to `false`. |
| `sales_reps` | [`List[SalesRep]`](../../doc/models/sales-rep.md) | Optional | A list of sales representatives. |
| `status` | `str` | Optional | The status of the client in the business. Possible values are:<br><br>* Declined<br>* Non-Member<br>* Active<br>* Expired<br>* Suspended<br>* Terminated |
| `action` | [`Action1Enum`](../../doc/models/action-1-enum.md) | Optional | The action taken. |
| `send_account_emails` | `bool` | Optional | When `true`, indicates that the client has opted to receive general account notifications by email. This property is editable.<br><br />Default: **false** |
| `send_account_texts` | `bool` | Optional | When `true`, indicates that the client has opted to receive general account notifications by text message. This parameter cannot be updated by developers. If included in a request, it is ignored. |
| `send_promotional_emails` | `bool` | Optional | When `true`, indicates that the client has opted to receive promotional notifications by email. This property is editable.<br><br />Default: **false** |
| `send_promotional_texts` | `bool` | Optional | When `true`, indicates that the client has opted to receive promotional notifications by text message. This parameter cannot be updated by developers. If included in a request, it is ignored. |
| `send_schedule_emails` | `bool` | Optional | When `true`, indicates that the client has opted to receive schedule notifications by email. This property is editable.<br><br />Default: **false** |
| `send_schedule_texts` | `bool` | Optional | When `true`, indicates that the client has opted to receive schedule notifications by text message. This parameter cannot be updated by developers. If included in a request, it is ignored. |
| `home_location` | [`Location`](../../doc/models/location.md) | Optional | - |
| `locker_number` | `str` | Optional | The clients locker number. |

## Example (as JSON)

```json
{
  "SuspensionInfo": {
    "BookingSuspended": false,
    "SuspensionStartDate": "SuspensionStartDate8",
    "SuspensionEndDate": "SuspensionEndDate2"
  },
  "AppointmentGenderPreference": "None",
  "BirthDate": "2016-03-13T12:52:32.123Z",
  "Country": "Country0",
  "CreationDate": "2016-03-13T12:52:32.123Z"
}
```

