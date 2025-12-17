
# Custom Header Signature



Documentation for accessing and setting credentials for MppToken.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| Authorization | `str` | Digital Payments access token ([How to obtain Digital Payments access token?](page:guided-walkthrough/walkthrough1)) | `authorization` |



**Note:** Auth credentials can be set using `MppTokenCredentials` object, passed in as named parameter `mpp_token_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from shelldigitalpayments.http.auth.mpp_token import MppTokenCredentials
from shelldigitalpayments.shell_digital_payments_client import ShellDigitalPaymentsClient

client = ShellDigitalPaymentsClient(
    mpp_token_credentials=MppTokenCredentials(
        authorization='Authorization'
    )
)
```


