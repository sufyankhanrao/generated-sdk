
# Get Client Rewards Response

## Structure

`GetClientRewardsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `balance` | `int` | Optional | The total rewards points available to the indicated client after the above transaction. |
| `transactions` | [`List[ClientRewardTransaction]`](../../doc/models/client-reward-transaction.md) | Optional | Contains information about the reward transaction details. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Balance": 222,
  "Transactions": [
    {
      "ActionDateTime": "2016-03-13T12:52:32.123Z",
      "Action": "Returned",
      "Source": "Source2",
      "SourceID": 144,
      "ExpirationDateTime": "2016-03-13T12:52:32.123Z"
    },
    {
      "ActionDateTime": "2016-03-13T12:52:32.123Z",
      "Action": "Returned",
      "Source": "Source2",
      "SourceID": 144,
      "ExpirationDateTime": "2016-03-13T12:52:32.123Z"
    }
  ]
}
```

