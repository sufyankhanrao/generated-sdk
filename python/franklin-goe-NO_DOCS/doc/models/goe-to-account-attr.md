
# Goe to Account Attr

*This model accepts additional fields of type Any.*

## Structure

`GoeToAccountAttr`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `str` | Required | Used to identify an account |
| `account_type` | `str` | Required | Defines the type of account given.                    In the case of TDA and Roth accounts, the possible ‘accountType’ are: “401k” and “IRA”. <br>                    In the case of Taxable account, ‘accountType’ does not exist and this field should be passed as null. <br>                    In future releases, the recommendations would be tuned to the ‘accountType’. |
| `taxability_type` | `str` | Required | Defines the nature of the account. <br>                        “T”: taxable account <br>                        “D”: tax deferred account <br>                        “F”: Roth account |
| `member_i_ds` | `List[str]` | Required | List of member IDs that have claim over a single account. <br>                        It is recommended to have an aggregated “taxable” account for all members in the household. <br>                        In casethe case of tda / roth accounts, different members of a household can have different accounts. <br>                        For MVP, exactly one member should be passed in the request payload. |
| `current_balance` | `int` | Required | Account balance as of the current date |
| `current_holdings` | [`List[GoeToCategory]`](../../doc/models/goe-to-category.md) | Required | Details of the holdings in an account |
| `cashflow_details` | [`GoeToCashflowDetails2`](../../doc/models/goe-to-cashflow-details-2.md) | Required | Details of infusions i.e., money deposited in an account |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "accountID": "5",
  "accountType": "401k",
  "taxabilityType": "T",
  "memberIDs": [
    "memberIDs2",
    "memberIDs3"
  ],
  "currentBalance": 14589,
  "currentHoldings": [
    {
      "categoryName": "CASH",
      "categoryID": "10",
      "categoryPrice": 1.0,
      "quantity": 14589.0,
      "costBasis": 14589.0,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "cashflowDetails": {
    "startDate": "01-03-2024",
    "endDate": "01-11-2032",
    "cashflowAmt": [
      237.45
    ],
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

