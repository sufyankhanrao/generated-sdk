
# Webhook Events

## Structure

`WebhookEvents`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `folder_sent` | `bool` | Optional | When a document folder is sent via web and webhook channel set as “Account” level, Foxit eSign calls your webhook URL with this event information.<br><br>**Default**: `False` |
| `folder_viewed` | `bool` | Optional | When party open this document folder via email or embeddedSession URL, Foxit eSign calls your Webhook with this event information.<br><br>**Default**: `False` |
| `folder_signed` | `bool` | Optional | When party signs this document folder, Foxit eSign calls your Webhook with this event information.<br><br>**Default**: `False` |
| `folder_cancelled` | `bool` | Optional | When party canceled this document folder than Foxit eSign calls your Webhook with this event information.<br><br>**Default**: `False` |
| `folder_executed` | `bool` | Optional | When all party signed this document folder, Foxit eSign calls your Webhook with this event information.<br><br>**Default**: `False` |
| `folder_deleted` | `bool` | Optional | When party canceled this document folder, Foxit eSign calls your Webhook with this event information.<br><br>**Default**: `False` |

## Example (as JSON)

```json
{
  "folder_sent": true,
  "folder_viewed": true,
  "folder_signed": false,
  "folder_cancelled": true,
  "folder_executed": true,
  "folder_deleted": true
}
```

