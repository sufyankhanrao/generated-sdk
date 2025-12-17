
# List 13

## Structure

`List13`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Optional | Location ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `default_product_transaction_id` | `str` | Optional | Product Transaction ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `terminal_application_id` | `str` | Optional | Terminal Application ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `terminal_cvm_id` | `str` | Optional | Terminal CVM ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `terminal_manufacturer_code` | [`TerminalManufacturerCodeEnum`](../../doc/models/terminal-manufacturer-code-enum.md) | Optional | Terminal Manufacturer Code |
| `title` | `str` | Optional | Terminal Name<br><br>**Constraints**: *Maximum Length*: `24` |
| `mac_address` | `str` | Optional | Terminal MAC Address<br><br>**Constraints**: *Pattern*: `^([0-9a-fA-F]{2}[:-]?){5}([0-9a-fA-F]{2})$` |
| `local_ip_address` | `str` | Optional | Terminal Local IP Address |
| `port` | `int` | Optional | Terminal Port<br><br>**Default**: `10009`<br><br>**Constraints**: `>= 0`, `<= 65535` |
| `serial_number` | `str` | Optional | Terminal Serial Number<br><br>**Constraints**: *Maximum Length*: `24`, *Pattern*: `^[a-zA-Z0-9]*$` |
| `terminal_number` | `str` | Optional | Terminal Number<br><br>**Constraints**: *Minimum Length*: `15`, *Maximum Length*: `15` |
| `terminal_timeouts` | [`TerminalTimeouts`](../../doc/models/terminal-timeouts.md) | Optional | The following options outlines some configurable timeout values that can be used to customize the experience at the terminal for the cardholder. |
| `tip_percents` | [`TipPercents`](../../doc/models/tip-percents.md) | Optional | A JSON of tip percents the JSON MUST contain only these three fields: percent_1, percent_2, percent_3 |
| `location_api_id` | `str` | Optional | Location Api ID<br><br>**Constraints**: *Maximum Length*: `64` |
| `terminal_api_id` | `str` | Optional | Terminal Api ID<br><br>**Constraints**: *Maximum Length*: `64` |
| `header_line_1` | `str` | Optional | Header Line 1<br><br>**Constraints**: *Maximum Length*: `32` |
| `header_line_2` | `str` | Optional | Header Line 2<br><br>**Constraints**: *Maximum Length*: `32` |
| `header_line_3` | `str` | Optional | Header Line 3<br><br>**Constraints**: *Maximum Length*: `32` |
| `header_line_4` | `str` | Optional | Header Line 4<br><br>**Constraints**: *Maximum Length*: `32` |
| `header_line_5` | `str` | Optional | Header Line 5<br><br>**Constraints**: *Maximum Length*: `32` |
| `trailer_line_1` | `str` | Optional | Trailer Line 1<br><br>**Constraints**: *Maximum Length*: `32` |
| `trailer_line_2` | `str` | Optional | Trailer Line 2<br><br>**Constraints**: *Maximum Length*: `32` |
| `trailer_line_3` | `str` | Optional | Trailer Line 3<br><br>**Constraints**: *Maximum Length*: `32` |
| `trailer_line_4` | `str` | Optional | Trailer Line 4<br><br>**Constraints**: *Maximum Length*: `32` |
| `trailer_line_5` | `str` | Optional | Trailer Line 5<br><br>**Constraints**: *Maximum Length*: `32` |
| `default_checkin` | `str` | Optional | Default Checkin<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[\d]{4}-[\d]{2}-[\d]{2}$` |
| `default_checkout` | `str` | Optional | Default Checkout<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[\d]{4}-[\d]{2}-[\d]{2}$` |
| `default_room_rate` | `int` | Optional | Default Room Rate<br><br>**Constraints**: `>= 0`, `<= 100` |
| `default_room_number` | `str` | Optional | Default Room Number<br><br>**Constraints**: *Maximum Length*: `12` |
| `debit` | `bool` | Optional | Debit |
| `emv` | `bool` | Optional | EMV |
| `cashback_enable` | `bool` | Optional | Cashback Enable |
| `print_enable` | `bool` | Optional | Print Enable |
| `sig_capture_enable` | `bool` | Optional | Sig Capture Enable |
| `is_provisioned` | `bool` | Optional | Is Provisioned |
| `tip_enable` | `bool` | Optional | Tip Enable |
| `validated_decryption` | `bool` | Optional | Validated Decryption |
| `communication_type` | [`CommunicationTypeEnum`](../../doc/models/communication-type-enum.md) | Optional | Communication Type |
| `active` | `bool` | Optional | Active |
| `id` | `str` | Optional | Terminal ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `created_ts` | `int` | Optional | Created Time Stamp |
| `modified_ts` | `int` | Optional | Modified Time Stamp |
| `last_registration_ts` | `int` | Optional | Modified Time Stamp |
| `created_user_id` | `str` | Optional | User ID Created the register<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `modified_user_id` | `str` | Optional | Last User ID that updated the register<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `location` | [`Location`](../../doc/models/location.md) | Optional | Location Information on `expand` |
| `created_user` | [`CreatedUser`](../../doc/models/created-user.md) | Optional | User Information on `expand` |
| `terminal_application` | [`TerminalApplication`](../../doc/models/terminal-application.md) | Optional | Terminal Application Information on `expand` |
| `changelogs` | [`List[Changelog]`](../../doc/models/changelog.md) | Optional | Changelog Information on `expand` |
| `terminal_routers` | [`List[TerminalRouter]`](../../doc/models/terminal-router.md) | Optional | Terminal Router Information on `expand` |
| `has_terminal_routers` | `bool` | Optional | Has Terminal Router Information on `expand` |
| `terminal_cvm` | [`TerminalCvm`](../../doc/models/terminal-cvm.md) | Optional | Terminal Cvm Information on `expand` |
| `terminal_manufacturer` | [`TerminalManufacturer`](../../doc/models/terminal-manufacturer.md) | Optional | Terminal Manufacturer Information on `expand` |

## Example (as JSON)

```json
{
  "location_id": "11e95f8ec39de8fbdb0a4f1a",
  "default_product_transaction_id": "11e95f8ec39de8fbdb0a4f1a",
  "terminal_application_id": "11e95f8ec39de8fbdb0a4f1a",
  "terminal_cvm_id": "11e95f8ec39de8fbdb0a4f1a",
  "terminal_manufacturer_code": "1",
  "title": "My terminal",
  "mac_address": "3D:F2:C9:A6:B3:4F",
  "local_ip_address": "192.168.0.10",
  "port": 10009,
  "serial_number": "1234567890",
  "terminal_number": "973456789012367",
  "header_line_1": "line 1 sample",
  "header_line_2": "line 2 sample",
  "header_line_3": "line 3 sample",
  "header_line_4": "line 4 sample",
  "header_line_5": "line 5 sample",
  "trailer_line_1": "trailer 1 sample",
  "trailer_line_2": "trailer 2 sample",
  "trailer_line_3": "trailer 3 sample",
  "trailer_line_4": "trailer 4 sample",
  "trailer_line_5": "trailer 5 sample",
  "default_checkin": "2021-12-01",
  "default_checkout": "2021-12-01",
  "default_room_rate": 56,
  "default_room_number": "303",
  "debit": false,
  "emv": false,
  "cashback_enable": false,
  "print_enable": false,
  "sig_capture_enable": false,
  "is_provisioned": false,
  "tip_enable": false,
  "validated_decryption": false,
  "communication_type": "http",
  "active": true,
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "created_ts": 1422040992,
  "modified_ts": 1422040992,
  "last_registration_ts": 1422040992,
  "created_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "modified_user_id": "11e95f8ec39de8fbdb0a4f1a",
  "has_terminal_routers": true
}
```

