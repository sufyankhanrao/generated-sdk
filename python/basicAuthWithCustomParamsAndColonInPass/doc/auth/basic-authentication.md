
# Basic Authentication



Documentation for accessing and setting credentials for httpBasic.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| username | `str` | - | `username` |
| password | `str` | - | `password` |



**Note:** Auth credentials can be set using `BasicAuthCredentials` object, passed in as named parameter `basic_auth_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from batesterparamscoloninpassword.batesterparamscoloninpassword_client import BatesterparamscoloninpasswordClient
from batesterparamscoloninpassword.http.auth.basic_auth import BasicAuthCredentials

client = BatesterparamscoloninpasswordClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='username',
        password='password'
    )
)
```


