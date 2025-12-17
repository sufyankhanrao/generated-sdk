
# EID Document

## Structure

`EIDDocument`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_id` | `int` | Optional | Technical identifier for the EID file. Should not be stored in database as it is not guaranteed to stay unchanged over time. |
| `account_group_id` | `str` | Optional | Account Group Id |
| `account_group_name` | `str` | Optional | Account group name |
| `document_type` | `str` | Optional | Document type.<br>Possible values:<br>•	NAT (National)<br>•	INT (International) |
| `document_format` | `str` | Optional | Document format (CHORUS, DIFI etc.) |
| `document_date` | `str` | Optional | Document date.<br>Example: 20170101 |
| `number_of_invoices` | `int` | Optional | Number of invoices |
| `file_size` | `int` | Optional | Document size |
| `document_status` | `str` | Optional | Document status.<br>Possible values:<br>•	NEW<br>•	VIEWED<br>•	DOWNLOADED<br>•	RESTORED |
| `document_name` | `str` | Optional | Document file name. |

## Example (as JSON)

```json
{
  "DocumentId": 250,
  "AccountGroupId": "AccountGroupId2",
  "AccountGroupName": "AccountGroupName0",
  "DocumentType": "DocumentType8",
  "DocumentFormat": "DocumentFormat4"
}
```

