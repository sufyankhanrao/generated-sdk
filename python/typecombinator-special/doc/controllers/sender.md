# Sender

```python
sender_controller = client.sender
```

## Class Name

`SenderController`

## Methods

* [Send Params](../../doc/controllers/sender.md#send-params)
* [Send Params Default](../../doc/controllers/sender.md#send-params-default)
* [Send Collect Params](../../doc/controllers/sender.md#send-collect-params)
* [Send Enum Param](../../doc/controllers/sender.md#send-enum-param)
* [Send Date Time Param](../../doc/controllers/sender.md#send-date-time-param)
* [Send Req Opt Param](../../doc/controllers/sender.md#send-req-opt-param)
* [Send Combined](../../doc/controllers/sender.md#send-combined)
* [Send Collect Combined](../../doc/controllers/sender.md#send-collect-combined)
* [Send in Model Params](../../doc/controllers/sender.md#send-in-model-params)
* [Send in Model](../../doc/controllers/sender.md#send-in-model)


# Send Params

```python
def send_params(self,
               template,
               form_enum,
               form_date_time,
               query_req_opt,
               header=None,
               form_req_opt=None,
               query_enum=None,
               query_date_time=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `template` | [Days](../../doc/models/days-enum.md) \| [MonthName](../../doc/models/month-name-enum.md) \| [MonthNumber](../../doc/models/month-number-enum.md) | Template, Required | This is a container for one-of cases. |
| `form_enum` | List[[Days](../../doc/models/days-enum.md) \| [MonthName](../../doc/models/month-name-enum.md) \| [MonthNumber](../../doc/models/month-number-enum.md)] | Form, Required | This is List of a container for one-of cases. |
| `form_date_time` | List[date \| datetime] | Form, Required | This is List of a container for one-of cases. |
| `query_req_opt` | [Cat](../../doc/models/cat.md) \| [Dog](../../doc/models/dog.md) \| [Rabbit](../../doc/models/rabbit.md) | Query, Required | This is a container for one-of cases. |
| `header` | datetime \| str \| None | Header, Optional | This is a container for any-of cases. |
| `form_req_opt` | [Cat](../../doc/models/cat.md) \| [Dog](../../doc/models/dog.md) \| [Rabbit](../../doc/models/rabbit.md) \| None | Form, Optional | This is a container for one-of cases. |
| `query_enum` | List[[Days](../../doc/models/days-enum.md) \| [MonthName](../../doc/models/month-name-enum.md) \| [MonthNumber](../../doc/models/month-number-enum.md)] \| None | Query, Optional | This is List of a container for one-of cases. |
| `query_date_time` | List[date \| datetime] \| None | Query, Optional | This is List of a container for one-of cases. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
template = DaysEnum.WEDNESDAY_

form_enum = [
    DaysEnum.TUESDAY,
    DaysEnum.WEDNESDAY_
]

form_date_time = [
    dateutil.parser.parse('2016-03-13').date(),
    dateutil.parser.parse('2016-03-13').date(),
    dateutil.parser.parse('2016-03-13').date()
]

query_req_opt = Cat(
    bark=False,
    age=238,
    cute=False
)

header = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

form_req_opt = Cat(
    bark=False,
    age=238,
    cute=False
)

query_enum = [
    DaysEnum.SATURDAY
]

query_date_time = [
    dateutil.parser.parse('2016-03-13').date()
]

result = sender_controller.send_params(
    template,
    form_enum,
    form_date_time,
    query_req_opt,
    header=header,
    form_req_opt=form_req_opt,
    query_enum=query_enum,
    query_date_time=query_date_time
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Send Params Default

```python
def send_params_default(self,
                       form_default_enum=February,
                       query_default_enum=Monday,
                       template_default_enum=1)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `form_default_enum` | [Days](../../doc/models/days-enum.md) \| [MonthName](../../doc/models/month-name-enum.md) \| [MonthNumber](../../doc/models/month-number-enum.md) \| None | Form, Optional | This is a container for one-of cases.<br><br>**Default**: `February` |
| `query_default_enum` | [Days](../../doc/models/days-enum.md) \| [MonthName](../../doc/models/month-name-enum.md) \| [MonthNumber](../../doc/models/month-number-enum.md) \| None | Query, Optional | This is a container for one-of cases.<br><br>**Default**: `Monday` |
| `template_default_enum` | [Days](../../doc/models/days-enum.md) \| [MonthName](../../doc/models/month-name-enum.md) \| [MonthNumber](../../doc/models/month-number-enum.md) \| None | Template, Optional | This is a container for one-of cases.<br><br>**Default**: `1` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
form_default_enum = MonthNameEnum.FEBRUARY

query_default_enum = DaysEnum.MONDAY

template_default_enum = MonthNumberEnum.JANUARY

result = sender_controller.send_params_default(
    form_default_enum=form_default_enum,
    query_default_enum=query_default_enum,
    template_default_enum=template_default_enum
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Send Collect Params

```python
def send_collect_params(self,
                       options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `template` | [Days](../../doc/models/days-enum.md) \| [MonthName](../../doc/models/month-name-enum.md) \| [MonthNumber](../../doc/models/month-number-enum.md) | Template, Required | This is a container for one-of cases. |
| `form_enum` | List[[Days](../../doc/models/days-enum.md) \| [MonthName](../../doc/models/month-name-enum.md) \| [MonthNumber](../../doc/models/month-number-enum.md)] | Form, Required | This is List of a container for one-of cases. |
| `form_date_time` | List[date \| datetime] | Form, Required | This is List of a container for one-of cases. |
| `query_req_opt` | [Cat](../../doc/models/cat.md) \| [Dog](../../doc/models/dog.md) \| [Rabbit](../../doc/models/rabbit.md) | Query, Required | This is a container for one-of cases. |
| `header` | datetime \| str \| None | Header, Optional | This is a container for any-of cases. |
| `form_req_opt` | [Cat](../../doc/models/cat.md) \| [Dog](../../doc/models/dog.md) \| [Rabbit](../../doc/models/rabbit.md) \| None | Form, Optional | This is a container for one-of cases. |
| `query_enum` | List[[Days](../../doc/models/days-enum.md) \| [MonthName](../../doc/models/month-name-enum.md) \| [MonthNumber](../../doc/models/month-number-enum.md)] \| None | Query, Optional | This is List of a container for one-of cases. |
| `query_date_time` | List[date \| datetime] \| None | Query, Optional | This is List of a container for one-of cases. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
collect = {
    'template': DaysEnum.WEDNESDAY_,
    'form_enum': [
        DaysEnum.TUESDAY,
        DaysEnum.WEDNESDAY_
    ],
    'form_date_time': [
        dateutil.parser.parse('2016-03-13').date(),
        dateutil.parser.parse('2016-03-13').date(),
        dateutil.parser.parse('2016-03-13').date()
    ],
    'query_req_opt': Cat(
        bark=False,
        age=238,
        cute=False
    ),
    'header': dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    'form_req_opt': Cat(
        bark=False,
        age=238,
        cute=False
    ),
    'query_enum': [
        DaysEnum.SATURDAY
    ],
    'query_date_time': [
        dateutil.parser.parse('2016-03-13').date()
    ]
}
result = sender_controller.send_collect_params(collect)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Send Enum Param

```python
def send_enum_param(self,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | List[[Days](../../doc/models/days-enum.md) \| [MonthName](../../doc/models/month-name-enum.md) \| [MonthNumber](../../doc/models/month-number-enum.md)] | Body, Required | This is List of a container for one-of cases. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = [
    DaysEnum.TUESDAY,
    DaysEnum.WEDNESDAY_
]

result = sender_controller.send_enum_param(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Send Date Time Param

```python
def send_date_time_param(self,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | List[date \| datetime] | Body, Required | This is List of a container for one-of cases. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = [
    dateutil.parser.parse('2016-03-13').date(),
    dateutil.parser.parse('2016-03-13').date()
]

result = sender_controller.send_date_time_param(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Send Req Opt Param

```python
def send_req_opt_param(self,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [Cat](../../doc/models/cat.md) \| [Dog](../../doc/models/dog.md) \| [Rabbit](../../doc/models/rabbit.md) | Body, Required | This is a container for one-of cases. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = Cat(
    bark=False,
    age=238,
    cute=False
)

result = sender_controller.send_req_opt_param(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Send Combined

```python
def send_combined(self,
                 body_enum,
                 body_date_time,
                 body_req_opt)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body_enum` | List[[Days](../../doc/models/days-enum.md) \| [MonthName](../../doc/models/month-name-enum.md) \| [MonthNumber](../../doc/models/month-number-enum.md)] | Body, Required | This is List of a container for one-of cases. |
| `body_date_time` | List[date \| datetime] | Body, Required | This is List of a container for one-of cases. |
| `body_req_opt` | [Cat](../../doc/models/cat.md) \| [Dog](../../doc/models/dog.md) \| [Rabbit](../../doc/models/rabbit.md) | Body, Required | This is a container for one-of cases. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body_enum = [
    DaysEnum.WEDNESDAY_,
    DaysEnum.THURSDAY,
    DaysEnum.FRI_DAY
]

body_date_time = [
    dateutil.parser.parse('2016-03-13').date(),
    dateutil.parser.parse('2016-03-13').date()
]

body_req_opt = Cat(
    bark=False,
    age=238,
    cute=False
)

result = sender_controller.send_combined(
    body_enum,
    body_date_time,
    body_req_opt
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Send Collect Combined

```python
def send_collect_combined(self,
                         options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body_enum` | List[[Days](../../doc/models/days-enum.md) \| [MonthName](../../doc/models/month-name-enum.md) \| [MonthNumber](../../doc/models/month-number-enum.md)] | Body, Required | This is List of a container for one-of cases. |
| `body_date_time` | List[date \| datetime] | Body, Required | This is List of a container for one-of cases. |
| `body_req_opt` | [Cat](../../doc/models/cat.md) \| [Dog](../../doc/models/dog.md) \| [Rabbit](../../doc/models/rabbit.md) | Body, Required | This is a container for one-of cases. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
collect = {
    'body_enum': [
        DaysEnum.WEDNESDAY_,
        DaysEnum.THURSDAY,
        DaysEnum.FRI_DAY
    ],
    'body_date_time': [
        dateutil.parser.parse('2016-03-13').date(),
        dateutil.parser.parse('2016-03-13').date()
    ],
    'body_req_opt': Cat(
        bark=False,
        age=238,
        cute=False
    )
}
result = sender_controller.send_collect_combined(collect)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Send in Model Params

```python
def send_in_model_params(self,
                        form_date_time_cases,
                        query_date_time_cases,
                        query_factoring_schema,
                        form_multiple_enums=None,
                        form_factoring_schema=None,
                        query_multiple_enums=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `form_date_time_cases` | [`DateTimeCases`](../../doc/models/date-time-cases.md) | Form, Required | - |
| `query_date_time_cases` | [`DateTimeCases`](../../doc/models/date-time-cases.md) | Query, Required | - |
| `query_factoring_schema` | [`FactoringSchema`](../../doc/models/factoring-schema.md) | Query, Required | - |
| `form_multiple_enums` | [`MultipleEnums`](../../doc/models/multiple-enums.md) | Form, Optional | - |
| `form_factoring_schema` | [`FactoringSchema`](../../doc/models/factoring-schema.md) | Form, Optional | - |
| `query_multiple_enums` | [`MultipleEnums`](../../doc/models/multiple-enums.md) | Query, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
form_date_time_cases = DateTimeCases(
    rfc_3339_vs_string=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    all_one_of=dateutil.parser.parse('2016-03-13').date(),
    all_outer_array=[
        dateutil.parser.parse('2016-03-13').date(),
        dateutil.parser.parse('2016-03-13').date()
    ],
    datevs_array=[
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime
    ],
    mapvs_array=[
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime
    ]
)

query_date_time_cases = DateTimeCases(
    rfc_3339_vs_string=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    all_one_of=dateutil.parser.parse('2016-03-13').date(),
    all_outer_array=[
        dateutil.parser.parse('2016-03-13').date(),
        dateutil.parser.parse('2016-03-13').date()
    ],
    datevs_array=[
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime
    ],
    mapvs_array=[
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime
    ]
)

query_factoring_schema = FactoringSchema(
    any_of_dog_cat=Dog(
        bark=False,
        age=140,
        cute=False,
        breed='breed0'
    ),
    any_of_cat_dog=Cat(
        bark=False,
        age=238,
        cute=False
    ),
    any_of_squirrel_dog=Squirrel(
        squeak=False,
        childern=22
    ),
    one_of_cat_dog_rabbit=Cat(
        bark=False,
        age=238,
        cute=False
    ),
    one_of_vehicles=VehicleA(
        number_of_tyres='NumberOfTyres8',
        model='model8'
    )
)

form_multiple_enums = MultipleEnums(
    daysvs_string=DaysEnum.MONDAY,
    all_one_of=DaysEnum.TUESDAY,
    all_outer_array=[
        DaysEnum.WEDNESDAY_,
        DaysEnum.THURSDAY
    ],
    enumvs_array=DaysEnum.WEDNESDAY_,
    mapvs_array={
        'key0': DaysEnum.SUNDAY,
        'key1': DaysEnum.MONDAY
    }
)

form_factoring_schema = FactoringSchema(
    any_of_dog_cat=Dog(
        bark=False,
        age=140,
        cute=False,
        breed='breed0'
    ),
    any_of_cat_dog=Cat(
        bark=False,
        age=238,
        cute=False
    ),
    any_of_squirrel_dog=Squirrel(
        squeak=False,
        childern=22
    ),
    one_of_cat_dog_rabbit=Cat(
        bark=False,
        age=238,
        cute=False
    ),
    one_of_vehicles=VehicleA(
        number_of_tyres='NumberOfTyres8',
        model='model8'
    )
)

query_multiple_enums = MultipleEnums(
    daysvs_string=DaysEnum.WEDNESDAY_,
    all_one_of=DaysEnum.SUNDAY,
    all_outer_array=[
        DaysEnum.MONDAY,
        DaysEnum.TUESDAY,
        DaysEnum.WEDNESDAY_
    ],
    enumvs_array=DaysEnum.MONDAY,
    mapvs_array={
        'key0': DaysEnum.FRI_DAY,
        'key1': DaysEnum.SATURDAY,
        'key2': DaysEnum.SUNDAY
    }
)

result = sender_controller.send_in_model_params(
    form_date_time_cases,
    query_date_time_cases,
    query_factoring_schema,
    form_multiple_enums=form_multiple_enums,
    form_factoring_schema=form_factoring_schema,
    query_multiple_enums=query_multiple_enums
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Send in Model

```python
def send_in_model(self,
                 date_time_cases,
                 factoring_schema,
                 multiple_enums=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_time_cases` | [`DateTimeCases`](../../doc/models/date-time-cases.md) | Body, Required | - |
| `factoring_schema` | [`FactoringSchema`](../../doc/models/factoring-schema.md) | Body, Required | - |
| `multiple_enums` | [`MultipleEnums`](../../doc/models/multiple-enums.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
date_time_cases = DateTimeCases(
    rfc_3339_vs_string=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    all_one_of=dateutil.parser.parse('2016-03-13').date(),
    all_outer_array=[
        dateutil.parser.parse('2016-03-13').date()
    ],
    datevs_array=[
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime
    ],
    mapvs_array=[
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime
    ]
)

factoring_schema = FactoringSchema(
    any_of_dog_cat=Dog(
        bark=False,
        age=140,
        cute=False,
        breed='breed0'
    ),
    any_of_cat_dog=Cat(
        bark=False,
        age=238,
        cute=False
    ),
    any_of_squirrel_dog=Squirrel(
        squeak=False,
        childern=22
    ),
    one_of_cat_dog_rabbit=Cat(
        bark=False,
        age=238,
        cute=False
    ),
    one_of_vehicles=VehicleA(
        number_of_tyres='NumberOfTyres8',
        model='model8'
    )
)

multiple_enums = MultipleEnums(
    daysvs_string=DaysEnum.WEDNESDAY_,
    all_one_of=DaysEnum.SUNDAY,
    all_outer_array=[
        DaysEnum.MONDAY
    ],
    enumvs_array=DaysEnum.MONDAY,
    mapvs_array={
        'key0': DaysEnum.FRI_DAY
    }
)

result = sender_controller.send_in_model(
    date_time_cases,
    factoring_schema,
    multiple_enums=multiple_enums
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |

