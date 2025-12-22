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
| `template` | List[float \| str \| List[List[float] \| str]] | Template, Required | This is List of a container for one-of cases. |
| `form_scalar` | List[float] \| str \| None | Form, Required | This is a container for any-of cases. |
| `form_non_scalar` | Dict[str, [Car](../../doc/models/car.md) \| [Morning](../../doc/models/morning.md) \| [Atom](../../doc/models/atom.md)] | Form, Required | This is Dictionary of a container for one-of cases. |
| `query_mixed` | Dict[str, int] \| Dict[str, [Atom](../../doc/models/atom.md)] | Query, Required | This is a container for any-of cases. |
| `header` | float \| str \| None | Header, Optional | This is a container for one-of cases. |
| `form_mixed` | Dict[str, int] \| Dict[str, [Atom](../../doc/models/atom.md)] \| None | Form, Optional | This is a container for any-of cases. |
| `query_scalar` | List[float] \| str \| None | Query, Optional | This is a container for any-of cases. |
| `query_non_scalar` | Dict[str, [Car](../../doc/models/car.md) \| [Morning](../../doc/models/morning.md) \| [Atom](../../doc/models/atom.md)] \| None | Query, Optional | This is Dictionary of a container for one-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
template = [
    11.12,
    11.13,
    11.14
]

form_scalar = [
    113.06,
    113.07,
    113.08
]

form_non_scalar = {
    'key0': Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    'key1': Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    'key2': Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    )
}

query_mixed = {
    'key0': 86
}

header = 227

form_mixed = {
    'key0': 124,
    'key1': 125
}

query_scalar = [
    114.62,
    114.63,
    114.64
]

query_non_scalar = {
    'key0': Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    'key1': Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    )
}

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
| `template` | List[float \| str] | Template, Required | This is List of a container for one-of cases. |
| `form_scalar` | List[float] \| str \| None | Form, Required | This is a container for any-of cases. |
| `form_non_scalar` | Dict[str, [Car](../../doc/models/car.md) \| [Morning](../../doc/models/morning.md) \| [Atom](../../doc/models/atom.md)] | Form, Required | This is Dictionary of a container for one-of cases. |
| `query_mixed` | Dict[str, int] \| Dict[str, [Atom](../../doc/models/atom.md)] | Query, Required | This is a container for any-of cases. |
| `header` | float \| str \| None | Header, Optional | This is a container for one-of cases. |
| `form_mixed` | Dict[str, int] \| Dict[str, [Atom](../../doc/models/atom.md)] \| None | Form, Optional | This is a container for any-of cases. |
| `query_scalar` | List[float] \| str \| None | Query, Optional | This is a container for any-of cases. |
| `query_non_scalar` | Dict[str, [Car](../../doc/models/car.md) \| [Morning](../../doc/models/morning.md) \| [Atom](../../doc/models/atom.md)] \| None | Query, Optional | This is Dictionary of a container for one-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
collect = {
    'template': [
        11.12,
        11.13,
        11.14
    ],
    'form_scalar': [
        113.06,
        113.07,
        113.08
    ],
    'form_non_scalar': {
        'key0': Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        'key1': Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        'key2': Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        )
    },
    'query_mixed': {
        'key0': 86
    },
    'header': 227,
    'form_mixed': {
        'key0': 124,
        'key1': 125
    },
    'query_scalar': [
        114.62,
        114.63,
        114.64
    ],
    'query_non_scalar': {
        'key0': Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        'key1': Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        )
    }
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
| `body` | List[float] \| str \| None | Body, Required | This is a container for any-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = [
    108.84
]

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
| `body` | Dict[str, [Car](../../doc/models/car.md) \| [Morning](../../doc/models/morning.md) \| [Atom](../../doc/models/atom.md)] | Body, Required | This is Dictionary of a container for one-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = {
    'key0': Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    'key1': Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    )
}

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
| `body` | Dict[str, int] \| Dict[str, [Atom](../../doc/models/atom.md)] | Body, Required | This is a container for any-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = {
    'key0': 108,
    'key1': 109,
    'key2': 110
}

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
| `body_scalar` | List[float] \| str | Body, Required | This is a container for any-of cases. |
| `body_non_scalar` | Dict[str, [Car](../../doc/models/car.md) \| [Morning](../../doc/models/morning.md) \| [Atom](../../doc/models/atom.md)] | Body, Required | This is Dictionary of a container for one-of cases. |
| `body_mixed` | Dict[str, int] \| Dict[str, [Atom](../../doc/models/atom.md)] | Body, Required | This is a container for any-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body_scalar = [
    75.62
]

body_non_scalar = {
    'key0': Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    'key1': Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    )
}

body_mixed = {
    'key0': 216
}

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
| `body_scalar` | List[float] \| str | Body, Required | This is a container for any-of cases. |
| `body_non_scalar` | Dict[str, [Car](../../doc/models/car.md) \| [Morning](../../doc/models/morning.md) \| [Atom](../../doc/models/atom.md)] | Body, Required | This is Dictionary of a container for one-of cases. |
| `body_mixed` | Dict[str, int] \| Dict[str, [Atom](../../doc/models/atom.md)] | Body, Required | This is a container for any-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
collect = {
    'body_scalar': [
        75.62
    ],
    'body_non_scalar': {
        'key0': Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        'key1': Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        )
    },
    'body_mixed': {
        'key0': 216
    }
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
    single_inner_map={
        'key0': Atom(
            number_of_electrons=224,
            number_of_protons=134
        )
    },
    all_inner_array=[
        Orbit(
            number_of_electrons=218
        ),
        Orbit(
            number_of_electrons=218
        ),
        Orbit(
            number_of_electrons=218
        )
    ],
    outer_array=[
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        )
    ],
    outer_map={
        'key0': Morning(
            starts_at='startsAt6',
            ends_at='endsAt2',
            offer_tea_break=False,
            session_type='Morning'
        ),
        'key1': Morning(
            starts_at='startsAt6',
            ends_at='endsAt2',
            offer_tea_break=False,
            session_type='Morning'
        ),
        'key2': Morning(
            starts_at='startsAt6',
            ends_at='endsAt2',
            offer_tea_break=False,
            session_type='Morning'
        )
    },
    inner_collection_with_nullable=Atom(
        number_of_electrons=224,
        number_of_protons=134
    )
)

query_non_scalar_model = NonScalarModel(
    single_inner_map={
        'key0': Atom(
            number_of_electrons=224,
            number_of_protons=134
        ),
        'key1': Atom(
            number_of_electrons=224,
            number_of_protons=134
        ),
        'key2': Atom(
            number_of_electrons=224,
            number_of_protons=134
        )
    },
    all_inner_array=[
        Orbit(
            number_of_electrons=218
        ),
        Orbit(
            number_of_electrons=218
        ),
        Orbit(
            number_of_electrons=218
        )
    ],
    outer_array=[
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        )
    ],
    outer_map={
        'key0': Morning(
            starts_at='startsAt6',
            ends_at='endsAt2',
            offer_tea_break=False,
            session_type='Morning'
        ),
        'key1': Morning(
            starts_at='startsAt6',
            ends_at='endsAt2',
            offer_tea_break=False,
            session_type='Morning'
        )
    },
    inner_collection_with_nullable=Atom(
        number_of_electrons=224,
        number_of_protons=134
    )
)

query_mixed_model = MixedModel(
    single_inner_map={
        'key0': 240,
        'key1': 241,
        'key2': 242
    },
    all_inner_array=[
        False,
        True,
        False
    ],
    outer_array=[
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        )
    ],
    outer_map={
        'key0': Postman(
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
            joining_day=DaysEnum.WEDNESDAY_,
            salary=210,
            working_days=[
                DaysEnum.THURSDAY
            ],
            person_type='Post'
        ),
        'key1': Postman(
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
            joining_day=DaysEnum.WEDNESDAY_,
            salary=210,
            working_days=[
                DaysEnum.THURSDAY
            ],
            person_type='Post'
        )
    }
)

form_scalar_model = ScalarModel(
    single_inner_map={
        'key0': 149.92
    },
    all_inner_array=[
        102,
        103,
        104
    ],
    outer_array=[
        2,
        3
    ],
    outer_map={
        'key0': 127,
        'key1': 128
    },
    inner_nullable=94,
    inner_array_with_nullable=[
        218,
        219
    ],
    inner_map_with_nullable={
        'key0': 150,
        'key1': 151,
        'key2': 152
    }
)

form_mixed_model = MixedModel(
    single_inner_map={
        'key0': 62,
        'key1': 63,
        'key2': 64
    },
    all_inner_array=[
        False
    ],
    outer_array=[
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        )
    ],
    outer_map={
        'key0': Postman(
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
            joining_day=DaysEnum.WEDNESDAY_,
            salary=210,
            working_days=[
                DaysEnum.THURSDAY
            ],
            person_type='Post'
        ),
        'key1': Postman(
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
            joining_day=DaysEnum.WEDNESDAY_,
            salary=210,
            working_days=[
                DaysEnum.THURSDAY
            ],
            person_type='Post'
        )
    }
)

query_scalar_model = ScalarModel(
    single_inner_map={
        'key0': 2.02
    },
    all_inner_array=[
        196
    ],
    outer_array=[
        216,
        217
    ],
    outer_map={
        'key0': 185,
        'key1': 186
    },
    inner_nullable=52,
    inner_array_with_nullable=[
        20,
        21
    ],
    inner_map_with_nullable={
        'key0': 208,
        'key1': 209,
        'key2': 210
    }
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
    single_inner_map={
        'key0': Atom(
            number_of_electrons=224,
            number_of_protons=134
        ),
        'key1': Atom(
            number_of_electrons=224,
            number_of_protons=134
        ),
        'key2': Atom(
            number_of_electrons=224,
            number_of_protons=134
        )
    },
    all_inner_array=[
        Orbit(
            number_of_electrons=218
        ),
        Orbit(
            number_of_electrons=218
        )
    ],
    outer_array=[
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        )
    ],
    outer_map={
        'key0': Morning(
            starts_at='startsAt6',
            ends_at='endsAt2',
            offer_tea_break=False,
            session_type='Morning'
        ),
        'key1': Morning(
            starts_at='startsAt6',
            ends_at='endsAt2',
            offer_tea_break=False,
            session_type='Morning'
        )
    },
    inner_collection_with_nullable=Atom(
        number_of_electrons=224,
        number_of_protons=134
    )
)

mixed_model = MixedModel(
    single_inner_map={
        'key0': 194,
        'key1': 195,
        'key2': 196
    },
    all_inner_array=[
        False
    ],
    outer_array=[
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        )
    ],
    outer_map={
        'key0': Postman(
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
            joining_day=DaysEnum.WEDNESDAY_,
            salary=210,
            working_days=[
                DaysEnum.THURSDAY
            ],
            person_type='Post'
        ),
        'key1': Postman(
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
            joining_day=DaysEnum.WEDNESDAY_,
            salary=210,
            working_days=[
                DaysEnum.THURSDAY
            ],
            person_type='Post'
        )
    }
)

scalar_model = ScalarModel(
    single_inner_map={
        'key0': 175.62,
        'key1': 175.63,
        'key2': 175.64
    },
    all_inner_array=[
        112,
        113
    ],
    outer_array=[
        12
    ],
    outer_map={
        'key0': 137
    },
    inner_nullable=104,
    inner_array_with_nullable=[
        228
    ],
    inner_map_with_nullable={
        'key0': 160,
        'key1': 161
    }
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

