
# Change Request

## Structure

`ChangeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `deleted` | `str` | Optional | In case resource is deleted, this field will then show the date it occurred. The format should be YYYY-MM-DD HH:MM:SS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}` |
| `login` | `str` | Optional | The identifier of the Login associated with this ChangeRequest. |
| `auth_type` | `int` | Optional | Auth Type that originate the request. |
| `operation` | [`OperationEnum`](../../doc/models/operation-enum.md) | Optional | The operation being performed on the resource.<br><br><details><br><summary>Valid Values</summary><br>- `create` - **When creating a model.**<br>- `update` - **When updating a model.**<br></details><br> |
| `status` | [`ChangeRequestStatusEnum`](../../doc/models/change-request-status-enum.md) | Optional | The status of the requested change.<br><br><details><br><summary>Valid Values</summary><br>- `pending` - **The Change Request has a pending status.**<br>- `manualReview` - **The Change Request was escalated to be manually reviewed.**<br>- `approved` - **The Change Request has been approved.**<br>- `declined` - **The Change Request was declined.**<br></details><br> |
| `reason_type` | `str` | Optional | A type which categorizes the reason, in case the change was declined. |
| `reason` | `str` | Optional | The reason in case the change was declined. |
| `changes` | `str` | Optional | A JSON encoded string with the request payload |
| `model` | `str` | Optional | The model being changed. |
| `record_id` | `str` | Optional | The id of the model, only set when operation is update |
| `entity` | `str` | Optional | The identifier of the Entity associated with this Account. |
| `analyst` | `str` | Optional | The person who review the request. |
| `reviewed` | `str` | Optional | If this change request was reviewed. The format should be YYYY-MM-DD HH:MM:SS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}` |

## Example (as JSON)

```json
{
  "id": "id0",
  "created": "created0",
  "modified": "modified8",
  "creator": "String9",
  "modifier": "modifier4"
}
```

