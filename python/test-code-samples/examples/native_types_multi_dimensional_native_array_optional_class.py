from testcodesamples.configuration import Environment
from testcodesamples.exceptions.api_exception import APIException
from testcodesamples.testcodesamples_client import TestcodesamplesClient

client = TestcodesamplesClient(
    environment=Environment.TESTING,
    port='80',
    suites=1
)

native_types_controller = client.native_types
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

try:
    result = native_types_controller.multi_dimensional_native_array_optional(
        boolean_array=boolean_array
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

