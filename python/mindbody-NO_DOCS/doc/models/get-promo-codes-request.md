
# Get Promo Codes Request

## Structure

`GetPromoCodesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `active_only` | `bool` | Optional | If true, filters results to show only promocodes that are active. If **false**, all promocodes are returned.<br>Default: **true** |
| `online_only` | `bool` | Optional | If `true`, filters results to show only promocodes that can be used for online sale.<br>If `false`, all promocodes are returned.<br>Default: **false** |
| `start_date` | `datetime` | Optional | Filters results to promocodes that were activated after this date. |
| `end_date` | `datetime` | Optional | Filters results to promocodes that were activated before this date. |
| `last_modified_date` | `datetime` | Optional | Filters results to promocodes that were modified on or after this date. |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ActiveOnly": false,
  "OnlineOnly": false,
  "StartDate": "2016-03-13T12:52:32.123Z",
  "EndDate": "2016-03-13T12:52:32.123Z",
  "LastModifiedDate": "2016-03-13T12:52:32.123Z"
}
```

