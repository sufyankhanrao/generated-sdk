# Multipart Params

```python
multipart_params_controller = client.multipart_params
```

## Class Name

`MultipartParamsController`


# Send Multipart With Json

Make a multipart request with a file, a json parameter and form parameters.

```python
def send_multipart_with_json(self,
                            options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file` | `typing.BinaryIO` | Form, Required | - |
| `integers` | `int` | Form, Required | - |
| `models` | [`List[Employee]`](../../doc/models/employee.md) | Form (JSON-Encoded), Required | - |
| `strings` | `str` | Form, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
collect = {
    'file': FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type'),
    'integers': 30,
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
            joining_day=Days.MONDAY,
            salary=88,
            working_days=[
                Days.SATURDAY,
                Days.SUNDAY
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
    'strings': 'strings0'
}
result = multipart_params_controller.send_multipart_with_json(collect)
print(result)
```

