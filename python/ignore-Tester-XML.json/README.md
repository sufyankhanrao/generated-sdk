
# Getting Started with Tester-XML

## Building

You must have Python `3.7+` installed on your system to install and run this SDK. This SDK package depends on other Python packages like pytest, etc. These dependencies are defined in the `requirements.txt` file that comes with the SDK. To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type `pip --version`. This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including `requirements.txt`) for the SDK.
* Run the command `pip install -r requirements.txt`. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Testerxml-Python&step=installDependencies)

## Installation

The following section explains how to use the testerxml library in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Testerxml-Python&step=pyCharm)

Click on `Open` in PyCharm to browse to your generated SDK directory and then click `OK`.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Testerxml-Python&step=openProject0)

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Testerxml-Python&projectName=testerxml&step=openProject1)

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Testerxml-Python&projectName=testerxml&step=createDirectory)

Name the directory as "test".

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Testerxml-Python&step=nameDirectory)

Add a python file to this project.

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Testerxml-Python&projectName=testerxml&step=createFile)

Name it "testSDK".

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?workspaceFolder=Testerxml-Python&projectName=testerxml&step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```python
from testerxml.testerxml_client import TesterxmlClient
```

![Add a new project in PyCharm - Step 5](https://apidocs.io/illustration/python?workspaceFolder=Testerxml-Python&projectName=testerxml&libraryName=testerxml.testerxml_client&className=TesterxmlClient&step=projectFiles)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on `Run`

![Run Test Project - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Testerxml-Python&projectName=testerxml&libraryName=testerxml.testerxml_client&className=TesterxmlClient&step=runProject)

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| environment | `Environment` | The API environment. <br> **Default: `Environment.TESTING`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 60** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 0** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |

The API client can be initialized as follows:

### Code-Based Client Initialization

```python
from testerxml.configuration import Environment
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)
```

### Environment-Based Client Initialization

```python
from testerxml.testerxml_client import TesterxmlClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = TesterxmlClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](doc/environment-based-client-initialization.md) section for details.

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| production | - |
| testing | **Default** http://localhost:3000/body-xml |

## List of APIs

* [Discriminateusingattribute](doc/controllers/discriminateusingattribute.md)
* [Discriminateusingelement](doc/controllers/discriminateusingelement.md)
* [Simple Attributes Model](doc/controllers/simple-attributes-model.md)
* [Attributes Model With Inheritance](doc/controllers/attributes-model-with-inheritance.md)
* [Nested Attributes Model](doc/controllers/nested-attributes-model.md)
* [Simple Elements Model](doc/controllers/simple-elements-model.md)
* [Elements Model With Inheritance](doc/controllers/elements-model-with-inheritance.md)
* [Nested Elements Model](doc/controllers/nested-elements-model.md)
* [Single Element Model With Model Node Name](doc/controllers/single-element-model-with-model-node-name.md)
* [Attributes and Elements Model](doc/controllers/attributes-and-elements-model.md)
* [String Enumeration](doc/controllers/string-enumeration.md)
* [Integer Enumeration](doc/controllers/integer-enumeration.md)
* [Elements Array](doc/controllers/elements-array.md)
* [Named Elements Array](doc/controllers/named-elements-array.md)
* [Wrapped Array](doc/controllers/wrapped-array.md)
* [Wrapped and Named Array](doc/controllers/wrapped-and-named-array.md)
* [Simple Integer](doc/controllers/simple-integer.md)
* [Simple Precision](doc/controllers/simple-precision.md)
* [Simple Long](doc/controllers/simple-long.md)
* [Simple String](doc/controllers/simple-string.md)
* [Simple UUID](doc/controllers/simple-uuid.md)

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

