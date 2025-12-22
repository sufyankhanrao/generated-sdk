# Native Types

```python
native_types_controller = client.native_types
```

## Class Name

`NativeTypesController`

## Methods

* [Send String Boolean Object Dynamic Required](../../doc/controllers/native-types.md#send-string-boolean-object-dynamic-required)
* [Send String Boolean Object Dynamic Optional](../../doc/controllers/native-types.md#send-string-boolean-object-dynamic-optional)
* [Send Date and Time Required](../../doc/controllers/native-types.md#send-date-and-time-required)
* [Send Date and Time Optional](../../doc/controllers/native-types.md#send-date-and-time-optional)
* [Multi Dimensional Native Array Required](../../doc/controllers/native-types.md#multi-dimensional-native-array-required)
* [Multi Dimensional Native Array Optional](../../doc/controllers/native-types.md#multi-dimensional-native-array-optional)
* [Native Map of Array and Array of Map Required](../../doc/controllers/native-types.md#native-map-of-array-and-array-of-map-required)
* [Native Map of Array and Array of Map Optional](../../doc/controllers/native-types.md#native-map-of-array-and-array-of-map-optional)


# Send String Boolean Object Dynamic Required

```python
def send_string_boolean_object_dynamic_required(self,
                                               string_var,
                                               boolean_var,
                                               object_var,
                                               dynamic_var)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `string_var` | `str` | Form, Required | - |
| `boolean_var` | `bool` | Form, Required | - |
| `object_var` | `Any` | Form, Required | - |
| `dynamic_var` | `Any` | Form, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
string_var = 'stringVar8'

boolean_var = False

object_var = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

dynamic_var = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

result = native_types_controller.send_string_boolean_object_dynamic_required(
    string_var,
    boolean_var,
    object_var,
    dynamic_var
)
print(result)
```


# Send String Boolean Object Dynamic Optional

```python
def send_string_boolean_object_dynamic_optional(self,
                                               string_var=None,
                                               boolean_var=None,
                                               object_var=None,
                                               dynamic_var=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `string_var` | `str` | Form, Optional | - |
| `boolean_var` | `bool` | Form, Optional | - |
| `object_var` | `Any` | Form, Optional | - |
| `dynamic_var` | `Any` | Form, Optional | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
string_var = 'stringVar8'

boolean_var = False

object_var = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

dynamic_var = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

result = native_types_controller.send_string_boolean_object_dynamic_optional(
    string_var=string_var,
    boolean_var=boolean_var,
    object_var=object_var,
    dynamic_var=dynamic_var
)
print(result)
```


# Send Date and Time Required

```python
def send_date_and_time_required(self,
                               unix_date_time_var,
                               rfc_1123_date_time_var,
                               rfc_3339_date_time,
                               date_var)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `unix_date_time_var` | `datetime` | Form, Required | - |
| `rfc_1123_date_time_var` | `datetime` | Form, Required | - |
| `rfc_3339_date_time` | `datetime` | Form, Required | - |
| `date_var` | `date` | Form, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
unix_date_time_var = dateutil.datetime.utcfromtimestamp(1480809600)

rfc_1123_date_time_var = APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime

rfc_3339_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

date_var = dateutil.parser.parse('2016-03-13').date()

result = native_types_controller.send_date_and_time_required(
    unix_date_time_var,
    rfc_1123_date_time_var,
    rfc_3339_date_time,
    date_var
)
print(result)
```


# Send Date and Time Optional

```python
def send_date_and_time_optional(self,
                               unix_date_time_var=None,
                               rfc_1123_date_time_var=None,
                               rfc_3339_date_time=None,
                               date_var=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `unix_date_time_var` | `datetime` | Form, Optional | - |
| `rfc_1123_date_time_var` | `datetime` | Form, Optional | - |
| `rfc_3339_date_time` | `datetime` | Form, Optional | - |
| `date_var` | `date` | Form, Optional | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
unix_date_time_var = dateutil.datetime.utcfromtimestamp(1480809600)

rfc_1123_date_time_var = APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime

rfc_3339_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

date_var = dateutil.parser.parse('2016-03-13').date()

result = native_types_controller.send_date_and_time_optional(
    unix_date_time_var=unix_date_time_var,
    rfc_1123_date_time_var=rfc_1123_date_time_var,
    rfc_3339_date_time=rfc_3339_date_time,
    date_var=date_var
)
print(result)
```


# Multi Dimensional Native Array Required

```python
def multi_dimensional_native_array_required(self,
                                           boolean_array)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `boolean_array` | `List[bool]` | Form, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
boolean_array = [
    [
        [
            [
                True,
                False
            ],
            [
                True,
                False
            ]
        ],
        [
            [
                True,
                False
            ],
            [
                True,
                False
            ]
        ]
    ],
    [
        [
            [
                True,
                False
            ],
            [
                True,
                False
            ]
        ],
        [
            [
                True,
                False
            ],
            [
                True,
                False
            ]
        ]
    ]
]

result = native_types_controller.multi_dimensional_native_array_required(boolean_array)
print(result)
```


# Multi Dimensional Native Array Optional

```python
def multi_dimensional_native_array_optional(self,
                                           boolean_array=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `boolean_array` | `List[bool]` | Form, Optional | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
boolean_array = [
    [
        [
            [
                True,
                False
            ],
            [
                True,
                False
            ]
        ],
        [
            [
                True,
                False
            ],
            [
                True,
                False
            ]
        ]
    ],
    [
        [
            [
                True,
                False
            ],
            [
                True,
                False
            ]
        ],
        [
            [
                True,
                False
            ],
            [
                True,
                False
            ]
        ]
    ]
]

result = native_types_controller.multi_dimensional_native_array_optional(
    boolean_array=boolean_array
)
print(result)
```


# Native Map of Array and Array of Map Required

```python
def native_map_of_array_and_array_of_map_required(self,
                                                 boolean_array_of_map,
                                                 boolean_map_of_array)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `boolean_array_of_map` | `bool` | Form, Required | - |
| `boolean_map_of_array` | `List[bool]` | Form, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
boolean_array_of_map = False

boolean_map_of_array = {
    'key0': [
        False
    ]
}

result = native_types_controller.native_map_of_array_and_array_of_map_required(
    boolean_array_of_map,
    boolean_map_of_array
)
print(result)
```


# Native Map of Array and Array of Map Optional

```python
def native_map_of_array_and_array_of_map_optional(self,
                                                 boolean_array_of_map=None,
                                                 boolean_map_of_array=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `boolean_array_of_map` | `bool` | Form, Optional | - |
| `boolean_map_of_array` | `List[bool]` | Form, Optional | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
boolean_array_of_map = False

boolean_map_of_array = {
    'key0': [
        False
    ]
}

result = native_types_controller.native_map_of_array_and_array_of_map_optional(
    boolean_array_of_map=boolean_array_of_map,
    boolean_map_of_array=boolean_map_of_array
)
print(result)
```

