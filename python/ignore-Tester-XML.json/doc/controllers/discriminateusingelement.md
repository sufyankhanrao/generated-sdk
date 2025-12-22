# Discriminateusingelement

```python
discriminateusingelement_controller = client.discriminateusingelement
```

## Class Name

`Discriminateusingelement`

## Methods

* [Generate](../../doc/controllers/discriminateusingelement.md#generate)
* [Validate](../../doc/controllers/discriminateusingelement.md#validate)


# Generate

This endpoint returns a 'Discriminator in Element' model as xml.

```python
def generate(self)
```

## Response Type

[`BaseForDiscriminatorInElement`](../../doc/models/base-for-discriminator-in-element.md)

## Example Usage

```python
result = discriminate_using_element_controller.generate()
print(result)
```


# Validate

This endpoint expects a 'Discriminator in Element' model as xml.

```python
def validate(self,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BaseForDiscriminatorInElement`](../../doc/models/base-for-discriminator-in-element.md) | Body, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = BaseForDiscriminatorInElement(
    base_field='Base Field6',
    discriminator='Anakin Skywalker'
)

result = discriminate_using_element_controller.validate(body)
print(result)
```

