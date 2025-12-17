
# Apple Domains Response

## Structure

`AppleDomainsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `registered_merchant` | `str` | Optional | The identifier of the Merchant registered with Apple Pay for this domain. |
| `owner_entity` | `str` | Optional | The identifier of the Entity that controls this domain. This is to identify the Vendor or Facilitator hosting the Apple Pay domain for the merchant. If this domain is controlled by the actual registered Merchant, the Entity field will be the Merchant's Entity. |
| `status` | [`StatusEnum`](../../doc/models/status-enum.md) | Optional | The registration status of this domain for the given Registered Merchant.<br><br><details><br><summary>Valid Values</summary><br>- `registration_requested` **The domains that have been requested to be registered.**<br>- `registering` **In the process of being registered with Apple.**<br>- `registered` **Successfully Registered with Apple.**<br>- `failed_registration` **A Failure occurred Registering.**<br>- `unregistration_requested` **Unregistration requested.**<br>- `unregistering` **In the process of being un-registered from Apple.**<br>- `unregistered` **Successfully Unregistered with Apple.**<br></details><br> |
| `domain` | `str` | Optional | The domain(FQDN) associated with the Registered Merchant. |
| `error_note` | `str` | Optional | For a failed Registration or Un-Registration, will contain the reason for the failure. |

## Example (as JSON)

```json
{
  "id": "id8",
  "created": "created8",
  "modified": "modified6",
  "creator": "String7",
  "modifier": "modifier8"
}
```

