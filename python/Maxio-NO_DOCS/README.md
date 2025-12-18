
# Getting Started with Maxio Advanced Billing

## Introduction

Maxio Advanced Billing (formerly Chargify) provides an HTTP-based API that conforms to the principles of REST.
One of the many reasons to use Advanced Billing is the immense feature set and surrounding community [client libraries](page:development-tools/client-libraries).
The Maxio API returns JSON responses as the primary and recommended format, but XML is also provided as a backwards compatible option for Merchants who require it.

### Steps to make your first Maxio Advanced Billing API call

1. [Sign-up](https://app.chargify.com/signup/maxio-billing-sandbox) or [log-in](https://app.chargify.com/login.html) to your [test site](https://maxio-chargify.zendesk.com/hc/en-us/articles/5405553861773-Testing-Intro) account.
2. [Setup and configure authentication](https://maxio-chargify.zendesk.com/hc/en-us/articles/5405281550477-API-Keys#api) credentials.
3. Submit your API request and try it out.
4. Verify results through response.
5. Test our integrations.

We strongly suggest exploring the developer portal, our [integrations](https://www.maxio.com/integrations) and the API guide, as well as the entire set of application-based documentation to aid in your discovery of the product.

#### Example

The following example uses the curl command-line tool to execute API requests.

**Request**

curl -u <api_key>:x -H Accept:application/json -H Content-Type:application/json https://acme.chargify.com/subscriptions.json

## Building

You must have Python `3.7+` installed on your system to install and run this SDK. This SDK package depends on other Python packages like pytest, etc. These dependencies are defined in the `requirements.txt` file that comes with the SDK. To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type `pip --version`. This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including `requirements.txt`) for the SDK.
* Run the command `pip install -r requirements.txt`. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?workspaceFolder=AdvancedBilling-Python&step=installDependencies)

## Installation

The following section explains how to use the advanced_billing library in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=AdvancedBilling-Python&step=pyCharm)

Click on `Open` in PyCharm to browse to your generated SDK directory and then click `OK`.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=AdvancedBilling-Python&step=openProject0)

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=AdvancedBilling-Python&projectName=advanced_billing&step=openProject1)

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=AdvancedBilling-Python&projectName=advanced_billing&step=createDirectory)

Name the directory as "test".

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=AdvancedBilling-Python&step=nameDirectory)

Add a python file to this project.

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=AdvancedBilling-Python&projectName=advanced_billing&step=createFile)

Name it "testSDK".

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?workspaceFolder=AdvancedBilling-Python&projectName=advanced_billing&step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```python
from advanced_billing.advanced_billing_client import AdvancedBillingClient
```

![Add a new project in PyCharm - Step 5](https://apidocs.io/illustration/python?workspaceFolder=AdvancedBilling-Python&projectName=advanced_billing&libraryName=advanced_billing.advanced_billing_client&className=AdvancedBillingClient&step=projectFiles)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on `Run`

![Run Test Project - Step 1](https://apidocs.io/illustration/python?workspaceFolder=AdvancedBilling-Python&projectName=advanced_billing&libraryName=advanced_billing.advanced_billing_client&className=AdvancedBillingClient&step=runProject)

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| subdomain | `str` | The subdomain for your Chargify site.<br>*Default*: `'subdomain'` |
| domain | `str` | The Chargify server domain.<br>*Default*: `'chargify.com'` |
| environment | `Environment` | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 30** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| proxy_settings | [`ProxySettings`](doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| basic_auth_credentials | [`BasicAuthCredentials`](doc/auth/basic-authentication.md) | The credential object for Basic Authentication |

The API client can be initialized as follows:

### Code-Based Client Initialization

```python
from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)
```

### Environment-Based Client Initialization

```python
from advancedbilling.advanced_billing_client import AdvancedBillingClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = AdvancedBillingClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](doc/environment-based-client-initialization.md) section for details.

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| production | **Default** Production server |
| environment2 | Production server |

## Authorization

This API uses the following authentication schemes.

* [`BasicAuth (Basic Authentication)`](doc/auth/basic-authentication.md)

## List of APIs

* [API Exports](doc/controllers/api-exports.md)
* [Advance Invoice](doc/controllers/advance-invoice.md)
* [Billing Portal](doc/controllers/billing-portal.md)
* [Custom Fields](doc/controllers/custom-fields.md)
* [Events-Based Billing Segments](doc/controllers/events-based-billing-segments.md)
* [Payment Profiles](doc/controllers/payment-profiles.md)
* [Product Families](doc/controllers/product-families.md)
* [Product Price Points](doc/controllers/product-price-points.md)
* [Proforma Invoices](doc/controllers/proforma-invoices.md)
* [Reason Codes](doc/controllers/reason-codes.md)
* [Referral Codes](doc/controllers/referral-codes.md)
* [Sales Commissions](doc/controllers/sales-commissions.md)
* [Subscription Components](doc/controllers/subscription-components.md)
* [Subscription Groups](doc/controllers/subscription-groups.md)
* [Subscription Group Invoice Account](doc/controllers/subscription-group-invoice-account.md)
* [Subscription Group Status](doc/controllers/subscription-group-status.md)
* [Subscription Invoice Account](doc/controllers/subscription-invoice-account.md)
* [Subscription Notes](doc/controllers/subscription-notes.md)
* [Subscription Products](doc/controllers/subscription-products.md)
* [Subscription Status](doc/controllers/subscription-status.md)
* [Coupons](doc/controllers/coupons.md)
* [Components](doc/controllers/components.md)
* [Customers](doc/controllers/customers.md)
* [Events](doc/controllers/events.md)
* [Insights](doc/controllers/insights.md)
* [Invoices](doc/controllers/invoices.md)
* [Offers](doc/controllers/offers.md)
* [Products](doc/controllers/products.md)
* [Sites](doc/controllers/sites.md)
* [Subscriptions](doc/controllers/subscriptions.md)
* [Webhooks](doc/controllers/webhooks.md)

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

