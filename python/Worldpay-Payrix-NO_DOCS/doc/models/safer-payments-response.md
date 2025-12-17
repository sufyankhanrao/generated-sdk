
# Safer Payments Response

## Structure

`SaferPaymentsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `entity` | `str` | Optional | The identifier of the Entity that saferPayments is associated to. |
| `status` | [`SaferPaymentStatusEnum`](../../doc/models/safer-payment-status-enum.md) | Optional | This field indicates the entity's current PCI compliance status for the service.<br><br><details><br><summary>Valid Values</summary><br>- `compliance` - **Compliance**<br>- `non-compliance` - **Non-Compliance**<br>- `pending` - **Pending**<br></details><br> |
| `enablement_date` | `str` | Optional | The Date and time when an entity was enabled for saferPayments.\nThe date is specified as an eight digit string in YYYY-MM-DD hh:mm:ss format, for example, '2023-06-01 01:00:00' for June 01, 2023. 1:00 am.<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}` |
| `pci_non_validation_fee_enabled` | [`SaferPaymentPciNonValidationFeeEnabledEnum`](../../doc/models/safer-payment-pci-non-validation-fee-enabled-enum.md) | Optional | This field indicates if the entity should be charged penalty fees for non-compliance.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Penalty Disabled.**<br>- `1` - **Penalty Enabled.**<br></details><br> |
| `org` | `str` | Optional | The identifier of the Org (group) that saferPayments is associated to. |
| `division` | `str` | Optional | The identifier of the Division that saferPayments  is associated to. |
| `partition` | `str` | Optional | The identifier of the Partition that saferPayments is associated to. |
| `program` | [`SaferPaymentProgramEnum`](../../doc/models/safer-payment-program-enum.md) | Optional | This field contains the program type of the saferPayments.<br><br><details><br><summary>Valid Values</summary><br>- `basic` - **Basic**<br>- `managed` - **Managed**<br></details><br> |
| `deleted` | `str` | Optional | The date and time at which this resource was deleted.\nThe date is specified as an eight digit string in YYYY-MM-DD hh:mm:ss format, for example, '2023-06-01 01:00:00' for June 01, 2023. 1:00 am.<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}` |
| `deleter` | `str` | Optional | The id of user who deleted the omniToken. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "inactive": 0,
  "frozen": 0,
  "id": "id2",
  "created": "created2",
  "modified": "modified0",
  "creator": "String1",
  "modifier": "modifier6"
}
```

