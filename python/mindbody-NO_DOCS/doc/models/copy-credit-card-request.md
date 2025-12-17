
# Copy Credit Card Request

crosssite/copycreditcard

## Structure

`CopyCreditCardRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `source_site_id` | `int` | Optional | The siteId of the source clientId. |
| `source_client_id` | `str` | Optional | The clientId at the source siteId. |
| `target_site_id` | `int` | Optional | The siteId of the target clientId. |
| `target_client_id` | `str` | Optional | The clientId at the target siteId. |

## Example (as JSON)

```json
{
  "SourceSiteId": 96,
  "SourceClientId": "SourceClientId8",
  "TargetSiteId": 228,
  "TargetClientId": "TargetClientId2"
}
```

