
# Pci Scan Data

## Structure

`PciScanData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vulnerability_scanning_required` | `str` | Optional | Vulnerability Scanning Required<br><br>**Constraints**: *Maximum Length*: `1` |
| `last_scan_date` | `str` | Optional | Last Scan Date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-2]{2}-[0-2]{2}` |
| `pci_validated` | `str` | Optional | pci Validated<br><br>**Constraints**: *Maximum Length*: `1` |
| `pci_validated_date` | `str` | Optional | pci Validated Date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-2]{2}-[0-2]{2}` |

## Example (as JSON)

```json
{
  "vulnerabilityScanningRequired": "N",
  "pciValidated": "N",
  "lastScanDate": "lastScanDate0",
  "pciValidatedDate": "pciValidatedDate8"
}
```

