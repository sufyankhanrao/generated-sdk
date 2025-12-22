# Form

This controller contains the usage of globally defined type combinators in form

```python
form_controller = client.form
```

## Class Name

`FormController`

## Methods

* [Send All of Discriminated](../../doc/controllers/form.md#send-all-of-discriminated)
* [Send Oaf Discriminated](../../doc/controllers/form.md#send-oaf-discriminated)
* [Send Alias](../../doc/controllers/form.md#send-alias)
* [Send Oaf With All of Discriminated Variants](../../doc/controllers/form.md#send-oaf-with-all-of-discriminated-variants)


# Send All of Discriminated

Send all Globally defined allOf discriminated TypeCombinators in form

```python
def send_all_of_discriminated(self,
                             one_of_cat_dog_all_of_pet_type,
                             one_of_cat_dog_oaf_pet_type,
                             one_of_cat_dog_kind)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `one_of_cat_dog_all_of_pet_type` | [Cat](../../doc/models/cat.md) \| [Dog](../../doc/models/dog.md) | Form, Required | OneOf (Cat, Dog) with "pet_type" discriminator without mapping |
| `one_of_cat_dog_oaf_pet_type` | [Cat](../../doc/models/cat.md) \| [Dog](../../doc/models/dog.md) | Form, Required | OneOf (Cat, Dog) with "pet_type" discriminator same as allOf with different mapping |
| `one_of_cat_dog_kind` | [Cat](../../doc/models/cat.md) \| [Dog](../../doc/models/dog.md) | Form, Required | OneOf (Cat, Dog) with an additional "kind" discriminator with mapping (small:Cat, large:Dog) |

## Response Type

[Cat](../../doc/models/cat.md) | [Dog](../../doc/models/dog.md)

## Example Usage

```python
one_of_cat_dog_all_of_pet_type = Cat(
    name='hosico',
    color='yellow',
    one_of_kind='One Of kind2',
    pet_type='Cat',
    id='String5',
    friend=Lion(
        id='id0',
        weight='weight6',
        mtype='hunter',
        kind='kind8'
    ),
    enemy=Lion(
        id='id0',
        weight='weight6',
        mtype='type0',
        kind='northener'
    ),
    kind='kind2'
)

one_of_cat_dog_oaf_pet_type = Cat(
    name='hosico',
    color='yellow',
    one_of_kind='One Of kind2',
    pet_type='Kitty',
    id='String5',
    friend=Lion(
        id='id0',
        weight='weight6',
        mtype='hunter',
        kind='kind8'
    ),
    enemy=Lion(
        id='id0',
        weight='weight6',
        mtype='type0',
        kind='northener'
    ),
    kind='kind2'
)

one_of_cat_dog_kind = Cat(
    name='hosico',
    color='yellow',
    one_of_kind='small',
    pet_type='Cat',
    id='String5',
    friend=Lion(
        id='id0',
        weight='weight6',
        mtype='hunter',
        kind='kind8'
    ),
    enemy=Lion(
        id='id0',
        weight='weight6',
        mtype='type0',
        kind='northener'
    ),
    kind='kind2'
)

result = form_controller.send_all_of_discriminated(
    one_of_cat_dog_all_of_pet_type,
    one_of_cat_dog_oaf_pet_type,
    one_of_cat_dog_kind
)
print(result)
```

## Example Response

```
{
  "name": "hosico",
  "color": "yellow",
  "pet_type": "Cat"
}
```


# Send Oaf Discriminated

Send all Globally defined oneOf and anyOf TypeCombinators in form

```python
def send_oaf_discriminated(self,
                          one_of_lion_and_dear,
                          one_of_lion_and_dear_2,
                          one_of_dear_and_one_of_lion_squirrel,
                          one_of_lion_and_squirrel_speed,
                          one_of_lion_and_squirrel_area)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `one_of_lion_and_dear` | [Lion](../../doc/models/lion.md) \| [Deer](../../doc/models/deer.md) | Form, Required | OneOf (Lion, Deer) with "type" discriminator of mapping (hunter:Lion, Hunted:Deer) |
| `one_of_lion_and_dear_2` | [Lion](../../doc/models/lion.md) \| [Deer](../../doc/models/deer.md) | Form, Required | OneOf (Lion, Deer) with "type" discriminator of mapping (h$u\n(	,e),r:Lion, hunted:Deer) |
| `one_of_dear_and_one_of_lion_squirrel` | [Deer](../../doc/models/deer.md) \| [Lion](../../doc/models/lion.md) \| [Squirrel](../../doc/models/squirrel.md) | Form, Required | Multi level OneOf (Deer, OneOf (Lion, Squirrel)) |
| `one_of_lion_and_squirrel_speed` | [Lion](../../doc/models/lion.md) \| [Squirrel](../../doc/models/squirrel.md) | Form, Required | OneOf (Lion, Squirrel) with an additional "kind" property discriminator of mapping (fast:Lion, faster:Squirrel) |
| `one_of_lion_and_squirrel_area` | [Lion](../../doc/models/lion.md) \| [Squirrel](../../doc/models/squirrel.md) | Form, Required | OneOf (Lion, Squirrel) with an additional "kind" property discriminator of mapping (northener:Lion, westener:Squirrel) |

## Response Type

[Lion](../../doc/models/lion.md) | [Squirrel](../../doc/models/squirrel.md)

## Example Usage

```python
one_of_lion_and_dear = Lion(
    id='23',
    weight='100 kg',
    mtype='hunter',
    kind='kind8'
)

one_of_lion_and_dear_2 = Lion(
    id='23',
    weight='100 kg',
    mtype='h$u\\n(	,e),r',
    kind='kind8'
)

one_of_dear_and_one_of_lion_squirrel = Deer(
    name='name0',
    weight='100 kg',
    mtype='hunter'
)

one_of_lion_and_squirrel_speed = Lion(
    id='23',
    weight='100 kg',
    mtype='hunter',
    kind='{fa{}st}'
)

one_of_lion_and_squirrel_area = Lion(
    id='23',
    weight='100 kg',
    mtype='hunter',
    kind='northener'
)

result = form_controller.send_oaf_discriminated(
    one_of_lion_and_dear,
    one_of_lion_and_dear_2,
    one_of_dear_and_one_of_lion_squirrel,
    one_of_lion_and_squirrel_speed,
    one_of_lion_and_squirrel_area
)
print(result)
```


# Send Alias

Send all Globally defined TypeCombinators Aliases in form

```python
def send_alias(self,
              alias,
              alias_of_alias)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `alias` | [Lion](../../doc/models/lion.md) \| [Deer](../../doc/models/deer.md) | Form, Required | OneOf (Lion, Deer) with "type" discriminator of mapping (hunter:Lion, Hunted:Deer) |
| `alias_of_alias` | [Lion](../../doc/models/lion.md) \| [Deer](../../doc/models/deer.md) | Form, Required | OneOf (Lion, Deer) with "type" discriminator of mapping (hunter:Lion, Hunted:Deer) |

## Response Type

[Lion](../../doc/models/lion.md) | [Deer](../../doc/models/deer.md)

## Example Usage

```python
alias = Deer(
    name='deer21',
    weight='30 kg',
    mtype='Hunted'
)

alias_of_alias = Deer(
    name='deer22',
    weight='20 kg',
    mtype='Hunted'
)

result = form_controller.send_alias(
    alias,
    alias_of_alias
)
print(result)
```

## Example Response

```
{
  "name": "deer21",
  "weight": "30 kg",
  "type": "Hunted"
}
```


# Send Oaf With All of Discriminated Variants

**This endpoint is deprecated since version 2.0. This operation is deprecated. Use createPet**

Send all Globally defined oneOf and anyOf TypeCombinators in form

```python
def send_oaf_with_all_of_discriminated_variants(self,
                                               one_of_animal_lion_disc_kind,
                                               one_of_cat_lion_disc_kind,
                                               one_of_animal_lion,
                                               one_of_cat_lion,
                                               one_of_cat_dog_and_lion_deer,
                                               one_of_employee_entrepreneur_disc,
                                               one_of_employee_entrepreneur)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `one_of_animal_lion_disc_kind` | [Animal](../../doc/models/animal.md) \| [Lion](../../doc/models/lion.md) | Form, Required | OneOf (Animal, Lion) with "kind" discriminator of mapping (wild:Lion, pet:Animal) |
| `one_of_cat_lion_disc_kind` | [Cat](../../doc/models/cat.md) \| [Lion](../../doc/models/lion.md) | Form, Required | OneOf (Animal, Lion) with "kind" discriminator of mapping (wild:Lion, pet:Cat) |
| `one_of_animal_lion` | [Animal](../../doc/models/animal.md) \| [Lion](../../doc/models/lion.md) | Form, Required | OneOf (Animal, Lion) without discriminator. Here AllOf discriminator is implicitly applied through Animal. |
| `one_of_cat_lion` | [Cat](../../doc/models/cat.md) \| [Lion](../../doc/models/lion.md) | Form, Required | OneOf (Cat, Lion) without discriminator. |
| `one_of_cat_dog_and_lion_deer` | [Animal](../../doc/models/animal.md) \| [Lion](../../doc/models/lion.md) \| [Squirrel](../../doc/models/squirrel.md) | Form, Required | OneOf (Animal, OneOfDeerAndOneOfLionSquirrel) without discriminator. |
| `one_of_employee_entrepreneur_disc` | [Employee](../../doc/models/employee.md) \| [Entrepreneur](../../doc/models/entrepreneur.md) | Form, Required | OneOf (Employee, Entrepreneur) with "build" discriminator of mapping (Endomorphs:Employee, Mesomorphs:Entrepreneur) |
| `one_of_employee_entrepreneur` | [Employee](../../doc/models/employee.md) \| [Entrepreneur](../../doc/models/entrepreneur.md) | Form, Required | OneOf (Employee, Entrepreneur) without discriminator mapping. |

## Response Type

[Animal](../../doc/models/animal.md) | [Lion](../../doc/models/lion.md) | [Cat](../../doc/models/cat.md) | [Squirrel](../../doc/models/squirrel.md) | [Employee](../../doc/models/employee.md) | [Entrepreneur](../../doc/models/entrepreneur.md)

## Example Usage

```python
one_of_animal_lion_disc_kind = Lion(
    id='23',
    weight='100 kg',
    mtype='hunter',
    kind='wild'
)

one_of_cat_lion_disc_kind = Lion(
    id='23',
    weight='100 kg',
    mtype='hunter',
    kind='wild'
)

one_of_animal_lion = Animal(
    pet_type='Animal',
    id=2,
    friend=Deer(
        name='deer22',
        weight='20 kg',
        mtype='Hunted'
    ),
    enemy=Lion(
        id='23',
        weight='100 kg',
        mtype='hunter',
        kind='northener'
    ),
    kind='kind2'
)

one_of_cat_lion = Cat(
    name='hosico',
    color='yellow',
    one_of_kind='One Of kind2',
    pet_type='catty',
    id='String5',
    friend=Lion(
        id='id0',
        weight='weight6',
        mtype='hunter',
        kind='kind8'
    ),
    enemy=Lion(
        id='id0',
        weight='weight6',
        mtype='type0',
        kind='northener'
    ),
    kind='kind2'
)

one_of_cat_dog_and_lion_deer = Animal(
    pet_type='Animal',
    id='23',
    friend=Lion(
        id='id0',
        weight='weight6',
        mtype='hunter',
        kind='kind8'
    ),
    enemy=Lion(
        id='id0',
        weight='weight6',
        mtype='type0',
        kind='northener'
    ),
    kind='kind2'
)

one_of_employee_entrepreneur_disc = Employee(
    name='John',
    ssn=123,
    salary=157.76,
    build='Endomorphs',
    mtype='Empl'
)

one_of_employee_entrepreneur = Employee(
    name='John',
    ssn=123,
    salary=157.76,
    build='Endomorphs',
    mtype='Empl'
)

result = form_controller.send_oaf_with_all_of_discriminated_variants(
    one_of_animal_lion_disc_kind,
    one_of_cat_lion_disc_kind,
    one_of_animal_lion,
    one_of_cat_lion,
    one_of_cat_dog_and_lion_deer,
    one_of_employee_entrepreneur_disc,
    one_of_employee_entrepreneur
)
print(result)
```

