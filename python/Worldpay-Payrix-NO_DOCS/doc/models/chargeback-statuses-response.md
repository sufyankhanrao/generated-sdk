
# Chargeback Statuses Response

## Structure

`ChargebackStatusesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `chargeback` | `str` | Optional | ID of the related chargeback. |
| `chargeback_message` | `str` | Optional | ID of the chargeback message associated with this chargeback. |
| `status` | [`ChargebackStatusesStatusEnum`](../../doc/models/chargeback-statuses-status-enum.md) | Optional | The Chargeback's status. <details><summary>Valid Values</summary><br><br>- `open` - **Chargeback is open, responses may be submitted.**<br><br>- `closed` - **Chargeback is closed, responses may no longer be submitted.**<br><br>- `won` - **Chargeback won.**<br><br>- `lost` - **Chargeback lost.**<br><br> </details><br> |

## Example (as JSON)

```json
{
  "id": "id4",
  "created": "created4",
  "modified": "modified8",
  "creator": "String3",
  "modifier": "modifier2"
}
```

