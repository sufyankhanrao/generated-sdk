
# Statement of Account Response

## Structure

`StatementOfAccountResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | Unique request identifier passed from end user. This identifier helps in tracing a transaction |
| `status` | `str` | Optional | Indicates overall status of the request. Allowed values: SUCCES, FAILED |
| `data` | [`List[StatementOfAccountResp]`](../../doc/models/statement-of-account-resp.md) | Optional | - |

## Example (as JSON)

```json
{
  "RequestId": "RequestId8",
  "Status": "Status4",
  "Data": [
    {
      "LastStatementOfAccount": {
        "AmountDue": 220.3,
        "AmountNotOverdue": 42.96,
        "AmountOverdue": 58.04,
        "CreditLimit": 162,
        "CreditLimitCurrencyCode": "CreditLimitCurrencyCode4"
      },
      "MonthlyInvoiceTrend": [
        {
          "CurrencyCode": "CurrencyCode8",
          "CurrencySymbol": "CurrencySymbol4",
          "Month": 36,
          "TotalNetAmount": 98.02,
          "TotalVATAmount": 158.14
        }
      ],
      "PastStatementOfAccounts": [
        {
          "AmountDue": 208.8,
          "AmountNotOverdue": 54.46,
          "AmountOverdue": 69.54,
          "AmountOverdueFromUnallocated": 130.1,
          "AmountPaid": 138.64
        }
      ],
      "PaymentsSinceLastSOA": [
        {
          "AccountId": 0,
          "AccountNumber": "AccountNumber4",
          "AccountShortName": "AccountShortName6",
          "SummaryDocumentId": 92,
          "SummaryDocumentNumber": "SummaryDocumentNumber8"
        },
        {
          "AccountId": 0,
          "AccountNumber": "AccountNumber4",
          "AccountShortName": "AccountShortName6",
          "SummaryDocumentId": 92,
          "SummaryDocumentNumber": "SummaryDocumentNumber8"
        },
        {
          "AccountId": 0,
          "AccountNumber": "AccountNumber4",
          "AccountShortName": "AccountShortName6",
          "SummaryDocumentId": 92,
          "SummaryDocumentNumber": "SummaryDocumentNumber8"
        }
      ],
      "InvoicesSummaries": [
        {
          "AmountDue": 132.62,
          "AmountNotOverdue": 125.36,
          "AmountOverdue": 110.28,
          "AmountPaid": 62.46,
          "BillingCurrencyCode": "BillingCurrencyCode0"
        },
        {
          "AmountDue": 132.62,
          "AmountNotOverdue": 125.36,
          "AmountOverdue": 110.28,
          "AmountPaid": 62.46,
          "BillingCurrencyCode": "BillingCurrencyCode0"
        }
      ]
    },
    {
      "LastStatementOfAccount": {
        "AmountDue": 220.3,
        "AmountNotOverdue": 42.96,
        "AmountOverdue": 58.04,
        "CreditLimit": 162,
        "CreditLimitCurrencyCode": "CreditLimitCurrencyCode4"
      },
      "MonthlyInvoiceTrend": [
        {
          "CurrencyCode": "CurrencyCode8",
          "CurrencySymbol": "CurrencySymbol4",
          "Month": 36,
          "TotalNetAmount": 98.02,
          "TotalVATAmount": 158.14
        }
      ],
      "PastStatementOfAccounts": [
        {
          "AmountDue": 208.8,
          "AmountNotOverdue": 54.46,
          "AmountOverdue": 69.54,
          "AmountOverdueFromUnallocated": 130.1,
          "AmountPaid": 138.64
        }
      ],
      "PaymentsSinceLastSOA": [
        {
          "AccountId": 0,
          "AccountNumber": "AccountNumber4",
          "AccountShortName": "AccountShortName6",
          "SummaryDocumentId": 92,
          "SummaryDocumentNumber": "SummaryDocumentNumber8"
        },
        {
          "AccountId": 0,
          "AccountNumber": "AccountNumber4",
          "AccountShortName": "AccountShortName6",
          "SummaryDocumentId": 92,
          "SummaryDocumentNumber": "SummaryDocumentNumber8"
        },
        {
          "AccountId": 0,
          "AccountNumber": "AccountNumber4",
          "AccountShortName": "AccountShortName6",
          "SummaryDocumentId": 92,
          "SummaryDocumentNumber": "SummaryDocumentNumber8"
        }
      ],
      "InvoicesSummaries": [
        {
          "AmountDue": 132.62,
          "AmountNotOverdue": 125.36,
          "AmountOverdue": 110.28,
          "AmountPaid": 62.46,
          "BillingCurrencyCode": "BillingCurrencyCode0"
        },
        {
          "AmountDue": 132.62,
          "AmountNotOverdue": 125.36,
          "AmountOverdue": 110.28,
          "AmountPaid": 62.46,
          "BillingCurrencyCode": "BillingCurrencyCode0"
        }
      ]
    },
    {
      "LastStatementOfAccount": {
        "AmountDue": 220.3,
        "AmountNotOverdue": 42.96,
        "AmountOverdue": 58.04,
        "CreditLimit": 162,
        "CreditLimitCurrencyCode": "CreditLimitCurrencyCode4"
      },
      "MonthlyInvoiceTrend": [
        {
          "CurrencyCode": "CurrencyCode8",
          "CurrencySymbol": "CurrencySymbol4",
          "Month": 36,
          "TotalNetAmount": 98.02,
          "TotalVATAmount": 158.14
        }
      ],
      "PastStatementOfAccounts": [
        {
          "AmountDue": 208.8,
          "AmountNotOverdue": 54.46,
          "AmountOverdue": 69.54,
          "AmountOverdueFromUnallocated": 130.1,
          "AmountPaid": 138.64
        }
      ],
      "PaymentsSinceLastSOA": [
        {
          "AccountId": 0,
          "AccountNumber": "AccountNumber4",
          "AccountShortName": "AccountShortName6",
          "SummaryDocumentId": 92,
          "SummaryDocumentNumber": "SummaryDocumentNumber8"
        },
        {
          "AccountId": 0,
          "AccountNumber": "AccountNumber4",
          "AccountShortName": "AccountShortName6",
          "SummaryDocumentId": 92,
          "SummaryDocumentNumber": "SummaryDocumentNumber8"
        },
        {
          "AccountId": 0,
          "AccountNumber": "AccountNumber4",
          "AccountShortName": "AccountShortName6",
          "SummaryDocumentId": 92,
          "SummaryDocumentNumber": "SummaryDocumentNumber8"
        }
      ],
      "InvoicesSummaries": [
        {
          "AmountDue": 132.62,
          "AmountNotOverdue": 125.36,
          "AmountOverdue": 110.28,
          "AmountPaid": 62.46,
          "BillingCurrencyCode": "BillingCurrencyCode0"
        },
        {
          "AmountDue": 132.62,
          "AmountNotOverdue": 125.36,
          "AmountOverdue": 110.28,
          "AmountPaid": 62.46,
          "BillingCurrencyCode": "BillingCurrencyCode0"
        }
      ]
    }
  ]
}
```

