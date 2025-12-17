# Revenue Boosts

```python
revenue_boosts_controller = client.revenue_boosts
```

## Class Name

`RevenueBoostsController`

## Methods

* [Get Revenue Boosts Id](../../doc/controllers/revenue-boosts.md#get-revenue-boosts-id)
* [Get Revenue Boosts](../../doc/controllers/revenue-boosts.md#get-revenue-boosts)
* [Post Revenue Boosts](../../doc/controllers/revenue-boosts.md#post-revenue-boosts)


# Get Revenue Boosts Id

Query a RevenueBoost

```python
def get_revenue_boosts_id(self,
                         id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`RevenueBoostsResponseResult`](../../doc/models/revenue-boosts-response-result.md).

## Example Usage

```python
id = 't1_rev_12a003cde5d6b2ec3d9canb'

result = revenue_boosts_controller.get_revenue_boosts_id(id)

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
        "id": "t1_rev_67a18bcde1a1b2ec3d9c9az",
        "created": "2025-01-31 08:42:16.7318",
        "modified": "2025-01-31 08:42:16.7318",
        "creator": "t1_log_0092b50e8812b18e41d511s",
        "modifier": "t1_log_0092b50e8812b18e41d511s",
        "entity": "t1_ent_681238635755abf676f300f",
        "enablementDate": "2025-04-30 12:00:09",
        "org": "t1_org_11b51635da21f7399ce2af1",
        "division": "t1_div_67b51635da21f7399ce2af1",
        "partition": "t1_ptn_666834d4d504f11234578f5",
        "platform": "VCORE",
        "inactive": 0,
        "frozen": 0,
        "enableRevenueBoost": 1,
        "resourceId": "110821978",
        "deleted": "2025-04-30 12:00:09",
        "deleter": "t1_log_0092b50e8812b18e41d511s"
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


# Get Revenue Boosts

Query revenue boosts

```python
def get_revenue_boosts(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`RevenueBoostsResponseResult`](../../doc/models/revenue-boosts-response-result.md).

## Example Usage

```python
search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = revenue_boosts_controller.get_revenue_boosts(
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
        "id": "t1_rev_67a18bcde1a1b2ec3d9c9az",
        "created": "2025-01-31 08:42:16.7318",
        "modified": "2025-01-31 08:42:16.7318",
        "creator": "t1_log_0092b50e8812b18e41d511s",
        "modifier": "t1_log_0092b50e8812b18e41d511s",
        "entity": "t1_ent_681238635755abf676f300f",
        "enablementDate": "2025-04-30 12:00:09",
        "org": "t1_org_11b51635da21f7399ce2af1",
        "division": "t1_div_67b51635da21f7399ce2af1",
        "partition": "t1_ptn_666834d4d504f11234578f5",
        "platform": "VCORE",
        "inactive": 0,
        "frozen": 0,
        "enableRevenueBoost": 1,
        "resourceId": "110821978",
        "deleted": "2025-04-30 12:00:09",
        "deleter": "t1_log_0092b50e8812b18e41d511s"
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


# Post Revenue Boosts

Create a Value Added Service networkPaymentManager

```python
def post_revenue_boosts(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`RevenueBoostsPostRequest`](../../doc/models/revenue-boosts-post-request.md) | Body, Required | Add RevenueBoosts Request |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`RevenueBoostsResponseResult`](../../doc/models/revenue-boosts-response-result.md).

## Example Usage

```python
body = RevenueBoostsPostRequest(
    entity='t1_ent_5a1pf5a1234531155a12345',
    platform='VCORE',
    org='t1_org_5a1pf5a1234531155a12345',
    division='t1_div_67b51635da21f7399ce2af1',
    partition='t1_ptn_666834d4d504f11234578f5',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

result = revenue_boosts_controller.post_revenue_boosts(body)

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
        "id": "t1_rev_67a18bcde1a1b2ec3d9c9az",
        "created": "2025-01-31 08:42:16.7318",
        "modified": "2025-01-31 08:42:16.7318",
        "creator": "t1_log_0092b50e8812b18e41d511s",
        "modifier": "t1_log_0092b50e8812b18e41d511s",
        "entity": "t1_ent_681238635755abf676f300f",
        "enablementDate": "2025-04-30 12:00:09",
        "org": "t1_org_11b51635da21f7399ce2af1",
        "division": "t1_div_67b51635da21f7399ce2af1",
        "partition": "t1_ptn_666834d4d504f11234578f5",
        "platform": "VCORE",
        "inactive": 0,
        "frozen": 0,
        "enableRevenueBoost": 1,
        "resourceId": "110821978",
        "deleted": "2025-04-30 12:00:09",
        "deleter": "t1_log_0092b50e8812b18e41d511s"
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

