
# Secrets Response

## Structure

`SecretsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `login` | `str` | Optional | The identifier of the Login that owns this secret resource. |
| `entity` | `str` | Optional | The identifier of the Entity associated with this secret. |
| `org` | `str` | Optional | The identifier of the Org associated with this secret. |
| `division` | `str` | Optional | The identifier of the Division associated with this secret. |
| `partition` | `str` | Optional | The identifier of the Partition associated with this secret. |
| `mtype` | [`SecretTypeEnum`](../../doc/models/secret-type-enum.md) | Optional | The type of secret.<br><br><details><br><summary>Valid Values</summary><br>- `baseKey` - **Base Derivation Key.**<br>- `sftp` - **SFTP Server Key.**<br>- `publicKey` - **Public Key.**<br>- `privateKey` - **Private Key.**<br>- `ecPrivateKey` - **Elliptic Curve Private Key.**<br>- `apikey` - **API Key.**<br>- `oldPrivateKey` - **Expired Private Key.**<br></details><br> |
| `platform` | [`SecretsPlatformEnum`](../../doc/models/secrets-platform-enum.md) | Optional | The platform used to process this Transaction.<br><br><details><br><summary>Valid Values</summary><br>- `APPLE` - **Apple Payment Processor**<br>- `ELAVON` - **ELAVON Payment Processor**<br>- `FIRSTDATA` - **FirstData Payment Processor**<br>- `GOOGLE` - **Google Payment Processor**<br>- `VANTIV` - **WorldPay / Vantiv eComm Payment Processor (VAP)**<br>- `VCORE` - **WorldPay / Vantiv Core Payment Processor**<br>- `WELLSACH` - **Wells Fargo Merchant Services Payment Processor (ACH)**<br>- `WELLSFARGO` - **Wells Fargo Merchant Services Payment Processor**<br>- `WFSINGLE` - **Wells Fargo Single Payment Processor**<br>- `WORLDPAY` - **WORLDPAY**<br>- `TDBANKCA` - **TDBANKCA**<br></details><br> |
| `name` | `str` | Optional | The name of this Secret.<br>This field is stored as a text string and must be between 0 and 100 characters long. |
| `description` | `str` | Optional | A description of this Secret.<br>This field is stored as a text string and must be between 0 and 500 characters long. |
| `key` | `str` | Optional | The actual key or the indicator of which key to use.<br>This field is stored as a text string and must be between 1 and 5000 characters long. |
| `locked` | [`SecretLockedEnum`](../../doc/models/secret-locked-enum.md) | Optional | Whether this secret is locked or not.<br>If it is locked, then the value of this type of secret will prevail.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Locked**<br>- `1` - **Locked**<br></details><br>**Default**: `0`<br> |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "locked": 0,
  "inactive": 0,
  "frozen": 0,
  "id": "id0",
  "created": "created0",
  "modified": "modified8",
  "creator": "String9",
  "modifier": "modifier4"
}
```

