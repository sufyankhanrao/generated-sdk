
# Household Goe for Taxes Obj 2

contains all information about all the participants.

*This model accepts additional fields of type Any.*

## Structure

`HouseholdGoeForTaxesObj2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `household_id` | `str` | Required | a unique id assigned to the entire household. |
| `state_of_residence` | `str` | Optional | State of residence in United States.                    This is an optional field. |
| `member_list` | [`List[MemberGoeForTaxesObj]`](../../doc/models/member-goe-for-taxes-obj.md) | Required | Contains details about members in the household. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "householdID": "house_1",
  "stateOfResidence": "CA",
  "memberList": [
    {
      "DOB": "12-1968",
      "RMDUtilized": 2000.0,
      "TDABalanceForRMD": 10000.0,
      "currentAge": 55,
      "currentSalary": 50000.0,
      "existingMonthlySocialSecurityAmount": 1000.0,
      "memberID": "1234",
      "memberType": "Primary",
      "retirementAge": 65,
      "socialSecurityStartAge": 62,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

