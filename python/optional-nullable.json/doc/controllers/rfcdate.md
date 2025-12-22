# Rfcdate

```python
rfcdate_controller = client.rfcdate
```

## Class Name

`RfcdateController`

## Methods

* [Create Send Rfc 1123 Date](../../doc/controllers/rfcdate.md#create-send-rfc-1123-date)
* [Create Send Rfc 1123 Date Array](../../doc/controllers/rfcdate.md#create-send-rfc-1123-date-array)
* [Create Send Rfc 1123 Date Map](../../doc/controllers/rfcdate.md#create-send-rfc-1123-date-map)


# Create Send Rfc 1123 Date

```python
def create_send_rfc_1123_date(self,
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
| `date` | [`Rfc1123Date`](../../doc/models/rfc-1123-date.md) | Body, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
un_set = False

set_to_null = False

field = 'field6'

date = Rfc1123Date(
    date_time_1=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime
)

result = rfc_date_controller.create_send_rfc_1123_date(
    un_set,
    set_to_null,
    field,
    date
)
print(result)
```


# Create Send Rfc 1123 Date Array

```python
def create_send_rfc_1123_date_array(self,
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
| `date` | [`Rfc1123DateArray`](../../doc/models/rfc-1123-date-array.md) | Body, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
un_set = False

set_to_null = False

field = 'field6'

date = Rfc1123DateArray(
    date_time_1=[
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime
    ]
)

result = rfc_date_controller.create_send_rfc_1123_date_array(
    un_set,
    set_to_null,
    field,
    date
)
print(result)
```


# Create Send Rfc 1123 Date Map

```python
def create_send_rfc_1123_date_map(self,
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
| `date` | [`Rfc1123DateMap`](../../doc/models/rfc-1123-date-map.md) | Body, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
un_set = False

set_to_null = False

field = 'field6'

date = Rfc1123DateMap(
    date_time_1={
        'key0': APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
        'key1': APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime
    }
)

result = rfc_date_controller.create_send_rfc_1123_date_map(
    un_set,
    set_to_null,
    field,
    date
)
print(result)
```

