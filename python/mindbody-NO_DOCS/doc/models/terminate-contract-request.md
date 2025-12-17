
# Terminate Contract Request

## Structure

`TerminateContractRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Required | The ID of the client. |
| `client_contract_id` | `int` | Required | The unique ID of the sale of the contract |
| `termination_date` | `datetime` | Required | The contract termination date. |
| `termination_code` | `str` | Optional | ex. Illness, Injury, Moving, BreakingContract (Note this can be customized by each studio). |
| `termination_comments` | `str` | Optional | The comments for terminating a contract. |

## Example (as JSON)

```json
{
  "ClientId": "ClientId2",
  "ClientContractId": 242,
  "TerminationDate": "2016-03-13T12:52:32.123Z",
  "TerminationCode": "TerminationCode8",
  "TerminationComments": "TerminationComments0"
}
```

