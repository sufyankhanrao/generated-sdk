
# EID Search Req

## Structure

`EIDSearchReq`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_code` | `int` | Required | Collecting Company Code of the selected payer.<br>Mandatory |
| `account_group_country` | `int` | Required | Country code (colco code) of the account group.<br>Mandatory |
| `account_group_id` | `List[str]` | Required | List of IDs of the account groups that user has access to.<br>Mandatory |
| `account_group_name` | `str` | Optional | Account group name<br>Optional.<br>This input is a search criterion, if given. |
| `from_date` | `str` | Optional | EID date searched from this date.<br>Optional. |
| `to_date` | `str` | Optional | Invoice date searched until this date.<br>Optional. |
| `invoice_type` | `str` | Optional | Invoice type.<br>Optional.<br>Possible values:<br>•	NAT (National)<br>•	INT (International) |
| `invoice_status` | `str` | Optional | Status of the document.<br>Optional.<br>Possible values:<br>•	NEW<br>•	VIEWED<br>•	DOWNLOADED<br>•	RESTORED |
| `sort_by` | `List[str]` | Optional | Sort option –<br>•    InvoiceNumber ASC<br>•    InvoiceDate ASC<br>•    InvoiceNumber DESC<br>•    InvoiceDate DESC<br>Optional |

## Example (as JSON)

```json
{
  "ColCoCode": 222,
  "AccountGroupCountry": 138,
  "AccountGroupId": [
    "AccountGroupId7",
    "AccountGroupId8"
  ],
  "AccountGroupName": "AccountGroupName8",
  "FromDate": "FromDate4",
  "ToDate": "ToDate4",
  "InvoiceType": "InvoiceType6",
  "InvoiceStatus": "InvoiceStatus2"
}
```

