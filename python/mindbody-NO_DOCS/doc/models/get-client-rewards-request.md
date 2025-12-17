
# Get Client Rewards Request

## Structure

`GetClientRewardsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Required | The ID of the client. |
| `start_date` | `datetime` | Optional | The start date of transaction.<br>Default: **today** |
| `end_date` | `datetime` | Optional | The end date of transaction.<br>Default: **StartDate** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ClientId": "ClientId4",
  "StartDate": "2016-03-13T12:52:32.123Z",
  "EndDate": "2016-03-13T12:52:32.123Z",
  "Limit": 218,
  "Offset": 152
}
```

