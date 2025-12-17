
# Scalar Model

This class contains scalar types in oneOf/anyOf cases.

## Structure

`ScalarModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `multi_any_of` | float \| str \| int | Required | This is a container for any-of cases. |
| `multi_one_of_any_of` | float \| int \| str | Required | This is a container for one-of cases. |
| `single_inner_map_of_array` | Dict[str, List[float]] \| Dict[str, float] | Required | This is a container for any-of cases. |
| `outer_map_of_single_inner_array` | Dict[str, List[float] \| float] | Required | This is Dictionary of a container for any-of cases. |
| `all_inner_array_of_map` | List[Dict[str, int]] \| List[Dict[str, str]] \| None | Required | This is a container for one-of cases. |
| `all_inner_array_of_map_2` | Dict[str, List[Dict[str, int]] \| List[Dict[str, str]]] \| None | Required | This is Dictionary of a container for one-of cases. |
| `outer_array_of_map` | List[Dict[str, int \| bool \| str]] \| None | Optional | This is List of Dictionary of a container for one-of cases. |
| `outer_array_of_map_2` | List[Dict[str, List[int] \| List[bool] \| List[str]]] \| None | Optional | This is List of Dictionary of a container for one-of cases. |
| `outer_map_of_array` | Dict[str, List[int \| bool]] \| None | Optional | This is Dictionary of List of a container for any-of cases. |
| `outer_map_of_array_2` | Dict[str, List[Dict[str, int] \| Dict[str, bool]]] \| None | Optional | This is Dictionary of List of a container for any-of cases. |

## Example (as JSON)

```json
{
  "multiAnyOf": 65.55,
  "multiOneOfAnyOf": 253.97,
  "singleInnerMapOfArray": {
    "key0": [
      231.42,
      231.43
    ],
    "key1": [
      231.43,
      231.44,
      231.45
    ],
    "key2": [
      231.44
    ]
  },
  "outerMapOfSingleInnerArray": {
    "key0": [
      51.72,
      51.73
    ],
    "key1": [
      51.73,
      51.74,
      51.75
    ],
    "key2": [
      51.74
    ]
  },
  "allInnerArrayOfMap": [
    {
      "key0": 196
    },
    {
      "key0": 197,
      "key1": 198
    },
    {
      "key0": 198,
      "key1": 199,
      "key2": 200
    }
  ],
  "allInnerArrayOfMap2": {
    "key0": [
      {
        "key0": 191,
        "key1": 192,
        "key2": 193
      },
      {
        "key0": 192
      }
    ],
    "key1": [
      {
        "key0": 192
      },
      {
        "key0": 193,
        "key1": 194
      },
      {
        "key0": 194,
        "key1": 195,
        "key2": 196
      }
    ],
    "key2": [
      {
        "key0": 193,
        "key1": 194
      }
    ]
  },
  "outerArrayOfMap": [
    {
      "key0": 240
    },
    {
      "key0": 239,
      "key1": 238
    },
    {
      "key0": 238,
      "key1": 237,
      "key2": 236
    }
  ],
  "outerArrayOfMap2": [
    {
      "key0": [
        170
      ],
      "key1": [
        171,
        172
      ],
      "key2": [
        172,
        173,
        174
      ]
    },
    {
      "key0": [
        171,
        172
      ]
    },
    {
      "key0": [
        172,
        173,
        174
      ],
      "key1": [
        173
      ]
    }
  ],
  "outerMapOfArray": {
    "key0": [
      48,
      49,
      50
    ]
  },
  "outerMapOfArray2": {
    "key0": [
      {
        "key0": 202,
        "key1": 203
      },
      {
        "key0": 203,
        "key1": 204,
        "key2": 205
      },
      {
        "key0": 204
      }
    ],
    "key1": [
      {
        "key0": 203,
        "key1": 204,
        "key2": 205
      }
    ]
  }
}
```

