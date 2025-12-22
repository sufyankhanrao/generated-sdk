
# Getting Started with MultiAuth-Sample

## Introduction

API for Markdown Notes app.

## Building

You must have Python `3.7+` installed on your system to install and run this SDK. This SDK package depends on other Python packages like pytest, etc. These dependencies are defined in the `requirements.txt` file that comes with the SDK. To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type `pip --version`. This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including `requirements.txt`) for the SDK.
* Run the command `pip install -r requirements.txt`. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Multiauthsample-Python&step=installDependencies)

## Installation

The following section explains how to use the multiauthsample library in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Multiauthsample-Python&step=pyCharm)

Click on `Open` in PyCharm to browse to your generated SDK directory and then click `OK`.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Multiauthsample-Python&step=openProject0)

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Multiauthsample-Python&projectName=multiauthsample&step=openProject1)

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Multiauthsample-Python&projectName=multiauthsample&step=createDirectory)

Name the directory as "test".

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Multiauthsample-Python&step=nameDirectory)

Add a python file to this project.

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Multiauthsample-Python&projectName=multiauthsample&step=createFile)

Name it "testSDK".

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?workspaceFolder=Multiauthsample-Python&projectName=multiauthsample&step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```python
from multiauthsample.multiauthsample_client import MultiauthsampleClient
```

![Add a new project in PyCharm - Step 5](https://apidocs.io/illustration/python?workspaceFolder=Multiauthsample-Python&projectName=multiauthsample&libraryName=multiauthsample.multiauthsample_client&className=MultiauthsampleClient&step=projectFiles)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on `Run`

![Run Test Project - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Multiauthsample-Python&projectName=multiauthsample&libraryName=multiauthsample.multiauthsample_client&className=MultiauthsampleClient&step=runProject)

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
| access_token | `str` |  |
| port | `str` | *Default*: `"80"` |
| suites | `SuiteCodeEnum` | *Default*: `1` |
| environment | `Environment` | The API environment. <br> **Default: `Environment.TESTING`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 60** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| basic_auth_credentials | [`BasicAuthCredentials`](doc/auth/basic-authentication.md) | The credential object for Basic Authentication |
| api_key_credentials | [`ApiKeyCredentials`](doc/auth/custom-query-parameter.md) | The credential object for Custom Query Parameter |
| api_header_credentials | [`ApiHeaderCredentials`](doc/auth/custom-header-signature.md) | The credential object for Custom Header Signature |
| o_auth_ccg_credentials | [`OAuthCCGCredentials`](doc/auth/oauth-2-client-credentials-grant.md) | The credential object for OAuth 2 Client Credentials Grant |
| o_auth_acg_credentials | [`OAuthACGCredentials`](doc/auth/oauth-2-authorization-code-grant.md) | The credential object for OAuth 2 Authorization Code Grant |
| o_auth_ropcg_credentials | [`OAuthROPCGCredentials`](doc/auth/oauth-2-resource-owner-credentials-grant.md) | The credential object for OAuth 2 Resource Owner Credentials Grant |
| o_auth_bearer_token_credentials | [`OAuthBearerTokenCredentials`](doc/auth/oauth-2-bearer-token.md) | The credential object for OAuth 2 Bearer token |

The API client can be initialized as follows:

### Code-Based Client Initialization

```python
from multiauthsample.configuration import Environment
from multiauthsample.http.auth.api_header import ApiHeaderCredentials
from multiauthsample.http.auth.api_key import ApiKeyCredentials
from multiauthsample.http.auth.basic_auth import BasicAuthCredentials
from multiauthsample.http.auth.o_auth_acg import OAuthACGCredentials
from multiauthsample.http.auth.o_auth_bearer_token import OAuthBearerTokenCredentials
from multiauthsample.http.auth.o_auth_ccg import OAuthCCGCredentials
from multiauthsample.http.auth.o_auth_ropcg import OAuthROPCGCredentials
from multiauthsample.models.o_auth_scope_o_auth_acg_enum import OAuthScopeOAuthACGEnum
from multiauthsample.models.suite_code_enum import SuiteCodeEnum
from multiauthsample.multiauthsample_client import MultiauthsampleClient

client = MultiauthsampleClient(
    access_token='accessToken',
    basic_auth_credentials=BasicAuthCredentials(
        username='Username',
        password='Password'
    ),
    api_key_credentials=ApiKeyCredentials(
        token='token',
        api_key='api-key'
    ),
    api_header_credentials=ApiHeaderCredentials(
        token='token',
        api_key='api-key'
    ),
    o_auth_ccg_credentials=OAuthCCGCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    ),
    o_auth_acg_credentials=OAuthACGCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_redirect_uri='OAuthRedirectUri',
        o_auth_scopes=[
            OAuthScopeOAuthACGEnum.READ_SCOPE
        ]
    ),
    o_auth_ropcg_credentials=OAuthROPCGCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_username='OAuthUsername',
        o_auth_password='OAuthPassword'
    ),
    o_auth_bearer_token_credentials=OAuthBearerTokenCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)
```

### Environment-Based Client Initialization

```python
from multiauthsample.multiauthsample_client import MultiauthsampleClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = MultiauthsampleClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](doc/environment-based-client-initialization.md) section for details.

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| production | - |
| testing | **Default** |

## Authorization

This API uses the following authentication schemes.

* [`basicAuth (Basic Authentication)`](doc/auth/basic-authentication.md)
* [`apiKey (Custom Query Parameter)`](doc/auth/custom-query-parameter.md)
* [`apiHeader (Custom Header Signature)`](doc/auth/custom-header-signature.md)
* [`OAuthCCG (OAuth 2 Client Credentials Grant)`](doc/auth/oauth-2-client-credentials-grant.md)
* [`OAuthACG (OAuth 2 Authorization Code Grant)`](doc/auth/oauth-2-authorization-code-grant.md)
* [`OAuthROPCG (OAuth 2 Resource Owner Credentials Grant)`](doc/auth/oauth-2-resource-owner-credentials-grant.md)
* [`OAuthBearerToken (OAuth 2 Bearer token)`](doc/auth/oauth-2-bearer-token.md)
* `CustomAuth (Custom Authentication)`

## List of APIs

* [Authentication](doc/controllers/authentication.md)

## SDK Infrastructure

### Configuration

* [ProxySettings](doc/proxy-settings.md)
* [Environment-Based Client Initialization](doc/environment-based-client-initialization.md)

### HTTP

* [HttpResponse](doc/http-response.md)
* [HttpRequest](doc/http-request.md)

### Utilities

* [ApiHelper](doc/api-helper.md)
* [HttpDateTime](doc/http-date-time.md)
* [RFC3339DateTime](doc/rfc3339-date-time.md)
* [UnixDateTime](doc/unix-date-time.md)

