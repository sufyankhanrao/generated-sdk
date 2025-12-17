
# Custom Header Signature



Documentation for accessing and setting credentials for password.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| PASSWORD | `str` | - | `password` |



**Note:** Auth credentials can be set using `PasswordCredentials` object, passed in as named parameter `password_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from payrix.http.auth.password import PasswordCredentials
from payrix.payrix_client import PayrixClient

client = PayrixClient(
    password_credentials=PasswordCredentials(
        password='PASSWORD'
    )
)
```


