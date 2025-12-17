
# Client Configuration

General configuration data.

## Structure

`ClientConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `str` | Required | The title of your Greenbyte Platform website. |
| `tag` | `str` | Required | Your internal customer tag. |
| `url_web` | `str` | Required | Your URL to access the Greenbyte Platform website. |
| `url_api` | `str` | Required | Your URL to access the Greenbyte Platform API. |

## Example (as JSON)

```json
{
  "title": "intro",
  "tag": "intro",
  "urlWeb": "https://intro.greenbyte.cloud/",
  "urlApi": "https://intro.greenbyte.cloud/api/2/"
}
```

