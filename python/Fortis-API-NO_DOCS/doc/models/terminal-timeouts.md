
# Terminal Timeouts

The following options outlines some configurable timeout values that can be used to customize the experience at the terminal for the cardholder.

## Structure

`TerminalTimeouts`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_entry_timeout` | `int` | Optional | How long to wait for input from cardholder.<br><br>**Default**: `120`<br><br>**Constraints**: `>= 20`, `<= 120` |
| `device_terms_prompt_timeout` | `int` | Optional | How long the terms will be displayed on the device.<br><br>**Default**: `60`<br><br>**Constraints**: `>= 5`, `<= 300` |
| `overall_timeout` | `int` | Optional | How long to wait for response from /v2/routertransactions endpoint.<br><br>**Default**: `300`<br><br>**Constraints**: `>= 30`, `<= 300` |
| `pin_entry_timeout` | `int` | Optional | How long to wait for pin entry by cardholder.<br><br>**Default**: `30`<br><br>**Constraints**: `>= 20`, `<= 50` |
| `signature_input_timeout` | `int` | Optional | How long to wait for first "touch" to signature.<br><br>**Default**: `10`<br><br>**Constraints**: `>= 10`, `<= 50` |
| `signature_submit_timeout` | `int` | Optional | How long to wait for signature to be submitted.<br><br>**Default**: `30`<br><br>**Constraints**: `>= 20`, `<= 50` |
| `status_display_time` | `int` | Optional | How long the approve/decline status message stays on screen.<br><br>**Default**: `7`<br><br>**Constraints**: `>= 1`, `<= 30` |
| `tip_cashback_timeout` | `int` | Optional | How long to wait for input on a tip or cashback screen.<br><br>**Default**: `30`<br><br>**Constraints**: `>= 20`, `<= 50` |
| `transaction_timeout` | `int` | Optional | How long to wait for response from the processor.<br><br>**Default**: `10`<br><br>**Constraints**: `>= 10`, `<= 20` |

## Example (as JSON)

```json
{
  "card_entry_timeout": 47,
  "device_terms_prompt_timeout": 30,
  "overall_timeout": 125,
  "pin_entry_timeout": 40,
  "signature_input_timeout": 35,
  "signature_submit_timeout": 38,
  "status_display_time": 12,
  "tip_cashback_timeout": 25,
  "transaction_timeout": 17
}
```

