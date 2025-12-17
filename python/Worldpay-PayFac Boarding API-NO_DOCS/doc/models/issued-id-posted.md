
# Issued Id Posted

Id Verification for the  Owners

## Structure

`IssuedIdPosted`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id_number` | `str` | Required | ID Number of the Owner<br><br>**Constraints**: *Maximum Length*: `40` |
| `issued_city` | `str` | Optional | City in which ID has been issued<br><br>**Constraints**: *Maximum Length*: `28` |
| `issued_state` | [`IssuedStateEnum`](../../doc/models/issued-state-enum.md) | Optional | State in which ID has been issued. Only valid US state codes (including Puerto Rico, Guam and Virgin Islands), Canadian province codes and Military state codes (AE - Armed Forces Africa, Canada, Europe, Middle East; AA - Armed Forces Americas (except Canada) ; AP - Armed Forces Pacific) are allowed |
| `issued_country` | [`IssuedCountryEnum`](../../doc/models/issued-country-enum.md) | Optional | Country Code in which ID has been issued<br><br>**Constraints**: *Maximum Length*: `2` |
| `date_issued` | `date` | Optional | Format yyyy-mm-dd. Date on which ID has been issued |
| `date_expires` | `date` | Optional | Format yyyy-mm-dd. Date on which ID expires |

## Example (as JSON)

```json
{
  "idNumber": "1234567",
  "issuedCity": "Anchorage",
  "issuedCountry": "US",
  "issuedState": "DE",
  "dateIssued": "2016-03-13",
  "dateExpires": "2016-03-13"
}
```

