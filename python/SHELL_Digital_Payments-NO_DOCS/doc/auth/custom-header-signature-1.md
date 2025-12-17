
# Custom Header Signature



Documentation for accessing and setting credentials for oAuthTokenPost.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| X-Apigee-Authorization | `str` | APIGEE access token ([How to obtain APIGEE access token?](page:guided-walkthrough/walkthrough1)) | `x_apigee_authorization` |



**Note:** Auth credentials can be set using `OAuthTokenPostCredentials` object, passed in as named parameter `o_auth_token_post_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from shelldigitalpayments.http.auth.o_auth_token_post import OAuthTokenPostCredentials
from shelldigitalpayments.shell_digital_payments_client import ShellDigitalPaymentsClient

client = ShellDigitalPaymentsClient(
    o_auth_token_post_credentials=OAuthTokenPostCredentials(
        x_apigee_authorization='X-Apigee-Authorization'
    )
)
```


