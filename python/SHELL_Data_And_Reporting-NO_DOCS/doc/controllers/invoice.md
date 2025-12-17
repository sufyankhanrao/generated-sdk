# Invoice

API's for Retrieve and download Invoice details

```python
invoice_controller = client.invoice
```

## Class Name

`InvoiceController`

## Methods

* [Invoice Search](../../doc/controllers/invoice.md#invoice-search)
* [Invoice Summary](../../doc/controllers/invoice.md#invoice-summary)
* [Statement of Account](../../doc/controllers/invoice.md#statement-of-account)
* [Dates](../../doc/controllers/invoice.md#dates)
* [Search Statement of Account](../../doc/controllers/invoice.md#search-statement-of-account)
* [Search Documents](../../doc/controllers/invoice.md#search-documents)
* [Eid Search](../../doc/controllers/invoice.md#eid-search)
* [Download](../../doc/controllers/invoice.md#download)
* [Eid Download](../../doc/controllers/invoice.md#eid-download)


# Invoice Search

This API allows to search invoice data in the Shell Card Platform. It provides flexible search criteria in the request body and supports paging.

This API will also query the relevant invoice documents list and return a reference number that can be used to download invoice documents (PDF and Proofing elements in a zip file).

#### Supported operations

* Search invoices by account
* Search invoices by invoice type or invoice status
* Search invoices by invoice id or number
* Search invoices by invoiced country
* Search invoices including einvoices
* Search invoices by summary document
* Search invoices by statement of account
* Search invoices by fixed and custom date periods

```python
def invoice_search(self,
                  request_id,
                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request.<br><br>**Constraints**: *Minimum Length*: `36`, *Maximum Length*: `36`, *Pattern*: `^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$` |
| `body` | [`InvoiceSearchRequest`](../../doc/models/invoice-search-request.md) | Body, Optional | Invoice Search RequestBody |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceSearchResponse`](../../doc/models/invoice-search-response.md).

## Example Usage

```python
request_id = '2b0cbe11-f109-4c43-9201-49af0370df1c'

body = InvoiceSearchRequest(
    filters=InvoiceSearchRequestFilters(
        col_co_id=14,
        payer_id=78,
        payer_number='DE26688478',
        invoice_id=4013059,
        invoice_number='0123456789',
        from_date='20170830',
        to_date='20171031',
        invoice_date='20171031',
        summary_document_id=1616729,
        summary_document_number='1283899/289261063/2019',
        statement_of_account_id='DE26702892',
        so_a_reference_number='1283899',
        period=1,
        invoice_status='Due',
        invoiced_on_behalf_of='DE',
        include_e_invoice_details=False,
        mtype='Original'
    ),
    page_size=50,
    page=1
)

result = invoice_controller.invoice_search(
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "18c955d1-b3ec-4dc0-95da-76e67afb891a",
  "Status": "SUCCESS",
  "Data": [
    {
      "AccountFullName": "powder ambition ERF  ",
      "AccountId": 179827,
      "AccountNumber": "DE26702892",
      "AccountShortName": "soft grocery Argyle  ",
      "ColCoId": 14,
      "ColCoOpCoId": "014",
      "CurrentBillingFrequency": "Last day of month",
      "CurrentBillingFrequencyId": 40,
      "CurrentDistributionMethod": "e-mail",
      "CurrentDistributionMethodId": 1,
      "CustomerCurrencyCode": "EUR",
      "CustomerCurrencySymbol": "€",
      "DelCoClientNumber": "014",
      "DelCoId": 14,
      "DelCoOpCoId": "014",
      "DocumentType": "Invoice",
      "DocumentTypeId": 1,
      "DueDate": "20190707",
      "GrossAmountCustomerCurrency": 22.85,
      "GrossAmountTransactionCurrency": 22.85,
      "InvoiceDate": "20190630",
      "InvoicedBy": "euroShell Deutschland GmbH & Co. KG",
      "InvoicedOnBehalfOf": "Germany",
      "InvoiceId": 4013059,
      "InvoiceNumber": "6402009004",
      "IsInternational": false,
      "IsNational": true,
      "NetAmountCustomerCurrency": 19.2,
      "NetAmountTransactionCurrency": 19.2,
      "PayerId": 164825,
      "PayerNumber": "DE26688478",
      "PaymentTerms": "7 days after invoice",
      "PaymentTermsId": 9,
      "ReplacementInvoiceId": null,
      "ReversalInvoiceId": null,
      "Status": "Paid",
      "SummaryDocumentBillingType": "Standard Invoice",
      "SummaryDocumentBillingTypeId": 0,
      "SummaryDocumentDate": "20190630",
      "SummaryDocumentDDAmount": 22.85,
      "SummaryDocumentDueDate": "20190707",
      "SummaryDocumentId": 1616729,
      "SummaryDocumentIsFullyPaid": true,
      "SummaryDocumentNumber": "1283899/289261063/2019",
      "SummaryDocumentPaidAmount": 22.85,
      "SummaryDocumentSoAReferenceNumber": "2000745709",
      "SummaryDocumentStatementOfAccountId": 2000745709,
      "TransactionCurrencyCode": "EUR",
      "TransactionCurrencySymbol": "€",
      "Type": "Original",
      "TypeId": 1,
      "VATAmountCustomerCurrency": 3.65,
      "VATAmountTransactionCurrency": 3.65,
      "VATCountry": "Germany",
      "VATCountryId": 9,
      "VATCountryISOCode": "DE",
      "VATCountryOpCoId": "014"
    }
  ],
  "Page": 1,
  "PageSize": 50,
  "TotalRecords": 1,
  "TotalPages": 1
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Invoice Summary

This API returns the high level summary of invoices that match the  given search criteria. The same search criteria as the endpoint `/v1/invoice/search` is supported with the exception of paging related parameters.

#### Supported operations

* Search invoices by account
* Search invoices by invoice type or invoice status
* Search invoices by invoice id or number
* Search invoices by invoiced country
* Search invoices including einvoices
* Search invoices by summary document
* Search invoices by statement of account
* Search invoices by fixed and custom date periods

```python
def invoice_summary(self,
                   request_id,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request.<br><br>**Constraints**: *Minimum Length*: `36`, *Maximum Length*: `36`, *Pattern*: `^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$` |
| `body` | [`InvoiceSummaryRequest`](../../doc/models/invoice-summary-request.md) | Body, Optional | Invoice Search RequestBody |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceSummaryResponse`](../../doc/models/invoice-summary-response.md).

## Example Usage

```python
request_id = '2b0cbe11-f109-4c43-9201-49af0370df1c'

body = InvoiceSummaryRequest(
    filters=InvoiceSummaryRequestFilters(
        col_co_id=14,
        payer_id=78,
        payer_number='DE26688478',
        invoice_id=4013059,
        invoice_number='0123456789',
        from_date='20170830',
        to_date='20171031',
        invoice_date='20171031',
        summary_document_id=1616729,
        summary_document_number='1283899/289261063/2019',
        statement_of_account_id='DE26702892',
        so_a_reference_number='1283899',
        period=1,
        invoice_status='Due',
        invoiced_on_behalf_of='DE',
        include_e_invoice_details=False,
        mtype='Original'
    )
)

result = invoice_controller.invoice_summary(
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "a0a1596f-b242-4672-b513-66c5e5554195",
  "Status": "SUCCESS",
  "Data": [
    {
      "TotalInvoices": 1,
      "TotalGrossAmountCustomerCurrency": 22.85,
      "TotalNetAmountCustomerCurrency": 19.2,
      "TotalVATAmountCustomerCurrency": 3.65,
      "CustomerCurrencyCode": "EUR",
      "CustomerCurrencySymbol": "€"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Statement of Account

This API allows querying the details of the latest statement of account (SOA) generated for a given Payer.

The endpoint supports querying SOA documents by various input parameters specified in the request body.

#### Supported operations

* Search invoice SOA by payer and account
* Search invoice SOA including monthly trend (last 13 months invocie trend summary)
* Search invoice SOA including past SOAs
* Search invoice SOA including due/overdue documents
* Search invoice SOA including invoice summary

```python
def statement_of_account(self,
                        request_id,
                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request.<br><br>**Constraints**: *Minimum Length*: `36`, *Maximum Length*: `36`, *Pattern*: `^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$` |
| `body` | [`StatementOfAccountRequest`](../../doc/models/statement-of-account-request.md) | Body, Optional | StatementOfAccount RequestBody |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`StatementOfAccountResponse`](../../doc/models/statement-of-account-response.md).

## Example Usage

```python
request_id = '2b0cbe11-f109-4c43-9201-49af0370df1c'

body = StatementOfAccountRequest(
    filters=StatementOfAccountRequestFilters(
        col_co_code=32,
        payer_id=308,
        payer_number='CZ56891709',
        include_monthly_invoice_trend=True,
        include_past_statement_of_accounts=True,
        due_or_over_due_soa_documents_only=False,
        number_of_soa_documents=10,
        include_account_invoices_summary=True
    )
)

result = invoice_controller.statement_of_account(
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "5acba53b-3ce7-4f4b-ab59-1db09399aa6a",
  "Status": "SUCCESS",
  "Data": [
    {
      "LastStatementOfAccount": {
        "AmountDue": 123699.71,
        "AmountNotOverdue": 136604.83,
        "AmountOverdue": 926469.11,
        "CreditLimit": 7000000,
        "CreditLimitCurrencyCode": "CZK",
        "CreditLimitCurrencySymbol": "Kč",
        "CreditLimitInCustomerCurrency": 286826.469986,
        "CurrencyCode": "EUR",
        "CurrencySymbol": "€",
        "LastPaymentCurrencyCode": "EUR",
        "LastPaymentCurrencySymbol": "€",
        "LastPaymentDate": "20220209",
        "LastPaymentValue": 17918.98,
        "OutstandingBalance": 1186773.65,
        "PayerId": 308,
        "PayerNumber": "CZ56891709",
        "PaymentDueDate": "20230608",
        "PaymentMethod": "Incoming - Bank Transfer",
        "PaymentMethodId": 4,
        "PaymentTerms": "30 days after Invoice",
        "PaymentTermsId": 4,
        "SoAReferenceNumber": "2003923319",
        "StatementDate": "20230509",
        "StatementOfAccountId": 2003923319,
        "TotalBillingDocuments": 6,
        "TotalSummaryBillingDocuments": 1,
        "UnallocatedPayment": 0
      },
      "MonthlyInvoiceTrend": null,
      "PastStatementOfAccounts": [
        {
          "AmountDue": 136604.83,
          "AmountNotOverdue": 130344.09,
          "AmountOverdue": 796109.41,
          "AmountOverdueFromUnallocated": 0,
          "AmountPaid": 0,
          "BalanceOnThisStatement": 5866.1,
          "BillingCurrencyCode": "EUR",
          "BillingCurrencySymbol": "€",
          "CreditLimit": 7000000,
          "CreditLimitCurrencyCode": "CZK",
          "CreditLimitCurrencySymbol": "Kč",
          "CreditLimitInCustomerCurrency": 286826.4699857,
          "CurrencyCode": "EUR",
          "CurrencySymbol": "€",
          "FullyPaid": false,
          "LastPaymentCurrencyCode": "EUR",
          "LastPaymentCurrencySymbol": "€",
          "LastPaymentDate": "20220209",
          "LastPaymentValue": 17918.98,
          "OutstandingBalance": 1063058.33,
          "PayerId": 308,
          "PayerNumber": "CZ56891709",
          "PaymentDueDate": "20230511",
          "SoAReferenceNumber": "2003920583",
          "StatementDate": "20230411",
          "StatementOfAccountId": 2003920583,
          "TotalBillingDocuments": 3,
          "TotalNetAmountBillingCurrency": 4847.94,
          "TotalSummaryBillingDocuments": 1,
          "TotalVATAmountBillingCurrency": 1018.16,
          "UnallocatedPayment": 0,
          "LocalCurrencyCode": "EUR",
          "LocalCurrencySymbol": "€",
          "LocalCurrencyExchangeRate": 24.405
        }
      ],
      "PaymentsSinceLastSOA": null,
      "InvoicesSummaries": null
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Dates

- This API will return the list of Invoice Dates and Numbers for the given date range. If the dates are not provided then it will fetch the data for past 13 months.

```python
def dates(self,
         request_id,
         body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request.<br><br>**Constraints**: *Minimum Length*: `36`, *Maximum Length*: `36`, *Pattern*: `^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$` |
| `body` | [`InvoiceDatesRequest`](../../doc/models/invoice-dates-request.md) | Body, Optional | StatementOfAccount RequestBody |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvoiceDatesResponseData`](../../doc/models/invoice-dates-response-data.md).

## Example Usage

```python
request_id = '2b0cbe11-f109-4c43-9201-49af0370df1c'

body = InvoiceDatesRequest(
    filters=InvoiceDatesRequestFilters(
        col_co_code=0,
        col_co_id=0,
        payer_id=0,
        payer_number='string',
        accounts=[
            Accounts(
                account_id=3453,
                account_number='GB000000124'
            )
        ]
    )
)

result = invoice_controller.dates(
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "a0a1596f-b242-4672-b513-66c5e5554195",
  "Status": "SUCCESS",
  "Data": [
    {
      "InvoiceNumbers": [
        "6402009004"
      ],
      "InvoiceDates": [
        "20170101"
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Search Statement of Account

- This API will allow querying of SOA from different systems

```python
def search_statement_of_account(self,
                               request_id,
                               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request.<br><br>**Constraints**: *Minimum Length*: `36`, *Maximum Length*: `36`, *Pattern*: `^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$` |
| `body` | [`SearchStatementOfAccountRequest`](../../doc/models/search-statement-of-account-request.md) | Body, Optional | searchstatementofaccount RequestBody |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SearchStatementOfAccountResponse`](../../doc/models/search-statement-of-account-response.md).

## Example Usage

```python
request_id = '2b0cbe11-f109-4c43-9201-49af0370df1c'

body = SearchStatementOfAccountRequest(
    filters=SearchSOAReq(
        col_co_code=18,
        payer_number='NL99781417',
        invoice_number='0123456789',
        from_date='2022/05/04',
        to_date='2022/05/10',
        period=1,
        invoice_date='20170830',
        invoice_status=[
            'Due'
        ],
        sort_by=[
            1
        ]
    ),
    page=1,
    page_size=10
)

result = invoice_controller.search_statement_of_account(
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "a0a1596f-b242-4672-b513-66c5e5554195",
  "Status": "SUCCESS",
  "Data": [
    {
      "StatementOfAccountId": 2001581712,
      "SoAReferenceNumber": "2001581712",
      "DocumentReferenceNumber": null,
      "StatementDate": "20220505",
      "PayerId": 17150,
      "PayerNumber": "NL99781417",
      "AmountDue": 0,
      "AmountOverdue": 197046.47,
      "CurrencyCode": "EUR",
      "CurrencySymbol": "€",
      "DueDate": "20220604",
      "InvoicedOnBehalfOf": "Netherlands",
      "Status": "OverDue",
      "GrossAmountCustomerCurrency": 0
    }
  ],
  "Page": 1,
  "TotalRecords": 62,
  "TotalPages": 7,
  "PageSize": 10
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Search Documents

- This API allows querying the details of all invoices successfully uploaded to the Worldline invoice repository and file reference numbers for downloading.

```python
def search_documents(self,
                    request_id,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request.<br><br>**Constraints**: *Minimum Length*: `36`, *Maximum Length*: `36`, *Pattern*: `^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$` |
| `body` | [`SearchDocumentsRequest`](../../doc/models/search-documents-request.md) | Body, Optional | SearchDocuments RequestBody |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SearchDocumentsResponse`](../../doc/models/search-documents-response.md).

## Example Usage

```python
request_id = '2b0cbe11-f109-4c43-9201-49af0370df1c'

body = SearchDocumentsRequest(
    filters=SearchDocReq(
        payer_number='DE00000096',
        col_co_code=14,
        account_number='DE00000096',
        account_number_list=[
            'DE00000123',
            'DE00000225'
        ],
        invoice_number='1234567',
        invoice_number_list=[
            '6400013693',
            '9421000010'
        ],
        invoice_status='NEW',
        issuing_date_from='2023/05/01',
        issuing_date_to='2023/06/30',
        due_date_from='2023/05/04',
        due_date_to='2023/06/30',
        gross_amount='1000',
        gross_amount_operator='LT',
        document_type='SOA',
        vat_issuer_country='DE',
        sorty_by=[
            'InvoiceNumber ASC',
            'InvoiceDate DESC'
        ]
    ),
    page='1',
    page_size='50'
)

result = invoice_controller.search_documents(
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "a8b81c1d-f44a-4365-8113-8958061c0b7e",
  "Status": "SUCCESS",
  "Data": [
    {
      "DocumentReference": 311161,
      "InvoiceNumber": "6400013693",
      "PayerName": "DE00000096",
      "AccountNumber": "DE00000096",
      "AccountName": "DE00000096",
      "DocumentType": "NAT",
      "GrossAmount": -3141.93,
      "NetAmount": 0,
      "TaxAmount": 0,
      "CurrencyCode": "EUR",
      "InvoiceStatus": "NEW",
      "InvoiceDate": "2023/01/31",
      "DueDate": "2023/02/07",
      "VATCountryISOCode": "DE"
    }
  ],
  "TotalRecords": 2,
  "TotalRecordsOnPage": 2,
  "IsFirstPage": true,
  "IsLastPage": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Eid Search

- This API provides the functionality needed for the screen “EID FILES” in the web interface. It allows retrieving a list of EIDs based on search criteria.

```python
def eid_search(self,
              request_id,
              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request.<br><br>**Constraints**: *Minimum Length*: `36`, *Maximum Length*: `36`, *Pattern*: `^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$` |
| `body` | [`EIDSearchRequest`](../../doc/models/eid-search-request.md) | Body, Optional | EIDSearch RequestBody |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EIDDocumentResponse`](../../doc/models/eid-document-response.md).

## Example Usage

```python
request_id = '2b0cbe11-f109-4c43-9201-49af0370df1c'

body = EIDSearchRequest(
    filters=EIDSearchReq(
        col_co_code=32,
        account_group_country=32,
        account_group_id=[
            '122'
        ],
        account_group_name=None,
        from_date='2017/08/30',
        to_date='2017/10/31',
        invoice_type='NAT',
        invoice_status='NEW',
        sort_by=[
            'DocumentDate ASC'
        ]
    ),
    page=1,
    page_size=10
)

result = invoice_controller.eid_search(
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "a0a1596f-b242-4672-b513-66c5e5554195",
  "Status": "SUCCESS",
  "Data": [
    {
      "DocumentId": 15029,
      "AccountGroupId": "122",
      "AccountGroupName": "EID-122",
      "DocumentType": "INT",
      "DocumentFormat": "FLAT",
      "DocumentDate": "2022/12/28",
      "NumberOfInvoices": 1,
      "FileSize": 1624,
      "DocumentStatus": "DOWNLOADED",
      "DocumentName": "032_122_INT_28122022.TXT"
    }
  ],
  "PageSize": 1,
  "Page": 1,
  "TotalPages": 12,
  "TotalRecords": 120,
  "IsFirstPage": true,
  "IsLastPage": false
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Download

- This API downloads Invoice Documents i.e., ZIP file with Invoice PDF file and Proofing Elements in XML format from invoice repository.

```python
def download(self,
            request_id,
            body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request.<br><br>**Constraints**: *Minimum Length*: `36`, *Maximum Length*: `36`, *Pattern*: `^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$` |
| `body` | [`InvoiceDownloadRequest`](../../doc/models/invoice-download-request.md) | Body, Optional | Invoice Download RequestBody |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `binary`.

## Example Usage

```python
request_id = '2b0cbe11-f109-4c43-9201-49af0370df1c'

body = InvoiceDownloadRequest(
    filters=InvoiceDownloadReq(
        col_co_code=18,
        payer_number='NL99781417',
        account_number=[
            'NL99781420'
        ],
        document_reference=[
            1234567890
        ],
        invoice_or_soa_number='2234556'
    )
)

result = invoice_controller.download(
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Eid Download

- This service allows downloading one or more EID documents and the corresponding signature material (where applicable) in one single request
- The number of EID that can be downloaded at once is limited to 100 documents.

```python
def eid_download(self,
                request_id,
                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request.<br><br>**Constraints**: *Minimum Length*: `36`, *Maximum Length*: `36`, *Pattern*: `^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$` |
| `body` | [`EIDDownloadRequest`](../../doc/models/eid-download-request.md) | Body, Optional | EIDInvoice Download RequestBody |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `binary`.

## Example Usage

```python
request_id = '2b0cbe11-f109-4c43-9201-49af0370df1c'

body = EIDDownloadRequest(
    filters=EIDDownloadReq(
        col_co_code=18,
        eid_list=[
            '1710187',
            '1734566'
        ],
        account_group_country=18,
        account_group_id_list=[
            '26685402'
        ]
    )
)

result = invoice_controller.eid_download(
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |

