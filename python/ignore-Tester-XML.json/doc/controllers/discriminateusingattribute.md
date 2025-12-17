# Discriminateusingattribute

```python
discriminateusingattribute_controller = client.discriminateusingattribute
```

## Class Name

`Discriminateusingattribute`

## Methods

* [Generate](../../doc/controllers/discriminateusingattribute.md#generate)
* [Validate](../../doc/controllers/discriminateusingattribute.md#validate)


# Generate

This endpoint returns a 'Discriminator in Attribute' model as xml.

```python
def generate(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BaseForDiscriminatorInAttribute`](../../doc/models/base-for-discriminator-in-attribute.md).

## Example Usage

```python
result = discriminate_using_attribute_controller.generate()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Validate

This endpoint expects a 'Discriminator in Attribute' model as xml.

```python
def validate(self,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BaseForDiscriminatorInAttribute`](../../doc/models/base-for-discriminator-in-attribute.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = BaseForDiscriminatorInAttribute(
    base_field='Base Field6',
    discriminator='Darth Vader'
)

result = discriminate_using_attribute_controller.validate(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

