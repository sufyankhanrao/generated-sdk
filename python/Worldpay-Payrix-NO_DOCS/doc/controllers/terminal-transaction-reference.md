# Terminal Transaction Reference

```python
terminal_transaction_reference_controller = client.terminal_transaction_reference
```

## Class Name

`TerminalTransactionReferenceController`


# Post Terminal Txn Refs

Create a terminalTxnRefs resource, which represents a reference code issued by the Processor in relation to a particular Transaction.

```python
def post_terminal_txn_refs(self,
                          body,
                          request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TerminalTxnRefPostRequest`](../../doc/models/terminal-txn-ref-post-request.md) | Body, Required | Create Terminal Transaction Reference Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalTxnRefResponseResult`](../../doc/models/terminal-txn-ref-response-result.md).

## Example Usage

```python
body = TerminalTxnRefPostRequest(
    terminal_txn='t1_ttx_6806cde42b47ee61cdf6ab9',
    ref='MCC000012',
    stage=TerminalTxnRefStageEnum.AUTHORIZATION,
    platform=Platform1Enum.VCORE
)

request_token = '20250423-yourmerchant-refunds-001'

result = terminal_transaction_reference_controller.post_terminal_txn_refs(
    body,
    request_token=request_token
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "response": {
    "data": [
      {
        "id": "t1_ttr_6806cde43831bc88d5f4e00",
        "created": "2025-04-21 18:59:48.2388",
        "modified": "2025-04-21 18:59:48.2388",
        "creator": "t1_log_62fd0aa37c3d8ec3a9dcea8",
        "modifier": "t1_log_62fd0aa37c3d8ec3a9dcea8",
        "terminalTxn": "t1_ttx_6806cde42b47ee61cdf6ab9",
        "ref": "MCC000012",
        "stage": "auth",
        "platform": "VCORE"
      }
    ],
    "details": {
      "requestId": "1",
      "totals": [],
      "page": {
        "current": 1,
        "last": 1,
        "hasMore": false
      }
    },
    "errors": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ErrorFourHundredException`](../../doc/models/error-four-hundred-exception.md) |

