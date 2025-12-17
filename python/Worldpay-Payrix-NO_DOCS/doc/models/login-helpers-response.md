
# Login Helpers Response

## Structure

`LoginHelpersResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `login` | `str` | Optional | The Login that owns this resource. |
| `mfa_sms_code` | `str` | Optional | The most recent SMS Code which has been texted to the user. |
| `mfa_sms_code_unix_time` | `int` | Optional | The expiry date of the most recent SMS Code. |
| `mfa_sms_code_attempts` | `int` | Optional | The number of times the most recent code has been attempted. |
| `mfa_sms_codes_count` | `int` | Optional | The number of codes which has been created in the current window.<br>If this goes above the max, you must wait until a new window to create more. |
| `mfa_sms_window` | `int` | Optional | The end time of the current MFA SMS window which is a sliding window limiting how many codes can be generated during a given window. |
| `login_as_enabled` | [`LoginAsEnabledEnum`](../../doc/models/login-as-enabled-enum.md) | Optional | Whether the associated login can use loginAs or not.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **OFF**<br>- `1` - **ON**<br></details><br> |

## Example (as JSON)

```json
{
  "id": "id2",
  "created": "created2",
  "modified": "modified0",
  "creator": "String1",
  "modifier": "modifier6"
}
```

