
# Getting Started with Fortis API

## Building

You must have Python `3.7+` installed on your system to install and run this SDK. This SDK package depends on other Python packages like pytest, etc. These dependencies are defined in the `requirements.txt` file that comes with the SDK. To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type `pip --version`. This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including `requirements.txt`) for the SDK.
* Run the command `pip install -r requirements.txt`. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Fortisapi-Python&step=installDependencies)

## Installation

The following section explains how to use the fortisapi library in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Fortisapi-Python&step=pyCharm)

Click on `Open` in PyCharm to browse to your generated SDK directory and then click `OK`.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Fortisapi-Python&step=openProject0)

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Fortisapi-Python&projectName=fortisapi&step=openProject1)

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Fortisapi-Python&projectName=fortisapi&step=createDirectory)

Name the directory as "test".

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Fortisapi-Python&step=nameDirectory)

Add a python file to this project.

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Fortisapi-Python&projectName=fortisapi&step=createFile)

Name it "testSDK".

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?workspaceFolder=Fortisapi-Python&projectName=fortisapi&step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```python
from fortisapi.fortisapi_client import FortisapiClient
```

![Add a new project in PyCharm - Step 5](https://apidocs.io/illustration/python?workspaceFolder=Fortisapi-Python&projectName=fortisapi&libraryName=fortisapi.fortisapi_client&className=FortisapiClient&step=projectFiles)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on `Run`

![Run Test Project - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Fortisapi-Python&projectName=fortisapi&libraryName=fortisapi.fortisapi_client&className=FortisapiClient&step=runProject)

## Test the SDK

You can test the generated SDK and the server with test cases. `unittest` is used as the testing framework and `pytest` is used as the test runner. You can run the tests as follows:

Navigate to the root directory of the SDK and run the following commands


pip install -r test-requirements.txt
pytest


## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| environment | `Environment` | The API environment. <br> **Default: `Environment.SANDBOX`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 60** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| user_id_credentials | [`UserIdCredentials`](doc/auth/custom-header-signature.md) | The credential object for Custom Header Signature |
| user_api_key_credentials | [`UserApiKeyCredentials`](doc/auth/custom-header-signature-1.md) | The credential object for Custom Header Signature |
| developer_id_credentials | [`DeveloperIdCredentials`](doc/auth/custom-header-signature-2.md) | The credential object for Custom Header Signature |
| access_token_credentials | [`AccessTokenCredentials`](doc/auth/custom-header-signature-3.md) | The credential object for Custom Header Signature |

The API client can be initialized as follows:

### Code-Based Client Initialization

```python
from fortisapi.configuration import Environment
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.access_token import AccessTokenCredentials
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials

client = FortisapiClient(
    user_id_credentials=UserIdCredentials(
        user_id='user-id'
    ),
    user_api_key_credentials=UserApiKeyCredentials(
        user_api_key='user-api-key'
    ),
    developer_id_credentials=DeveloperIdCredentials(
        developer_id='developer-id'
    ),
    access_token_credentials=AccessTokenCredentials(
        access_token='access-token'
    ),
    environment=Environment.SANDBOX
)
```

### Environment-Based Client Initialization

```python
from fortisapi.fortisapi_client import FortisapiClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = FortisapiClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](doc/environment-based-client-initialization.md) section for details.

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| sandbox | **Default** |
| production | - |

## Authorization

This API uses the following authentication schemes.

* [`user-id (Custom Header Signature)`](doc/auth/custom-header-signature.md)
* [`user-api-key (Custom Header Signature)`](doc/auth/custom-header-signature-1.md)
* [`developer-id (Custom Header Signature)`](doc/auth/custom-header-signature-2.md)
* [`access-token (Custom Header Signature)`](doc/auth/custom-header-signature-3.md)

## List of APIs

* [Async Processing](doc/controllers/async-processing.md)
* [Declined Recurring Transactions](doc/controllers/declined-recurring-transactions.md)
* [Device Terms](doc/controllers/device-terms.md)
* [Full Boarding](doc/controllers/full-boarding.md)
* [On Boarding](doc/controllers/on-boarding.md)
* [Quick Invoices](doc/controllers/quick-invoices.md)
* [Transactions-ACH](doc/controllers/transactions-ach.md)
* [Transactions-Cash](doc/controllers/transactions-cash.md)
* [Transactions-Credit Card](doc/controllers/transactions-credit-card.md)
* [Transactions-Read](doc/controllers/transactions-read.md)
* [Level 3 Data](doc/controllers/level-3-data.md)
* [Transactions-Updates](doc/controllers/transactions-updates.md)
* [User Verifications](doc/controllers/user-verifications.md)
* [Merchant Details](doc/controllers/merchant-details.md)
* [Apple Pay Validate Merchant](doc/controllers/apple-pay-validate-merchant.md)
* [Batches](doc/controllers/batches.md)
* [Contacts](doc/controllers/contacts.md)
* [Elements](doc/controllers/elements.md)
* [Locations](doc/controllers/locations.md)
* [Paylinks](doc/controllers/paylinks.md)
* [Recurring](doc/controllers/recurring.md)
* [Signatures](doc/controllers/signatures.md)
* [Tags](doc/controllers/tags.md)
* [Terminals](doc/controllers/terminals.md)
* [Tickets](doc/controllers/tickets.md)
* [Tokens](doc/controllers/tokens.md)
* [Users](doc/controllers/users.md)
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

