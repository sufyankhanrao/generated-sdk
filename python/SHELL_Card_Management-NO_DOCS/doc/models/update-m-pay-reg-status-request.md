
# Update M Pay Reg Status Request

## Structure

`UpdateMPayRegStatusRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_id` | `int` | Optional | Collecting Company Id  of the selected payer.<br>Optional if ColCoCode is passed else Mandatory.<br>Example:<br>1-Philippines<br>5-UK |
| `col_co_code` | `int` | Optional | Collecting Company Code (Shell Code) of the selected payer.<br>Mandatory for serviced OUs such as Romania, Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other countries if ColCoID is provided.<br>Example:<br>86-Philippines<br>5-UK |
| `payer_id` | `int` | Optional | Payer Id  of the selected payer.<br>Optional if PayerNumber is passed else Mandatory |
| `payer_number` | `str` | Optional | Payer Number (Ex: GB000000123) of the selected payer.<br>Optional if PayerId is passed else Mandatory |
| `m_pay_requests` | [`List[UpdateMPayRegStatusRequestMPayRequestsItems]`](../../doc/models/update-m-pay-reg-status-request-m-pay-requests-items.md) | Optional | List of MPay Request to be updated for Fleet Manager approval status.<br>Mandatory<br>Maximum number of requests that can be submitted are 50 |

## Example (as JSON)

```json
{
  "ColCoId": 38,
  "ColCoCode": 52,
  "PayerId": 86,
  "PayerNumber": "PayerNumber8",
  "MPayRequests": [
    {
      "GlobalRequestID": "GlobalRequestID6",
      "Status": "Status6",
      "ApproverUserID": "ApproverUserID8",
      "ApproverUserDisplayName": "ApproverUserDisplayName2",
      "Reason": "Reason0"
    },
    {
      "GlobalRequestID": "GlobalRequestID6",
      "Status": "Status6",
      "ApproverUserID": "ApproverUserID8",
      "ApproverUserDisplayName": "ApproverUserDisplayName2",
      "Reason": "Reason0"
    },
    {
      "GlobalRequestID": "GlobalRequestID6",
      "Status": "Status6",
      "ApproverUserID": "ApproverUserID8",
      "ApproverUserDisplayName": "ApproverUserDisplayName2",
      "Reason": "Reason0"
    }
  ]
}
```

