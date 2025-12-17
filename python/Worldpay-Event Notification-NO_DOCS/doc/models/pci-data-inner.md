
# PCI Data Inner

## Structure

`PCIDataInner`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pci_scan_data` | [`PciScanData`](../../doc/models/pci-scan-data.md) | Optional | Details on PCI Scan Data |
| `saq_data` | [`SaqData`](../../doc/models/saq-data.md) | Optional | Details on SAQ Data |

## Example (as JSON)

```json
{
  "pciScanData": {
    "vulnerabilityScanningRequired": "vulnerabilityScanningRequired0",
    "lastScanDate": "lastScanDate8",
    "pciValidated": "pciValidated6",
    "pciValidatedDate": "pciValidatedDate6"
  },
  "saqData": {
    "type": "type2",
    "status": "status0",
    "completedDate": "completedDate4",
    "statusDate": "statusDate4",
    "nextDueDate": "nextDueDate8"
  }
}
```

