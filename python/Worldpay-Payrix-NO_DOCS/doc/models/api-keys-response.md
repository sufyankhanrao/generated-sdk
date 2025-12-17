
# Api Keys Response

## Structure

`ApiKeysResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `login` | `str` | Optional | The identifier of the login under which to perform this action. If you do not supply a login in this field, then the API defaults to the login that is currently authenticated. |
| `key` | `str` | Optional | The cryptographically secure, randomly generated key to be used<br>in authentication.<br><br>An apikey may represent a private (secret) key code that is used internally (server-side) by the application authenticating to the API.<br><br>A private key should never be exposed to external/untrusted entities and should be immediately deactivated if compromised. All API resources and actions can be accessed and performed with a private apikey. |
| `name` | `str` | Optional | The name of the API key. |
| `description` | `str` | Optional | Description of the ApiKey. |
| `public` | [`ApiKeyPublicEnum`](../../doc/models/api-key-public-enum.md) | Optional | Whether this API key should have access to only public resources.<br>Public resources include Transactions, Tokens, Customers, and Items.<br>All other resources are private. <details> <summary>Valid Values</summary><br><br>- `0` - **The key can also access private resources.**<br>- `1` - **The key can only access public resources.**<br><br> </details><br> |
| `token` | [`TokenEnum`](../../doc/models/token-enum.md) | Optional | Whether or not an AuthToken is required as part of the authentication when this Apikey is used.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **The authToken mechanism is disabled.**<br>- `1` - **The authToken mechanism is required for 'POST' and 'DELETE' requests.**<br></details><br> |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "inactive": 0,
  "frozen": 0,
  "id": "id0",
  "created": "created0",
  "modified": "modified2",
  "creator": "String9",
  "modifier": "modifier6"
}
```

