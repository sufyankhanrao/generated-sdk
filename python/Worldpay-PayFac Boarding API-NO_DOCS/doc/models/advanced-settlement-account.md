
# Advanced Settlement Account

Provides information about the various advanced settlement options and associated bank accounts

## Structure

`AdvancedSettlementAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account` | [`BankAccount`](../../doc/models/bank-account.md) | Required | - |
| `settlement_categories` | [`List[SettlementCategoryEnum]`](../../doc/models/settlement-category-enum.md) | Required | Advanced Settlement Category |
| `one_ach_for_all_categories` | [`OneACHForAllCategoriesEnum`](../../doc/models/one-ach-for-all-categories-enum.md) | Optional | Denotes one ACH (Automated Clearing House) item for all categories - Deposits, Chargebacks,ProcessingFees, ConvenienceFees with in a method of payment - Credit and Debit for this adavanced settlement account<br><br>**Default**: `'No'` |
| `one_ach_for_credit_and_debit` | [`OneACHForCreditAndDebitEnum`](../../doc/models/one-ach-for-credit-and-debit-enum.md) | Optional | Denotes one ACH item for credit and debit methods of payment with in a category for this adavanced settlement account<br><br>**Default**: `'No'` |

## Example (as JSON)

```json
{
  "bankAccount": {
    "ddaType": "Checking",
    "accountNumber": "12345678910",
    "routingNumber": "123456789",
    "achType": "CommercialChecking"
  },
  "settlementCategories": [
    "DebitConvenienceFees"
  ],
  "oneACHForAllCategories": "No",
  "oneACHForCreditAndDebit": "No"
}
```

