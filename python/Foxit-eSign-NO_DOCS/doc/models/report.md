
# Report

The optional filters that a report may leverage

## Structure

`Report`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`EnvelopeStatusEnum`](../../doc/models/envelope-status-enum.md) | Required | Download data by the folder status. Status parameter can have any of the following values: EXECUTED,SHARED,DRAFT, PARTIALLY SIGNED, CANCELLED, EXPIRED and DELETED. |
| `creation_date_from` | `str` | Required | Start of the Creation Date range. Accepted format: YYYY-MM-DD.<br><br>**Constraints**: *Pattern*: `^\d{4}\-(0[1-9]\|1[012])\-(0[1-9]\|[12][0-9]\|3[01])$` |
| `creation_date_to` | `str` | Required | End of the Creation Date range. Accepted format: YYYY-MM-DD.<br><br>**Constraints**: *Pattern*: `^\d{4}\-(0[1-9]\|1[012])\-(0[1-9]\|[12][0-9]\|3[01])$` |
| `folder_name` | `str` | Optional | Any folder which contains this string. |
| `include_fields` | `str` | Optional | Including folder fields in report.<br><br>**Default**: `"false"` |
| `author_email` | `str` | Optional | Author email in report. |
| `signer_email` | `str` | Optional | Signer email in report. |

## Example (as JSON)

```json
{
  "status": "EXECUTED",
  "creationDateFrom": "2022-01-01",
  "creationDateTo": "2022-04-01",
  "includeFields": "false",
  "folderName": "folderName2",
  "authorEmail": "authorEmail6",
  "signerEmail": "signerEmail6"
}
```

