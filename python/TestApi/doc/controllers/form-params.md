# Form Params

```python
form_params_controller = client.form_params
```

## Class Name

`FormParamsController`

## Methods

* [Send Delete Form](../../doc/controllers/form-params.md#send-delete-form)
* [Send Delete Multipart](../../doc/controllers/form-params.md#send-delete-multipart)
* [Send Date Array](../../doc/controllers/form-params.md#send-date-array)
* [Send Date](../../doc/controllers/form-params.md#send-date)
* [Send Unix Date Time](../../doc/controllers/form-params.md#send-unix-date-time)
* [Send Rfc 1123 Date Time](../../doc/controllers/form-params.md#send-rfc-1123-date-time)
* [Send Rfc 3339 Date Time](../../doc/controllers/form-params.md#send-rfc-3339-date-time)
* [Send Unix Date Time Array](../../doc/controllers/form-params.md#send-unix-date-time-array)
* [Send Rfc 1123 Date Time Array](../../doc/controllers/form-params.md#send-rfc-1123-date-time-array)
* [Send Long](../../doc/controllers/form-params.md#send-long)
* [Send Integer Array](../../doc/controllers/form-params.md#send-integer-array)
* [Send String Array](../../doc/controllers/form-params.md#send-string-array)
* [Allow Dynamic Form Fields](../../doc/controllers/form-params.md#allow-dynamic-form-fields)
* [Send Model](../../doc/controllers/form-params.md#send-model)
* [Send Model Array](../../doc/controllers/form-params.md#send-model-array)
* [Send File](../../doc/controllers/form-params.md#send-file)
* [Send Multiple Files](../../doc/controllers/form-params.md#send-multiple-files)
* [Send String](../../doc/controllers/form-params.md#send-string)
* [Send Rfc 3339 Date Time Array](../../doc/controllers/form-params.md#send-rfc-3339-date-time-array)
* [Send Mixed Array](../../doc/controllers/form-params.md#send-mixed-array)
* [Update Model With Form](../../doc/controllers/form-params.md#update-model-with-form)
* [Send Delete Form 1](../../doc/controllers/form-params.md#send-delete-form-1)
* [Send Delete Form With Model Array](../../doc/controllers/form-params.md#send-delete-form-with-model-array)
* [Update Model Array With Form](../../doc/controllers/form-params.md#update-model-array-with-form)
* [Update String With Form](../../doc/controllers/form-params.md#update-string-with-form)
* [Update String Array With Form](../../doc/controllers/form-params.md#update-string-array-with-form)
* [Send Integer Enum Array](../../doc/controllers/form-params.md#send-integer-enum-array)
* [Send String Enum Array](../../doc/controllers/form-params.md#send-string-enum-array)
* [Send String in Form With New Line](../../doc/controllers/form-params.md#send-string-in-form-with-new-line)
* [Send String in Form With R](../../doc/controllers/form-params.md#send-string-in-form-with-r)
* [Send String in Form With R N](../../doc/controllers/form-params.md#send-string-in-form-with-r-n)
* [All Optionals](../../doc/controllers/form-params.md#all-optionals)
* [Send Optional Unix Date Time in Body](../../doc/controllers/form-params.md#send-optional-unix-date-time-in-body)
* [Send Optional Rfc 1123 in Body](../../doc/controllers/form-params.md#send-optional-rfc-1123-in-body)
* [Send Datetime Optional in Endpoint](../../doc/controllers/form-params.md#send-datetime-optional-in-endpoint)
* [Send Optional Unix Time Stamp in Model Body](../../doc/controllers/form-params.md#send-optional-unix-time-stamp-in-model-body)
* [Send Optional Unix Time Stamp in Nested Model Body](../../doc/controllers/form-params.md#send-optional-unix-time-stamp-in-nested-model-body)
* [Send Rfc 1123 Date Time in Nested Model](../../doc/controllers/form-params.md#send-rfc-1123-date-time-in-nested-model)
* [Send Rfc 1123 Date Time in Model](../../doc/controllers/form-params.md#send-rfc-1123-date-time-in-model)
* [Send Optional Datetime in Model](../../doc/controllers/form-params.md#send-optional-datetime-in-model)
* [Send Rfc 339 Date Time in Nested Models](../../doc/controllers/form-params.md#send-rfc-339-date-time-in-nested-models)
* [Uuid as Optional](../../doc/controllers/form-params.md#uuid-as-optional)
* [Boolean as Optional](../../doc/controllers/form-params.md#boolean-as-optional)
* [Date as Optional](../../doc/controllers/form-params.md#date-as-optional)
* [Dynamic as Optional](../../doc/controllers/form-params.md#dynamic-as-optional)
* [String as Optional](../../doc/controllers/form-params.md#string-as-optional)
* [Precision as Optional](../../doc/controllers/form-params.md#precision-as-optional)
* [Long as Optional](../../doc/controllers/form-params.md#long-as-optional)
* [Send Number as Optional](../../doc/controllers/form-params.md#send-number-as-optional)


# Send Delete Form

```python
def send_delete_form(self,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeleteBody`](../../doc/models/delete-body.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = DeleteBody(
    name='name6',
    field='field0'
)

result = form_params_controller.send_delete_form(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Delete Multipart

```python
def send_delete_multipart(self,
                         file)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file` | `typing.BinaryIO` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
file = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

result = form_params_controller.send_delete_multipart(file)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Date Array

```python
def send_date_array(self,
                   dates)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dates` | `List[date]` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
dates = [
    dateutil.parser.parse('2016-03-13').date(),
    dateutil.parser.parse('2016-03-13').date()
]

result = form_params_controller.send_date_array(dates)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Date

```python
def send_date(self,
             date)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date` | `date` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
date = dateutil.parser.parse('2016-03-13').date()

result = form_params_controller.send_date(date)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Unix Date Time

```python
def send_unix_date_time(self,
                       datetime)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `datetime` | `datetime` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
datetime = dateutil.datetime.utcfromtimestamp(1480809600)

result = form_params_controller.send_unix_date_time(datetime)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Rfc 1123 Date Time

```python
def send_rfc_1123_date_time(self,
                           datetime)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `datetime` | `datetime` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
datetime = APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime

result = form_params_controller.send_rfc_1123_date_time(datetime)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Rfc 3339 Date Time

```python
def send_rfc_3339_date_time(self,
                           datetime)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `datetime` | `datetime` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
datetime = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = form_params_controller.send_rfc_3339_date_time(datetime)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Unix Date Time Array

```python
def send_unix_date_time_array(self,
                             datetimes)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `datetimes` | `List[datetime]` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
datetimes = [
    dateutil.datetime.utcfromtimestamp(1480809600),
    dateutil.datetime.utcfromtimestamp(1480809600),
    dateutil.datetime.utcfromtimestamp(1480809600)
]

result = form_params_controller.send_unix_date_time_array(datetimes)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Rfc 1123 Date Time Array

```python
def send_rfc_1123_date_time_array(self,
                                 datetimes)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `datetimes` | `List[datetime]` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
datetimes = [
    APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
    APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
    APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime
]

result = form_params_controller.send_rfc_1123_date_time_array(datetimes)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Long

```python
def send_long(self,
             value)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `int` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
value = 64

result = form_params_controller.send_long(value)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Integer Array

```python
def send_integer_array(self,
                      integers)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `integers` | `List[int]` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
integers = [
    45,
    46,
    47
]

result = form_params_controller.send_integer_array(integers)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send String Array

```python
def send_string_array(self,
                     strings)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `strings` | `List[str]` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
strings = [
    'a\'b\'c'
]

result = form_params_controller.send_string_array(strings)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Allow Dynamic Form Fields

```python
def allow_dynamic_form_fields(self,
                             name,
                             _optional_form_parameters=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Form, Required | - |
| `_optional_form_parameters` | `array` | Optional | Pass additional field parameters. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
name = 'name0'

_optional_form_parameters = {
    'key0': 'additionalFieldParams9'
}

result = form_params_controller.allow_dynamic_form_fields(
    name,
    _optional_form_parameters=_optional_form_parameters
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Model

```python
def send_model(self,
              model)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | [`Employee`](../../doc/models/employee.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
model = Employee(
    address='address0',
    age=122,
    birthday=dateutil.parser.parse('2016-03-13').date(),
    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    name='name4',
    uid='uid4',
    department='department8',
    dependents=[
        Person(
            address='address4',
            age=28,
            birthday=dateutil.parser.parse('2016-03-13').date(),
            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            name='name8',
            uid='uid8',
            person_type='Per'
        )
    ],
    hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
    joining_day=Days1Enum.MONDAY,
    salary=240,
    working_days=[
        DaysEnum.FRI_DAY,
        DaysEnum.THURSDAY,
        DaysEnum.WEDNESDAY_
    ],
    boss=Person(
        address='address8',
        age=94,
        birthday=dateutil.parser.parse('2016-03-13').date(),
        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        name='name2',
        uid='uid2',
        person_type='Per'
    ),
    person_type='Empl'
)

result = form_params_controller.send_model(model)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Model Array

```python
def send_model_array(self,
                    models)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `models` | [`List[Employee]`](../../doc/models/employee.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
models = [
    Employee(
        address='address0',
        age=122,
        birthday=dateutil.parser.parse('2016-03-13').date(),
        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        name='name4',
        uid='uid4',
        department='department6',
        dependents=[
            Person(
                address='address4',
                age=28,
                birthday=dateutil.parser.parse('2016-03-13').date(),
                birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                name='name8',
                uid='uid8',
                person_type='Per'
            )
        ],
        hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
        joining_day=Days1Enum.MONDAY,
        salary=88,
        working_days=[
            DaysEnum.MONDAY,
            DaysEnum.TUESDAY
        ],
        boss=Person(
            address='address8',
            age=94,
            birthday=dateutil.parser.parse('2016-03-13').date(),
            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            name='name2',
            uid='uid2',
            person_type='Per'
        ),
        person_type='Empl'
    )
]

result = form_params_controller.send_model_array(models)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send File

```python
def send_file(self,
             file)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file` | `typing.BinaryIO` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
file = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

result = form_params_controller.send_file(file)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Multiple Files

```python
def send_multiple_files(self,
                       file,
                       file_1)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file` | `typing.BinaryIO` | Form, Required | - |
| `file_1` | `typing.BinaryIO` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
file = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

file_1 = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

result = form_params_controller.send_multiple_files(
    file,
    file_1
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send String

```python
def send_string(self,
               value)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `str` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
value = 'value2'

result = form_params_controller.send_string(value)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Rfc 3339 Date Time Array

```python
def send_rfc_3339_date_time_array(self,
                                 datetimes)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `datetimes` | `List[datetime]` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
datetimes = [
    dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    dateutil.parser.parse('2016-03-13T12:52:32.123Z')
]

result = form_params_controller.send_rfc_3339_date_time_array(datetimes)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Mixed Array

Send a variety for form params. Returns file count and body params

```python
def send_mixed_array(self,
                    options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file` | `typing.BinaryIO` | Form, Required | - |
| `integers` | `List[int]` | Form, Required | - |
| `models` | [`List[Employee]`](../../doc/models/employee.md) | Form, Required | - |
| `strings` | `List[str]` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
collect = {
    'file': FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type'),
    'integers': [
        45,
        46,
        47
    ],
    'models': [
        Employee(
            address='address0',
            age=122,
            birthday=dateutil.parser.parse('2016-03-13').date(),
            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            name='name4',
            uid='uid4',
            department='department6',
            dependents=[
                Person(
                    address='address4',
                    age=28,
                    birthday=dateutil.parser.parse('2016-03-13').date(),
                    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    name='name8',
                    uid='uid8',
                    person_type='Per'
                )
            ],
            hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
            joining_day=Days1Enum.MONDAY,
            salary=88,
            working_days=[
                DaysEnum.MONDAY,
                DaysEnum.TUESDAY
            ],
            boss=Person(
                address='address8',
                age=94,
                birthday=dateutil.parser.parse('2016-03-13').date(),
                birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                name='name2',
                uid='uid2',
                person_type='Per'
            ),
            person_type='Empl'
        )
    ],
    'strings': [
        'strings5'
    ]
}
result = form_params_controller.send_mixed_array(collect)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Model With Form

```python
def update_model_with_form(self,
                          model)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | [`Employee`](../../doc/models/employee.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
model = Employee(
    address='address0',
    age=122,
    birthday=dateutil.parser.parse('2016-03-13').date(),
    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    name='name4',
    uid='uid4',
    department='department8',
    dependents=[
        Person(
            address='address4',
            age=28,
            birthday=dateutil.parser.parse('2016-03-13').date(),
            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            name='name8',
            uid='uid8',
            person_type='Per'
        )
    ],
    hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
    joining_day=Days1Enum.MONDAY,
    salary=240,
    working_days=[
        DaysEnum.FRI_DAY,
        DaysEnum.THURSDAY,
        DaysEnum.WEDNESDAY_
    ],
    boss=Person(
        address='address8',
        age=94,
        birthday=dateutil.parser.parse('2016-03-13').date(),
        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        name='name2',
        uid='uid2',
        person_type='Per'
    ),
    person_type='Empl'
)

result = form_params_controller.update_model_with_form(model)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Delete Form 1

```python
def send_delete_form_1(self,
                      model)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | [`Employee`](../../doc/models/employee.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
model = Employee(
    address='address0',
    age=122,
    birthday=dateutil.parser.parse('2016-03-13').date(),
    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    name='name4',
    uid='uid4',
    department='department8',
    dependents=[
        Person(
            address='address4',
            age=28,
            birthday=dateutil.parser.parse('2016-03-13').date(),
            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            name='name8',
            uid='uid8',
            person_type='Per'
        )
    ],
    hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
    joining_day=Days1Enum.MONDAY,
    salary=240,
    working_days=[
        DaysEnum.FRI_DAY,
        DaysEnum.THURSDAY,
        DaysEnum.WEDNESDAY_
    ],
    boss=Person(
        address='address8',
        age=94,
        birthday=dateutil.parser.parse('2016-03-13').date(),
        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        name='name2',
        uid='uid2',
        person_type='Per'
    ),
    person_type='Empl'
)

result = form_params_controller.send_delete_form_1(model)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Delete Form With Model Array

```python
def send_delete_form_with_model_array(self,
                                     models)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `models` | [`List[Employee]`](../../doc/models/employee.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
models = [
    Employee(
        address='address0',
        age=122,
        birthday=dateutil.parser.parse('2016-03-13').date(),
        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        name='name4',
        uid='uid4',
        department='department6',
        dependents=[
            Person(
                address='address4',
                age=28,
                birthday=dateutil.parser.parse('2016-03-13').date(),
                birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                name='name8',
                uid='uid8',
                person_type='Per'
            )
        ],
        hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
        joining_day=Days1Enum.MONDAY,
        salary=88,
        working_days=[
            DaysEnum.MONDAY,
            DaysEnum.TUESDAY
        ],
        boss=Person(
            address='address8',
            age=94,
            birthday=dateutil.parser.parse('2016-03-13').date(),
            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            name='name2',
            uid='uid2',
            person_type='Per'
        ),
        person_type='Empl'
    )
]

result = form_params_controller.send_delete_form_with_model_array(models)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Model Array With Form

```python
def update_model_array_with_form(self,
                                models)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `models` | [`List[Employee]`](../../doc/models/employee.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
models = [
    Employee(
        address='address0',
        age=122,
        birthday=dateutil.parser.parse('2016-03-13').date(),
        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        name='name4',
        uid='uid4',
        department='department6',
        dependents=[
            Person(
                address='address4',
                age=28,
                birthday=dateutil.parser.parse('2016-03-13').date(),
                birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                name='name8',
                uid='uid8',
                person_type='Per'
            )
        ],
        hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
        joining_day=Days1Enum.MONDAY,
        salary=88,
        working_days=[
            DaysEnum.MONDAY,
            DaysEnum.TUESDAY
        ],
        boss=Person(
            address='address8',
            age=94,
            birthday=dateutil.parser.parse('2016-03-13').date(),
            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            name='name2',
            uid='uid2',
            person_type='Per'
        ),
        person_type='Empl'
    )
]

result = form_params_controller.update_model_array_with_form(models)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update String With Form

```python
def update_string_with_form(self,
                           value)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `str` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
value = 'value2'

result = form_params_controller.update_string_with_form(value)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update String Array With Form

```python
def update_string_array_with_form(self,
                                 strings)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `strings` | `List[str]` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
strings = [
    'strings5'
]

result = form_params_controller.update_string_array_with_form(strings)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Integer Enum Array

```python
def send_integer_enum_array(self,
                           suites)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `suites` | [`List[SuiteCodeEnum]`](../../doc/models/suite-code-enum.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
suites = [
    SuiteCodeEnum.HEARTS,
    SuiteCodeEnum.SPADES,
    SuiteCodeEnum.CLUBS
]

result = form_params_controller.send_integer_enum_array(suites)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send String Enum Array

```python
def send_string_enum_array(self,
                          days)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `days` | [`List[Days1Enum]`](../../doc/models/days-1-enum.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
days = [
    Days1Enum.SUNDAY,
    Days1Enum.MONDAY,
    Days1Enum.TUESDAY
]

result = form_params_controller.send_string_enum_array(days)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send String in Form With New Line

```python
def send_string_in_form_with_new_line(self,
                                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TestNstringEncoding`](../../doc/models/test-nstring-encoding.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = TestNstringEncoding(
    field='field0',
    name='name6'
)

result = form_params_controller.send_string_in_form_with_new_line(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send String in Form With R

```python
def send_string_in_form_with_r(self,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TestRstringEncoding`](../../doc/models/test-rstring-encoding.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = TestRstringEncoding(
    field='field0',
    name='name6'
)

result = form_params_controller.send_string_in_form_with_r(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send String in Form With R N

```python
def send_string_in_form_with_r_n(self,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TestRNstringEncoding`](../../doc/models/test-r-nstring-encoding.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = TestRNstringEncoding(
    field='field0',
    name='name6'
)

result = form_params_controller.send_string_in_form_with_r_n(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# All Optionals

```python
def all_optionals(self,
                 model,
                 option="empty")
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | [`AllOptionals`](../../doc/models/all-optionals.md) | Form, Required | - |
| `option` | [`OptionalsEnum`](../../doc/models/optionals-enum.md) | Form, Optional | **Default**: `"empty"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
model = AllOptionals()

option = OptionalsEnum.EMPTYBODY

result = form_params_controller.all_optionals(
    model,
    option=option
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Optional Unix Date Time in Body

```python
def send_optional_unix_date_time_in_body(self,
                                        date_time=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_time` | `datetime` | Form, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
date_time = dateutil.datetime.utcfromtimestamp(1484719381)

result = form_params_controller.send_optional_unix_date_time_in_body(
    date_time=date_time
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Optional Rfc 1123 in Body

```python
def send_optional_rfc_1123_in_body(self,
                                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `datetime` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = APIHelper.HttpDateTime.from_value('Sun, 06 Nov 1994 08:49:37 GMT').datetime

result = form_params_controller.send_optional_rfc_1123_in_body(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Datetime Optional in Endpoint

```python
def send_datetime_optional_in_endpoint(self,
                                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `datetime` | Form, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = dateutil.parser.parse('02/13/1994 14:01:54')

result = form_params_controller.send_datetime_optional_in_endpoint(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Optional Unix Time Stamp in Model Body

```python
def send_optional_unix_time_stamp_in_model_body(self,
                                               date_time)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_time` | [`UnixDateTime`](../../doc/models/unix-date-time.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
date_time = UnixDateTime(
    date_time=dateutil.datetime.utcfromtimestamp(1484719381)
)

result = form_params_controller.send_optional_unix_time_stamp_in_model_body(date_time)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Optional Unix Time Stamp in Nested Model Body

```python
def send_optional_unix_time_stamp_in_nested_model_body(self,
                                                      date_time)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_time` | [`SendUnixDateTime`](../../doc/models/send-unix-date-time.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
date_time = SendUnixDateTime(
    date_time=UnixDateTime(
        date_time=dateutil.datetime.utcfromtimestamp(1484719381)
    )
)

result = form_params_controller.send_optional_unix_time_stamp_in_nested_model_body(date_time)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Rfc 1123 Date Time in Nested Model

```python
def send_rfc_1123_date_time_in_nested_model(self,
                                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SendRfc1123DateTime`](../../doc/models/send-rfc-1123-date-time.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = SendRfc1123DateTime(
    date_time=ModelWithOptionalRfc1123DateTime(
        date_time=APIHelper.HttpDateTime.from_value('Sun, 06 Nov 1994 08:49:37 GMT').datetime
    )
)

result = form_params_controller.send_rfc_1123_date_time_in_nested_model(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Rfc 1123 Date Time in Model

```python
def send_rfc_1123_date_time_in_model(self,
                                    date_time)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_time` | [`ModelWithOptionalRfc1123DateTime`](../../doc/models/model-with-optional-rfc-1123-date-time.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
date_time = ModelWithOptionalRfc1123DateTime(
    date_time=APIHelper.HttpDateTime.from_value('Sun, 06 Nov 1994 08:49:37 GMT').datetime
)

result = form_params_controller.send_rfc_1123_date_time_in_model(date_time)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Optional Datetime in Model

```python
def send_optional_datetime_in_model(self,
                                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ModelWithOptionalRfc3339DateTime`](../../doc/models/model-with-optional-rfc-3339-date-time.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = ModelWithOptionalRfc3339DateTime(
    date_time=dateutil.parser.parse('1994-02-13T14:01:54.9571247Z')
)

result = form_params_controller.send_optional_datetime_in_model(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Rfc 339 Date Time in Nested Models

```python
def send_rfc_339_date_time_in_nested_models(self,
                                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SendRfc339DateTime`](../../doc/models/send-rfc-339-date-time.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = SendRfc339DateTime(
    date_time=ModelWithOptionalRfc3339DateTime(
        date_time=dateutil.parser.parse('1994-02-13T14:01:54.9571247Z')
    )
)

result = form_params_controller.send_rfc_339_date_time_in_nested_models(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Uuid as Optional

```python
def uuid_as_optional(self,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`UuidAsOptional`](../../doc/models/uuid-as-optional.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = UuidAsOptional(
    uuid='123e4567-e89b-12d3-a456-426655440000'
)

result = form_params_controller.uuid_as_optional(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Boolean as Optional

```python
def boolean_as_optional(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BooleanAsOptional`](../../doc/models/boolean-as-optional.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = BooleanAsOptional(
    boolean=True
)

result = form_params_controller.boolean_as_optional(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Date as Optional

```python
def date_as_optional(self,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DateAsOptional`](../../doc/models/date-as-optional.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = DateAsOptional(
    date=dateutil.parser.parse('1994-02-13').date()
)

result = form_params_controller.date_as_optional(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Dynamic as Optional

```python
def dynamic_as_optional(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DynamicAsOptional`](../../doc/models/dynamic-as-optional.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = DynamicAsOptional(
    dynamic=jsonpickle.decode('{"dynamic":"test"}')
)

result = form_params_controller.dynamic_as_optional(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# String as Optional

```python
def string_as_optional(self,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`StringAsOptional`](../../doc/models/string-as-optional.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = AllOptionals(
    string='test'
)

result = form_params_controller.string_as_optional(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Precision as Optional

```python
def precision_as_optional(self,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PrecisionAsOptional`](../../doc/models/precision-as-optional.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = PrecisionAsOptional(
    precision=1.23
)

result = form_params_controller.precision_as_optional(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Long as Optional

```python
def long_as_optional(self,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LongAsOptional`](../../doc/models/long-as-optional.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = LongAsOptional(
    long=123123
)

result = form_params_controller.long_as_optional(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Number as Optional

```python
def send_number_as_optional(self,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`NumberAsOptional`](../../doc/models/number-as-optional.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = NumberAsOptional(
    number=1
)

result = form_params_controller.send_number_as_optional(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

