
# Fleetmanagement V1 User Loggedinuser Request

## Structure

`FleetmanagementV1UserLoggedinuserRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `include_payer_group` | `bool` | Optional | True/False. The output will include the payer group information only when true is passed.<br><br>**Default**: `False` |
| `include_eid_details` | `bool` | Optional | True/False. The output will include the EID (Electronic Invoice data) information only when true is passed..<br><br>**Default**: `False` |
| `requested_api_name` | `str` | Optional | Name of the API on which user access needs to be validated<br>Optional. |
| `payer_id` | `int` | Optional | Payer id of the customer.</br><br>Optional.</br><br>This input is a search criterion.</br><br>Note: If PayerId or PayerNumber is provided in the input, the given payer will be available in the output if the user has access to the given payer. |
| `payer_number` | `str` | Optional | PayerNumber of the customer.</br><br>Optional</br><br>This input is a search criterion.</br><br>Note: If Payerid or PayerNumber is provided in the input, the given payer will be available in the output if the user has access to the given payer. |

## Example (as JSON)

```json
{
  "IncludePayerGroup": false,
  "IncludeEIDDetails": false,
  "RequestedAPIName": "Name of the API",
  "PayerId": 123456,
  "PayerNumber": "GB00123456"
}
```

