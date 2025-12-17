
# Invoice Distribution Method

## Structure

`InvoiceDistributionMethod`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `is_primary` | `bool` | Optional | If True then this distribution method is the default distribution method.<br><br>**Default**: `True` |
| `frequency_type` | `str` | Optional | Frequency type unit Id & description<br>E.g.:<br>1- Daily<br>2-Weekly<br>3-Monthly<br>4-Invoicing<br>6-Calendar quarter |
| `distribution_method` | `str` | Optional | Invoice Distribution Method (Id-Description)<br>E.g.:<br>1-e-mail<br>2-Fax<br>3-Courier to Customer<br>4-Courier to Client<br>5-Print<br>6-FTP<br>7-SMS |
| `output_type` | `str` | Optional | Invoice output type (Id - Description) |

## Example (as JSON)

```json
{
  "IsPrimary": true,
  "FrequencyType": "weekly",
  "DistributionMethod": "e-mail",
  "OutputType": "1 - PDF"
}
```

