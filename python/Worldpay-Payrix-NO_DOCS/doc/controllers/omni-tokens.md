# Omni Tokens

OmniTokens stores information related to the activation of the resource for an entity. OmniToken's Valued Added Service helps protect transactions and reduce transaction risk.

```python
omni_tokens_controller = client.omni_tokens
```

## Class Name

`OmniTokensController`

## Methods

* [Get Omni Tokens Id](../../doc/controllers/omni-tokens.md#get-omni-tokens-id)
* [Put Omni Tokens Id](../../doc/controllers/omni-tokens.md#put-omni-tokens-id)
* [Get Omni Tokens](../../doc/controllers/omni-tokens.md#get-omni-tokens)
* [Post Omni Tokens](../../doc/controllers/omni-tokens.md#post-omni-tokens)


# Get Omni Tokens Id

Query a omniToken.

```python
def get_omni_tokens_id(self,
                      id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this OmniToken. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OmniTokensResponseResult`](../../doc/models/omni-tokens-response-result.md).

## Example Usage

```python
id = 't1_otk_6809db98230a5b02b08f00z'

result = omni_tokens_controller.get_omni_tokens_id(id)

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
        "id": "t1_otk_6809db98230a5b02b08f00z",
        "created": "2025-04-24 02:35:04.1649",
        "modified": "2025-04-24 02:35:04.1649",
        "creator": "t1_log_663ce214b2f25f2325a9935",
        "modifier": "t1_log_663ce214b2f25f2325a9935",
        "enablementDate": "2025-04-24 02:35:04",
        "org": "t1_org_5b0e08025ec790d3f9b8c00",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f21414978z0",
        "entity": "t1_ent_6809db6dd78923dadbfd904",
        "platform": "VCORE",
        "inactive": 0,
        "frozen": 0,
        "deleted": "2025-04-24 02:35:04",
        "deleter": ""
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


# Put Omni Tokens Id

Update a Token.

```python
def put_omni_tokens_id(self,
                      id,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this OmniToken. |
| `body` | [`OmniTokensPutRequest`](../../doc/models/omni-tokens-put-request.md) | Body, Required | Update OmniToken Request |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OmniTokensResponseResult`](../../doc/models/omni-tokens-response-result.md).

## Example Usage

```python
id = 't1_otk_6809db98230a5b02b08f00z'

body = OmniTokensPutRequest(
    enablement_date='2025-04-24 02:35:04',
    org='t1_org_5b0e08025ec790d3f9b8c00',
    division='t1_div_67c56806728fbbf0bae0b00',
    partition='t1_ptn_666834d4d504f21414978z0',
    entity='t1_ent_6809db6dd78923dadbfd904',
    platform=Platform1Enum.VCORE,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    deleted='2025-04-24 02:35:04',
    deleter=''
)

result = omni_tokens_controller.put_omni_tokens_id(
    id,
    body
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
        "id": "t1_otk_6809db98230a5b02b08f00z",
        "created": "2025-04-24 02:35:04.1649",
        "modified": "2025-04-24 02:35:04.1649",
        "creator": "t1_log_663ce214b2f25f2325a9935",
        "modifier": "t1_log_663ce214b2f25f2325a9935",
        "enablementDate": "2025-04-24 02:35:04",
        "org": "t1_org_5b0e08025ec790d3f9b8c00",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f21414978z0",
        "entity": "t1_ent_6809db6dd78923dadbfd904",
        "platform": "VCORE",
        "inactive": 0,
        "frozen": 0,
        "deleted": "2025-04-24 02:35:04",
        "deleter": ""
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


# Get Omni Tokens

Query a omniTokens.

```python
def get_omni_tokens(self,
                   search=None,
                   totals=None,
                   page_number=None,
                   page_limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `search` | `str` | Header, Optional | Set this header to filter or sort the list of resources that the method returns.<br>See [Searches](page:welcome#searches) for detailed information and examples on how to use search header. |
| `totals` | `str` | Header, Optional | To configure a request to return a total for all instances of a field in a result set,  use the totals header in the format `totals={operator}[]={key}`.  This will calculate the desired total and return it in the `details > totals` object of the response.  For instance, if you want to sum the `total` field of all transactions,  you would use the `sum` operator. The response will include the result set,  along with the calculated total in the `details` section. See [Collection Operators](page:welcome#collection-operators) for detailed information and examples on how to use totals header. |
| `page_number` | `int` | Query, Optional | Set this path parameter to request a specific page of records.<br>For example, set `?page[number]=2` to retrieve the second page of records for this request. |
| `page_limit` | `int` | Query, Optional | Set this path parameter to request up to a specific amount of records. By default 30 records are retrieved per page. The maximum limit that can be set is 100.<br>For example, set `?page[limit]=50` to retrieve up to 50 records for this request. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OmniTokensResponseResult`](../../doc/models/omni-tokens-response-result.md).

## Example Usage

```python
search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = omni_tokens_controller.get_omni_tokens(
    search=search,
    totals=totals,
    page_number=page_number,
    page_limit=page_limit
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
        "id": "t1_otk_6809db98230a5b02b08f00z",
        "created": "2025-04-24 02:35:04.1649",
        "modified": "2025-04-24 02:35:04.1649",
        "creator": "t1_log_663ce214b2f25f2325a9935",
        "modifier": "t1_log_663ce214b2f25f2325a9935",
        "enablementDate": "2025-04-24 02:35:04",
        "org": "t1_org_5b0e08025ec790d3f9b8c00",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f21414978z0",
        "entity": "t1_ent_6809db6dd78923dadbfd904",
        "platform": "VCORE",
        "inactive": 0,
        "frozen": 0,
        "deleted": "2025-04-24 02:35:04",
        "deleter": ""
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


# Post Omni Tokens

Create a omniTokens.

```python
def post_omni_tokens(self,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`OmniTokensPostRequest`](../../doc/models/omni-tokens-post-request.md) | Body, Required | Create omniTokens |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OmniTokensResponseResult`](../../doc/models/omni-tokens-response-result.md).

## Example Usage

```python
body = OmniTokensPostRequest(
    enablement_date='2025-04-24 02:35:04',
    org='t1_org_5b0e08025ec790d3f9b8c00',
    division='t1_div_67c56806728fbbf0bae0b00',
    partition='t1_ptn_666834d4d504f21414978z0',
    entity='t1_ent_6809db6dd78923dadbfd904',
    platform=Platform1Enum.VCORE,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    deleted='2025-04-24 02:35:04',
    deleter=''
)

result = omni_tokens_controller.post_omni_tokens(body)

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
        "id": "t1_otk_6809db98230a5b02b08f00z",
        "created": "2025-04-24 02:35:04.1649",
        "modified": "2025-04-24 02:35:04.1649",
        "creator": "t1_log_663ce214b2f25f2325a9935",
        "modifier": "t1_log_663ce214b2f25f2325a9935",
        "enablementDate": "2025-04-24 02:35:04",
        "org": "t1_org_5b0e08025ec790d3f9b8c00",
        "division": "t1_div_67c56806728fbbf0bae0b00",
        "partition": "t1_ptn_666834d4d504f21414978z0",
        "entity": "t1_ent_6809db6dd78923dadbfd904",
        "platform": "VCORE",
        "inactive": 0,
        "frozen": 0,
        "deleted": "2025-04-24 02:35:04",
        "deleter": ""
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

