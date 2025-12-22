# API

```python
client_controller = client.client
```

## Class Name

`APIController`

## Methods

* [Retrieve Checkout Order](../../doc/controllers/api.md#retrieve-checkout-order)
* [Submit Vehicle Information](../../doc/controllers/api.md#submit-vehicle-information)
* [Submit a One of Vehicle](../../doc/controllers/api.md#submit-a-one-of-vehicle)
* [Submit a Map of Vehicles](../../doc/controllers/api.md#submit-a-map-of-vehicles)
* [Submit an Array of Vehicles](../../doc/controllers/api.md#submit-an-array-of-vehicles)


# Retrieve Checkout Order

Retrieves a checkout order, allowing response simulation via a complex header.

```python
def retrieve_checkout_order(self,
                           pay_pal_mock_response=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pay_pal_mock_response` | [`PaypalMockResponseSchema`](../../doc/models/paypal-mock-response-schema.md) | Header, Optional | Simulates negative responses. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SuccessResponse`](../../doc/models/success-response.md).

## Example Usage

```python
pay_pal_mock_response = PaypalMockResponseSchema(
    mock_application_codes='DUPLICATE_INVOICE_ID'
)

result = client_controller.retrieve_checkout_order(
    pay_pal_mock_response=pay_pal_mock_response
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Submit Vehicle Information

Accepts a single vehicle object in the header.

```python
def submit_vehicle_information(self,
                              vehicle_header)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vehicle_header` | [`Vehicle`](../../doc/models/vehicle.md) | Header, Required | JSON-serialized Vehicle object. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SuccessResponse`](../../doc/models/success-response.md).

## Example Usage

```python
vehicle_header = Vehicle(
    make='Toyota',
    model='Camry',
    year=2022,
    engine=Engine(
        horsepower=3000,
        fuel_type=FuelTypeEnum.PETROL
    )
)

result = client_controller.submit_vehicle_information(vehicle_header)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid input. | `APIException` |


# Submit a One of Vehicle

Accepts a Car or a Bike object in the header.

```python
def submit_a_one_of_vehicle(self,
                           one_of_vehicle)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `one_of_vehicle` | [Car](../../doc/models/car.md) \| [Bike](../../doc/models/bike.md) | Header, Required | Either a Car or a Bike. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SuccessResponse`](../../doc/models/success-response.md).

## Example Usage

```python
one_of_vehicle = Car(
    make='Toyota',
    model='Yaris',
    doors=2,
    engine=Engine(
        horsepower=1500,
        fuel_type=FuelTypeEnum.PETROL
    )
)

result = client_controller.submit_a_one_of_vehicle(one_of_vehicle)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Submit a Map of Vehicles

Accepts a map of vehicle objects in the header.

```python
def submit_a_map_of_vehicles(self,
                            map_of_vehicles)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `map_of_vehicles` | [`Dict[str, Vehicle]`](../../doc/models/vehicle.md) | Header, Required | JSON-serialized map of Vehicle objects. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SuccessResponse`](../../doc/models/success-response.md).

## Example Usage

```python
map_of_vehicles = {
    'Toyota Camry': Vehicle(
        make='Toyota',
        model='Camry',
        year=2022,
        engine=Engine(
            horsepower=3000,
            fuel_type=FuelTypeEnum.PETROL
        )
    ),
    'Toyota Yaris': Vehicle(
        make='Toyota',
        model='Yaris',
        year=2020,
        engine=Engine(
            horsepower=1300,
            fuel_type=FuelTypeEnum.PETROL
        )
    )
}

result = client_controller.submit_a_map_of_vehicles(map_of_vehicles)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid input | `APIException` |


# Submit an Array of Vehicles

Accepts an array of vehicles in the request body.

```python
def submit_an_array_of_vehicles(self,
                               array_of_vehicles)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `array_of_vehicles` | [`List[Vehicle]`](../../doc/models/vehicle.md) | Header, Required | Array parameter for Vehicle |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SuccessResponse`](../../doc/models/success-response.md).

## Example Usage

```python
array_of_vehicles = [
    Vehicle(
        make='Toyota',
        model='Camry',
        year=2022,
        engine=Engine(
            horsepower=3000,
            fuel_type=FuelTypeEnum.PETROL
        )
    ),
    Vehicle(
        make='Toyota',
        model='Yaris',
        year=2020,
        engine=Engine(
            horsepower=1300,
            fuel_type=FuelTypeEnum.PETROL
        )
    )
]

result = client_controller.submit_an_array_of_vehicles(array_of_vehicles)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid input | `APIException` |

