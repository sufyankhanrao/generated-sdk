
# Client Class Documentation

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
| proxy_settings | [`ProxySettings`](../doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |

The API client can be initialized as follows:

## Code-Based Client Initialization

```python
from testerxml.configuration import Environment
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)
```

## Environment-Based Client Initialization

```python
from testerxml.testerxml_client import TesterxmlClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = TesterxmlClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](../doc/environment-based-client-initialization.md) section for details.

## Tester-XML Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| discriminate_using_attribute | Gets DiscriminateUsingAttribute |
| discriminate_using_element | Gets DiscriminateUsingElement |
| simple_attributes_model | Gets SimpleAttributesModel |
| attributes_model_with_inheritance | Gets AttributesModelWithInheritance |
| nested_attributes_model | Gets NestedAttributesModel |
| simple_elements_model | Gets SimpleElementsModel |
| elements_model_with_inheritance | Gets ElementsModelWithInheritance |
| nested_elements_model | Gets NestedElementsModel |
| single_element_model_with_model_node_name | Gets SingleElementModelWithModelNodeName |
| attributes_and_elements_model | Gets AttributesAndElementsModel |
| string_enumeration | Gets StringEnumeration |
| integer_enumeration | Gets IntegerEnumeration |
| elements_array | Gets ElementsArray |
| named_elements_array | Gets NamedElementsArray |
| wrapped_array | Gets WrappedArray |
| wrapped_and_named_array | Gets WrappedAndNamedArray |
| simple_integer | Gets SimpleInteger |
| simple_precision | Gets SimplePrecision |
| simple_long | Gets SimpleLong |
| simple_string | Gets SimpleString |
| simple_uuid | Gets SimpleUUID |

