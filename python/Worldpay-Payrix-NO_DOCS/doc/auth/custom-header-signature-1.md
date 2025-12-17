
# Custom Header Signature



Documentation for accessing and setting credentials for sessionKey.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| SESSIONKEY | `str` | - | `sessionkey` |



**Note:** Auth credentials can be set using `SessionKeyCredentials` object, passed in as named parameter `session_key_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.payrix_client import PayrixClient

client = PayrixClient(
    session_key_credentials=SessionKeyCredentials(
        sessionkey='SESSIONKEY'
    )
)
```


