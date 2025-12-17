
# Tax Data

Tax data container for API requests and responses

*This model accepts additional fields of type Any.*

## Structure

`TaxData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `business_income_statement` | [`BusinessIncomeStatement`](../../doc/models/business-income-statement.md) | Optional | Business Income Statement for IRS Form 1040 Schedule C |
| `cryptocurrency_tax_statement` | [`CryptocurrencyTaxStatementList`](../../doc/models/cryptocurrency-tax-statement-list.md) | Optional | Cryptocurrency Tax Statement list |
| `farm_income_statement` | [`FarmIncomeStatement`](../../doc/models/farm-income-statement.md) | Optional | Farm Income Statement for IRS Form 1040 Schedule F |
| `farm_rental_income_statement` | [`FarmRentalIncomeStatement`](../../doc/models/farm-rental-income-statement.md) | Optional | Farm Rental Income Statement for IRS Form 4835 |
| `rental_income_statement` | [`RentalIncomeStatement`](../../doc/models/rental-income-statement.md) | Optional | Rental Income Statement for IRS Form 1040 Schedule E |
| `royalty_income_statement` | [`RoyaltyIncomeStatement`](../../doc/models/royalty-income-statement.md) | Optional | Royalty Income Statement for IRS Form 1040 Schedule E |
| `tax_1041_k_1` | [`Form1041K1`](../../doc/models/form-1041-k1.md) | Optional | Beneficiary's Share of Income, Deductions, Credits, etc. |
| `tax_1042_s` | [`Form1042S`](../../doc/models/form-1042-s.md) | Optional | Foreign Person's U.S. Source Income Subject to Withholding |
| `tax_1065_k_1` | [`Form1065K1`](../../doc/models/form-1065-k1.md) | Optional | Partner's Share of Income, Deductions, Credits, etc. |
| `tax_1095_a` | [`Form1095A`](../../doc/models/form-1095-a.md) | Optional | Health Insurance Marketplace Statement |
| `tax_1095_b` | [`Form1095B`](../../doc/models/form-1095-b.md) | Optional | Health Coverage |
| `tax_1095_c` | [`Form1095C`](../../doc/models/form-1095-c.md) | Optional | Employer-Provided Health Insurance Offer and Coverage |
| `tax_1097_btc` | [`Form1097Btc`](../../doc/models/form-1097-btc.md) | Optional | Bond Tax Credit |
| `tax_1098` | [`Form1098`](../../doc/models/form-1098.md) | Optional | Mortgage Interest Statement |
| `tax_1098_c` | [`Form1098C`](../../doc/models/form-1098-c.md) | Optional | Contributions of Motor Vehicles, Boats, and Airplanes |
| `tax_1098_e` | [`Form1098E`](../../doc/models/form-1098-e.md) | Optional | Student Loan Interest Statement |
| `tax_1098_ma` | [`Form1098Ma`](../../doc/models/form-1098-ma.md) | Optional | Mortgage Assistance Payments |
| `tax_1098_q` | [`Form1098Q`](../../doc/models/form-1098-q.md) | Optional | Qualifying Longevity Annuity Contract Information |
| `tax_1098_t` | [`Form1098T`](../../doc/models/form-1098-t.md) | Optional | Tuition Statement |
| `tax_1099_a` | [`Form1099A`](../../doc/models/form-1099-a.md) | Optional | Acquisition or Abandonment of Secured Property |
| `tax_1099_b` | [`Form1099B`](../../doc/models/form-1099-b.md) | Optional | Proceeds From Broker and Barter Exchange Transactions |
| `tax_1099_c` | [`Form1099C`](../../doc/models/form-1099-c.md) | Optional | Cancellation of Debt |
| `tax_1099_cap` | [`Form1099Cap`](../../doc/models/form-1099-cap.md) | Optional | Changes in Corporate Control and Capital Structure |
| `tax_1099_consolidated_statement` | [`Form1099ConsolidatedStatement`](../../doc/models/form-1099-consolidated-statement.md) | Optional | Consolidated Statement for combined IRS Form 1099s |
| `tax_1099_div` | [`Form1099Div`](../../doc/models/form-1099-div.md) | Optional | Dividends and Distributions |
| `tax_1099_g` | [`Form1099G`](../../doc/models/form-1099-g.md) | Optional | Certain Government Payments |
| `tax_1099_h` | [`Form1099H`](../../doc/models/form-1099-h.md) | Optional | Health Coverage Tax Credit (HCTC) Advance Payments |
| `tax_1099_int` | [`Form1099Int`](../../doc/models/form-1099-int.md) | Optional | Interest Income |
| `tax_1099_k` | [`Form1099K`](../../doc/models/form-1099-k.md) | Optional | Merchant Card and Third-Party Network Payments |
| `tax_1099_ls` | [`Form1099Ls`](../../doc/models/form-1099-ls.md) | Optional | Reportable Life Insurance Sale |
| `tax_1099_ltc` | [`Form1099Ltc`](../../doc/models/form-1099-ltc.md) | Optional | Long-Term Care and Accelerated Death Benefits |
| `tax_1099_misc` | [`Form1099Misc`](../../doc/models/form-1099-misc.md) | Optional | Miscellaneous Income |
| `tax_1099_nec` | [`Form1099Nec`](../../doc/models/form-1099-nec.md) | Optional | Non-Employee Compensation |
| `tax_1099_oid` | [`Form1099Oid`](../../doc/models/form-1099-oid.md) | Optional | Original Issue Discount |
| `tax_1099_patr` | [`Form1099Patr`](../../doc/models/form-1099-patr.md) | Optional | Taxable Distributions Received From Cooperatives |
| `tax_1099_q` | [`Form1099Q`](../../doc/models/form-1099-q.md) | Optional | Payments From Qualified Education Programs |
| `tax_1099_qa` | [`Form1099Qa`](../../doc/models/form-1099-qa.md) | Optional | Distributions From ABLE Accounts |
| `tax_1099_r` | [`Form1099R`](../../doc/models/form-1099-r.md) | Optional | Distributions from Pensions, Annuities, Retirement or Profit-Sharing Plans, IRAs, Insurance Contracts, etc. |
| `tax_1099_s` | [`Form1099S`](../../doc/models/form-1099-s.md) | Optional | Proceeds From Real Estate Transactions |
| `tax_1099_sa` | [`Form1099Sa`](../../doc/models/form-1099-sa.md) | Optional | Distributions From an HSA, Archer MSA, or Medicare Advantage MSA |
| `tax_1099_sb` | [`Form1099Sb`](../../doc/models/form-1099-sb.md) | Optional | Seller's Investment in Life Insurance Contract |
| `tax_1120_sk_1` | [`Form1120Sk1`](../../doc/models/form-1120-sk1.md) | Optional | Shareholder's Share of Income, Deductions, Credits, etc. |
| `tax_2439` | [`Form2439`](../../doc/models/form-2439.md) | Optional | Notice to Shareholder of Undistributed Long-Term Capital Gains |
| `tax_3921` | [`Form3921`](../../doc/models/form-3921.md) | Optional | Exercise of an Incentive Stock Option Under Section 422(b) |
| `tax_3922` | [`Form3922`](../../doc/models/form-3922.md) | Optional | Transfer of Stock Acquired Through an Employee Stock Purchase Plan under Section 423(c) |
| `tax_5227_k_1` | [`Form1041K1`](../../doc/models/form-1041-k1.md) | Optional | Split-Interest Trust Beneficiary's schedule K-1 |
| `tax_5498` | [`Form5498`](../../doc/models/form-5498.md) | Optional | IRA Contribution Information |
| `tax_5498_esa` | [`Form5498Esa`](../../doc/models/form-5498-esa.md) | Optional | Coverdell ESA Contribution Information |
| `tax_5498_qa` | [`Form5498Qa`](../../doc/models/form-5498-qa.md) | Optional | ABLE Account Contribution Information |
| `tax_5498_sa` | [`Form5498Sa`](../../doc/models/form-5498-sa.md) | Optional | HSA, Archer MSA, or Medicare Advantage (MA) MSA Information |
| `tax_w_2` | [`FormW2`](../../doc/models/form-w2.md) | Optional | Wage and Tax Statement |
| `tax_w_2_c` | [`FormW2C`](../../doc/models/form-w2-c.md) | Optional | IRS form W-2c, Corrected Wage and Tax Statement |
| `tax_w_2_g` | [`FormW2G`](../../doc/models/form-w2-g.md) | Optional | Certain Gambling Winnings |
| `tax_refund_direct_deposit` | [`TaxRefundDirectDeposit`](../../doc/models/tax-refund-direct-deposit.md) | Optional | Tax refund direct deposit information |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "businessIncomeStatement": {
    "taxYear": 2018,
    "corrected": false,
    "accountId": "accountId4",
    "taxFormId": "taxFormId2",
    "taxFormDate": "2016-03-13",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "cryptocurrencyTaxStatement": {
    "taxYear": 2018,
    "corrected": false,
    "accountId": "accountId2",
    "taxFormId": "taxFormId0",
    "taxFormDate": "2016-03-13",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "farmIncomeStatement": {
    "taxYear": 2018,
    "corrected": false,
    "accountId": "accountId4",
    "taxFormId": "taxFormId2",
    "taxFormDate": "2016-03-13",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "farmRentalIncomeStatement": {
    "taxYear": 2018,
    "corrected": false,
    "accountId": "accountId8",
    "taxFormId": "taxFormId6",
    "taxFormDate": "2016-03-13",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "rentalIncomeStatement": {
    "taxYear": 2018,
    "corrected": false,
    "accountId": "accountId8",
    "taxFormId": "taxFormId6",
    "taxFormDate": "2016-03-13",
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

