# Simpledate

```python
simpledate_controller = client.simpledate
```

## Class Name

`SimpledateController`

## Methods

* [Create Send Simple Date](../../doc/controllers/simpledate.md#create-send-simple-date)
* [Create Send Simple Date Array](../../doc/controllers/simpledate.md#create-send-simple-date-array)


# Create Send Simple Date

```python
def create_send_simple_date(self,
                           un_set,
                           set_to_null,
                           field,
                           date)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `un_set` | `bool` | Query, Required | - |
| `set_to_null` | `bool` | Query, Required | - |
| `field` | `str` | Query, Required | - |
| `date` | [`SimpleDate`](../../doc/models/simple-date.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
un_set = False

set_to_null = False

field = 'field6'

date = SimpleDate(
    date_nullable=dateutil.parser.parse('1994-02-13').date(),
    date=dateutil.parser.parse('1994-02-13').date()
)

result = simple_date_controller.create_send_simple_date(
    un_set,
    set_to_null,
    field,
    date
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Send Simple Date Array

```python
def create_send_simple_date_array(self,
                                 un_set,
                                 set_to_null,
                                 field,
                                 date)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `un_set` | `bool` | Query, Required | - |
| `set_to_null` | `bool` | Query, Required | - |
| `field` | `str` | Query, Required | - |
| `date` | [`SimpleDateArray`](../../doc/models/simple-date-array.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
un_set = False

set_to_null = False

field = 'field6'

date = SimpleDateArray(
    date=[
        dateutil.parser.parse('1994-02-13').date(),
        dateutil.parser.parse('1994-02-14').date()
    ],
    date_1=[
        dateutil.parser.parse('1994-02-13').date(),
        dateutil.parser.parse('1994-02-14').date()
    ]
)

result = simple_date_controller.create_send_simple_date_array(
    un_set,
    set_to_null,
    field,
    date
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

