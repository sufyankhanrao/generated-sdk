
# Getting Started with Payrix

## Building

You must have Python `3.7+` installed on your system to install and run this SDK. This SDK package depends on other Python packages like pytest, etc. These dependencies are defined in the `requirements.txt` file that comes with the SDK. To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type `pip --version`. This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including `requirements.txt`) for the SDK.
* Run the command `pip install -r requirements.txt`. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Payrix-Python&step=installDependencies)

## Installation

The following section explains how to use the payrix library in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Payrix-Python&step=pyCharm)

Click on `Open` in PyCharm to browse to your generated SDK directory and then click `OK`.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Payrix-Python&step=openProject0)

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Payrix-Python&projectName=payrix&step=openProject1)

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Payrix-Python&projectName=payrix&step=createDirectory)

Name the directory as "test".

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Payrix-Python&step=nameDirectory)

Add a python file to this project.

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Payrix-Python&projectName=payrix&step=createFile)

Name it "testSDK".

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?workspaceFolder=Payrix-Python&projectName=payrix&step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```python
from payrix.payrix_client import PayrixClient
```

![Add a new project in PyCharm - Step 5](https://apidocs.io/illustration/python?workspaceFolder=Payrix-Python&projectName=payrix&libraryName=payrix.payrix_client&className=PayrixClient&step=projectFiles)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on `Run`

![Run Test Project - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Payrix-Python&projectName=payrix&libraryName=payrix.payrix_client&className=PayrixClient&step=runProject)

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](doc/client.md)

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
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| proxy_settings | [`ProxySettings`](doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| api_key_credentials | [`ApiKeyCredentials`](doc/auth/custom-header-signature.md) | The credential object for Custom Header Signature |
| session_key_credentials | [`SessionKeyCredentials`](doc/auth/custom-header-signature-1.md) | The credential object for Custom Header Signature |
| txn_session_key_credentials | [`TxnSessionKeyCredentials`](doc/auth/custom-header-signature-2.md) | The credential object for Custom Header Signature |
| username_credentials | [`UsernameCredentials`](doc/auth/custom-header-signature-3.md) | The credential object for Custom Header Signature |
| password_credentials | [`PasswordCredentials`](doc/auth/custom-header-signature-4.md) | The credential object for Custom Header Signature |

The API client can be initialized as follows:

### Code-Based Client Initialization

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

### Environment-Based Client Initialization

```python
from payrix.payrix_client import PayrixClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = PayrixClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](doc/environment-based-client-initialization.md) section for details.

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| devex-qa | - |
| qa | **Default** |

## Authorization

This API uses the following authentication schemes.

* [`apiKey (Custom Header Signature)`](doc/auth/custom-header-signature.md)
* [`sessionKey (Custom Header Signature)`](doc/auth/custom-header-signature-1.md)
* [`txnSessionKey (Custom Header Signature)`](doc/auth/custom-header-signature-2.md)
* [`username (Custom Header Signature)`](doc/auth/custom-header-signature-3.md)
* [`password (Custom Header Signature)`](doc/auth/custom-header-signature-4.md)

## List of APIs

* [API Keys](doc/controllers/api-keys.md)
* [Apple Domains](doc/controllers/apple-domains.md)
* [Accounts Verifications](doc/controllers/accounts-verifications.md)
* [Aggregation Result Groups](doc/controllers/aggregation-result-groups.md)
* [Aggregation Results](doc/controllers/aggregation-results.md)
* [Alert Actions](doc/controllers/alert-actions.md)
* [Alert Triggers](doc/controllers/alert-triggers.md)
* [Authentication Tokens](doc/controllers/authentication-tokens.md)
* [Batches Settlements](doc/controllers/batches-settlements.md)
* [Billing Modifiers](doc/controllers/billing-modifiers.md)
* [Billing Events](doc/controllers/billing-events.md)
* [Change Requests](doc/controllers/change-requests.md)
* [Chargeback Documents](doc/controllers/chargeback-documents.md)
* [Chargeback Message Results](doc/controllers/chargeback-message-results.md)
* [Chargeback Messages](doc/controllers/chargeback-messages.md)
* [Chargeback Statuses](doc/controllers/chargeback-statuses.md)
* [Confirmation Codes](doc/controllers/confirmation-codes.md)
* [Decision Actions](doc/controllers/decision-actions.md)
* [Decision Rules](doc/controllers/decision-rules.md)
* [Disbursement Entries](doc/controllers/disbursement-entries.md)
* [Disbursement Reference](doc/controllers/disbursement-reference.md)
* [Disbursement Results](doc/controllers/disbursement-results.md)
* [Embedded Finance](doc/controllers/embedded-finance.md)
* [Entity Debts](doc/controllers/entity-debts.md)
* [Entity Reserves](doc/controllers/entity-reserves.md)
* [Entity Returns](doc/controllers/entity-returns.md)
* [Entity Terms](doc/controllers/entity-terms.md)
* [Entry Origin](doc/controllers/entry-origin.md)
* [Fee Modifiers](doc/controllers/fee-modifiers.md)
* [Fee Rules](doc/controllers/fee-rules.md)
* [Host Themes](doc/controllers/host-themes.md)
* [Fund Origins](doc/controllers/fund-origins.md)
* [IP Address Lists](doc/controllers/ip-address-lists.md)
* [Invoice Items](doc/controllers/invoice-items.md)
* [Invoice Parameters](doc/controllers/invoice-parameters.md)
* [Invoice Line Items](doc/controllers/invoice-line-items.md)
* [Invoice Results](doc/controllers/invoice-results.md)
* [Logins Helpers](doc/controllers/logins-helpers.md)
* [Merchant Results](doc/controllers/merchant-results.md)
* [Merchant Platform Statuses](doc/controllers/merchant-platform-statuses.md)
* [Message Threads](doc/controllers/message-threads.md)
* [Note Documents](doc/controllers/note-documents.md)
* [Orgs VAS Efe Products](doc/controllers/orgs-vas-efe-products.md)
* [Orgs VAS Omni Tokens](doc/controllers/orgs-vas-omni-tokens.md)
* [Orgs VAS Pinless Debit Conversions](doc/controllers/orgs-vas-pinless-debit-conversions.md)
* [Orgs VAS Revenue Boosts](doc/controllers/orgs-vas-revenue-boosts.md)
* [Orgs VAS Safer Payments](doc/controllers/orgs-vas-safer-payments.md)
* [Org Entities](doc/controllers/org-entities.md)
* [Org Flow Actions](doc/controllers/org-flow-actions.md)
* [Org Flows](doc/controllers/org-flows.md)
* [Org Flow Rules](doc/controllers/org-flow-rules.md)
* [Payment Update Groups](doc/controllers/payment-update-groups.md)
* [Payment Updates](doc/controllers/payment-updates.md)
* [Payout Flows](doc/controllers/payout-flows.md)
* [Pending Entry](doc/controllers/pending-entry.md)
* [Pinless Debit Conversions](doc/controllers/pinless-debit-conversions.md)
* [Profit Share Results](doc/controllers/profit-share-results.md)
* [Profit Share Rules](doc/controllers/profit-share-rules.md)
* [Profit Shares](doc/controllers/profit-shares.md)
* [Reserve Entry](doc/controllers/reserve-entry.md)
* [Revenue Boosts](doc/controllers/revenue-boosts.md)
* [Rev Share Schedules](doc/controllers/rev-share-schedules.md)
* [Rev Share Statements](doc/controllers/rev-share-statements.md)
* [Safer Payments](doc/controllers/safer-payments.md)
* [Statement Entry](doc/controllers/statement-entry.md)
* [Subscription Tokens](doc/controllers/subscription-tokens.md)
* [Tax Form Requests](doc/controllers/tax-form-requests.md)
* [Team Logins](doc/controllers/team-logins.md)
* [Terminal Transaction Reference](doc/controllers/terminal-transaction-reference.md)
* [Terminal Transactions Datas](doc/controllers/terminal-transactions-datas.md)
* [Terminal Transactions](doc/controllers/terminal-transactions.md)
* [Terminal Transaction Results](doc/controllers/terminal-transaction-results.md)
* [Terminal Transactions Metadatas](doc/controllers/terminal-transactions-metadatas.md)
* [Token Results](doc/controllers/token-results.md)
* [Transaction Datas](doc/controllers/transaction-datas.md)
* [Transaction Metadatas](doc/controllers/transaction-metadatas.md)
* [Transaction Holds](doc/controllers/transaction-holds.md)
* [Transaction Items](doc/controllers/transaction-items.md)
* [Transactions Results](doc/controllers/transactions-results.md)
* [Fee Refunds](doc/controllers/fee-refunds.md)
* [Transactions Txns](doc/controllers/transactions-txns.md)
* [Txn Sessions](doc/controllers/txn-sessions.md)
* [VAS Efe Offers](doc/controllers/vas-efe-offers.md)
* [Accounts](doc/controllers/accounts.md)
* [Adjustments](doc/controllers/adjustments.md)
* [Aggregations](doc/controllers/aggregations.md)
* [Alerts](doc/controllers/alerts.md)
* [Assessments](doc/controllers/assessments.md)
* [Billing](doc/controllers/billing.md)
* [Bins](doc/controllers/bins.md)
* [Chargebacks](doc/controllers/chargebacks.md)
* [Contacts](doc/controllers/contacts.md)
* [Credentials](doc/controllers/credentials.md)
* [Customers](doc/controllers/customers.md)
* [Decisions](doc/controllers/decisions.md)
* [Disbursements](doc/controllers/disbursements.md)
* [Divisions](doc/controllers/divisions.md)
* [Entities](doc/controllers/entities.md)
* [Entity Refs](doc/controllers/entity-refs.md)
* [Entity Data](doc/controllers/entity-data.md)
* [Entities Custom Fields](doc/controllers/entities-custom-fields.md)
* [Entries](doc/controllers/entries.md)
* [Fees](doc/controllers/fees.md)
* [Funds](doc/controllers/funds.md)
* [Invoices](doc/controllers/invoices.md)
* [Logins](doc/controllers/logins.md)
* [Mappings](doc/controllers/mappings.md)
* [Members](doc/controllers/members.md)
* [Merchants](doc/controllers/merchants.md)
* [Messages](doc/controllers/messages.md)
* [Notes](doc/controllers/notes.md)
* [Omni Tokens](doc/controllers/omni-tokens.md)
* [Orgs](doc/controllers/orgs.md)
* [Payouts](doc/controllers/payouts.md)
* [Plans](doc/controllers/plans.md)
* [Reserves](doc/controllers/reserves.md)
* [Secrets](doc/controllers/secrets.md)
* [Sessions](doc/controllers/sessions.md)
* [Statements](doc/controllers/statements.md)
* [Subscriptions](doc/controllers/subscriptions.md)
* [Teams](doc/controllers/teams.md)
* [Terminals](doc/controllers/terminals.md)
* [Tokens](doc/controllers/tokens.md)
* [Vendors](doc/controllers/vendors.md)

## SDK Infrastructure

### Configuration

* [ProxySettings](doc/proxy-settings.md)
* [Environment-Based Client Initialization](doc/environment-based-client-initialization.md)

### HTTP

* [HttpResponse](doc/http-response.md)
* [HttpRequest](doc/http-request.md)

### Utilities

* [ApiResponse](doc/api-response.md)
* [ApiHelper](doc/api-helper.md)
* [HttpDateTime](doc/http-date-time.md)
* [RFC3339DateTime](doc/rfc3339-date-time.md)
* [UnixDateTime](doc/unix-date-time.md)

