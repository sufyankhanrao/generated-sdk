
# Entity Routes Post Request

## Structure

`EntityRoutesPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `login` | `str` | Required | The Login that owns this EntityRoute. |
| `division` | `str` | Optional | Division ID in which the entity route is associated. |
| `entity` | `str` | Optional | The identifier of the Entity that this entityRoute applies to. |
| `org` | `str` | Optional | The identifier of the Org that this entityRoute applies to. |
| `partition` | `str` | Optional | ID of the partition in which this entity operates. |
| `platform` | [`EntityPlatformEnum`](../../doc/models/entity-platform-enum.md) | Required | The processor that issued this terminalTxnRef.<br><br><details><br><summary>Valid Values</summary><br>- `APPLE` - **APPLE**<br>- `ELAVON` - **ELAVON**<br>- `FIRSTDATA` - **FIRSTDATA**<br>- `GOOGLE` - **GOOGLE**<br>- `VANTIV` - **VANTIV**<br>- `VCORE` - **VCORE**<br>- `WELLSACH` - **WELLSACH**<br>- `WELLSFARGO` - **WELLSFARGO**<br>- `WFSINGLE` - **WFSINGLE**<br>- `WORLDPAY` - **WORLDPAY**<br>- `TDBANKCA` - **TDBANKCA**<br></details><br> |
| `currency` | [`CurrencyEnum`](../../doc/models/currency-enum.md) | Optional | The currency in which an entity should board with. This is an optional field that is only required for some platforms. See <a href="https://www.iban.com/currency-codes" target="_blank">Currency codes</a>  for all valid values. |
| `funding_currency` | [`FundingCurrency4Enum`](../../doc/models/funding-currency-4-enum.md) | Optional | The currency for which this entity will be funded on.<br><br><details><br><summary>Valid Values</summary><br>- `USD` - **US Dollar.**<br>- `CAD` - **Canadian Dollar.**<br></details><br> |
| `options` | `str` | Optional | Whether to disable ACH.<br>This is a JSON field.<br>Accepted values are {"eCheckDisabled": true}. |
| `default` | [`Default5Enum`](../../doc/models/default-5-enum.md) | Required | Whether all entityRefs created through this entityRoute will be set as default. Default entityRefs will have priority when processing transactions with no MID or Platform set.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Default.**<br>- `1` - **Default.**<br></details><br> |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Required | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Required | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "login": "login2",
  "platform": "VCORE",
  "currency": "USD",
  "default": 0,
  "inactive": 0,
  "frozen": 0,
  "division": "division2",
  "entity": "entity0",
  "org": "org8",
  "partition": "partition4"
}
```

