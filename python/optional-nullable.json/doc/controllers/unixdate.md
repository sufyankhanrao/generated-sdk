# Unixdate

```python
unixdate_controller = client.unixdate
```

## Class Name

`UnixdateController`

## Methods

* [Create Send Unix Date](../../doc/controllers/unixdate.md#create-send-unix-date)
* [Create Send Unix Date Array](../../doc/controllers/unixdate.md#create-send-unix-date-array)
* [Create Send Unix Date Map](../../doc/controllers/unixdate.md#create-send-unix-date-map)


# Create Send Unix Date

```python
def create_send_unix_date(self,
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
| `date` | [`UnixDate`](../../doc/models/unix-date.md) | Body, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
un_set = False

set_to_null = False

field = 'field6'

date = UnixDate(
    date_time_1=dateutil.datetime.utcfromtimestamp(1484719381),
    date_time=dateutil.datetime.utcfromtimestamp(1484719381)
)

result = unix_date_controller.create_send_unix_date(
    un_set,
    set_to_null,
    field,
    date
)
print(result)
```


# Create Send Unix Date Array

```python
def create_send_unix_date_array(self,
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
| `date` | [`UnixDateArray`](../../doc/models/unix-date-array.md) | Body, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
un_set = False

set_to_null = False

field = 'field6'

date = UnixDateArray(
    date_time_1=[
        dateutil.datetime.utcfromtimestamp(1480809600),
        dateutil.datetime.utcfromtimestamp(1480809600)
    ]
)

result = unix_date_controller.create_send_unix_date_array(
    un_set,
    set_to_null,
    field,
    date
)
print(result)
```


# Create Send Unix Date Map

```python
def create_send_unix_date_map(self,
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
| `date` | [`UnixDateMap`](../../doc/models/unix-date-map.md) | Body, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
un_set = False

set_to_null = False

field = 'field6'

date = UnixDateMap(
    date_time_1={
        'key0': dateutil.datetime.utcfromtimestamp(1480809600),
        'key1': dateutil.datetime.utcfromtimestamp(1480809600)
    }
)

result = unix_date_controller.create_send_unix_date_map(
    un_set,
    set_to_null,
    field,
    date
)
print(result)
```

