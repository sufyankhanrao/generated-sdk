# Sender

```python
sender_controller = client.sender
```

## Class Name

`SenderController`

## Methods

* [Send Params](../../doc/controllers/sender.md#send-params)
* [Send Collect Params](../../doc/controllers/sender.md#send-collect-params)
* [Send Scalar Param](../../doc/controllers/sender.md#send-scalar-param)
* [Send Non Scalar Param](../../doc/controllers/sender.md#send-non-scalar-param)
* [Send Mixed Param](../../doc/controllers/sender.md#send-mixed-param)
* [Send Combined](../../doc/controllers/sender.md#send-combined)
* [Send Collect Combined](../../doc/controllers/sender.md#send-collect-combined)
* [Send in Model Params](../../doc/controllers/sender.md#send-in-model-params)
* [Send in Model](../../doc/controllers/sender.md#send-in-model)


# Send Params

```python
def send_params(self,
               template,
               form_scalar,
               form_non_scalar,
               query_mixed,
               header=None,
               form_mixed=None,
               query_scalar=None,
               query_non_scalar=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `template` | float \| str | Template, Required | This is a container for one-of cases. |
| `form_scalar` | float \| str \| None | Form, Required | This is a container for any-of cases. |
| `form_non_scalar` | [Car](../../doc/models/car.md) \| [Morning](../../doc/models/morning.md) \| [Atom](../../doc/models/atom.md) | Form, Required | This is a container for one-of cases. |
| `query_mixed` | int \| [Atom](../../doc/models/atom.md) | Query, Required | This is a container for any-of cases. |
| `header` | float \| str \| None | Header, Optional | This is a container for one-of cases. |
| `form_mixed` | int \| [Atom](../../doc/models/atom.md) \| None | Form, Optional | This is a container for any-of cases. |
| `query_scalar` | float \| str \| None | Query, Optional | This is a container for any-of cases. |
| `query_non_scalar` | [Car](../../doc/models/car.md) \| [Morning](../../doc/models/morning.md) \| [Atom](../../doc/models/atom.md) \| None | Query, Optional | This is a container for one-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
template = 35.7

form_scalar = 126.52

form_non_scalar = Car(
    number_of_tyres='NumberOfTyres4',
    have_trunk=False
)

query_mixed = 164

header = 227

form_mixed = 202

query_scalar = 128.08

query_non_scalar = Car(
    number_of_tyres='NumberOfTyres4',
    have_trunk=False
)

result = sender_controller.send_params(
    template,
    form_scalar,
    form_non_scalar,
    query_mixed,
    header=header,
    form_mixed=form_mixed,
    query_scalar=query_scalar,
    query_non_scalar=query_non_scalar
)
print(result)
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
| `template` | float \| str | Template, Required | This is a container for any-of cases. |
| `form_scalar` | float \| str \| None | Form, Required | This is a container for any-of cases. |
| `form_non_scalar` | [Car](../../doc/models/car.md) \| [Morning](../../doc/models/morning.md) \| [Atom](../../doc/models/atom.md) | Form, Required | This is a container for one-of cases. |
| `query_mixed` | int \| [Atom](../../doc/models/atom.md) | Query, Required | This is a container for any-of cases. |
| `header` | float \| str \| None | Header, Optional | This is a container for any-of cases. |
| `form_mixed` | int \| [Atom](../../doc/models/atom.md) \| None | Form, Optional | This is a container for any-of cases. |
| `query_scalar` | float \| str \| None | Query, Optional | This is a container for any-of cases. |
| `query_non_scalar` | [Car](../../doc/models/car.md) \| [Morning](../../doc/models/morning.md) \| [Atom](../../doc/models/atom.md) \| None | Query, Optional | This is a container for one-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
collect = {
    'template': 35.7,
    'form_scalar': 126.52,
    'form_non_scalar': Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    'query_mixed': 164,
    'header': 227,
    'form_mixed': 202,
    'query_scalar': 128.08,
    'query_non_scalar': Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    )
}
result = sender_controller.send_collect_params(collect)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Send Scalar Param

```python
def send_scalar_param(self,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | float \| str \| None | Body, Required | This is a container for any-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = 122.3

result = sender_controller.send_scalar_param(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Send Non Scalar Param

```python
def send_non_scalar_param(self,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [Car](../../doc/models/car.md) \| [Morning](../../doc/models/morning.md) \| [Atom](../../doc/models/atom.md) | Body, Required | This is a container for one-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = Car(
    number_of_tyres='NumberOfTyres4',
    have_trunk=False
)

result = sender_controller.send_non_scalar_param(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Send Mixed Param

```python
def send_mixed_param(self,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | int \| [Atom](../../doc/models/atom.md) | Body, Required | This is a container for any-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = 186

result = sender_controller.send_mixed_param(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Send Combined

```python
def send_combined(self,
                 body_scalar,
                 body_non_scalar,
                 body_mixed)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body_scalar` | float \| str | Body, Required | This is a container for any-of cases. |
| `body_non_scalar` | [Car](../../doc/models/car.md) \| [Morning](../../doc/models/morning.md) \| [Atom](../../doc/models/atom.md) | Body, Required | This is a container for one-of cases. |
| `body_mixed` | int \| [Atom](../../doc/models/atom.md) | Body, Required | This is a container for any-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body_scalar = 89.08

body_non_scalar = Car(
    number_of_tyres='NumberOfTyres4',
    have_trunk=False
)

body_mixed = 118

result = sender_controller.send_combined(
    body_scalar,
    body_non_scalar,
    body_mixed
)
print(result)
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
| `body_scalar` | float \| str | Body, Required | This is a container for any-of cases. |
| `body_non_scalar` | [Car](../../doc/models/car.md) \| [Morning](../../doc/models/morning.md) \| [Atom](../../doc/models/atom.md) | Body, Required | This is a container for one-of cases. |
| `body_mixed` | int \| [Atom](../../doc/models/atom.md) | Body, Required | This is a container for any-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
collect = {
    'body_scalar': 89.08,
    'body_non_scalar': Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    'body_mixed': 118
}
result = sender_controller.send_collect_combined(collect)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Send in Model Params

```python
def send_in_model_params(self,
                        form_non_scalar_model,
                        query_non_scalar_model,
                        query_mixed_model,
                        form_scalar_model=None,
                        form_mixed_model=None,
                        query_scalar_model=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `form_non_scalar_model` | [`NonScalarModel`](../../doc/models/non-scalar-model.md) | Form, Required | - |
| `query_non_scalar_model` | [`NonScalarModel`](../../doc/models/non-scalar-model.md) | Query, Required | - |
| `query_mixed_model` | [`MixedModel`](../../doc/models/mixed-model.md) | Query, Required | - |
| `form_scalar_model` | [`ScalarModel`](../../doc/models/scalar-model.md) | Form, Optional | - |
| `form_mixed_model` | [`MixedModel`](../../doc/models/mixed-model.md) | Form, Optional | - |
| `query_scalar_model` | [`ScalarModel`](../../doc/models/scalar-model.md) | Query, Optional | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
form_non_scalar_model = NonScalarModel(
    any_of_required=Atom(
        number_of_electrons=224,
        number_of_protons=134
    ),
    one_of_req_nullable=Orbit(
        number_of_electrons=218
    ),
    one_of_optional=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    any_of_opt_nullable=Morning(
        starts_at='startsAt6',
        ends_at='endsAt2',
        offer_tea_break=False,
        session_type='Morning'
    )
)

query_non_scalar_model = NonScalarModel(
    any_of_required=Atom(
        number_of_electrons=224,
        number_of_protons=134
    ),
    one_of_req_nullable=Orbit(
        number_of_electrons=218
    ),
    one_of_optional=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    any_of_opt_nullable=Morning(
        starts_at='startsAt6',
        ends_at='endsAt2',
        offer_tea_break=False,
        session_type='Morning'
    )
)

query_mixed_model = MixedModel(
    any_of_required=126,
    one_of_req_nullable=True,
    one_of_optional=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    any_of_opt_nullable=Postman(
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
            ),
            Person(
                address='address4',
                age=28,
                birthday=dateutil.parser.parse('2016-03-13').date(),
                birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                name='name8',
                uid='uid8',
                person_type='Per'
            ),
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
        joining_day=DaysEnum.MONDAY,
        salary=210,
        working_days=[
            DaysEnum.THURSDAY
        ],
        person_type='Post'
    )
)

form_scalar_model = ScalarModel(
    any_of_required=89.78,
    one_of_req_nullable=158,
    one_of_optional=238,
    any_of_opt_nullable=22
)

form_mixed_model = MixedModel(
    any_of_required=204,
    one_of_req_nullable=True,
    one_of_optional=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    any_of_opt_nullable=Postman(
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
            ),
            Person(
                address='address4',
                age=28,
                birthday=dateutil.parser.parse('2016-03-13').date(),
                birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                name='name8',
                uid='uid8',
                person_type='Per'
            ),
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
        joining_day=DaysEnum.MONDAY,
        salary=210,
        working_days=[
            DaysEnum.THURSDAY
        ],
        person_type='Post'
    )
)

query_scalar_model = ScalarModel(
    any_of_required=197.88,
    one_of_req_nullable=200,
    one_of_optional=40,
    any_of_opt_nullable=80
)

result = sender_controller.send_in_model_params(
    form_non_scalar_model,
    query_non_scalar_model,
    query_mixed_model,
    form_scalar_model=form_scalar_model,
    form_mixed_model=form_mixed_model,
    query_scalar_model=query_scalar_model
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Send in Model

```python
def send_in_model(self,
                 non_scalar_model,
                 mixed_model,
                 scalar_model=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `non_scalar_model` | [`NonScalarModel`](../../doc/models/non-scalar-model.md) | Body, Required | - |
| `mixed_model` | [`MixedModel`](../../doc/models/mixed-model.md) | Body, Required | - |
| `scalar_model` | [`ScalarModel`](../../doc/models/scalar-model.md) | Body, Optional | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
non_scalar_model = NonScalarModel(
    any_of_required=Atom(
        number_of_electrons=224,
        number_of_protons=134
    ),
    one_of_req_nullable=Orbit(
        number_of_electrons=218
    ),
    one_of_optional=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    any_of_opt_nullable=Morning(
        starts_at='startsAt6',
        ends_at='endsAt2',
        offer_tea_break=False,
        session_type='Morning'
    )
)

mixed_model = MixedModel(
    any_of_required=80,
    one_of_req_nullable=True,
    one_of_optional=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    any_of_opt_nullable=Postman(
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
            ),
            Person(
                address='address4',
                age=28,
                birthday=dateutil.parser.parse('2016-03-13').date(),
                birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                name='name8',
                uid='uid8',
                person_type='Per'
            ),
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
        joining_day=DaysEnum.MONDAY,
        salary=210,
        working_days=[
            DaysEnum.THURSDAY
        ],
        person_type='Post'
    )
)

scalar_model = ScalarModel(
    any_of_required=115.48,
    one_of_req_nullable=148,
    one_of_optional=248,
    any_of_opt_nullable=32
)

result = sender_controller.send_in_model(
    non_scalar_model,
    mixed_model,
    scalar_model=scalar_model
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |

