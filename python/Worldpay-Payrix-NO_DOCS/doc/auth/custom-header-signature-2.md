
# Custom Header Signature



Documentation for accessing and setting credentials for txnSessionKey.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| TXNSESSIONKEY | `str` | - | `txnsessionkey` |



**Note:** Auth credentials can be set using `TxnSessionKeyCredentials` object, passed in as named parameter `txn_session_key_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.payrix_client import PayrixClient

client = PayrixClient(
    txn_session_key_credentials=TxnSessionKeyCredentials(
        txnsessionkey='TXNSESSIONKEY'
    )
)
```


