
# Custom Header Signature



Documentation for accessing and setting credentials for VZ-M2M-Token.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| VZ-M2M-Token | `str` | M2M Session Token ([How to generate an M2M session token?](../../doc/controllers/session-management.md#start-connectivity-management-session)) | `vz_m2m_token` |



**Note:** Auth credentials can be set using `VZM2mTokenCredentials` object, passed in as named parameter `vz_m2m_token_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.verizon_client import VerizonClient

client = VerizonClient(
    vz_m2m_token_credentials=VZM2mTokenCredentials(
        vz_m2m_token='VZ-M2M-Token'
    )
)
```


