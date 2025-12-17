
# Client Service

A service that is on a client's account.

## Structure

`ClientService`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `active_date` | `datetime` | Optional | The date that this pricing option became active and could be used to pay for services. |
| `count` | `int` | Optional | The number of service sessions this pricing option contained when first purchased. |
| `current` | `bool` | Optional | When `true`, there are service sessions remaining on the pricing option that can be used pay for the current session.<br /><br>When `false`, the client cannot use this pricing option to pay for other services. |
| `expiration_date` | `datetime` | Optional | The date when the pricing option expires and can no longer be used to pay for services, even if unused service sessions remain on the option; expressed as UTC. |
| `id` | `int` | Optional | The unique ID assigned to this pricing option, specific to when it was purchased by the client. |
| `product_id` | `int` | Optional | The unique ID of this pricing option, not specific to any client's purchase of it. |
| `name` | `str` | Optional | The name of this pricing option. |
| `payment_date` | `datetime` | Optional | The date on which the client paid for this pricing option. |
| `program` | [`Program`](../../doc/models/program.md) | Optional | - |
| `remaining` | `int` | Optional | The number of service sessions remaining in the pricing option that can still be used. |
| `site_id` | `int` | Optional | The ID of the subscriber site associated with this pricing option. |
| `action` | [`Action1Enum`](../../doc/models/action-1-enum.md) | Optional | The action taken. |
| `client_id` | `str` | Optional | The Client ID assigned to this pricing option, specific to when it was purchased by the client. |

## Example (as JSON)

```json
{
  "ActiveDate": "2016-03-13T12:52:32.123Z",
  "Count": 70,
  "Current": false,
  "ExpirationDate": "2016-03-13T12:52:32.123Z",
  "Id": 6
}
```

