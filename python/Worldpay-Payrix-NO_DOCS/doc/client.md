
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| environment | `Environment` | The API environment. <br> **Default: `Environment.QA`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 60** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](../doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| api_key_credentials | [`ApiKeyCredentials`](auth/custom-header-signature.md) | The credential object for Custom Header Signature |
| session_key_credentials | [`SessionKeyCredentials`](auth/custom-header-signature-1.md) | The credential object for Custom Header Signature |
| txn_session_key_credentials | [`TxnSessionKeyCredentials`](auth/custom-header-signature-2.md) | The credential object for Custom Header Signature |
| username_credentials | [`UsernameCredentials`](auth/custom-header-signature-3.md) | The credential object for Custom Header Signature |
| password_credentials | [`PasswordCredentials`](auth/custom-header-signature-4.md) | The credential object for Custom Header Signature |

The API client can be initialized as follows:

## Code-Based Client Initialization

```python
from payrix.configuration import Environment
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.password import PasswordCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.http.auth.username import UsernameCredentials
from payrix.payrix_client import PayrixClient

client = PayrixClient(
    api_key_credentials=ApiKeyCredentials(
        apikey='APIKEY'
    ),
    session_key_credentials=SessionKeyCredentials(
        sessionkey='SESSIONKEY'
    ),
    txn_session_key_credentials=TxnSessionKeyCredentials(
        txnsessionkey='TXNSESSIONKEY'
    ),
    username_credentials=UsernameCredentials(
        username='USERNAME'
    ),
    password_credentials=PasswordCredentials(
        password='PASSWORD'
    ),
    environment=Environment.QA
)
```

## Environment-Based Client Initialization

```python
from payrix.payrix_client import PayrixClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = PayrixClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](../doc/environment-based-client-initialization.md) section for details.

## Payrix Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| api_keys | Gets APIKeysController |
| apple_domains | Gets AppleDomainsController |
| accounts | Gets AccountsController |
| accounts_verifications | Gets AccountsVerificationsController |
| adjustments | Gets AdjustmentsController |
| aggregations | Gets AggregationsController |
| aggregation_result_groups | Gets AggregationResultGroupsController |
| aggregation_results | Gets AggregationResultsController |
| alert_actions | Gets AlertActionsController |
| alert_triggers | Gets AlertTriggersController |
| alerts | Gets AlertsController |
| assessments | Gets AssessmentsController |
| authentication_tokens | Gets AuthenticationTokensController |
| batches_settlements | Gets BatchesSettlementsController |
| billing | Gets BillingController |
| billing_modifiers | Gets BillingModifiersController |
| billing_events | Gets BillingEventsController |
| bins | Gets BinsController |
| change_requests | Gets ChangeRequestsController |
| chargebacks | Gets ChargebacksController |
| chargeback_documents | Gets ChargebackDocumentsController |
| chargeback_message_results | Gets ChargebackMessageResultsController |
| chargeback_messages | Gets ChargebackMessagesController |
| chargeback_statuses | Gets ChargebackStatusesController |
| confirmation_codes | Gets ConfirmationCodesController |
| contacts | Gets ContactsController |
| credentials | Gets CredentialsController |
| customers | Gets CustomersController |
| decision_actions | Gets DecisionActionsController |
| decision_rules | Gets DecisionRulesController |
| decisions | Gets DecisionsController |
| disbursements | Gets DisbursementsController |
| disbursement_entries | Gets DisbursementEntriesController |
| disbursement_reference | Gets DisbursementReferenceController |
| disbursement_results | Gets DisbursementResultsController |
| divisions | Gets DivisionsController |
| embedded_finance | Gets EmbeddedFinanceController |
| entities | Gets EntitiesController |
| entity_refs | Gets EntityRefsController |
| entity_data | Gets EntityDataController |
| entities_custom_fields | Gets EntitiesCustomFieldsController |
| entity_debts | Gets EntityDebtsController |
| entity_reserves | Gets EntityReservesController |
| entity_returns | Gets EntityReturnsController |
| entries | Gets EntriesController |
| entity_terms | Gets EntityTermsController |
| entry_origin | Gets EntryOriginController |
| fee_modifiers | Gets FeeModifiersController |
| fee_rules | Gets FeeRulesController |
| fees | Gets FeesController |
| funds | Gets FundsController |
| host_themes | Gets HostThemesController |
| fund_origins | Gets FundOriginsController |
| ip_address_lists | Gets IPAddressListsController |
| invoice_items | Gets InvoiceItemsController |
| invoice_parameters | Gets InvoiceParametersController |
| invoice_line_items | Gets InvoiceLineItemsController |
| invoice_results | Gets InvoiceResultsController |
| invoices | Gets InvoicesController |
| logins_helpers | Gets LoginsHelpersController |
| logins | Gets LoginsController |
| mappings | Gets MappingsController |
| members | Gets MembersController |
| merchant_results | Gets MerchantResultsController |
| merchants | Gets MerchantsController |
| merchant_platform_statuses | Gets MerchantPlatformStatusesController |
| message_threads | Gets MessageThreadsController |
| messages | Gets MessagesController |
| note_documents | Gets NoteDocumentsController |
| notes | Gets NotesController |
| omni_tokens | Gets OmniTokensController |
| orgs_vas_efe_products | Gets OrgsVASEfeProductsController |
| orgs_vas_omni_tokens | Gets OrgsVASOmniTokensController |
| orgs_vas_pinless_debit_conversions | Gets OrgsVASPinlessDebitConversionsController |
| orgs_vas_revenue_boosts | Gets OrgsVASRevenueBoostsController |
| orgs_vas_safer_payments | Gets OrgsVASSaferPaymentsController |
| org_entities | Gets OrgEntitiesController |
| org_flow_actions | Gets OrgFlowActionsController |
| org_flows | Gets OrgFlowsController |
| org_flow_rules | Gets OrgFlowRulesController |
| orgs | Gets OrgsController |
| payment_update_groups | Gets PaymentUpdateGroupsController |
| payment_updates | Gets PaymentUpdatesController |
| payout_flows | Gets PayoutFlowsController |
| payouts | Gets PayoutsController |
| pending_entry | Gets PendingEntryController |
| pinless_debit_conversions | Gets PinlessDebitConversionsController |
| plans | Gets PlansController |
| profit_share_results | Gets ProfitShareResultsController |
| profit_share_rules | Gets ProfitShareRulesController |
| profit_shares | Gets ProfitSharesController |
| reserve_entry | Gets ReserveEntryController |
| reserves | Gets ReservesController |
| revenue_boosts | Gets RevenueBoostsController |
| rev_share_schedules | Gets RevShareSchedulesController |
| rev_share_statements | Gets RevShareStatementsController |
| safer_payments | Gets SaferPaymentsController |
| secrets | Gets SecretsController |
| sessions | Gets SessionsController |
| statement_entry | Gets StatementEntryController |
| statements | Gets StatementsController |
| subscription_tokens | Gets SubscriptionTokensController |
| subscriptions | Gets SubscriptionsController |
| tax_form_requests | Gets TaxFormRequestsController |
| team_logins | Gets TeamLoginsController |
| teams | Gets TeamsController |
| terminal_transaction_reference | Gets TerminalTransactionReferenceController |
| terminal_transactions_datas | Gets TerminalTransactionsDatasController |
| terminal_transactions | Gets TerminalTransactionsController |
| terminal_transaction_results | Gets TerminalTransactionResultsController |
| terminal_transactions_metadatas | Gets TerminalTransactionsMetadatasController |
| terminals | Gets TerminalsController |
| tokens | Gets TokensController |
| token_results | Gets TokenResultsController |
| transaction_datas | Gets TransactionDatasController |
| transaction_metadatas | Gets TransactionMetadatasController |
| transaction_holds | Gets TransactionHoldsController |
| transaction_items | Gets TransactionItemsController |
| transactions_results | Gets TransactionsResultsController |
| fee_refunds | Gets FeeRefundsController |
| transactions_txns | Gets TransactionsTxnsController |
| txn_sessions | Gets TxnSessionsController |
| vas_efe_offers | Gets VASEfeOffersController |
| vendors | Gets VendorsController |

