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
               query_scalar,
               query_non_scalar,
               header=None,
               form_mixed=None,
               query_mixed=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `template` | float \| str \| int | Template, Required | This is a container for any-of cases. |
| `form_scalar` | List[Dict[str, int \| bool \| str]] \| None | Form, Required | This is List of Dictionary of a container for one-of cases. |
| `form_non_scalar` | Dict[str, List[[Atom](../../doc/models/atom.md)] \| [Atom](../../doc/models/atom.md)] | Form, Required | This is Dictionary of a container for any-of cases. |
| `query_scalar` | List[Dict[str, int \| bool \| str]] \| None | Query, Required | This is List of Dictionary of a container for one-of cases. |
| `query_non_scalar` | Dict[str, List[[Atom](../../doc/models/atom.md)] \| [Atom](../../doc/models/atom.md)] | Query, Required | This is Dictionary of a container for any-of cases. |
| `header` | float \| int \| str \| None | Header, Optional | This is a container for one-of cases. |
| `form_mixed` | List[Dict[str, bool]] \| List[Dict[str, [Vehicle](../../doc/models/vehicle.md)]] \| None | Form, Optional | This is a container for one-of cases. |
| `query_mixed` | List[Dict[str, bool]] \| List[Dict[str, [Vehicle](../../doc/models/vehicle.md)]] \| None | Query, Optional | This is a container for one-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
template = 67.15

form_scalar = [
    {
        'key0': 78
    }
]

form_non_scalar = {
    'key0': [
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        ),
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        ),
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        )
    ],
    'key1': [
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        )
    ],
    'key2': [
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        ),
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        )
    ]
}

query_scalar = [
    {
        'key0': 70
    }
]

query_non_scalar = {
    'key0': [
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        )
    ],
    'key1': [
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        ),
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        )
    ]
}

header = 2.45

form_mixed = [
    {
        'key0': True,
        'key1': False,
        'key2': True
    },
    {
        'key0': False
    }
]

query_mixed = [
    {
        'key0': True,
        'key1': False
    }
]

result = sender_controller.send_params(
    template,
    form_scalar,
    form_non_scalar,
    query_scalar,
    query_non_scalar,
    header=header,
    form_mixed=form_mixed,
    query_mixed=query_mixed
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
| `template` | float \| str \| int | Template, Required | This is a container for any-of cases. |
| `form_scalar` | List[Dict[str, int \| bool \| str]] \| None | Form, Required | This is List of Dictionary of a container for one-of cases. |
| `form_non_scalar` | Dict[str, List[[Atom](../../doc/models/atom.md)] \| [Atom](../../doc/models/atom.md)] | Form, Required | This is Dictionary of a container for any-of cases. |
| `query_scalar` | List[Dict[str, int \| bool \| str]] \| None | Query, Required | This is List of Dictionary of a container for one-of cases. |
| `query_non_scalar` | Dict[str, List[[Atom](../../doc/models/atom.md)] \| [Atom](../../doc/models/atom.md)] | Query, Required | This is Dictionary of a container for any-of cases. |
| `header` | float \| int \| str \| None | Header, Optional | This is a container for one-of cases. |
| `form_mixed` | List[Dict[str, bool]] \| List[Dict[str, [Vehicle](../../doc/models/vehicle.md)]] \| None | Form, Optional | This is a container for one-of cases. |
| `query_mixed` | List[Dict[str, bool]] \| List[Dict[str, [Vehicle](../../doc/models/vehicle.md)]] \| None | Query, Optional | This is a container for one-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
collect = {
    'template': 67.15,
    'form_scalar': [
        {
            'key0': 78
        }
    ],
    'form_non_scalar': {
        'key0': [
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            ),
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            ),
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            )
        ],
        'key1': [
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            )
        ],
        'key2': [
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            ),
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            )
        ]
    },
    'query_scalar': [
        {
            'key0': 70
        }
    ],
    'query_non_scalar': {
        'key0': [
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            )
        ],
        'key1': [
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            ),
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            )
        ]
    },
    'header': 2.45,
    'form_mixed': [
        {
            'key0': True,
            'key1': False,
            'key2': True
        },
        {
            'key0': False
        }
    ],
    'query_mixed': [
        {
            'key0': True,
            'key1': False
        }
    ]
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
| `body` | List[Dict[str, int \| bool \| str]] \| None | Body, Required | This is List of Dictionary of a container for one-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = [
    {
        'key0': 194
    },
    {
        'key0': 195,
        'key1': 196
    }
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
| `body` | Dict[str, List[[Atom](../../doc/models/atom.md)] \| [Atom](../../doc/models/atom.md)] | Body, Required | This is Dictionary of a container for any-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = {
    'key0': [
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        ),
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        )
    ],
    'key1': [
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        ),
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        ),
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        )
    ]
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
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | List[Dict[str, bool]] \| List[Dict[str, [Vehicle](../../doc/models/vehicle.md)]] \| None | Body, Optional | This is a container for one-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = [
    {
        'key0': True
    },
    {
        'key0': False,
        'key1': True
    },
    {
        'key0': True,
        'key1': False,
        'key2': True
    }
]

result = sender_controller.send_mixed_param(
    body=body
)
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
                 body_mixed=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body_scalar` | List[Dict[str, int \| bool \| str]] \| None | Body, Required | This is List of Dictionary of a container for one-of cases. |
| `body_non_scalar` | Dict[str, List[[Atom](../../doc/models/atom.md)] \| [Atom](../../doc/models/atom.md)] | Body, Required | This is Dictionary of a container for any-of cases. |
| `body_mixed` | List[Dict[str, bool]] \| List[Dict[str, [Vehicle](../../doc/models/vehicle.md)]] \| None | Body, Optional | This is a container for one-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body_scalar = [
    {
        'key0': 206
    },
    {
        'key0': 207,
        'key1': 208
    }
]

body_non_scalar = {
    'key0': [
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        ),
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        )
    ],
    'key1': [
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        ),
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        ),
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        )
    ]
}

body_mixed = [
    {
        'key0': True,
        'key1': False
    }
]

result = sender_controller.send_combined(
    body_scalar,
    body_non_scalar,
    body_mixed=body_mixed
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
| `body_scalar` | List[Dict[str, int \| bool \| str]] \| None | Body, Required | This is List of Dictionary of a container for one-of cases. |
| `body_non_scalar` | Dict[str, List[[Atom](../../doc/models/atom.md)] \| [Atom](../../doc/models/atom.md)] | Body, Required | This is Dictionary of a container for any-of cases. |
| `body_mixed` | List[Dict[str, bool]] \| List[Dict[str, [Vehicle](../../doc/models/vehicle.md)]] \| None | Body, Optional | This is a container for one-of cases. |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
collect = {
    'body_scalar': [
        {
            'key0': 206
        },
        {
            'key0': 207,
            'key1': 208
        }
    ],
    'body_non_scalar': {
        'key0': [
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            ),
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            )
        ],
        'key1': [
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            ),
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            ),
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            )
        ]
    },
    'body_mixed': [
        {
            'key0': True,
            'key1': False
        }
    ]
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
                        form_scalar_model=None,
                        form_non_scalar_model=None,
                        form_mixed_model=None,
                        query_scalar_model=None,
                        query_non_scalar_model=None,
                        query_mixed_model=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `form_scalar_model` | [`ScalarModel`](../../doc/models/scalar-model.md) | Form, Optional | - |
| `form_non_scalar_model` | [`NonScalarModel`](../../doc/models/non-scalar-model.md) | Form, Optional | - |
| `form_mixed_model` | [`MixedModel`](../../doc/models/mixed-model.md) | Form, Optional | - |
| `query_scalar_model` | [`ScalarModel`](../../doc/models/scalar-model.md) | Query, Optional | - |
| `query_non_scalar_model` | [`NonScalarModel`](../../doc/models/non-scalar-model.md) | Query, Optional | - |
| `query_mixed_model` | [`MixedModel`](../../doc/models/mixed-model.md) | Query, Optional | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
form_scalar_model = ScalarModel(
    multi_any_of=184.45,
    multi_one_of_any_of=156.91,
    single_inner_map_of_array={
        'key0': [
            62.72
        ],
        'key1': [
            62.73,
            62.74
        ]
    },
    outer_map_of_single_inner_array={
        'key0': [
            170.62
        ],
        'key1': [
            170.63,
            170.64
        ]
    },
    all_inner_array_of_map=[
        {
            'key0': 54,
            'key1': 55,
            'key2': 56
        },
        {
            'key0': 55
        }
    ],
    all_inner_array_of_map_2={
        'key0': [
            {
                'key0': 223,
                'key1': 224
            }
        ]
    },
    outer_array_of_map=[
        {
            'key0': 162,
            'key1': 163
        }
    ],
    outer_array_of_map_2=[
        {
            'key0': [
                28,
                29,
                30
            ],
            'key1': [
                29
            ]
        },
        {
            'key0': [
                29
            ],
            'key1': [
                30,
                31
            ],
            'key2': [
                31,
                32,
                33
            ]
        }
    ],
    outer_map_of_array={
        'key0': [
            162,
            163
        ],
        'key1': [
            163,
            164,
            165
        ],
        'key2': [
            164
        ]
    },
    outer_map_of_array_2={
        'key0': [
            {
                'key0': 60
            },
            {
                'key0': 61,
                'key1': 62
            }
        ]
    }
)

form_non_scalar_model = NonScalarModel(
    multi_any_of=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    multi_one_of_any_of=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    single_inner_map_of_array={
        'key0': [
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            ),
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            ),
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            )
        ],
        'key1': [
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            )
        ]
    },
    outer_map_of_single_inner_array={
        'key0': [
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            )
        ],
        'key1': [
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            ),
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            )
        ],
        'key2': [
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            ),
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            ),
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            )
        ]
    },
    all_inner_array_of_map=[
        {
            'key0': Orbit(
                number_of_electrons=218
            ),
            'key1': Orbit(
                number_of_electrons=218
            )
        },
        {
            'key0': Orbit(
                number_of_electrons=218
            ),
            'key1': Orbit(
                number_of_electrons=218
            ),
            'key2': Orbit(
                number_of_electrons=218
            )
        }
    ],
    all_inner_array_of_map_2={
        'key0': [
            {
                'key0': Orbit(
                    number_of_electrons=218
                )
            }
        ],
        'key1': [
            {
                'key0': Orbit(
                    number_of_electrons=218
                ),
                'key1': Orbit(
                    number_of_electrons=218
                ),
                'key2': Orbit(
                    number_of_electrons=218
                )
            },
            {
                'key0': Orbit(
                    number_of_electrons=218
                ),
                'key1': Orbit(
                    number_of_electrons=218
                )
            }
        ],
        'key2': [
            {
                'key0': Orbit(
                    number_of_electrons=218
                ),
                'key1': Orbit(
                    number_of_electrons=218
                )
            },
            {
                'key0': Orbit(
                    number_of_electrons=218
                )
            },
            {
                'key0': Orbit(
                    number_of_electrons=218
                ),
                'key1': Orbit(
                    number_of_electrons=218
                ),
                'key2': Orbit(
                    number_of_electrons=218
                )
            }
        ]
    },
    outer_array_of_map=[
        {
            'key0': Car(
                number_of_tyres='NumberOfTyres4',
                have_trunk=False
            ),
            'key1': Car(
                number_of_tyres='NumberOfTyres4',
                have_trunk=False
            )
        },
        {
            'key0': Car(
                number_of_tyres='NumberOfTyres4',
                have_trunk=False
            )
        }
    ],
    outer_array_of_map_2=[
        {
            'key0': [
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
            'key1': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ],
            'key2': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                ),
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ]
        },
        {
            'key0': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ]
        },
        {
            'key0': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                ),
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ],
            'key1': [
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
            ]
        }
    ],
    outer_map_of_array={
        'key0': [
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            ),
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            ),
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            )
        ]
    },
    outer_map_of_array_2={
        'key0': [
            {
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
            {
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
            {
                'key0': Morning(
                    starts_at='startsAt6',
                    ends_at='endsAt2',
                    offer_tea_break=False,
                    session_type='Morning'
                )
            }
        ],
        'key1': [
            {
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
            }
        ]
    }
)

form_mixed_model = MixedModel(
    multi_any_of=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    multi_one_of_any_of=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    single_inner_map_of_array={
        'key0': [
            10
        ],
        'key1': [
            11,
            12
        ],
        'key2': [
            12,
            13,
            14
        ]
    },
    outer_map_of_single_inner_array={
        'key0': [
            84,
            85,
            86
        ],
        'key1': [
            85
        ]
    },
    all_inner_array_of_map=[
        {
            'key0': True,
            'key1': False,
            'key2': True
        },
        {
            'key0': False
        }
    ],
    all_inner_array_of_map_2={
        'key0': [
            {
                'key0': False
            },
            {
                'key0': True,
                'key1': False
            },
            {
                'key0': False,
                'key1': True,
                'key2': False
            }
        ]
    },
    outer_array_of_map=[
        {
            'key0': Car(
                number_of_tyres='NumberOfTyres4',
                have_trunk=False
            ),
            'key1': Car(
                number_of_tyres='NumberOfTyres4',
                have_trunk=False
            )
        }
    ],
    outer_array_of_map_2=[
        {
            'key0': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                ),
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ],
            'key1': [
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
            ]
        },
        {
            'key0': [
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
            'key1': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ],
            'key2': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                ),
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ]
        }
    ],
    outer_map_of_array={
        'key0': [
            Postman(
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
            Postman(
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
        ],
        'key1': [
            Postman(
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
            Postman(
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
            Postman(
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
        ],
        'key2': [
            Postman(
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
        ]
    },
    outer_map_of_array_2={
        'key0': [
            {
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
                ),
                'key2': Postman(
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
            },
            {
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
                )
            }
        ]
    }
)

query_scalar_model = ScalarModel(
    multi_any_of=36.55,
    multi_one_of_any_of=26.97,
    single_inner_map_of_array={
        'key0': [
            4.42,
            4.43,
            4.44
        ]
    },
    outer_map_of_single_inner_array={
        'key0': [
            22.72
        ],
        'key1': [
            22.73,
            22.74
        ]
    },
    all_inner_array_of_map=[
        {
            'key0': 112,
            'key1': 113,
            'key2': 114
        },
        {
            'key0': 113
        }
    ],
    all_inner_array_of_map_2={
        'key0': [
            {
                'key0': 75,
                'key1': 74,
                'key2': 73
            }
        ]
    },
    outer_array_of_map=[
        {
            'key0': 110,
            'key1': 109,
            'key2': 108
        }
    ],
    outer_array_of_map_2=[
        {
            'key0': [
                86,
                87,
                88
            ],
            'key1': [
                87
            ]
        },
        {
            'key0': [
                87
            ],
            'key1': [
                88,
                89
            ],
            'key2': [
                89,
                90,
                91
            ]
        }
    ],
    outer_map_of_array={
        'key0': [
            220,
            221
        ],
        'key1': [
            221,
            222,
            223
        ],
        'key2': [
            222
        ]
    },
    outer_map_of_array_2={
        'key0': [
            {
                'key0': 118
            },
            {
                'key0': 119,
                'key1': 120
            }
        ]
    }
)

query_non_scalar_model = NonScalarModel(
    multi_any_of=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    multi_one_of_any_of=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    single_inner_map_of_array={
        'key0': [
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            )
        ],
        'key1': [
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            ),
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            )
        ],
        'key2': [
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            ),
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            ),
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            )
        ]
    },
    outer_map_of_single_inner_array={
        'key0': [
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            ),
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            ),
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            )
        ],
        'key1': [
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            )
        ]
    },
    all_inner_array_of_map=[
        {
            'key0': Orbit(
                number_of_electrons=218
            )
        }
    ],
    all_inner_array_of_map_2={
        'key0': [
            {
                'key0': Orbit(
                    number_of_electrons=218
                ),
                'key1': Orbit(
                    number_of_electrons=218
                )
            },
            {
                'key0': Orbit(
                    number_of_electrons=218
                ),
                'key1': Orbit(
                    number_of_electrons=218
                ),
                'key2': Orbit(
                    number_of_electrons=218
                )
            }
        ]
    },
    outer_array_of_map=[
        {
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
    ],
    outer_array_of_map_2=[
        {
            'key0': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                ),
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ],
            'key1': [
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
            ]
        },
        {
            'key0': [
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
            'key1': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ],
            'key2': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                ),
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ]
        }
    ],
    outer_map_of_array={
        'key0': [
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            ),
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            )
        ],
        'key1': [
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            ),
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            ),
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            )
        ],
        'key2': [
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            )
        ]
    },
    outer_map_of_array_2={
        'key0': [
            {
                'key0': Morning(
                    starts_at='startsAt6',
                    ends_at='endsAt2',
                    offer_tea_break=False,
                    session_type='Morning'
                )
            },
            {
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
            }
        ]
    }
)

query_mixed_model = MixedModel(
    multi_any_of=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    multi_one_of_any_of=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    single_inner_map_of_array={
        'key0': [
            44,
            43
        ]
    },
    outer_map_of_single_inner_array={
        'key0': [
            6,
            7,
            8
        ],
        'key1': [
            7
        ]
    },
    all_inner_array_of_map=[
        {
            'key0': True,
            'key1': False,
            'key2': True
        },
        {
            'key0': False
        }
    ],
    all_inner_array_of_map_2={
        'key0': [
            {
                'key0': False,
                'key1': True
            }
        ]
    },
    outer_array_of_map=[
        {
            'key0': Car(
                number_of_tyres='NumberOfTyres4',
                have_trunk=False
            ),
            'key1': Car(
                number_of_tyres='NumberOfTyres4',
                have_trunk=False
            )
        }
    ],
    outer_array_of_map_2=[
        {
            'key0': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                ),
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ],
            'key1': [
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
            ]
        },
        {
            'key0': [
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
            'key1': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ],
            'key2': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                ),
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ]
        }
    ],
    outer_map_of_array={
        'key0': [
            Postman(
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
            Postman(
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
        ],
        'key1': [
            Postman(
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
            Postman(
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
            Postman(
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
        ],
        'key2': [
            Postman(
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
        ]
    },
    outer_map_of_array_2={
        'key0': [
            {
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
                ),
                'key2': Postman(
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
            },
            {
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
                )
            }
        ]
    }
)

result = sender_controller.send_in_model_params(
    form_scalar_model=form_scalar_model,
    form_non_scalar_model=form_non_scalar_model,
    form_mixed_model=form_mixed_model,
    query_scalar_model=query_scalar_model,
    query_non_scalar_model=query_non_scalar_model,
    query_mixed_model=query_mixed_model
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
    multi_any_of=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    multi_one_of_any_of=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    single_inner_map_of_array={
        'key0': [
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            ),
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            )
        ]
    },
    outer_map_of_single_inner_array={
        'key0': [
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            ),
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            ),
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            )
        ],
        'key1': [
            Atom(
                number_of_electrons=224,
                number_of_protons=134
            )
        ]
    },
    all_inner_array_of_map=[
        {
            'key0': Orbit(
                number_of_electrons=218
            )
        }
    ],
    all_inner_array_of_map_2={
        'key0': [
            {
                'key0': Orbit(
                    number_of_electrons=218
                ),
                'key1': Orbit(
                    number_of_electrons=218
                ),
                'key2': Orbit(
                    number_of_electrons=218
                )
            },
            {
                'key0': Orbit(
                    number_of_electrons=218
                )
            },
            {
                'key0': Orbit(
                    number_of_electrons=218
                ),
                'key1': Orbit(
                    number_of_electrons=218
                )
            }
        ]
    },
    outer_array_of_map=[
        {
            'key0': Car(
                number_of_tyres='NumberOfTyres4',
                have_trunk=False
            ),
            'key1': Car(
                number_of_tyres='NumberOfTyres4',
                have_trunk=False
            )
        }
    ],
    outer_array_of_map_2=[
        {
            'key0': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                ),
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ],
            'key1': [
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
            ]
        },
        {
            'key0': [
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
            'key1': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ],
            'key2': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                ),
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ]
        }
    ],
    outer_map_of_array={
        'key0': [
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            ),
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            )
        ],
        'key1': [
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            ),
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            ),
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            )
        ],
        'key2': [
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            )
        ]
    },
    outer_map_of_array_2={
        'key0': [
            {
                'key0': Morning(
                    starts_at='startsAt6',
                    ends_at='endsAt2',
                    offer_tea_break=False,
                    session_type='Morning'
                )
            },
            {
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
            }
        ]
    }
)

mixed_model = MixedModel(
    multi_any_of=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    multi_one_of_any_of=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    single_inner_map_of_array={
        'key0': [
            134
        ],
        'key1': [
            135,
            136
        ],
        'key2': [
            136,
            137,
            138
        ]
    },
    outer_map_of_single_inner_array={
        'key0': [
            216,
            217,
            218
        ],
        'key1': [
            217
        ]
    },
    all_inner_array_of_map=[
        {
            'key0': True,
            'key1': False,
            'key2': True
        },
        {
            'key0': False
        }
    ],
    all_inner_array_of_map_2={
        'key0': [
            {
                'key0': False
            },
            {
                'key0': True,
                'key1': False
            },
            {
                'key0': False,
                'key1': True,
                'key2': False
            }
        ]
    },
    outer_array_of_map=[
        {
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
    ],
    outer_array_of_map_2=[
        {
            'key0': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                ),
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ],
            'key1': [
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
            ]
        },
        {
            'key0': [
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
            'key1': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ],
            'key2': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                ),
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ]
        }
    ],
    outer_map_of_array={
        'key0': [
            Postman(
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
            Postman(
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
        ],
        'key1': [
            Postman(
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
            Postman(
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
            Postman(
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
        ],
        'key2': [
            Postman(
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
        ]
    },
    outer_map_of_array_2={
        'key0': [
            {
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
                ),
                'key2': Postman(
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
            },
            {
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
                )
            }
        ]
    }
)

scalar_model = ScalarModel(
    multi_any_of=210.15,
    multi_one_of_any_of=182.61,
    single_inner_map_of_array={
        'key0': [
            88.42,
            88.43,
            88.44
        ]
    },
    outer_map_of_single_inner_array={
        'key0': [
            196.32,
            196.33,
            196.34
        ]
    },
    all_inner_array_of_map=[
        {
            'key0': 64,
            'key1': 65
        }
    ],
    all_inner_array_of_map_2={
        'key0': [
            {
                'key0': 233
            },
            {
                'key0': 234,
                'key1': 235
            },
            {
                'key0': 235,
                'key1': 236,
                'key2': 237
            }
        ],
        'key1': [
            {
                'key0': 232,
                'key1': 233,
                'key2': 234
            },
            {
                'key0': 233
            }
        ]
    },
    outer_array_of_map=[
        {
            'key0': 172
        },
        {
            'key0': 173,
            'key1': 174
        },
        {
            'key0': 174,
            'key1': 175,
            'key2': 176
        }
    ],
    outer_array_of_map_2=[
        {
            'key0': [
                38,
                39
            ]
        }
    ],
    outer_map_of_array={
        'key0': [
            172
        ],
        'key1': [
            173,
            174
        ]
    },
    outer_map_of_array_2={
        'key0': [
            {
                'key0': 70,
                'key1': 71,
                'key2': 72
            }
        ],
        'key1': [
            {
                'key0': 71
            },
            {
                'key0': 72,
                'key1': 73
            }
        ],
        'key2': [
            {
                'key0': 72,
                'key1': 73
            },
            {
                'key0': 73,
                'key1': 74,
                'key2': 75
            },
            {
                'key0': 74
            }
        ]
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

