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

[`BaseForDiscriminatorInAttribute`](../../doc/models/base-for-discriminator-in-attribute.md)

## Example Usage

```python
result = discriminate_using_attribute_controller.generate()
print(result)
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

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = BaseForDiscriminatorInAttribute(
    base_field='Base Field6',
    discriminator='Darth Vader'
)

result = discriminate_using_attribute_controller.validate(body)
print(result)
```

