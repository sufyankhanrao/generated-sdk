
# Client Duplicate

A client record that is considered a duplicate based on matching of the client's first name, last name, AND email fields

## Structure

`ClientDuplicate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The client’s ID, as configured by the business owner. This is the client’s barcode ID if the business owner assigns barcodes to clients. This ID is used throughout the Public API for client-related Public API calls. When used in a POST `UpdateClient` request, the `Id` is used to identify the client for the update. |
| `unique_id` | `int` | Optional | The client’s system-generated ID at the business. This value cannot be changed by business owners and is always unique across all clients at the business. This ID is not widely used in the Public API, but can be used by your application to uniquely identify clients. |
| `first_name` | `str` | Optional | The client’s first name. |
| `last_name` | `str` | Optional | The client’s last name. |
| `email` | `str` | Optional | The client’s email address. |

## Example (as JSON)

```json
{
  "Id": "Id4",
  "UniqueId": 228,
  "FirstName": "FirstName6",
  "LastName": "LastName6",
  "Email": "Email6"
}
```

