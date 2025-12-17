
# Message Threads Put Request

## Structure

`MessageThreadsPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `login` | `str` | Optional | The identifier of the Login that owns this messageThreads resource. |
| `forlogin` | `str` | Optional | The identifier of the receiving Login of this messageThreads resource. |
| `hold` | `str` | Optional | The identifier of the Hold that is related to this messageThread. |
| `entity_return` | `str` | Optional | This field has the ID from the EntityReturns table that hold ACH returns for disbursements or eCheck txns. |
| `opposing_message_thread` | `str` | Optional | Specifies whether this is the opposing MessageThread. |
| `folder` | `str` | Optional | Free-form text. By default, a messageThread resource is set as 'default'. |
| `sender` | `str` | Optional | Free-form text that represents the name of the sender of a messageThread resource. |
| `recipient` | `str` | Optional | Free-form text that represents the name of the recipient of a messageThread resource. |
| `subject` | `str` | Optional | Free-form text for adding a subject to a messageThread resource. |

## Example (as JSON)

```json
{
  "login": "t1_mtd_67ef5bad402b6b61e701e0z",
  "forlogin": "t1_log_61e9b7302360fbf12999d63",
  "hold": "t1_hld_67ef5bad3be038935902204",
  "entityReturn": "entityReturn",
  "opposingMessageThread": "t1_mtd_67ef5bad40f7e68822ac0c7",
  "folder": "default",
  "sender": "testnewmerchant",
  "recipient": "testnewmerchant1",
  "subject": "Transaction was put on hold"
}
```

