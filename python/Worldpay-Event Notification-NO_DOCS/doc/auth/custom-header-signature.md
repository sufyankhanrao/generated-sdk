
# Custom Header Signature



Documentation for accessing and setting credentials for api_key.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| Authorization | `str` | License format is WORLDPAY license="xxxx" | `authorization` |



**Note:** Auth credentials can be set using `CustomHeaderAuthenticationCredentials` object, passed in as named parameter `custom_header_authentication_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from enterpriseapimerchantaccountcreated.enterpriseapimerchantaccountcreated_client import EnterpriseapimerchantaccountcreatedClient
from enterpriseapimerchantaccountcreated.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials

client = EnterpriseapimerchantaccountcreatedClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    )
)
```


