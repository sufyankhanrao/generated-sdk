
# Terminal for Update

## Structure

`TerminalForUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customizations` | [`List[Customization]`](../../doc/models/customization.md) | Optional | Only Auto-Close Time and Auto-Close Type can be updated. The following are the name value pair formats that are allowed.<br><br>a) name = Auto-Close Time<br>value = '0430'<br><br>b) name = Auto-Close<br>value = 'T'<br><br>    T- Terminal Auto Close. The Auto Close Time will occur in relation to the time on the terminal itself<br><br>c) name = Auto-Close<br>value = 'H'<br><br>    H - Host Auto Close. The Auto Close Time will occur according to Eastern Standard Time (EST)<br><br>d) name = Auto-Close<br>value = 'N'<br><br>    The Auto Close Time option is off, and the terminal will NOT auto close no matter that time set for Auto Close Time |

## Example (as JSON)

```json
{
  "customizations": [
    {
      "name": "name2",
      "value": "value4"
    },
    {
      "name": "name2",
      "value": "value4"
    }
  ]
}
```

