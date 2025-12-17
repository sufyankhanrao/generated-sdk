
# Get Client Purchases Request

## Structure

`GetClientPurchasesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Required | The ID of the client you are querying for purchases. |
| `start_date` | `datetime` | Optional | Filters results to purchases made on or after this timestamp.<br /><br>Default: **now** |
| `end_date` | `datetime` | Optional | Filters results to purchases made before this timestamp.<br /><br>Default: **end of today** |
| `sale_id` | `int` | Optional | Filters results to the single record associated with this ID. |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ClientId": "ClientId6",
  "StartDate": "2016-03-13T12:52:32.123Z",
  "EndDate": "2016-03-13T12:52:32.123Z",
  "SaleId": 152,
  "Limit": 90,
  "Offset": 24
}
```

