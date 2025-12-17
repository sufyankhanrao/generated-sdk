
# Hateoas Link

REST application constraint (Hypermedia As The Engine Of Application State)

*This model accepts additional fields of type Any.*

## Structure

`HateoasLink`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Required | URL to invoke the action on the resource |
| `action` | [`HttpMethod`](../../doc/models/http-method.md) | Optional | HTTP Method to use for the request |
| `types` | [`List[ContentType]`](../../doc/models/content-type.md) | Optional | Content-types that can be used in the Accept header. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "href": "https://api.fi.com/fdx/v4/accounts/12345",
  "action": "DELETE",
  "types": [
    "image/gif"
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

