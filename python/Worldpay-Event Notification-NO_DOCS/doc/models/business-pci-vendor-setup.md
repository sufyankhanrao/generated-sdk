
# Business Pci Vendor Setup

This aggregate field includes PCI Setup related data

## Structure

`BusinessPciVendorSetup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email_suppression_indicator` | `bool` | Optional | Indicator for Email Suppression |
| `group_id` | `str` | Optional | Group identifier<br><br>**Constraints**: *Maximum Length*: `30` |
| `level` | `float` | Optional | Level for PCI Vendor Setup |
| `sponsor` | [`BusinessPciVendorSetupSponsor`](../../doc/models/business-pci-vendor-setup-sponsor.md) | Optional | This aggregate field includes PCI Setup related data for sponsor |

## Example (as JSON)

```json
{
  "emailSuppressionIndicator": false,
  "groupId": "121216543",
  "level": 4.0,
  "sponsor": {
    "code": "code8",
    "description": "description0"
  }
}
```

