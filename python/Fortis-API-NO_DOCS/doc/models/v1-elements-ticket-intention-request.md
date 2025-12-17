
# V1 Elements Ticket Intention Request

## Structure

`V1ElementsTicketIntentionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contact_id` | `str` | Optional | Used to associate the Ticket with a Contact.<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `contact_api_id` | `str` | Optional | Used to associate the Ticket with a Contact. |
| `location_id` | `str` | Required | A valid Location Id associated with the Contact for this Ticket<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `product_transaction_id` | `str` | Optional | Include a product_transaction_id to respect it's cvv and address field settings when creating a ticket.  These settings are enforced at the ticket creation level only.<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `message` | `str` | Optional | A custom text message that displays after the ticket is created.<br><br>**Constraints**: *Maximum Length*: `120` |

## Example (as JSON)

```json
{
  "contact_id": "11e95f8ec39de8fbdb0a4f1a",
  "location_id": "11e95f8ec39de8fbdb0a4f1a",
  "product_transaction_id": "11e95f8ec39de8fbdb0a4f1a",
  "contact_api_id": "contact_api_id4",
  "message": "message0"
}
```

