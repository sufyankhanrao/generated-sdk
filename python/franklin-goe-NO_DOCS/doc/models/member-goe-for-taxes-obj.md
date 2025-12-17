
# Member Goe for Taxes Obj

*This model accepts additional fields of type Any.*

## Structure

`MemberGoeForTaxesObj`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `member_type` | [`MemberType`](../../doc/models/member-type.md) | Required | Indicates the importance of member of to a household.             Usually, a higher earning member is assigned as “Primary” member. |
| `member_id` | `str` | Required | Identifier unique to each member of the household |
| `dob` | `str` | Required | Date of birth of a member in the household. <br>                    Used for checking early withdrawal possibility from                     the retirement accounts & the Social Security calculations. <br>                    Valid input format is date: MM-YYYY |
| `current_age` | `int` | Required | Current age of the household member |
| `retirement_age` | `int` | Required | Retirement age of the household member |
| `current_salary` | `float` | Required | Current salary of the household member.                        Used for Social Security calculations |
| `social_security_start_age` | `int` | Required | Custom age at which the member wishes to receive her Social Security benefits |
| `tda_balance_for_rmd` | `float` | Optional | The previous year’s ending TDA account balance that canbe used to compute the first year’s RMD value. <br>                    Can be ignored and removed from the payload no info is available. GOE will consider the current TDA account balance as a proxy |
| `rmd_utilized` | `float` | Optional | In the event the RMD computations are desired for the current financial year,                     this field specifies the amount of RMD already taken out before the GOE call was made. <br>                    Can be ignored removed from the payload if not applicable |
| `existing_monthly_social_security_amount` | `float` | Optional | In the event when the user is already receiving the SS amount and             their ‘currentAge’ is greater than the ‘socialSecurityStartAge’, <br>            they should not use the Social Security income calculator and can simply mention that monthly amount in this parameter. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "memberType": "Primary",
  "memberID": "memberID6",
  "DOB": "DOB6",
  "currentAge": 55,
  "retirementAge": 76,
  "currentSalary": 111.84,
  "socialSecurityStartAge": 62,
  "RMDUtilized": 2000.0,
  "existingMonthlySocialSecurityAmount": 1000.0,
  "TDABalanceForRMD": 239.86,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

