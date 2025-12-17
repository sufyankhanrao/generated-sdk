
# Personnel Site Induction

A site induction.

## Structure

`PersonnelSiteInduction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_induction_id` | `int` | Optional | The id of a personnel site induction.<br><br>**Constraints**: `>= 1` |
| `site_id` | `int` | Optional | The id of a site.<br><br>**Constraints**: `>= 1` |
| `date_expires` | `date` | Optional | When the site induction expires. |

## Example (as JSON)

```json
{
  "siteInductionId": 210,
  "siteId": 156,
  "dateExpires": "2016-03-13"
}
```

