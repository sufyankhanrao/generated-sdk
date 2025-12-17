
# Account Creation Company Object

The company object leveraged when providing details about the company of a new account.

## Structure

`AccountCreationCompanyObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_name` | `str` | Required | Name of company account to be created in Foxit eSign |
| `company_address` | `str` | Required | The address of the company to be created |

## Example (as JSON)

```json
{
  "companyName": "Wayne Tech",
  "companyAddress": "LA, US"
}
```

