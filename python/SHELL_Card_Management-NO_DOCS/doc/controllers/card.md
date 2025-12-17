# Card

APIs for Retrieve and update shell card details

```python
card_controller = client.card
```

## Class Name

`CardController`

## Methods

* [Searchcard](../../doc/controllers/card.md#searchcard)
* [Cardsummary](../../doc/controllers/card.md#cardsummary)
* [Cardordercard](../../doc/controllers/card.md#cardordercard)
* [Cardordercardenquiry](../../doc/controllers/card.md#cardordercardenquiry)
* [Cardcancel](../../doc/controllers/card.md#cardcancel)
* [Cardupdatestatus](../../doc/controllers/card.md#cardupdatestatus)
* [Purchase Category](../../doc/controllers/card.md#purchase-category)
* [Carddetails](../../doc/controllers/card.md#carddetails)
* [Card Move](../../doc/controllers/card.md#card-move)
* [Cardpinreminder](../../doc/controllers/card.md#cardpinreminder)
* [Schedule Card Block](../../doc/controllers/card.md#schedule-card-block)
* [Autorenew](../../doc/controllers/card.md#autorenew)
* [Updatemobilepaymentregistrationstatus](../../doc/controllers/card.md#updatemobilepaymentregistrationstatus)
* [Getkey](../../doc/controllers/card.md#getkey)
* [Deliveryaddressupdate](../../doc/controllers/card.md#deliveryaddressupdate)


# Searchcard

This API allows to search for Shell Cards in the Shell Card Platform. It provides flexible search criteria and supports paging.

#### New version updates

* Oauth authentication to access the API

* New parameters have been added in the response. Below are the list of parameters added
  
  * IsEMVContact
  
  * IsEMVContactless
  
  * IsRFID
  
  * RFIDUID
  
  * EMAID
  
  * EVPrintedNumber
  
  * CardMediaCode

#### Supported operations

* Search cards by card id or PAN

* Search cards by card status

* Search cards by excluding card status

* Search cards by date fields

* Search cards by embossed fields

* Search cards by card configuration fields

* Search cards by included/excluded list of cards

* Search cards by excluding card bundle Id

```python
def searchcard(self,
              request_id,
              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`SearchCardRequest`](../../doc/models/search-card-request.md) | Body, Optional | requestbody |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CardSearchResponse`](../../doc/models/card-search-response.md).

## Example Usage

```python
request_id = 'RequestId8'

body = SearchCardRequest(
    filters=Filters(
        card_status=[
            'ACTIVE',
            'BLOCKED'
        ],
        account_id=1223,
        account_number='CZ00000923',
        card_group_id=424,
        card_group_name='CARDGRP1',
        card_segment='Fleet',
        card_type_code='7077327',
        col_co_code=32,
        col_co_id=32,
        coverage='National',
        creation_date='20211222',
        driver_name=[
            'JAN KOLLER',
            'DRIVER23',
            'DRIVER25'
        ],
        effective_date='20211222',
        exclude_cancelled_cards=True,
        exclude_card_group_id=425,
        exclude_card_group_name='CARDGRP2',
        exclude_cards=[
            SearchCard(
                card_id=466907,
                pan='7077327290224795811'
            )
        ],
        exclude_fraud_cards=False,
        exclude_pending_renewal_cards=True,
        exclude_replaced_cards=False,
        expiry_month='052022',
        include_cards=[
            SearchCard(
                card_id=466906,
                pan='7077327290224795801'
            )
        ],
        include_intermediate_status=False,
        issued_after='20211123',
        network='ShellSitesOnly',
        pan_ends_with='1284',
        payer_id=1223,
        payer_number='CZ00000923',
        purchase_category_code='3',
        sort_order='1,3,7',
        include_scheduled_card_blocks=False,
        token_type_id=107,
        token_type_name='CZ CRT Int MultiNetwork - CHIP',
        vehicle_registration_number=[
            '5A2 7512',
            '5A2 7514'
        ],
        exclude_old_cards=False,
        exclude_expiring_cards=False,
        reissue_setting='true',
        request_id='233e4567-e89b-12d3-a456-426614174000'
    ),
    page_size='50',
    page='1'
)

result = card_controller.searchcard(
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "Page": 1,
  "TotalRecords": 3420,
  "TotalPages": 3420,
  "PageSize": 50,
  "Data": [
    {
      "AccountId": 1223,
      "AccountName": "NewtestPandB",
      "AccountNumber": "CZ00000923",
      "AccountShortName": "NewtestPandB",
      "BundleId": "null",
      "CardBlockSchedules": [
        {
          "null": null
        }
      ],
      "CardGroupId": 5,
      "CardGroupName": "null",
      "CardId": 385316,
      "CardTypeCode": "7077327",
      "CardTypeId": 105,
      "CardTypeName": "CZ CRT INT MUL R7",
      "ColCoCountryCode": "CZ",
      "CreationDate": "20190911 13:58:30",
      "DriverName": "Jhon",
      "EffectiveDate": "20190911",
      "ExpiryDate": "20230930",
      "FleetIdInput": true,
      "IsCRT": true,
      "IsFleet": false,
      "IsInternational": true,
      "IsNational": false,
      "IsPartnerSitesIncluded": true,
      "IsShellSitesOnly": false,
      "IssueDate": "20190911",
      "IsSuperseded": true,
      "IsVirtualCard": false,
      "LastModifiedDate": "20230720 09:33:28",
      "LastUsedDate": "20230720 09:33:28",
      "LocalCurrencyCode": "CZK",
      "LocalCurrencySymbol": "Kč",
      "OdometerInput": true,
      "PAN": "7077327290223410782",
      "PurchaseCategoryCode": "3",
      "PurchaseCategoryId": 103,
      "PurchaseCategoryName": "3 - No Restriction",
      "Reason": "Lost",
      "ReissueSetting": "False",
      "StatusDescription": "Active",
      "StatusId": 1,
      "TokenTypeID": 107,
      "TokenTypeName": "CZ CRT Int MultiNetwork - CHIP",
      "VRN": "GHJHJDKSDS",
      "ClientReferenceId": "233e4567-e89b-12d3-a456-426614174000",
      "IsEMVContact": false,
      "IsEMVContactless": false,
      "IsRFID": false,
      "RFIDUID": "AFR56T",
      "EMAID": "JUYHF767",
      "EVPrintedNumber": "87394FDE",
      "CardMediaCode": "100999",
      "MediumTypeID": 0,
      "MediumType": null
    }
  ],
  "RequestId": "4cb1d11e-c387-48a5-b667-a1d862be4343",
  "Status": "SUCCESS"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Cardsummary

This API allows to search for fuel cards in the Shell Card Platform and returns a high-level summary count. It provides flexible search criteria.

#### New version updates

* Oauth authentication to access the API
* Minor change in response structure with addition of Status parameter

#### Supported operations

* Search cards by card id or PAN
* Search cards by card status
* Search cards by excluding card status
* Search cards by date fields
* Search cards by embossed fields
* Search cards by card configuration fields
* Search cards by included/excluded list of cards

```python
def cardsummary(self,
               request_id,
               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`CardSummaryRequest`](../../doc/models/card-summary-request.md) | Body, Optional | summary request body |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CardSummaryResponse`](../../doc/models/card-summary-response.md).

## Example Usage

```python
request_id = 'RequestId8'

body = CardSummaryRequest(
    filters=Filters1(
        card_status=[
            'ACTIVE',
            'BLOCKED'
        ],
        request_id='233e4567-e89b-12d3-a456-426614174000',
        account_id=1223,
        account_number='CZ00000923',
        col_co_code=32,
        col_co_id=32,
        payer_id=1223,
        payer_number='CZ00000923',
        card_group_id=424,
        card_group_name='CARDGRP1',
        issued_after='20211123',
        pan_ends_with='1284',
        driver_name=[
            'JAN KOLLER',
            'DRIVER23',
            'DRIVER25'
        ],
        vehicle_registration_number=[
            '5A2 7512',
            '5A2 7514'
        ],
        include_cards=[
            SearchCard(
                card_id=466906,
                pan='7077327290224795801'
            )
        ],
        exclude_cards=[
            SearchCard(
                card_id=466907,
                pan='7077327290224795811'
            )
        ],
        card_segment='Fleet',
        purchase_category_code='3',
        card_type_code='7077327',
        exclude_pending_renewal_cards=True,
        exclude_cancelled_cards=True,
        exclude_replaced_cards=False,
        exclude_fraud_cards=False,
        exclude_card_group_id=425,
        exclude_card_group_name='CARDGRP2',
        creation_date='20211222',
        effective_date='20211222',
        network='ShellSitesOnly',
        coverage='National',
        expiry_month='052022',
        exclude_old_cards=False,
        reissue_setting='true'
    )
)

result = card_controller.cardsummary(
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "233e4567-e89b-12d3-a456-426614174000",
  "Status": "SUCCESS",
  "Data": [
    {
      "ActiveCards": 10,
      "BlockedCards": 5,
      "CancelledCards": 2,
      "ExpiredCards": 5,
      "ExpiringCards": 2,
      "FraudCards": 0,
      "NewCards": 0,
      "RenewalPendingCards": 0,
      "ReplacedCards": 0,
      "TemporaryBlockByCustomer": 0,
      "TemporaryBlockByShell": 0,
      "TotalCards": 24
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | `APIException` |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Cardordercard

This API allows ordering one or more fuel cards (up to 50). If the API call succeeds, the API will return a reference number and queue the request for asynchronous processing.

#### New version updates

* Oauth authentication to access the API
* New parameters have been added in the response for the new PIN management changes. Below parameters needs to be derived from the new PIN encryption method explained in our Mobility Card PIN Management product.
  * SelfSelectedEncryptedPIN
  * SelfSelectedPINKeyID
  * SelfSelectedPINSessionKey
* New parameters have been added in the response for card and pin delivery mechanism which gives the opportunity to deliver card & pin by email, SMS or post.
  Also the possibility to deliver card and pin to different address if the use case demands.
  * CardDeliveryType
  * PINDeliveryAddressType
  * PINAdviceType
  * PINContact
  * CardContact

#### Supported operations

* Order one or more cards (up to 50)
* Order card with self selected PIN
* Order card with vehicle registration number
* Order card and add to new or exisitng card group
* Order card and enable fleetId or odemeter input
* Order card and specify product groups

#### Validation rules

* Number of cards per request does not exceed 50

#### API response

* A main reference number for the API request (**OrderReference**)
* Individual reference numbers (**OrderCardReference**) for each new card

```python
def cardordercard(self,
                 request_id,
                 body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`CardManagementV1OrdercardRequest`](../../doc/models/card-management-v1-ordercard-request.md) | Body, Optional | Order card request body |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrderCardResponse`](../../doc/models/order-card-response.md).

## Example Usage

```python
request_id = 'RequestId8'

body = CardManagementV1OrdercardRequest(
    card_details=[
        CardDetail(
            card_delivery_type=1,
            pin_advice_type=1,
            payer_id=853,
            payer_number='PH50000843',
            account_id=854,
            account_number='PH50000844',
            col_co_code=86,
            col_co_id=1,
            card_type_id=1,
            token_type_id=107,
            emboss_text='PARKLEY',
            vrn='MV65YLH',
            driver_name='Robert',
            odometer_input_required=False,
            fleet_id_input_required=False,
            purchase_category_id=54,
            self_selected_encrypted_pin='0hCx7wfFp3z8QkW8dElhHiMwCwC1',
            self_selected_pin_key_id='123aaa33198dc8f3s4k77dsc78',
            self_selected_pin_session_key='WoWB+8UEd71+8QXwuE75flkAQ /4Q6gDFSn027oJ/0ne6LmzVIxJ87yoeqKS /C+OIBJ7bTvasLH+xvDSZtzoOZHr 7wfFmpfSyet8KnKjnagSicrUgpGk 7qFyOw3iA9/Qd6Oy9djYR3C3cDWEpj /YREZ1lBGReb9fqdSpoKx8mnGuPAw7',
            card_group_id=5,
            card_group_name='Group1',
            is_new_card_group=False,
            emboss_card_group=False,
            card_contact=CardContact(
                delivery_contact_name='Robert',
                delivery_company_name='WILTON AUFDERHAR',
                delivery_address_line_1='Herrn Dieter Whausen Lansstrab',
                delivery_zip_code='12130',
                delivery_city='manila',
                delivery_country='WILTON AUFDERHAR',
                delivery_contact_title='Mr.',
                delivery_address_line_2='10th avenue',
                delivery_address_line_3='makati city',
                delivery_region_id=43,
                delivery_region='Philippines',
                phone_number='99999999999',
                email_address='xxxxx@example.com',
                save_for_card_reissue=False
            ),
            pin_delivery_address_type=1,
            pin_contact=PINContact(
                delivery_contact_title='Mr.',
                delivery_contact_name='Robert',
                delivery_company_name='WILTON AUFDERHAR',
                delivery_address_line_1='Herrn Dieter Whausen Lansstrab',
                delivery_address_line_2='10th avenue',
                delivery_address_line_3='makati city',
                delivery_zip_code='12130',
                delivery_city='manila',
                delivery_region_id=43,
                delivery_region='Philippines',
                delivery_country='WILTON AUFDERHAR',
                phone_number='99999999999',
                email_address='xxxxx@example.com',
                save_for_pin_reminder=False
            ),
            notify_caller=False,
            caller='NextGenUI',
            notify_caller_on_sync=False,
            validate_fleet_id=False,
            fleet_option='ALERT',
            bundle_id='1046',
            usage_restriction_action='None',
            product_restriction_action='None',
            products=[
                '011',
                '033'
            ],
            product_groups=[
                '670246404',
                '40557126'
            ],
            expiry_date='1221',
            client_reference_id='cli123'
        )
    ]
)

result = card_controller.cardordercard(
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "b88525fd-6340-404e-9313-12e702c33cb7",
  "Status": "SUCCESS",
  "Data": [
    {
      "DriverAndVRN": "ROBERT:MV65YLH",
      "OrderCardReference": 488351
    }
  ],
  "MainReference": 488453
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | `APIException` |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | `APIException` |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | `APIException` |


# Cardordercardenquiry

This API retrieves the card order status from the Shell Card Platform based on the given reference numbers.

#### New version updates

    * Oauth authentication to access the API
    
    * Minor change in response structure with addition of Status parameter

#### Supported operations

    * Get order status by Bulk Card Order Reference
    
    * Get order status by Order Reference (main reference for the order)
    
    * Get order status by Card Reference (individual card reference belonging to an order reference)

```python
def cardordercardenquiry(self,
                        request_id,
                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`OrderCardEnquiryRequest`](../../doc/models/order-card-enquiry-request.md) | Body, Optional | Order Card Enquiry request body |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrderCardEnquiryResponse`](../../doc/models/order-card-enquiry-response.md).

## Example Usage

```python
request_id = 'RequestId8'

body = OrderCardEnquiryRequest(
    filters=Filters2(
        account_id=70,
        account_number='NL00000063',
        col_co_code=18,
        col_co_id=18,
        col_co_country_code='NL',
        payer_id=70,
        payer_number='NL00000063',
        reference_number=25,
        reference_type=OrderCardEnquiryReqReferenceTypeEnum.ENUM_1,
        from_date='20210502',
        to_date='20210505',
        order_request_id='34edbfbf-f05e-4d8d-bcd4-9eb7aea5ea41'
    )
)

result = card_controller.cardordercardenquiry(
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "6fb81ffe-bf1b-44b0-94f8-d6711afde392",
  "Status": "SUCCESS",
  "Data": [
    {
      "AccountId": 70,
      "AccountNumber": "NL00000063",
      "BCOReference": 0,
      "BCORowNumber": 0,
      "CardGroupId": 0,
      "CardGroupName": "null",
      "CardId": 41008,
      "CardPAN": "7077187910757000712",
      "CardTypeCode": "7077187",
      "CardTypeId": 704,
      "CardTypeName": "NL CRT Nat. Shell + partnernetwerk",
      "DriverName": "DAVE ROUSE TEST",
      "ErrorCode": "0000",
      "ErrorDescription": "null",
      "GatewaySyncErrorCode": "0000",
      "GatewaySyncErrorDescription": "Success",
      "GatewaySyncStatus": "S",
      "MainReference": 512164,
      "OrderCardReference": 714069,
      "OrderStatus": "S",
      "PayerId": 70,
      "PayerNumber": "NL00000063",
      "ProcessedDate": "20231219 10:12:21",
      "PurchaseCategoryCode": "3",
      "PurchaseCategoryId": 139,
      "PurchaseCategoryName": "3 - No Restriction",
      "SubmittedDate": "20231219 10:11:16",
      "SyncProcessedDate": "20231219 10:15:44",
      "SyncRequestedDate": "null",
      "VRN": "null",
      "OrderRequestId": "ee625150-8d84-496c-b824-a4c47b482ae3",
      "ExpiryDate": "20271231 00:00:00",
      "ClientReferenceId": "9073ab4e-c1f5-4f2d-947f-753ead176c3d",
      "StatusDescription": "Success"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | `APIException` |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | `APIException` |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | `APIException` |


# Cardcancel

This API allows cancelling one or multiple cards (up to 500) within a single API call. This API allows updating of
the card to the following status-

* Block (Cancelled)

#### New version updates

* Oauth authentication to access the API
* Change in the request body
  * PIN delivery address details have been added along with Email and Phone number for card and PIN delivery.

Requests that passed the below validations are queued-

* All Mandatory fields are passed.
* Card is present in the Shell Card Platform.
* Only one matching card is available in the cards platform for the given PAN and expiry date for Block requests.
* Card is allowed to be moved to proposed state as per the card status transition configuration in cards platform.
* A valid Reason Id or Reason Text is provided. The reason for card cancellation can be “Damaged” or “NoLongerRequired”.
* For the given card, there is no Cancel request already submitted via this API and is being processed.
* ‘IsReplacementChargeable’ is set to ‘False’ only to the configured customer, other customers need to set it as ‘True’ only. If other customers pass this value as ‘False’.

Note- Shell Card Platform will maintain the list of   customers, to whom ‘IsReplacementChargeable’ can be set as ‘False’.

If all validations are passed, the request will be accepted and the API will return reference numbers for tracking purpose. If any of the validations fail, the API will return the appropriate error details on response.  The API response will include-

* A main reference number for the API request.
* A list of successfully validated and accepted cards along with the individual reference numbers for each of the successful requests.
* A list of cards for which at least validation has failed along with the appropriate error code and details.

A permanent block (cancelled) request for the card will be queued in Shell Card Platform after the configured damaged card active period (configured as number of days).

When a card is requested to be Blocked permanently (cancelled) for which a request has already been submitted to report as Damaged and the damaged card active period is not yet completed, the damaged card request will be marked as superseded and the new Block (cancelled) request will be processed.

```python
def cardcancel(self,
              request_id,
              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`CardManagementV1CancelRequest`](../../doc/models/card-management-v1-cancel-request.md) | Body, Optional | Update status request body |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CancelCardResponse`](../../doc/models/cancel-card-response.md).

## Example Usage

```python
request_id = 'RequestId8'

body = CardManagementV1CancelRequest(
    cards=[
        UpdateCard(
            caller='NextGenUI',
            is_replacement_chargeable=True,
            notify_caller=False,
            notify_caller_on_sync=False,
            order_card_replacement=True,
            card_settings=CardSettings(
                card_delivery_type=1,
                self_selected_encrypted_pin='0hCx7wfFp3z8QkW8dElhHiMwCwC1',
                self_selected_pin_key_id='123aaa33198dc8f3s4k77dsc78',
                self_selected_pin_session_key='WoWB+8UEd71+8QXwuE75flkAQ /4Q6gDFSn027oJ/0ne6LmzVIxJ87yoeqKS /C+OIBJ7bTvasLH+xvDSZtzoOZHr 7wfFmpfSyet8KnKjnagSicrUgpGk 7qFyOw3iA9/Qd6Oy9djYR3C3cDWEpj /YREZ1lBGReb9fqdSpoKx8mnGuPAw7',
                validate_fleet_id=False,
                card_group_id=156,
                delivery_contact_title='Mr',
                delivery_contact_name='SAPE',
                delivery_company_name='welcome',
                delivery_address_line_1='123/89',
                delivery_address_line_2='Mac Street',
                delivery_address_line_3='NLStrret',
                delivery_zip_code='1213242',
                delivery_city='Chennai',
                delivery_region_id=54,
                delivery_region='Mountain Province',
                delivery_country='CZ',
                phone_number='99999999999',
                email_address='xxxxx@examp"le.com',
                pin_delivery_address_type=1,
                pin_advice_type=1,
                pin_delivery_contact_title='5058F1AF',
                pin_delivery_contact_name='WILTON',
                pin_delivery_company_name='WILTON AUFDERHAR',
                pin_delivery_address_line_1='Herrn Dieter Whausen Lansstrab',
                pin_delivery_address_line_2='Wall street',
                pin_delivery_address_line_3='Wall Street',
                pin_delivery_zip_code='12103',
                pin_delivery_city='Berlin',
                pin_delivery_region_id=1,
                pin_delivery_region='Berlin-Brandenburg',
                pin_delivery_country='DEU',
                pin_phone_number='99999999999',
                pin_email_address='xxxxx@example.com',
                save_for_pin_reminder=False,
                save_for_card_reissue=False,
                expiry_date='1221'
            ),
            account_id=854,
            account_number='PH50000844',
            card_expiry_date='20181031',
            card_id=125,
            col_co_code=86,
            col_co_id=1,
            pan='7002861007636000020',
            payer_id=853,
            payer_number='PH50000843'
        )
    ],
    reason_text='Lost'
)

result = card_controller.cardcancel(
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "ba093ec6-a738-47d3-d25d-2f15a6d04fc6",
  "MainReference": 466536,
  "OrderReplacementReference": 466537,
  "Status": "SUCCESS",
  "Data": [
    {
      "ReplacementCardReference": 599643,
      "UpdateCardReference": 39269,
      "AccountId": 1227,
      "AccountNumber": "CZ00000927",
      "CardExpiryDate": "20240930",
      "CardId": 462079,
      "ColCoCode": 32,
      "ColCoId": 32,
      "PAN": "7002329040232130111",
      "PayerId": 1227,
      "PayerNumber": "CZ00000927"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | `APIException` |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | `APIException` |


# Cardupdatestatus

This API allows updating of the card status for one or more cards (up to 500) within a single API call.  If the API call succeeds, the API will return a reference number and queue the request for asynchronous processing.

#### New version updates

* Oauth authentication to access the API
* Change in the request body
  * Pin change related parameters - SelfSelectedEncryptedPIN, SelfSelectedPINKeyID, SelfSelectedPINSessionKey
  * PIN delivery address details have been added along with Email and Phone number for card and PIN delivery.
  * SaveForPINReminder - The given address will be used for sending PIN reminders in future when requested.
  * SaveForCardReissue - If this is specified, the contact address will be saved in cards platform for card reissue processing.

#### Supported operations

* Updating a card status to Temporary block, Unblock, Block (Cancelled)
  or Damaged
* Requesting a replacement card when status is set to Block or Damaged

#### Validation rules

* Number of cards per request does not exceed 500
* A card can be changed to proposed status as per the card status transition configuration in the Shell Card Platform
* Locating a card -
  * If target status set to **TemporaryBlock**, then only one matching active card should exist in the Shell Card Platform for the given **PAN** and **CardExpiryDate**
  * If target status set to **Unblock** or **Block**, then only one matching card should exist in the Shell Card Platform for the given **PAN** and **CardExpiryDate**
* A valid Reason Id or Reason Text is provided
  * If target status set to **Block** or **Damaged** and a **ReasonText** is provided, the value must be from the fixed list - *'Lost'*, *'Stolen'* or *'Card no longer required'*
* For the given card, there is no Status Update request already submitted via this API and is being processed
* The **OrderReplacementCard** field is set to True only for cards with a target status set to Block or Damaged

#### API response

* A main reference number for the API request (**OrderReplacementReference**)
* A list of successfully validated and accepted cards along with the individual reference numbers (**UpdateCardReference**) for each of the successful  request
* A list of cards (**ErrorCards**) that failed validation along with the appropriate error code and message

#### Asynchronous processing of valid API request

* Replacement cards
  * Request for a replacement card will be placed only when the Block card or Block damaged card request is successfully placed.
  * The Replacement card request will be processed only when the permanent Block card request is successfully processed. In case of damaged card request, the replacement card request will be processed immediately.
* Damaged cards
  * Setting a card to Damaged will automatically trigger a request to permanently block the card. This will only take effect once the ‘Damaged Active’ period has passed.
  * The Damaged card active period is the number of days after which a "Damaged" card request will be processed. This value is configured at ColCo level.
  * If a card is reported as damaged at 10pm local time on 1st Nov and the damaged card period is set to 10 days, then the block request will be submitted to the Shell Card Platform on 11th Nov 00-01 local time.
  * If during the damage card active period another request is made to set the card to Temporarily Blocked or Blocked permanently (cancelled), then the damaged card request will be marked as superseded and the new Temporary Block or Block (cancelled) will be processed.

```python
def cardupdatestatus(self,
                    request_id,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`CardManagementV1UpdatestatusRequest`](../../doc/models/card-management-v1-updatestatus-request.md) | Body, Optional | Update status request body |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UpdateCardStatusResponse`](../../doc/models/update-card-status-response.md).

## Example Usage

```python
request_id = 'RequestId8'

body = CardManagementV1UpdatestatusRequest(
    cards=[
        UpdateCard(
            caller='Motix',
            is_replacement_chargeable=True,
            notify_caller=True,
            notify_caller_on_sync=False,
            order_card_replacement=True,
            card_settings=CardSettings(
                card_delivery_type=1,
                self_selected_encrypted_pin='0hCx7wfFp3z8QkW8dElhHiMwCwC1',
                self_selected_pin_key_id='123aaa33198dc8f3s4k77dsc78',
                self_selected_pin_session_key='WoWB+8UEd71+8QXwuE75flkAQ /4Q6gDFSn027oJ/0ne6LmzVIxJ87yoeqKS /C+OIBJ7bTvasLH+xvDSZtzoOZHr 7wfFmpfSyet8KnKjnagSicrUgpGk 7qFyOw3iA9/Qd6Oy9djYR3C3cDWEpj /YREZ1lBGReb9fqdSpoKx8mnGuPAw7',
                validate_fleet_id=False,
                card_group_id=156,
                delivery_contact_title='Mr',
                delivery_contact_name='SAPE',
                delivery_company_name='welcome',
                delivery_address_line_1='123/89',
                delivery_address_line_2='Mac Street',
                delivery_address_line_3='NLStrret',
                delivery_zip_code='1213242',
                delivery_city='Chennai',
                delivery_region_id=54,
                delivery_region='Mountain Province',
                delivery_country='CZ',
                phone_number='99999999999',
                email_address='xxxxx@example.com',
                pin_delivery_address_type=1,
                pin_advice_type=1,
                pin_delivery_contact_title='50388633F',
                pin_delivery_contact_name='WILTON',
                pin_delivery_company_name='WILTON AUFDERHAR',
                pin_delivery_address_line_1='Herrn Dieter Whausen Lansstrab',
                pin_delivery_address_line_2='Wall street',
                pin_delivery_address_line_3='Wall Street',
                pin_delivery_zip_code='12103',
                pin_delivery_city='Berlin',
                pin_delivery_region_id=1,
                pin_delivery_region='Berlin-Brandenburg',
                pin_delivery_country='DEU',
                pin_phone_number='99999999999',
                pin_email_address='xxxxx@example.com',
                save_for_pin_reminder=False,
                save_for_card_reissue=False,
                expiry_date='1221'
            ),
            account_id=1223,
            account_number='CZ00000928',
            card_expiry_date='20221215',
            card_id=385360,
            col_co_code=32,
            col_co_id=32,
            pan='7077327290223410816',
            payer_id=1223,
            payer_number='CZ00000928'
        )
    ],
    target_status='Unblock',
    reason_id=1236,
    reason_text='Unblock'
)

result = card_controller.cardupdatestatus(
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "233e4567-e89b-12d3-a456-426614174000",
  "MainReference": 466543,
  "OrderReplacementReference": 466544,
  "Status": "SUCCESS",
  "Data": [
    {
      "ReplacementCardReference": 599649,
      "UpdateCardReference": 39270,
      "AccountId": 1227,
      "AccountNumber": "CZ00000927",
      "CardExpiryDate": "20240930",
      "CardId": 462083,
      "ColCoCode": 32,
      "ColCoId": 32,
      "PAN": "7077327290223421201",
      "PayerId": 1227,
      "PayerNumber": "CZ00000927"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | `APIException` |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | `APIException` |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | `APIException` |


# Purchase Category

This API will allow querying the purchase categories of Card
for the given country and/or card type.
It will also include the below data associated with each of the purchase categories on it’s response.

* List of fuel and non-fuel product sets associated.
* List of products configured in each product set

```python
def purchase_category(self,
                     apikey,
                     request_id,
                     body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `apikey` | `str` | Header, Required | This is the API key of the specific environment which needs to be passed by the client. |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`PurchaseCategoryRequest`](../../doc/models/purchase-category-request.md) | Body, Optional | PurchaseCategory request body |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PurchaseCategoryResponse`](../../doc/models/purchase-category-response.md).

## Example Usage

```python
apikey = 'apikey6'

request_id = 'RequestId8'

body = PurchaseCategoryRequest(
    col_co_id=32,
    language_code='EN-GB'
)

result = card_controller.purchase_category(
    apikey,
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "PurchaseCategories": [
    {
      "Code": "0",
      "Id": 100,
      "IsVisible": false,
      "Name": "0 - Diesel Products and TMF",
      "Title": "0 - Diesel Products and TMF",
      "Description": "0 - Diesel Products and TMF",
      "ProductGroups": [
        {
          "IsDefault": false,
          "IsFuelType": true,
          "Name": "Other Fuels",
          "ProductGroupId": "P102",
          "Products": [
            {
              "Description": "Hydrogen",
              "GlobalProductCode": "019"
            },
            {
              "Description": "CNG",
              "GlobalProductCode": "029"
            },
            {
              "Description": "LPG",
              "GlobalProductCode": "034"
            }
          ],
          "ReferenceId": 100
        }
      ]
    }
  ],
  "Error": {
    "Code": "0000",
    "Description": "Success"
  },
  "RequestId": "47aca5b8-8186-49e5-b8d0-30f73fffd0f1"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request  due to something that is perceived to be a client<br>error (e.g., malformed request syntax, invalid<br>request message framing, or deceptive request routing). | `APIException` |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | `APIException` |
| 403 | The server understood the request but refuses to authorize it. | `APIException` |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | `APIException` |
| 500 | The server encountered an unexpected condition the prevented it from fulfilling the request. | `APIException` |


# Carddetails

This API allows to fetch details of a single fuel card from the Shell Card Platform. If a **CardId** request parameter is provided, this will return a single card.  If a **PAN** request parameter is provided, this may result in multiple fuel cards matching the search criteria. The card details of the most recently issued card will be returned.

#### Supported operations

* Get card by card id or PAN

```python
def carddetails(self,
               apikey,
               request_id,
               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `apikey` | `str` | Header, Required | This is the API key of the specific environment which needs to be passed by the client. |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`CardDetailsRequest`](../../doc/models/card-details-request.md) | Body, Optional | Card details request body |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CardDetailsResponse`](../../doc/models/card-details-response.md).

## Example Usage

```python
apikey = 'apikey6'

request_id = 'RequestId8'

body = CardDetailsRequest(
    col_co_code=86,
    col_co_id=1,
    col_co_country_code='PH',
    client_reference_id='adc-1671-ftwiQweh-67UJs',
    payer_number='PH50000843',
    payer_id=853,
    account_number='PH50000844',
    account_id=854,
    pan='7002861007636000020',
    card_id=125,
    token_type_id=107,
    token_type_name='PH FLE NAT SIN R1',
    creation_date='20181001',
    effective_date='20181001',
    include_bundle_details=False,
    include_intermediate_status=False,
    include_scheduled_card_blocks=False
)

result = card_controller.carddetails(
    apikey,
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "PayerId": 853,
  "PayerNumber": "PH50000843",
  "AccountId": 854,
  "AccountNumber": "PH50000844",
  "AccountShortName": "PARKLEY",
  "ColCoCountryCode": "PH",
  "LocalCurrencyCode": "EUR",
  "LocalCurrencySymbol": "€",
  "CardId": 125,
  "PAN": "7002861007636000020",
  "StatusId": 1,
  "Status": "string",
  "OdometerPrompt": true,
  "FleetIdPrompt": true,
  "PINType": "Card",
  "HasPIN": true,
  "IsSelfSelectedPIN": true,
  "TemporaryBlockAllowed": true,
  "UnblockAllowed": true,
  "PermanentBlockAllowed": true,
  "IssueNumber": 1,
  "ReissueSetting": "True",
  "InternationalPOSLanguageID": 8,
  "InternationalPOSLanguageCode": "eng",
  "LocalPOSLanguageID": 8,
  "LocalPOSLanguageCode": "eng",
  "CardTypeCode": "7077861",
  "CardTypeId": 1,
  "CardTypeName": "Philippines CRT 7077861",
  "TokenTypeId": 107,
  "TokenTypeName": "PH FLE NAT SIN R1",
  "IsChipCard": false,
  "IsMagStripCard": true,
  "IsVirtualCard": true,
  "PurchaseCategoryCode": "6",
  "PurchaseCategoryId": 54,
  "PurchaseCategoryName": "2 - FuelSave and Lubricants",
  "IsCRT": true,
  "IsFleet": true,
  "IsInternational": true,
  "IsNational": true,
  "IsPartnerSitesIncluded": true,
  "IsShellSitesOnly": true,
  "FuelSets": [
    {
      "ProductRestrictionId": 120,
      "Description": "FS02: Diesel"
    }
  ],
  "NonFuelSets": [
    {
      "ProductRestrictionId": 120,
      "Description": "FS02: Diesel"
    }
  ],
  "IssuedDate": "20181001",
  "ExpiryDate": "20181031",
  "LastUsedDate": "20181001 13:23:55",
  "MisuseDate": "20181001 13:23:55",
  "Temperature": "10-Warm",
  "DriverName": "ROBERT",
  "VRN": "MV65YLH",
  "EmbossText": "PARKLEY",
  "CardGroupId": 5,
  "CardGroupName": "GROUP1",
  "RenewalDate": "20181001",
  "RenewedCardId": 1325,
  "RenewedCardStatusId": 10,
  "RenewedCardStatus": "New",
  "RenewedCardExpiryDate": "20181031",
  "RenewedCardIssueNumber": 2,
  "RenewedCardReissueSetting": "True",
  "CreationDate": "20181001",
  "EffectiveDate": "20181001",
  "LastModifiedDate": "20181001 13:23:55",
  "BundleId": null,
  "CardDeliveryAddress": {
    "ContactForeName": "ROBERT",
    "ContactMiddleName": "M",
    "ContactLastName": "Langdon",
    "ContactTitle": "Mr.",
    "CompanyName": "PARKLEY Philippines",
    "AddressId": 1768,
    "AddressLine1": "No 345, 1st cross,",
    "AddressLine2": "10th avenue",
    "AddressLine3": "makati city",
    "ZipCode": "1630",
    "City": "manila",
    "RegionId": null,
    "Region": "EU",
    "CountryId": 1,
    "CountryISOCode": "PH",
    "Country": "Philippines"
  },
  "PINDeliveryAddress": {
    "ContactForeName": "ROBERT",
    "ContactMiddleName": "M",
    "ContactLastName": "Langdon",
    "ContactTitle": "Mr.",
    "CompanyName": "PARKLEY Philippines",
    "AddressId": 1768,
    "AddressLine1": "No 345, 1st cross,",
    "AddressLine2": "10th avenue",
    "AddressLine3": "makati city",
    "ZipCode": "1630",
    "City": "manila",
    "RegionId": null,
    "Region": "EU",
    "CountryId": 1,
    "CountryISOCode": "PH",
    "Country": "Philippines"
  },
  "CardBlockSchedules": [
    {
      "FromDate": "20210212",
      "ToDate": "20210212"
    }
  ],
  "Error": {
    "Code": "0000",
    "Description": "Success"
  },
  "RequestId": "ed557f02-c7d7-4c01-b3e5-11bf3239c8ed"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request  due to something that is perceived to be a client<br>error (e.g., malformed request syntax, invalid<br>request message framing, or deceptive request routing). | `APIException` |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | `APIException` |
| 403 | The server understood the request but refuses to authorize it. | `APIException` |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | `APIException` |
| 500 | The server encountered an unexpected condition the prevented it from fulfilling the request. | `APIException` |


# Card Move

This API allows to move one or more fuel cards (up to 500) across card groups within a single account or across accounts under the same payer. If the API call succeeds, the API will return a reference number and queue the request for asynchronous processing.

#### Supported operations

* Moving card to exisitng card group
* Moving card to new card group
* Removing a card from a card group

#### Validation rules

* Number of cards per request does not exceed 500
* Given **PAN** for a card matches with only one card
* A card is allowed to be moved to the **TargetCardGroupId** or **TargetAccountNumber**
* A pending move request does not exist in the queue for a card submitted on the same date (customers local)
* A card has not been moved as part of a previous request on the same date (customers local)

#### API response

* A main reference number for the API request (**MoveCardRequestReference**)
* Individual reference numbers (**MoveCardReference**) for each card move request that passes validation
* A list of cards (**ErrorCards**) that failed validation along with the appropriate error code and message

#### Asynchronous processing of valid API request

* Move card requests that have been submitted and processed will be reflected after midnight according to the customers local date

```python
def card_move(self,
             apikey,
             request_id,
             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `apikey` | `str` | Header, Required | This is the API key of the specific environment which needs to be passed by the client. |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`CardMoveRequest`](../../doc/models/card-move-request.md) | Body, Optional | Move cards request body. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CardMoveResponse`](../../doc/models/card-move-response.md).

## Example Usage

```python
apikey = 'apikey6'

request_id = 'RequestId8'

body = CardMoveRequest(
    col_co_code=86,
    col_co_id=1,
    col_co_country_code='PH',
    payer_number='PH50000843',
    payer_id=853,
    cards=[
        CardMoveRequestCardsItems(
            account_number='PH50000844',
            account_id=854,
            pan='7002861007636000020',
            card_id=125
        )
    ],
    target_account_id=855,
    target_account_number='GB000000123',
    target_card_group_id=93,
    target_new_card_group_name='GROUP1'
)

result = card_controller.card_move(
    apikey,
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "MoveCardRequestReference": 0,
  "SuccessfulRequests": [
    {
      "AccountNumber": "PH50000844",
      "AccountId": 854,
      "PAN": "7002861007636000020",
      "CardId": 125,
      "MoveCardReference": 9074
    }
  ],
  "ErrorCards": [
    {
      "AccountNumber": "PH50000844",
      "AccountId": 854,
      "PAN": "7002861007636000020",
      "CardId": 125,
      "ValidationErrorCode": "0000",
      "ValidationErrorDescription": "Invalid parameter value – [ParameterName]"
    }
  ],
  "RequestId": "ed557f02-c7d7-4c01-b3e5-11bf3239c8ed",
  "Error": {
    "Description": "Success",
    "Code": "0000"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request  due to something that is perceived to be a client<br>error (e.g., malformed request syntax, invalid<br>request message framing, or deceptive request routing). | `APIException` |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | `APIException` |
| 403 | The server understood the request but refuses to authorize it. | `APIException` |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | `APIException` |
| 500 | The server encountered an unexpected condition the prevented it from fulfilling the request. | `APIException` |


# Cardpinreminder

This API allows requesting a PIN reminder for a fuel card. If the API call succeeds, the API will return a reference number and queue the request for asynchronous processing.

#### New version updates

* Oauth authentication to access the API
* Change in request body where PIN delivery type can be requested via Email, SMS or Post. PIN delivery contact can be set to different values based on previous contact details of card or pin delivery or can set specific contact details for this request.
  * PINAdviceType
  * PINContactType
  * PINDeliverTo
* Please note that we have a **savePINReminder** parameter in order to save the contact details for future such requests.
* Change in response body where Card details are also provided along with expiry date and PAN details.

#### Supported operations

* Request a pin reminder by card Id or PAN

#### Validation rules

* Given **PAN** or **CardId** is active
* Given **PAN** matches only one active card
* Requested card has PIN
* There is no pending PIN Reminder request in the queue awaiting to be processed for the card
* A PIN reminder request has not been successfully processed in the last 48 hours for the card

```python
def cardpinreminder(self,
                   request_id,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`CardManagementV1PinreminderRequest`](../../doc/models/card-management-v1-pinreminder-request.md) | Body, Optional | PIN reminder request body |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PINReminderResponse`](../../doc/models/pin-reminder-response.md).

## Example Usage

```python
request_id = 'RequestId8'

body = CardManagementV1PinreminderRequest(
    account_number='CZ00000927',
    col_co_code=32,
    payer_number='CZ00000927',
    pin_reminder_card_details=[
        PINReminderCardDetails(
            pin_advice_type=1,
            card_id=463402,
            pan='7027329200000115820',
            card_expiry_date='20241031',
            pin_contact_type=4,
            pin_deliver_to=PINDeliverTo(
                company_name='CGI',
                address_line='Address1',
                zip_code='938373',
                city='City1',
                contact_name='Alex',
                contact_title='Mr',
                region_id=0,
                country_id=0,
                phone_number='9998883332',
                email_address='abc.gmail.com',
                save_pin_reminder=False
            )
        )
    ]
)

result = card_controller.cardpinreminder(
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "ba093ec6-a738-47d3-d25d-2f15a6d04fc6",
  "MainReference": 466588,
  "Status": "SUCCESS",
  "Data": [
    {
      "CardId": 463402,
      "PANID": null,
      "PAN": null,
      "CardExpiryDate": null,
      "ReferenceId": 2360
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Schedule Card Block

This API allows scheduling Card Block / Unblock requests for one or multiple cards (up to 500 (configurable)) within a single API call. This API is used to perform the following Actions:



* AddOrUpdate (Schedule a new request or update an existing     scheduled request for the overlapping period.
* AddAndOverwriteAll (all the existing requests of the given card will be removed and a new request with the specified FromDate and ToDate will be added.)
* Delete (Deletes the scheduled request for the same From and To date)
* DeleteAll (Deletes all the scheduled requests for the given card)

> Requests that passed the below validations are queue:

* All Mandatory fields are passed in the request.
* Card is present in the Shell Card Platform. Only one matching card is available in the cards platform for the given PAN and expiry date for the requests
* The scheduled period start date or end date should be later than or equal to the current date.

> If all validations are passed, the request will be accepted and saved in the intermediate queue  and the API will return reference numbers for tracking purpose.

> A background service will execute the block/unblock requests on a daily basis, based on the scheduled block or unblock date.

* The newly added block/unblock request will have a status ‘A’ when it is yet to be moved to the actual queue.

* When the request is moved to the actual queue table, the status will be updated as ‘P’ if the request has a value for ‘ToDate’, else, the status will be updated as ‘S’ or ‘F’ based on whether the request has been successfully moved to the actual queue table or if an error is encountered during processing.

* When the unblock request is moved to the actual queue table, the status of the request will be changed from ‘P’ to ‘S’ or ‘F’ based on whether the request has been successfully moved to the actual queue table or if an error has occurred during processing.

> If any of the validations fail, the API will return the appropriate error details in the response.
> The API response will include:

* An error entity holding the details of any error encountered.
* A list of submitted cards along with the individual reference numbers for each of the request.

```python
def schedule_card_block(self,
                       request_id,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`ScheduleCardBlockRequest`](../../doc/models/schedule-card-block-request.md) | Body, Optional | request body |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ScheduleCardBlockResponse`](../../doc/models/schedule-card-block-response.md).

## Example Usage

```python
request_id = 'RequestId8'

body = ScheduleCardBlockRequest(
    is_time_supported=True,
    schedule_card_block_cards=[
        ScheduleCardBlockCardsItems(
            action='AddOrUpdate',
            col_co_code=32,
            col_co_id=32,
            account_id=928,
            account_number='CZ00000928',
            payer_id=928,
            payer_number='CZ00000928',
            card_id=234,
            pan='7077327290223418348',
            card_expiry_date='20240731',
            from_date='20230701 14:30',
            to_date='20230731 16:30',
            caller='NextGenUI',
            notify_caller=True
        )
    ]
)

result = card_controller.schedule_card_block(
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "MainReference": 4124828,
  "RequestId": "b471023f-b1e1-45df-8fe8-126291bd0c30",
  "Status": "SUCCESS",
  "Data": [
    {
      "CardId": 458951,
      "FromDate": "20230613 00:00",
      "ToDate": "20230614 00:00",
      "ReferenceId": 342
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | `APIException` |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | `APIException` |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | `APIException` |


# Autorenew

This API allows to update the reissue indicator of a single card. If the API call succeeds, the API will return a reference number for tracking purposes and queue the request for asynchronous processing.

#### Supported operations

* Update the reissue indicator of a card to enable auto renewal
* Update the reissue indicator of a card to disable auto renewal

#### Validation rules

* Card status must be either Active, Temporary Block (Customer), Temporary Block (Shell) or Pending Renewal, otherwise an error code 9016 is returned

#### API response

* Returns a reference number for the API request (**AutoRenewReference**)

#### Asynchronous processing of valid API request

* If the provided card is superseded i.e. a replacement/new card is already issued, then the latest card's reissue indicator should be updated in the Shell Card Platform.
* Providing a **PAN** request paramter may result in multiple fuel cards being located in the Shell Card Platform. The card details of the most recently issued card will be considered.

```python
def autorenew(self,
             request_id,
             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`AutoRenewCardRequest`](../../doc/models/auto-renew-card-request.md) | Body, Optional | Auto renew request body |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AutoRenewCardResponse`](../../doc/models/auto-renew-card-response.md).

## Example Usage

```python
request_id = 'RequestId8'

body = AutoRenewCardRequest(
    col_co_id=32,
    col_co_code=32,
    payer_number='CZ00000928',
    payer_id=1227,
    auto_renew_cards=[
        AutoRenewCardRequestAutoRenewCardsItems(
            reissue_setting=True,
            account_number='CZ00000929',
            account_id=1229,
            pan='7077327290223440243',
            card_id=446472
        )
    ]
)

result = card_controller.autorenew(
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "MainReference": 326712,
  "RequestId": "0e6fb42a-51b0-43b2-f010-92f822657f6a",
  "Status": "SUCCESS",
  "Data": [
    {
      "AutoRenewReferenceId": 226,
      "CardIdAndPAN": "446472;7077327290223440243"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | `APIException` |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | `APIException` |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | `APIException` |


# Updatemobilepaymentregistrationstatus

This operation allows  update the approval status of Mobile Payment Registration requests requiring for Fleet Manager approval.
If the approval status is:

* “Approved” then the request status will be changed to Pending for processing.
* “Rejected” then status will be updated to “CI” (Failed) with appropriate error message.

```python
def updatemobilepaymentregistrationstatus(self,
                                         request_id,
                                         body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`UpdateMPayRegStatusRequest`](../../doc/models/update-m-pay-reg-status-request.md) | Body, Optional | Request body |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UpdateMPayRegStatusResponse`](../../doc/models/update-m-pay-reg-status-response.md).

## Example Usage

```python
request_id = 'RequestId8'

body = UpdateMPayRegStatusRequest(
    col_co_id=32,
    col_co_code=32,
    payer_id=1223,
    payer_number='CZ00000923',
    m_pay_requests=[
        UpdateMPayRegStatusRequestMPayRequestsItems(
            global_request_id='123',
            status='Rejected',
            approver_user_id='AdminUser100',
            approver_user_display_name='AdminUser100',
            reason='approved'
        )
    ]
)

result = card_controller.updatemobilepaymentregistrationstatus(
    request_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "b471023f-b1e1-45df-8fe8-126291bd0c30",
  "Status": "SUCCESS"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | `APIException` |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | `APIException` |


# Getkey

Get a new public key that will be used to encrypt data for selected PIN process when ordering new Shell Card. This encrypted data is used for further processing.

```python
def getkey(self,
          request_id,
          fleet=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `fleet` | `bool` | Query, Optional | If the public key will be used a long time for multiple files this parameter will be true. If the parameter is true then public Key will be valid for 90 days. If the parameter is false then the key will be valid for one time. default value will be false. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GeneratePINKeyResponse`](../../doc/models/generate-pin-key-response.md).

## Example Usage

```python
request_id = 'RequestId8'

result = card_controller.getkey(request_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "uid": "123aaa33198dc8f3s4k77dsc78",
  "value": "LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQ0lqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FnOEFNSUlDQ2dLQ0FnRUFvZ0dSQ3k4N1FjQ3d6MFI0NE9LTwpucEhhZ0p1bW83Wll1V21JdXY2b1ZseUxqYkcwWlgyUFBSUy9LVUdhbXdiWGQwMGtYeHBXbFA5cXJ2N2hYMlNSCkJ2TFJVWFR0TCtvWS9QajN0c2Z6d0liT3VDei9qUnQ5Uk9WdzNBTkZTNjF6blVFTkVsSlNXN2dudnJuL29USWwKRWlid2VVTE5aTlJObFRwQTI1QVhKanhXMzM3ZUx0Y2F5cXJiQlNJNVFmRitCTGJJbE1Rd2tqSkNhUFEzV0pUKwpxcnlCREFCME5ocm02VlBmK2toN2FyR2JqL3ZLS0NRWVBkQWhRKzI3OGp0ZGJZdFBzYWtjN0RqVXpTenl2Wm9HCmhiSEt4V0ZTODFnL2ZlQUZNbFFDVlErZk15ZVN5dFZKOGlmZjFZR2RydEJCdG16U0NRN2V0K1IwaHpUbzJXblcKZzREZG1oWmlZT0MvUU55dk5uY1VSeDRZMU84VW1nSmorNE56c3VyQ2dQMmRSUjNpVXRIYlZaZjRzTEpZWk5CWApORGxjUDNzYWlwTXJ6Z0RpM0VCbWZzdEJOODdvWVdsRzRQNmlPVGt3dzdDVyt0TUdRNmJPcVBBNFF0cWMrYUZMCktZR3FWREhWRnBhZWdwYXl0U2g3T25nd0cwckJod0M4ODNpeVFaZDNKRW1lSWt2V05wYTVRSExqRmJKTEg4M2YKdk9TR2E0aGR6ZmZqYUhUM2VvR2VCRU5NaTZIbFo4RVZHWUh0VUpXZGMzZ2h5OHdPbmZkTlN2NzV3SUZYbHNragpIdHM3Z3NkM3hDN1B3ZnBqOEV5Lyt2aTVLNHM5M29IaE5TYlRhNlUzNUVsZkFXL20zK1YxWjZqVUpwRWpmZkZYCnI0YlFiR3pQNVhWYkNKL21ndmVNM3lNQ0F3RUFBUT09Ci0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQo="
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request  due to something that is perceived to be a client<br>error (e.g., malformed request syntax, invalid<br>request message framing, or deceptive request routing). | `APIException` |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | `APIException` |
| 403 | The server understood the request but refuses to authorize it. | `APIException` |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | `APIException` |
| 500 | The server encountered an unexpected condition the prevented it from fulfilling the request. | `APIException` |


# Deliveryaddressupdate

This API allows users to update the card’s delivery addresses (card delivery address used for card re-issue and PIN delivery address used when PIN reminder is requested)

#### Supported operations

* card delivery address update

```python
def deliveryaddressupdate(self,
                         apikey,
                         body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `apikey` | `str` | Header, Required | This is the API key of the specific environment which needs to be passed by the client. |
| `body` | [`DeliveryAddressUpdateRequest`](../../doc/models/delivery-address-update-request.md) | Body, Optional | Delivery Address Update Request Body |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DeliveryAddressUpdateResponse`](../../doc/models/delivery-address-update-response.md).

## Example Usage

```python
apikey = 'apikey6'

body = DeliveryAddressUpdateRequest(
    col_co_id=5,
    col_co_code=5,
    payer_id=123456,
    payer_number='GB000000123',
    account_id=12356,
    account_number='GB000000124',
    delivery_address_updates=[
        DeliveryAddressUpdate(
            use_customer_default_address=True,
            card_id=123,
            pan='7002051006629889654',
            card_expiry_date='20170930',
            update_card_renewal_address=UpdateCardRenewalAddress2(
                contact_name='Jack',
                company_name='Travel Transport',
                address_line='Elm Street 11',
                zip_code='1023EA',
                country_id=8,
                contact_title='Mr',
                city='London',
                region_id=2,
                email_address='testmail@gmail.com',
                phone_number='+99999999999'
            )
        )
    ]
)

result = card_controller.deliveryaddressupdate(
    apikey,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "eb621f45-a543-4d9a-a934-2f223b263c42",
  "ServiceReference": 123456,
  "DeliveryAddressUpdateReferences": {
    "CardId": 12345,
    "CardPAN": "7002051006629889654",
    "AccountId": 12356,
    "AccountNumber": "GB000000124",
    "ReferenceId": 573567,
    "ErrorInfo": "null"
  },
  "Error": {
    "Code": "0000",
    "Description": "Success"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request  due to something that is perceived to be a client<br>error (e.g., malformed request syntax, invalid<br>request message framing, or deceptive request routing). | `APIException` |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | `APIException` |
| 403 | The server understood the request but refuses to authorize it. | `APIException` |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | `APIException` |
| 500 | The server encountered an unexpected condition the prevented it from fulfilling the request. | `APIException` |

