
# Custom Header Signature



Documentation for accessing and setting credentials for user-id.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| user-id | `str` | User ID | `user_id` |



**Note:** Auth credentials can be set using `UserIdCredentials` object, passed in as named parameter `user_id_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.user_id import UserIdCredentials

client = FortisapiClient(
    user_id_credentials=UserIdCredentials(
        user_id='user-id'
    )
)
```


