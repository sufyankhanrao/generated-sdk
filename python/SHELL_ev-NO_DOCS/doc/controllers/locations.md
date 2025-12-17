# Locations

APIs for Shell Recharge Locations

```python
locations_controller = client.locations
```

## Class Name

`LocationsController`

## Methods

* [Get EV Locations](../../doc/controllers/locations.md#get-ev-locations)
* [Ev Locations by ID](../../doc/controllers/locations.md#ev-locations-by-id)
* [Nearby Locations](../../doc/controllers/locations.md#nearby-locations)
* [Locations Markers](../../doc/controllers/locations.md#locations-markers)


# Get EV Locations

This API provides the list of all Shell Recharge locations. The list includes all Shell Recharge network and all locations available through our roaming partners. The end point provides flexible search criteria in order to get the list of Shell Recharge Network. The end point provides the details such as the exact location/address of the site along with the up-to-date status information of all the charging units in the site.

Supported Search Options

* Based on status of the Charging units. Eg : Available or Occupied
* Based on available connector types.
* Based on minimum Power output (in kW) available
* Based on a specific charging unit ID (EVSE ID)

```python
def get_ev_locations(self,
                    request_id,
                    evse_status=None,
                    connector_types=None,
                    connector_min_power=None,
                    authorization_methods=None,
                    with_operator_name=None,
                    evse_id=None,
                    location_external_id=None,
                    evse_external_id=None,
                    page_number=None,
                    per_page=None,
                    updated_since=None,
                    country=None,
                    exclude_country=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `uuid\|str` | Header, Required | RequestId must be unique identifier value that can be used by the consumer to correlate each request /response .<br>Format.<br> Its canonical textual representation, the 16 octets of a UUID are represented as 32 hexadecimal (base-16) digits, displayed in five groups separated by hyphens, in the form 8-4-4-4-12 for a total of 36 characters (32 hexadecimal characters and 4 hyphens) <br> |
| `evse_status` | [`GetEVLocationsEvseStatusEnum`](../../doc/models/get-ev-locations-evse-status-enum.md) | Query, Optional | Filter by Locations that have the given status |
| `connector_types` | [`GetEVLocationsConnectorTypesEnum`](../../doc/models/get-ev-locations-connector-types-enum.md) | Query, Optional | Filter by Locations that have Connectors with the set of Connector Types |
| `connector_min_power` | `float` | Query, Optional | Filter by Locations that have a Connector with at least this power output (in kW) |
| `authorization_methods` | [`GetEVLocationsAuthorizationMethodsEnum`](../../doc/models/get-ev-locations-authorization-methods-enum.md) | Query, Optional | Filter by Locations that support the given Authorization Methods |
| `with_operator_name` | `bool` | Query, Optional | Return operator name in marker response object |
| `evse_id` | `str` | Query, Optional | optional Standard EVSE (Electric Vehicle Supply Equipment) Id identifier (ISO-IEC-15118) |
| `location_external_id` | `str` | Query, Optional | Filter by Locations with the given externalId. (Unique Location externalID provided by Shell Recharge) |
| `evse_external_id` | `str` | Query, Optional | Filter by Locations that have an Evse with the given External Id. (Unique individual EVSE externalID provided by Shell Recharge) |
| `page_number` | `int` | Query, Optional | Restrict the response list by providing a specific set of page Number. Set perPage parameter also when page Number is used.<br><br>**Constraints**: `>= 1` |
| `per_page` | `int` | Query, Optional | Restrict the number of sites in response per page.<br><br>**Constraints**: `<= 500` |
| `updated_since` | `str` | Query, Optional | ZonedDateTime as string |
| `country` | `List[str]` | Query, Optional | Filter by Locations that are at least in one of the given countries (specified using ISO 3166-1 alpha-3 codes) |
| `exclude_country` | `List[str]` | Query, Optional | Filter by Locations that are not in one of the given countries (specified using ISO 3166-1 alpha-3 codes) |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Response`](../../doc/models/response.md).

## Example Usage

```python
request_id = '123e4567-e89b-12d3-a456-426614174000'

evse_id = 'NL*TNM*E01000401*0'

country = [
    'NED'
]

exclude_country = [
    'NED'
]

result = locations_controller.get_ev_locations(
    request_id,
    evse_id=evse_id,
    country=country,
    exclude_country=exclude_country
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`BadRequestException`](../../doc/models/bad-request-exception.md) |
| 401 | The request has not been applied because it lacks valid authentication credentials for the target resource. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 404 | Location Not Found | [`NotFoundException`](../../doc/models/not-found-exception.md) |
| 429 | The Request reached maximum allocated rate limit | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal Server error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |
| 503 | Service unavailable | [`ServiceunavailableException`](../../doc/models/serviceunavailable-exception.md) |


# Ev Locations by ID

This API provides the details on a single Shell Recharge location.
The query for a single location is to be made using the Unique Internal identifier used to refer to this Location by Shell Recharge. (Uid from List of locations API)

```python
def ev_locations_by_id(self,
                      request_id,
                      id,
                      provider_id=None,
                      since=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `uuid\|str` | Header, Required | RequestId must be unique identifier value that can be used by the consumer to correlate each request /response .<br>Format.<br> Its canonical textual representation, the 16 octets of a UUID are represented as 32 hexadecimal (base-16) digits, displayed in five groups separated by hyphens, in the form 8-4-4-4-12 for a total of 36 characters (32 hexadecimal characters and 4 hyphens) <br> |
| `id` | `str` | Template, Required | Unique Uid of the location from List of locations API |
| `provider_id` | `str` | Query, Optional | The provider id that you wish to see locations and tariffs for |
| `since` | `str` | Query, Optional | to get the locations modified after a date |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Response`](../../doc/models/response.md).

## Example Usage

```python
request_id = '123e4567-e89b-12d3-a456-426614174000'

id = 'id0'

result = locations_controller.ev_locations_by_id(
    request_id,
    id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`BadRequestException`](../../doc/models/bad-request-exception.md) |
| 401 | The request has not been applied because it lacks valid authentication credentials for the target resource. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 404 | Location Not Found | [`NotFoundException`](../../doc/models/not-found-exception.md) |
| 429 | The Request reached maximum allocated rate limit | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal Server error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |
| 503 | Service unavailable | [`ServiceunavailableException`](../../doc/models/serviceunavailable-exception.md) |


# Nearby Locations

This API provides the list of all nearby Shell Recharge locations based on the latitude and longitude provided in the request.
The list includes all Shell Recharge network and all sites available through our roaming partners.
The end point provides the details such as the exact location/address of the site along with the up-to-date status information of all the charging units in the site.

Supported Search Options

* Based on latitude and longitude of the location. (Mandatory)
* Based on status of the Charging units. Eg : Available or Occupied
* Based on available connector types.
* Based on minimum Power output (in kW) available

```python
def nearby_locations(self,
                    request_id,
                    latitude,
                    longitude,
                    limit=25,
                    location_external_id=None,
                    evse_id=None,
                    evse_external_id=None,
                    operator_name=None,
                    evse_status=None,
                    connector_types=None,
                    connector_min_power=None,
                    authorization_methods=None,
                    with_operator_name=None,
                    with_max_power=None,
                    country=None,
                    exclude_country=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `uuid\|str` | Header, Required | RequestId must be unique identifier value that can be used by the consumer to correlate each request /response .<br>Format.<br> Its canonical textual representation, the 16 octets of a UUID are represented as 32 hexadecimal (base-16) digits, displayed in five groups separated by hyphens, in the form 8-4-4-4-12 for a total of 36 characters (32 hexadecimal characters and 4 hyphens) <br> |
| `latitude` | `float` | Query, Required | Latitude to get Shell Recharge Locations nearby<br><br>**Constraints**: `>= -90`, `<= 90` |
| `longitude` | `float` | Query, Required | Longitude to get Shell Recharge Locations nearby<br><br>**Constraints**: `>= -180`, `<= 180` |
| `limit` | `float` | Query, Optional | Maximum number of Locations to retrieve<br><br>**Default**: `25`<br><br>**Constraints**: `<= 100` |
| `location_external_id` | `str` | Query, Optional | Filter by Locations with the given externalId Identifier as given by the Shell Recharge Operator, unique for that Operator |
| `evse_id` | `str` | Query, Optional | Filter by Locations that have an Evse with the given Evse Id |
| `evse_external_id` | `str` | Query, Optional | Filter by Locations that have an Evse with the given External Id Identifier of the Evse as given by the Operator, unique for that Operator |
| `operator_name` | `str` | Query, Optional | Filter by Locations that have the given operator |
| `evse_status` | [`NearbyLocationsEvseStatusEnum`](../../doc/models/nearby-locations-evse-status-enum.md) | Query, Optional | Filter by Locations that have the given status |
| `connector_types` | [`NearbyLocationsConnectorTypesEnum`](../../doc/models/nearby-locations-connector-types-enum.md) | Query, Optional | Filter by Locations that have Connectors with these Connector Types |
| `connector_min_power` | `float` | Query, Optional | Filter by Locations that have a Connector with at least this power output (in kW) |
| `authorization_methods` | [`NearbyLocationsAuthorizationMethodsEnum`](../../doc/models/nearby-locations-authorization-methods-enum.md) | Query, Optional | Filter by Locations that support the given Authorization Methods |
| `with_operator_name` | `bool` | Query, Optional | Return operator name in marker object (only for marker type Single ChargePoint) |
| `with_max_power` | `bool` | Query, Optional | Return maximum power in kW across all locations grouped in this marker (disregarding availability) |
| `country` | `List[str]` | Query, Optional | Filter by Locations that are at least in one of the given countries (specified using ISO 3166-1 alpha-3 codes) |
| `exclude_country` | `List[str]` | Query, Optional | Filter by Locations that are not in one of the given countries (specified using ISO 3166-1 alpha-3 codes) |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Response`](../../doc/models/response.md).

## Example Usage

```python
request_id = '123e4567-e89b-12d3-a456-426614174000'

latitude = 65.76

longitude = 180

limit = 25

country = [
    'NED'
]

exclude_country = [
    'NED'
]

result = locations_controller.nearby_locations(
    request_id,
    latitude,
    longitude,
    limit=limit,
    country=country,
    exclude_country=exclude_country
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`BadRequestException`](../../doc/models/bad-request-exception.md) |
| 401 | The request has not been applied because it lacks valid authentication credentials for the target resource. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 404 | Location Not Found | [`NotFoundException`](../../doc/models/not-found-exception.md) |
| 429 | The Request reached maximum allocated rate limit | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal Server error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |
| 503 | Service unavailable | [`ServiceunavailableException`](../../doc/models/serviceunavailable-exception.md) |


# Locations Markers

This API, when given a set of bounds on the geographical front (East,West, North, South) will return a set of Markers that fall within the requested bounds. The API will automatically group locations at the same position on the map into one Marker.

The API also provide further search options to filter the result set.

* Based on status of the Charging units. Eg : Available or Occupied
* Based on available connector types.
* Based on minimum Power output (in kW) available

```python
def locations_markers(self,
                     request_id,
                     west,
                     south,
                     east,
                     north,
                     zoom,
                     evse_status=None,
                     connector_types=None,
                     connector_min_power=None,
                     authorization_methods=None,
                     with_operator_name=None,
                     with_max_power=None,
                     location_external_id=None,
                     evse_id=None,
                     evse_external_id=None,
                     operator_name=None,
                     country=None,
                     exclude_country=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `uuid\|str` | Header, Required | RequestId must be unique identifier value that can be used by the consumer to correlate each request /response .<br>Format.<br> Its canonical textual representation, the 16 octets of a UUID are represented as 32 hexadecimal (base-16) digits, displayed in five groups separated by hyphens, in the form 8-4-4-4-12 for a total of 36 characters (32 hexadecimal characters and 4 hyphens) <br> |
| `west` | `float` | Query, Required | Longitude of the western bound to get the Shell Recharge Locations<br><br>**Constraints**: `>= -180`, `<= 180` |
| `south` | `float` | Query, Required | Latitude of the southern bound to get the Shell Recharge Locations<br><br>**Constraints**: `>= -90`, `<= 90` |
| `east` | `float` | Query, Required | Longitude of the eastern bound to get the Shell Recharge Locations<br><br>**Constraints**: `>= -180`, `<= 180` |
| `north` | `float` | Query, Required | Latitude of the northern bound to get the Shell Recharge Locations<br><br>**Constraints**: `>= -90`, `<= 90` |
| `zoom` | `str` | Query, Required | Zoom level to show ex: (1: World, 5: Landmass/continent, 10: City, 15: Streets, 20: Buildings) |
| `evse_status` | [`LocationsMarkersEvseStatusEnum`](../../doc/models/locations-markers-evse-status-enum.md) | Query, Optional | Filter by Locations that have the given status |
| `connector_types` | [`LocationsMarkersConnectorTypesEnum`](../../doc/models/locations-markers-connector-types-enum.md) | Query, Optional | Filter by Locations that have Connectors with the set of Connector Types |
| `connector_min_power` | `float` | Query, Optional | Filter by Locations that have a Connector with at least this power output (in kW) |
| `authorization_methods` | [`LocationsMarkersAuthorizationMethodsEnum`](../../doc/models/locations-markers-authorization-methods-enum.md) | Query, Optional | Filter by Locations that support the given Authorization Methods |
| `with_operator_name` | `bool` | Query, Optional | Return operator name in marker object (only for marker type SingleChargePoint) |
| `with_max_power` | `bool` | Query, Optional | Return maximum power in kW across all locations grouped in this marker (disregarding availability) |
| `location_external_id` | `str` | Query, Optional | Filter by Locations with the given externalId. (Unique Location externalID provided by Shell Recharge) |
| `evse_id` | `str` | Query, Optional | Filter by Locations that have an Evse with the given Evse Id |
| `evse_external_id` | `str` | Query, Optional | Filter by Locations that have an Evse with the given External Id Identifier of the Evse as given by the Operator, unique for that Operator |
| `operator_name` | `str` | Query, Optional | Filter by Locations that have the given operator |
| `country` | `List[str]` | Query, Optional | Filter by Locations that are at least in one of the given countries (specified using ISO 3166-1 alpha-3 codes) |
| `exclude_country` | `List[str]` | Query, Optional | Filter by Locations that are not in one of the given countries (specified using ISO 3166-1 alpha-3 codes) |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SingleLocationMarkerResponse`](../../doc/models/single-location-marker-response.md).

## Example Usage

```python
request_id = '123e4567-e89b-12d3-a456-426614174000'

west = 152.84

south = 13.76

east = 16.36

north = 73.98

zoom = 'zoom0'

country = [
    'NED'
]

exclude_country = [
    'NED'
]

result = locations_controller.locations_markers(
    request_id,
    west,
    south,
    east,
    north,
    zoom,
    country=country,
    exclude_country=exclude_country
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`BadRequestException`](../../doc/models/bad-request-exception.md) |
| 401 | The request has not been applied because it lacks valid authentication credentials for the target resource. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 404 | Location Not Found | [`NotFoundException`](../../doc/models/not-found-exception.md) |
| 429 | The Request reached maximum allocated rate limit | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal server error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |
| 503 | Service unavailable | [`ServiceunavailableException`](../../doc/models/serviceunavailable-exception.md) |

