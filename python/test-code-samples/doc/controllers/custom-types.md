# Custom Types

```python
custom_types_controller = client.custom_types
```

## Class Name

`CustomTypesController`

## Methods

* [Multi Dimensional Model Array Required](../../doc/controllers/custom-types.md#multi-dimensional-model-array-required)
* [Multi Dimensional Model Array Optional](../../doc/controllers/custom-types.md#multi-dimensional-model-array-optional)
* [Custom Type Map of Array and Array of Map Required](../../doc/controllers/custom-types.md#custom-type-map-of-array-and-array-of-map-required)
* [Custom Type Map of Array and Array of Map Optional](../../doc/controllers/custom-types.md#custom-type-map-of-array-and-array-of-map-optional)
* [Send Model in Form Required](../../doc/controllers/custom-types.md#send-model-in-form-required)
* [Send Model in Form Optional](../../doc/controllers/custom-types.md#send-model-in-form-optional)


# Multi Dimensional Model Array Required

```python
def multi_dimensional_model_array_required(self,
                                          employee_array,
                                          employee_array_optional=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `employee_array` | [`List[EmployeeRequired]`](../../doc/models/employee-required.md) | Form, Required | - |
| `employee_array_optional` | [`List[EmployeeRequired]`](../../doc/models/employee-required.md) | Form, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
employee_array = [
    [
        [
            [
                EmployeeRequired(
                    address='address0',
                    age=122,
                    name='name4',
                    uid='uid4',
                    department='department2',
                    boolean_var=False,
                    object_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                    dynamic_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                    date_time_unix_var=dateutil.datetime.utcfromtimestamp(1480809600),
                    r_fc_1123_var=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
                    r_fc_3339_var=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    date_var=dateutil.parser.parse('2016-03-13').date(),
                    dependents=[
                        Person(
                            address='address4',
                            age=28,
                            name='name8',
                            uid='uid8',
                            birthday=dateutil.parser.parse('2016-03-13').date(),
                            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                            person_type='Per'
                        ),
                        Person(
                            address='address4',
                            age=28,
                            name='name8',
                            uid='uid8',
                            birthday=dateutil.parser.parse('2016-03-13').date(),
                            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                            person_type='Per'
                        )
                    ],
                    hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
                    joining_day='Monday',
                    salary=82,
                    boss=Person(
                        address='address8',
                        age=94,
                        name='name2',
                        uid='uid2',
                        birthday=dateutil.parser.parse('2016-03-13').date(),
                        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                        person_type='Per'
                    ),
                    birthday=dateutil.parser.parse('2016-03-13').date(),
                    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    person_type='Empl'
                )
            ]
        ]
    ]
]

employee_array_optional = [
    [
        [
            [
                EmployeeRequired(
                    address='address0',
                    age=122,
                    name='name4',
                    uid='uid4',
                    department='department0',
                    boolean_var=False,
                    object_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                    dynamic_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                    date_time_unix_var=dateutil.datetime.utcfromtimestamp(1480809600),
                    r_fc_1123_var=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
                    r_fc_3339_var=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    date_var=dateutil.parser.parse('2016-03-13').date(),
                    dependents=[
                        Person(
                            address='address4',
                            age=28,
                            name='name8',
                            uid='uid8',
                            birthday=dateutil.parser.parse('2016-03-13').date(),
                            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                            person_type='Per'
                        ),
                        Person(
                            address='address4',
                            age=28,
                            name='name8',
                            uid='uid8',
                            birthday=dateutil.parser.parse('2016-03-13').date(),
                            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                            person_type='Per'
                        )
                    ],
                    hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
                    joining_day='Monday',
                    salary=70,
                    boss=Person(
                        address='address8',
                        age=94,
                        name='name2',
                        uid='uid2',
                        birthday=dateutil.parser.parse('2016-03-13').date(),
                        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                        person_type='Per'
                    ),
                    birthday=dateutil.parser.parse('2016-03-13').date(),
                    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    person_type='Empl'
                )
            ]
        ]
    ]
]

result = custom_types_controller.multi_dimensional_model_array_required(
    employee_array,
    employee_array_optional=employee_array_optional
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Multi Dimensional Model Array Optional

```python
def multi_dimensional_model_array_optional(self,
                                          employee_array=None,
                                          employee_array_optional=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `employee_array` | [`List[EmployeeRequired]`](../../doc/models/employee-required.md) | Form, Optional | - |
| `employee_array_optional` | [`List[EmployeeOptional]`](../../doc/models/employee-optional.md) | Form, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
employee_array = [
    [
        [
            [
                EmployeeRequired(
                    address='address0',
                    age=122,
                    name='name4',
                    uid='uid4',
                    department='department2',
                    boolean_var=False,
                    object_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                    dynamic_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                    date_time_unix_var=dateutil.datetime.utcfromtimestamp(1480809600),
                    r_fc_1123_var=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
                    r_fc_3339_var=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    date_var=dateutil.parser.parse('2016-03-13').date(),
                    dependents=[
                        Person(
                            address='address4',
                            age=28,
                            name='name8',
                            uid='uid8',
                            birthday=dateutil.parser.parse('2016-03-13').date(),
                            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                            person_type='Per'
                        ),
                        Person(
                            address='address4',
                            age=28,
                            name='name8',
                            uid='uid8',
                            birthday=dateutil.parser.parse('2016-03-13').date(),
                            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                            person_type='Per'
                        )
                    ],
                    hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
                    joining_day='Monday',
                    salary=82,
                    boss=Person(
                        address='address8',
                        age=94,
                        name='name2',
                        uid='uid2',
                        birthday=dateutil.parser.parse('2016-03-13').date(),
                        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                        person_type='Per'
                    ),
                    birthday=dateutil.parser.parse('2016-03-13').date(),
                    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    person_type='Empl'
                )
            ]
        ]
    ]
]

employee_array_optional = [
    [
        [
            [
                EmployeeOptional(
                    address='address0',
                    age=122,
                    name='name4',
                    uid='uid4',
                    department='department0',
                    boolean_var=False,
                    object_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                    dynamic_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                    date_time_unix_var=dateutil.datetime.utcfromtimestamp(1480809600),
                    joining_day='Monday',
                    birthday=dateutil.parser.parse('2016-03-13').date(),
                    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    person_type='Empl'
                )
            ]
        ]
    ]
]

result = custom_types_controller.multi_dimensional_model_array_optional(
    employee_array=employee_array,
    employee_array_optional=employee_array_optional
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Custom Type Map of Array and Array of Map Required

```python
def custom_type_map_of_array_and_array_of_map_required(self,
                                                      employee_array_of_map,
                                                      employee_map_of_array)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `employee_array_of_map` | [`EmployeeRequired`](../../doc/models/employee-required.md) | Form, Required | - |
| `employee_map_of_array` | `List[bool]` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
employee_array_of_map = EmployeeRequired(
    address='address0',
    age=122,
    name='name4',
    uid='uid4',
    department='department8',
    boolean_var=False,
    object_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    dynamic_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    date_time_unix_var=dateutil.datetime.utcfromtimestamp(1480809600),
    r_fc_1123_var=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
    r_fc_3339_var=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    date_var=dateutil.parser.parse('2016-03-13').date(),
    dependents=[
        Person(
            address='address4',
            age=28,
            name='name8',
            uid='uid8',
            birthday=dateutil.parser.parse('2016-03-13').date(),
            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            person_type='Per'
        )
    ],
    hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
    joining_day='Monday',
    salary=230,
    boss=Person(
        address='address8',
        age=94,
        name='name2',
        uid='uid2',
        birthday=dateutil.parser.parse('2016-03-13').date(),
        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        person_type='Per'
    ),
    birthday=dateutil.parser.parse('2016-03-13').date(),
    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    person_type='Empl'
)

employee_map_of_array = {
    'key0': [
        False,
        True
    ],
    'key1': [
        True,
        False,
        True
    ],
    'key2': [
        False
    ]
}

result = custom_types_controller.custom_type_map_of_array_and_array_of_map_required(
    employee_array_of_map,
    employee_map_of_array
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Custom Type Map of Array and Array of Map Optional

```python
def custom_type_map_of_array_and_array_of_map_optional(self,
                                                      employee_array_of_map=None,
                                                      employee_map_of_array=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `employee_array_of_map` | [`EmployeeRequired`](../../doc/models/employee-required.md) | Form, Optional | - |
| `employee_map_of_array` | `List[bool]` | Form, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
employee_array_of_map = EmployeeRequired(
    address='address0',
    age=122,
    name='name4',
    uid='uid4',
    department='department8',
    boolean_var=False,
    object_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    dynamic_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    date_time_unix_var=dateutil.datetime.utcfromtimestamp(1480809600),
    r_fc_1123_var=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
    r_fc_3339_var=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    date_var=dateutil.parser.parse('2016-03-13').date(),
    dependents=[
        Person(
            address='address4',
            age=28,
            name='name8',
            uid='uid8',
            birthday=dateutil.parser.parse('2016-03-13').date(),
            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            person_type='Per'
        )
    ],
    hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
    joining_day='Monday',
    salary=230,
    boss=Person(
        address='address8',
        age=94,
        name='name2',
        uid='uid2',
        birthday=dateutil.parser.parse('2016-03-13').date(),
        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        person_type='Per'
    ),
    birthday=dateutil.parser.parse('2016-03-13').date(),
    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    person_type='Empl'
)

employee_map_of_array = {
    'key0': [
        False,
        True
    ],
    'key1': [
        True,
        False,
        True
    ],
    'key2': [
        False
    ]
}

result = custom_types_controller.custom_type_map_of_array_and_array_of_map_optional(
    employee_array_of_map=employee_array_of_map,
    employee_map_of_array=employee_map_of_array
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Model in Form Required

```python
def send_model_in_form_required(self,
                               model,
                               model_optional=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | [`Dict[str, EmployeeRequired]`](../../doc/models/employee-required.md) | Form, Required | - |
| `model_optional` | [`Dict[str, EmployeeRequired]`](../../doc/models/employee-required.md) | Form, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
model = {
    'key0': EmployeeRequired(
        address='address0',
        age=122,
        name='name4',
        uid='uid4',
        department='department8',
        boolean_var=False,
        object_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        dynamic_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        date_time_unix_var=dateutil.datetime.utcfromtimestamp(1480809600),
        r_fc_1123_var=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
        r_fc_3339_var=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        date_var=dateutil.parser.parse('2016-03-13').date(),
        dependents=[
            Person(
                address='address4',
                age=28,
                name='name8',
                uid='uid8',
                birthday=dateutil.parser.parse('2016-03-13').date(),
                birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                person_type='Per'
            )
        ],
        hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
        joining_day='Tuesday',
        salary=240,
        boss=Person(
            address='address8',
            age=94,
            name='name2',
            uid='uid2',
            birthday=dateutil.parser.parse('2016-03-13').date(),
            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            person_type='Per'
        ),
        birthday=dateutil.parser.parse('2016-03-13').date(),
        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        person_type='Empl'
    ),
    'key1': EmployeeRequired(
        address='address0',
        age=122,
        name='name4',
        uid='uid4',
        department='department8',
        boolean_var=False,
        object_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        dynamic_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        date_time_unix_var=dateutil.datetime.utcfromtimestamp(1480809600),
        r_fc_1123_var=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
        r_fc_3339_var=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        date_var=dateutil.parser.parse('2016-03-13').date(),
        dependents=[
            Person(
                address='address4',
                age=28,
                name='name8',
                uid='uid8',
                birthday=dateutil.parser.parse('2016-03-13').date(),
                birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                person_type='Per'
            )
        ],
        hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
        joining_day='Tuesday',
        salary=240,
        boss=Person(
            address='address8',
            age=94,
            name='name2',
            uid='uid2',
            birthday=dateutil.parser.parse('2016-03-13').date(),
            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            person_type='Per'
        ),
        birthday=dateutil.parser.parse('2016-03-13').date(),
        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        person_type='Empl'
    )
}

model_optional = {
    'key0': EmployeeRequired(
        address='address0',
        age=122,
        name='name4',
        uid='uid4',
        department='department0',
        boolean_var=False,
        object_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        dynamic_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        date_time_unix_var=dateutil.datetime.utcfromtimestamp(1480809600),
        r_fc_1123_var=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
        r_fc_3339_var=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        date_var=dateutil.parser.parse('2016-03-13').date(),
        dependents=[
            Person(
                address='address4',
                age=28,
                name='name8',
                uid='uid8',
                birthday=dateutil.parser.parse('2016-03-13').date(),
                birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                person_type='Per'
            ),
            Person(
                address='address4',
                age=28,
                name='name8',
                uid='uid8',
                birthday=dateutil.parser.parse('2016-03-13').date(),
                birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                person_type='Per'
            ),
            Person(
                address='address4',
                age=28,
                name='name8',
                uid='uid8',
                birthday=dateutil.parser.parse('2016-03-13').date(),
                birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                person_type='Per'
            )
        ],
        hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
        joining_day='Sunday',
        salary=24,
        boss=Person(
            address='address8',
            age=94,
            name='name2',
            uid='uid2',
            birthday=dateutil.parser.parse('2016-03-13').date(),
            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            person_type='Per'
        ),
        birthday=dateutil.parser.parse('2016-03-13').date(),
        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        person_type='Empl'
    )
}

result = custom_types_controller.send_model_in_form_required(
    model,
    model_optional=model_optional
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Model in Form Optional

```python
def send_model_in_form_optional(self,
                               model,
                               model_optional=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | [`Dict[str, EmployeeOptional]`](../../doc/models/employee-optional.md) | Form, Required | - |
| `model_optional` | [`Dict[str, EmployeeOptional]`](../../doc/models/employee-optional.md) | Form, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
model = {
    'key0': EmployeeOptional(
        address='address0',
        age=122,
        name='name4',
        uid='uid4',
        department='department8',
        boolean_var=False,
        object_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        dynamic_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        date_time_unix_var=dateutil.datetime.utcfromtimestamp(1480809600),
        birthday=dateutil.parser.parse('2016-03-13').date(),
        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        person_type='Empl'
    ),
    'key1': EmployeeOptional(
        address='address0',
        age=122,
        name='name4',
        uid='uid4',
        department='department8',
        boolean_var=False,
        object_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        dynamic_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        date_time_unix_var=dateutil.datetime.utcfromtimestamp(1480809600),
        birthday=dateutil.parser.parse('2016-03-13').date(),
        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        person_type='Empl'
    )
}

model_optional = {
    'key0': EmployeeOptional(
        address='address0',
        age=122,
        name='name4',
        uid='uid4',
        department='department0',
        boolean_var=False,
        object_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        dynamic_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        date_time_unix_var=dateutil.datetime.utcfromtimestamp(1480809600),
        birthday=dateutil.parser.parse('2016-03-13').date(),
        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        person_type='Empl'
    )
}

result = custom_types_controller.send_model_in_form_optional(
    model,
    model_optional=model_optional
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

