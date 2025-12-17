# Pick a Spot

```python
pick_a_spot_controller = client.pick_a_spot
```

## Class Name

`PickASpotController`

## Methods

* [Get Class List](../../doc/controllers/pick-a-spot.md#get-class-list)
* [Get Class](../../doc/controllers/pick-a-spot.md#get-class)
* [Get Reservation](../../doc/controllers/pick-a-spot.md#get-reservation)
* [Update Reservation](../../doc/controllers/pick-a-spot.md#update-reservation)
* [Create Reservation](../../doc/controllers/pick-a-spot.md#create-reservation)
* [Delete Reservation](../../doc/controllers/pick-a-spot.md#delete-reservation)


# Get Class List

This endpoint supports pagination. See Pagination object for a description.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_class_list(self,
                  version,
                  site_id,
                  authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetPickASpotClassResponse`](../../doc/models/get-pick-a-spot-class-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

result = pick_a_spot_controller.get_class_list(
    version,
    site_id,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Class

Get a class filtered by classId.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_class(self,
             version,
             class_id,
             site_id,
             authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `class_id` | `str` | Template, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetPickASpotClassResponse`](../../doc/models/get-pick-a-spot-class-response.md).

## Example Usage

```python
version = '6'

class_id = 'classId0'

site_id = '-99'

authorization = 'authorization6'

result = pick_a_spot_controller.get_class(
    version,
    class_id,
    site_id,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Reservation

Retrieves reservation for Pick a Spot.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_reservation(self,
                   version,
                   path_info,
                   site_id,
                   authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `path_info` | `str` | Template, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetReservationResponse`](../../doc/models/get-reservation-response.md).

## Example Usage

```python
version = '6'

path_info = 'pathInfo8'

site_id = '-99'

authorization = 'authorization6'

result = pick_a_spot_controller.get_reservation(
    version,
    path_info,
    site_id,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Reservation

A user token is required for this endpoint.
This endpoint updates a single reservation.

:information_source: **Note** This endpoint does not require authentication.

```python
def update_reservation(self,
                      version,
                      path_info,
                      site_id,
                      authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `path_info` | `str` | Template, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UpdateReservationResponse`](../../doc/models/update-reservation-response.md).

## Example Usage

```python
version = '6'

path_info = 'pathInfo8'

site_id = '-99'

authorization = 'authorization6'

result = pick_a_spot_controller.update_reservation(
    version,
    path_info,
    site_id,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Reservation

Creates a spot reservation for a given pick-a-spot class. The actual class visit must be created prior to calling this endpoint.
A user token is required for this endpoint.

Sample request:

    POST /pickaspot/v1/reservation
    {
        "SiteId": -1147483363,
        "LocationId": 1,
        "ClassId": "64b14ac8c20ae8f0afd2d409",
        "ReservationExternalId": "44724", // this is a Visit.Id and should be linked to a specific class visit
        "MemberExternalId": "100000136", // this is Client's UniqueId
        "SpotNumber": "5",
        "ReservationDisplayName": "ReservationDisplayName", // optional
        "ReservationType": "Member" // optional. Can be Member, Guest, Instructor, FamilyMember
    }

:information_source: **Note** This endpoint does not require authentication.

```python
def create_reservation(self,
                      version,
                      path_info,
                      site_id,
                      authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `path_info` | `str` | Template, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CreateReservationResponse`](../../doc/models/create-reservation-response.md).

## Example Usage

```python
version = '6'

path_info = 'pathInfo8'

site_id = '-99'

authorization = 'authorization6'

result = pick_a_spot_controller.create_reservation(
    version,
    path_info,
    site_id,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Reservation

A user token is required for this endpoint.
This endpoint deletes a single reservation.

:information_source: **Note** This endpoint does not require authentication.

```python
def delete_reservation(self,
                      version,
                      path_info,
                      site_id,
                      authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `path_info` | `str` | Template, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`HttpContent`](../../doc/models/http-content.md).

## Example Usage

```python
version = '6'

path_info = 'pathInfo8'

site_id = '-99'

authorization = 'authorization6'

result = pick_a_spot_controller.delete_reservation(
    version,
    path_info,
    site_id,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

