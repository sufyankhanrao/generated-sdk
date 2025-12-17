
# Session Post Response

## Structure

`SessionPostResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `login` | `str` | Optional | The Login that owns this resource. |
| `key` | `str` | Optional | The cryptographically secure, randomly generated key to be used in authentication. |
| `public` | [`SessionPublicEnum`](../../doc/models/session-public-enum.md) | Optional | Whether this Session should have access to only public resources.<br>All other resources are private. <details> <summary>Valid Values</summary><br><br>- `0` - **Session can also access private resources.**<br>- `1` - **Session can only access public resources.**<br><br> </details><br> |
| `sso` | [`SsoEnum`](../../doc/models/sso-enum.md) | Optional | Whether or not the Session is created using SSO. <details> <summary>Valid Values</summary><br><br>- `0` - **Session not created with SSO.**<br>- `1` - **Session created with SSO.**<br><br> </details><br> |
| `token` | [`TokenEnum`](../../doc/models/token-enum.md) | Optional | Whether or not an AuthToken is required as part of the authentication when this Apikey is used.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **The authToken mechanism is disabled.**<br>- `1` - **The authToken mechanism is required for 'POST' and 'DELETE' requests.**<br></details><br> |
| `mfa_authenticated` | [`MfaAuthenticatedEnum`](../../doc/models/mfa-authenticated-enum.md) | Optional | Whether or not the MFA is enabled.. <details> <summary>Valid Values</summary><br><br>- `0` - **MFA is disabled.**<br>- `1` - **MFA is enabled.**<br><br> </details><br> |
| `effective_roles` | `float` | Optional | Effective roles for this login. |
| `effective_resources` | `str` | Optional | Array of all resources the login has access to with corresponding actions. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "inactive": 0,
  "frozen": 0,
  "id": "id0",
  "created": "created0",
  "modified": "modified8",
  "creator": "String9",
  "modifier": "modifier4"
}
```

