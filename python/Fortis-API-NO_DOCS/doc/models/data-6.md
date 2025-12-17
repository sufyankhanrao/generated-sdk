
# Data 6

## Structure

`Data6`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Optional | Location ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `terminal_id` | `str` | Optional | Terminal ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `require_signature` | `bool` | Optional | Set to true or 1 to require a signature from the customer |
| `device_term_api_id` | `str` | Optional | Can be used for associating record to external systems. Must be unique per location.<br><br>**Constraints**: *Maximum Length*: `64` |
| `terms_conditions` | `str` | Optional | This is the message that is displayed on the screen when prompting for a signature.<br><br>**Constraints**: *Maximum Length*: `4096` |
| `id` | `str` | Optional | Device term ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `reason_code_id` | `int` | Optional | Reason code ID |
| `signature` | [`Signature`](../../doc/models/signature.md) | Optional | Signature Information on `expand` |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `modified_ts` | `int` | Optional | Modified Time Stamp |
| `created_user_id` | `str` | Optional | System generated id for user who created record<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `created_user` | [`CreatedUser`](../../doc/models/created-user.md) | Optional | User Information on `expand` |
| `location` | [`Location`](../../doc/models/location.md) | Optional | Location Information on `expand` |
| `terminal` | [`Terminal`](../../doc/models/terminal.md) | Optional | Terminal Information on `expand` |
| `changelogs` | [`List[Changelog]`](../../doc/models/changelog.md) | Optional | Changelog Information on `expand` |
| `reason_code` | [`ReasonCode`](../../doc/models/reason-code.md) | Optional | Reason Code Information on `expand` |

## Example (as JSON)

```json
{
  "location_id": "11e95f8ec39de8fbdb0a4f1a",
  "terminal_id": "11e95f8ec39de8fbdb0a4f1a",
  "require_signature": true,
  "device_term_api_id": "device_term134",
  "terms_conditions": "FUNgib0Vh0B9c0Wbttvr50vNtGLOkTdFL0eFmhN1RJpKhK14IENeDa8irp2dEk9thEcVHvVEyriQeZLs5NjNsCzqNj9JDA4RSJwK647IFtYjrNPN1nBb9bw6hoQ71oT5kpsiXGt8HcqBFVBVeDA7psIzKAyDveAw2o1hfjipkOtXrPgWun0rYwyyFuvqkT1egQYKfYDj",
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "reason_code_id": 1000,
  "created_ts": 1422040992,
  "modified_ts": 1422040992,
  "created_user_id": "11e95f8ec39de8fbdb0a4f1a"
}
```

