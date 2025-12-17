
# Scan Data

## Structure

`ScanData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vulnerability_scan_required` | `bool` | Required | vulnerabilityScanningRequired true or false |
| `last_scan_date` | `str` | Required | Last PCI Scan Date<br><br>**Constraints**: *Maximum Length*: `10` |
| `pci_validated` | [`PciValidatedEnum`](../../doc/models/pci-validated-enum.md) | Required | Pci Validated status<br><br>**Constraints**: *Maximum Length*: `15` |
| `pci_validated_date` | `str` | Required | PCI Validated Date<br><br>**Constraints**: *Maximum Length*: `10` |
| `pci_scan_status` | [`PciScanStatusEnum`](../../doc/models/pci-scan-status-enum.md) | Optional | Pci scan status, Y-passed, F-failed,I-In-progress, X-Not started<br><br>**Constraints**: *Maximum Length*: `15` |

## Example (as JSON)

```json
{
  "vulnerabilityScanRequired": false,
  "lastScanDate": "lastScanDate0",
  "pciValidated": "COMPLIANT",
  "pciValidatedDate": "pciValidatedDate8",
  "pciScanStatus": "INCOMPLETE"
}
```

