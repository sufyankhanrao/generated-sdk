
# Orgs VAS Safer Payments Put Request

## Structure

`OrgsVASSaferPaymentsPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org` | `str` | Optional | The identifier of the Org (group) that OrgsVASOmniTokens is associated to. |
| `default_program` | [`OrgsVASSaferPaymentsDefaultProgramEnum`](../../doc/models/orgs-vas-safer-payments-default-program-enum.md) | Optional | This field contains the default program type of the orgsVASSaferPayments.<br><br><details><br><summary>Valid Values</summary><br>- `basic` - **Basic**<br>- `managed` - **Managed**<br></details><br> |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "org": "t1_org_680bfd2cea2729081810000",
  "defaultProgram": "basic",
  "inactive": 0,
  "frozen": 0
}
```

