
# Summary Account Number

## Structure

`SummaryAccountNumber`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationResponse1`](../../doc/models/pagination-response-1.md) | Optional | Used for pagination. |
| `total_credits_count` | `int` | Optional | Indicates the total count of credit sales over a given period of time.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `total_credited_amount` | `float` | Optional | Indicates the total amount of credit sales over a given period of time.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_debits_count` | `int` | Optional | Indicates the total count of debit sales over a given period of time.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `total_debited_amount` | `float` | Optional | Indicates the total amount of credit sales over a given period of time.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_net_amount` | `float` | Optional | Refers to the Amount left over after all deductions are made.<br><br>totalNetAmount= totalCreditedAmount - totalDebitedAmount.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `summaries` | [`List[Summary61]`](../../doc/models/summary-61.md) | Optional | - |

## Example (as JSON)

```json
{
  "totalCreditsCount": 7346,
  "totalCreditedAmount": 2353785.11,
  "totalDebitsCount": 3574,
  "totalDebitedAmount": 84464.28,
  "totalNetAmount": 2269320.83,
  "pagination": {
    "pageNumber": 16776215,
    "pageSize": 1000,
    "totalRowCount": 9999998999,
    "totalReturnedCount": 9999998999
  }
}
```

