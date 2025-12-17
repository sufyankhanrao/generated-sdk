
# Ui Prefs

Ui Prefs

## Structure

`UiPrefs`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entry_page` | `str` | Optional | Ui Prefs Entry Page |
| `page_size` | `int` | Optional | Ui Prefs Page Size<br><br>**Constraints**: `>= 0`, `<= 99` |
| `report_export_type` | [`ReportExportTypeEnum`](../../doc/models/report-export-type-enum.md) | Optional | Ui Prefs Export Type |
| `process_method` | [`ProcessMethodEnum`](../../doc/models/process-method-enum.md) | Optional | Ui Prefs Process Method |
| `default_terminal` | `str` | Optional | Ui Prefs Default Termianl<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |

## Example (as JSON)

```json
{
  "entry_page": "dashboard",
  "page_size": 2,
  "report_export_type": "csv",
  "process_method": "virtual_terminal",
  "default_terminal": "11e95f8ec39de8fbdb0a4f1a"
}
```

