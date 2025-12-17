
# Get Packages Request

## Structure

`GetPackagesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `package_ids` | `List[int]` | Optional | A list of the packages IDs to filter by. |
| `sell_online` | `bool` | Optional | When `true`, only returns products that can be sold online.<br /><br>When `false`, all products are returned.<br /><br>Default: **false** |
| `location_id` | `int` | Optional | The location ID to use to determine the tax for the products that this request returns.<br /><br>Default: **online store** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "PackageIds": [
    255,
    0,
    1
  ],
  "SellOnline": false,
  "LocationId": 226,
  "Limit": 20,
  "Offset": 210
}
```

