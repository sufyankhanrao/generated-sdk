
# Custom Header Signature



Documentation for accessing and setting credentials for username.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| USERNAME | `str` | - | `username` |



**Note:** Auth credentials can be set using `UsernameCredentials` object, passed in as named parameter `username_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from payrix.http.auth.username import UsernameCredentials
from payrix.payrix_client import PayrixClient

client = PayrixClient(
    username_credentials=UsernameCredentials(
        username='USERNAME'
    )
)
```


