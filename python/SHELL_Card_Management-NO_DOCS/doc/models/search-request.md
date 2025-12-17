
# Search Request

Encapsulate the Search details request.

## Structure

`SearchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `int` | Optional | Account ID of the customer.<br/> Optional.<br/> This input is a search criterion, if given. |
| `account_number` | `str` | Optional | Account Number of the customer.<br/> Optional.<br/> This input is a search criterion, if given. |
| `card_group_id` | `int` | Optional | Card group id. <br /><br>Optional.<br /><br>This input is a search criterion, if given.<br /><br>When -1 is passed, those cards that does not belong to any card group will be returned. |
| `card_group_name` | `str` | Optional | Card group name.<br /><br>Optional.<br /><br>This input is a search criterion, if given.<br /><br>If CardGroupId is provided then this search criterion will be ignored, else, those cards that have the card group name completely matching with the entered value will be returned. |
| `card_segment` | `str` | Optional | Market segment to which card belongs to.<br /><br>Optional.<br /><br>Allowed values<br /><br>• CRT<br /><br>• Fleet |
| `card_status` | `List[str]` | Required | Status of the card.<br /><br>Mandatory.<br /><br>Multiple statuses are allowed to be included in the search criteria.<br /><br>CardStatus filter accepts either of the two values for each status as described below. However, the output field “StatusDescription” is aligned with second value highlighted in italics.<br /><br>Below are the possible allowed statuses: <br /><br>• ACTIVE or Active – Cards at status Active if the IncludeIntermediateStatus flag is true: Active (Block in progress), Active (Cancel in progress), Active (Marked as damaged)), New (Cancel in progress).<br /><br>• ON_ORDER or New – Cards at status New<br /><br>• EXPIRED or Expired – Cards at status Expired<br /><br>• BLOCKED or Blocked Card – Cards at status Block (The result will include all cards having the following intermediate status, if the IncludeIntermediateStatus flag is true: Blocked card (Unblock in progress))<br /><br>• TEMP_BLOCKED_CUSTOMER or Temporary Block(Customer) – Cards at status Temporary Blocked By Customer<br /><br>• TEMP_BLOCKED_SHELL or Temporary Block (Shell) – Cards at Status Temporary Blocked by Shell<br /><br>• CANCELLED or Cancelled – Cards at status Cancelled<br /><br>• PENDING_RENEWAL or Pending Renewal - Cards that are in renewal process<br /><br>• REPLACED or Replaced – Cards at Status Replaced<br /><br>• FRAUD or Fraud – Cards at Status FRAUD<br /><br>• ALL |
| `card_type_code` | `str` | Optional | ISO code of the card i.e. first 7 digits of the PAN<br /><br>Optional. |
| `col_co_code` | `int` | Optional | Collecting Company Code (Shell Code) of the selected payer. <br /><br>Optional If ColCo Id or ColCoCountryCode is passed else Mandatory<br /> |
| `col_co_country_code` | `str` | Optional | The 2 character ISO Code for the customer and card owning country.<br /><br>Optional If ColCoId or ColCoCode is passed else Mandatory.<br /> |
| `col_co_id` | `int` | Optional | Collecting Company Id  of the selected payer. <br /><br>Optional If ColCoCode or ColCoCountryCode is passed else Mandatory <br /> |
| `coverage` | `str` | Optional | Cards allowed to used nationally/internationally.<br /><br>Optional.<br /><br>Allowed values<br /><br>-National<br /><br>-International |
| `creation_date` | `str` | Optional | Card Creation Date<br /><br>Optional<br /><br>Format: yyyyMMdd |
| `driver_name` | `List[str]` | Optional | Driver Name embossed on the card<br /><br>Optional<br /><br>Up to 10 driver names could be passed in the parameter.<br /><br>Minimum of 4 characters should be provided for each driver name else not considered.<br /><br>Those cards will be returned when part of the driver name matches with any of the string passed in the list.<br /><br>Max Length for each Driver name: 50 |
| `effective_date` | `str` | Optional | Effective date for the Card<br /><br>Optional<br /><br>Format: yyyyMMdd<br /> |
| `exclude_bundle_id` | `str` | Optional | Bundle Id for the Card, which needs to be excluded in the response.<br /><br>Optional |
| `exclude_cancelled_cards` | `bool` | Optional | Default value is True.<br /><br>When true, the API will not return cards that are at Cancelled Status in Cards Platform<br /> |
| `exclude_card_group_id` | `int` | Optional | Optional<br /><br>When passed, the API will not return cards that are currently in the Card Group specified<br /> |
| `exclude_card_group_name` | `str` | Optional | Optional<br /><br>When passed, the API will not return cards that are currently in the Card Group specified<br /> |
| `exclude_cards` | [`List[SearchCard]`](../../doc/models/search-card.md) | Optional | List of SearchCard entity i.e., Card Id or PAN, which needs to be excluded in the response. <br /><br>Details of the SerachCard entity are given below.<br /> |
| `exclude_fraud_cards` | `bool` | Optional | Default value is False.<br /><br>When true, the API will not return cards that are at Fraud Status in Cards Platform<br /> |
| `exclude_pending_renewal_cards` | `bool` | Optional | Default value is True.<br /><br>When true, the API will not return cards that are at Pending Renewal Status in Cards Platform |
| `exclude_replaced_cards` | `bool` | Optional | Default value is False.<br /><br>When true, the API will not return cards that are at Replaced Status in Cards Platform<br /> |
| `expiring_in_days` | `int` | Optional | Cards active and expiring in given number of days.<br /><br>Optional<br /><br>Note: When a value is passed in this parameter, only active cards will be considered while searching.<br /> |
| `expiry_month` | `str` | Optional | Month in which the card is expiring.<br /><br>Optional.<br /><br>Format: MMYYYY<br /> |
| `include_bundle_details` | `bool` | Optional | Default value is False,<br /><br>When the value is True, API will return bundle Id associated with card in response.<br /> |
| `include_cards` | [`List[SearchCard]`](../../doc/models/search-card.md) | Optional | List of SearchCard entity i.e., Card Id or PAN, which needs to be included in the response.<br /><br>Details of the SerachCard entity are given below.<br /> |
| `include_intermediate_status` | `bool` | Optional | A flag which indicates if the response can contain intermediate statuses.<br /><br>Optional<br /><br>Default: false |
| `issued_after` | `str` | Optional | If provided, only list cards issued after the given date<br /><br>Optional<br /><br>Format: yyyyMMdd<br /><br>Note: Clients to convert this to appropriate DateTime type. |
| `network` | `str` | Optional | Cards allowed to be used in site.<br /><br>Optional.<br /><br>Allowed values<br /><br>-ShellSitesOnly<br /><br>-PartnersSitesIncluded |
| `pan_ends_with` | `str` | Optional | Last digits of the PAN number<br /><br>Minimum 4 last digits of the card should be sent for this field to be considered as part of the search criteria.<br /><br>Optional<br /><br>Max Length: 50 |
| `payer_id` | `int` | Optional | Payer Id (i.e. Customer Id of the Payment Customer) of the selected payer.<br /><br>Optional if PayerNumber is passed else Mandatory<br /><br>Example: 123456 |
| `payer_number` | `str` | Optional | Payer Number of the selected payer.<br /><br>Optional if PayerId is passed else Mandatory<br /> |
| `purchase_category_code` | `str` | Optional | Purchase category code of the card.<br /><br>Optional. |
| `sort_order` | `str` | Optional | Possible options are:<br /><br>1.ExpiringDateAscending<br /><br>2.ExpiringDateDescending<br /><br>3.DriverNameAscending(If Driver Name is null then VRN value will be considered)<br /><br>4.DriverNameDescending(If Driver Name is null then VRN value will be considered)<br /><br>5.VRNAscending(If VRN is null then Driver Name value will be considered)<br /><br>6.VRNDescending(If VRN  is null then Driver Name value will be considered)<br /><br>7.LastUsedDateAscending<br /><br>8.LastUsedDateDescending<br /><br>9.IssueDateAscending<br /><br>10.IssueDateDescending<br /><br>11.PurchaseCategoryCodeAscending<br /><br>12.PurchaseCategoryCodeDescending<br /><br>13.CardSegmentAscending (CRT will appear first)<br /><br>14.CardSegmentDescending (Fleet will appear first)<br /><br>Optional |
| `include_scheduled_card_blocks` | `bool` | Optional | A flag which indicates if the response can contain scheduled card blocks details<br /><br>Optional<br /><br>Default: false |
| `token_type_id` | `int` | Optional | Token Type ID for the Card<br /><br>Optional |
| `token_type_name` | `str` | Optional | Token Type name for the Card<br /><br>Optional |
| `vehicle_registration_number` | `List[str]` | Optional | Vehicle Registration embossed on the card<br /><br>Optional<br /><br>Up to 10 vehicle registration numbers could be passed in the parameter.<br /><br>Minimum of 4 characters should be provided for each VRN else not considered<br /><br>Those cards will be returned when part of the VRN matches with any of the string passed in the list.<br /><br>Max Length for each VRN: 50 |
| `exclude_old_cards` | `bool` | Optional | Default Value: False<br /><br>When this field is set to True, cards with below status 2 years (configurable) ago and earlier are excluded from the result<br /><br>-Blocked Card<br /><br>-Expired<br /><br>-Cancelled<br /><br>-Suspended<br /><br>-Blocked<br /><br>-Expired and Cancelled<br /><br>-Replaced<br /><br>-Replaced By<br /><br>-Closed<br /><br>-Fraud<br /> |
| `exclude_expiring_cards` | `bool` | Optional | Default value is False.<br /><br>When true, the API will not return cards that are expiring <br /><br>within 120 (i.e. Configured) days, if the status of the card is 1 or 41 or 42 in Cards platform. |
| `client_reference_id` | `str` | Optional | Customer reference number of the card. |
| `reissue_setting` | `str` | Optional | Default Value: All<br /><br>Optional<br /><br>This option is used to filter the list of cards with ‘ReissueSetting’.<br /><br>If ‘True’, the API will return cards with ReIssueSetting value is true.<br /><br>If ‘False’, the API will return cards with ReIsssueSetting value is false.<br /><br>If ‘ALL’, API will return cards with ReIssueSetting value True &amp; False both.<br /><br>Allowed Values:<br /><br><br>1. All<br /><br>2. True<br /><br>3. False |
| `request_id` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "AccountId": 120,
  "AccountNumber": "AccountNumber6",
  "CardGroupId": 166,
  "CardGroupName": "CardGroupName0",
  "CardSegment": "CardSegment0",
  "CardStatus": [
    "CardStatus7",
    "CardStatus8"
  ]
}
```

