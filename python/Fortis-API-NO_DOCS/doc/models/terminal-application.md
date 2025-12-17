
# Terminal Application

Terminal Application Information on `expand`

## Structure

`TerminalApplication`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `standalone` | `bool` | Optional | Standalone |
| `emv_capable` | `bool` | Optional | Emv Capable |
| `nfc_capable` | `bool` | Optional | Nfc Capable |
| `pin_capable` | `bool` | Optional | Pin Capable |
| `print_capable` | `bool` | Optional | Print Capable |
| `msr_capable` | `bool` | Optional | Msr Capable |
| `sig_capture_capable` | `bool` | Optional | Sig Capture Capable |
| `mpos_terminal` | `bool` | Optional | Mpos Terminal |
| `title` | `str` | Optional | Title<br><br>**Constraints**: *Maximum Length*: `48` |
| `description` | `str` | Optional | Description<br><br>**Constraints**: *Maximum Length*: `256` |
| `id` | `str` | Optional | Terminal Application Id<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `modified_ts` | `int` | Optional | Modified Time Stamp |
| `created_user_id` | `str` | Optional | User ID Created the register<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |

## Example (as JSON)

```json
{
  "standalone": true,
  "emv_capable": true,
  "nfc_capable": false,
  "pin_capable": true,
  "print_capable": false,
  "msr_capable": true,
  "sig_capture_capable": false,
  "mpos_terminal": false,
  "title": "Ingenico Link2500",
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "created_ts": 1422040992,
  "modified_ts": 1422040992,
  "created_user_id": "11e95f8ec39de8fbdb0a4f1a"
}
```

