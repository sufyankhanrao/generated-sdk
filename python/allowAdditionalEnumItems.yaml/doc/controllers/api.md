# API

```python
client_controller = client.client
```

## Class Name

`APIController`


# Get Enums

```python
def get_enums(self,
             test_case=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `test_case` | [`TestCaseEnum`](../../doc/models/test-case-enum.md) | Query, Optional | - |

## Response Type

[`EnumsAllowAdditionalResponse`](../../doc/models/enums-allow-additional-response.md)

## Example Usage

```python
result = client_controller.get_enums()
print(result)
```

