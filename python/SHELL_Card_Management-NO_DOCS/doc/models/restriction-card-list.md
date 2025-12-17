
# Restriction Card List

## Structure

`RestrictionCardList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_id` | `int` | Optional | Unique Card Id |
| `pan` | `str` | Optional | Card PAN |
| `expiry_date` | `str` | Optional | Expiry date of the card<br>Format: yyyyMMdd<br>Note: Clients to convert this to appropriate DateTime type. |
| `status_id` | `int` | Optional | Card Status id |
| `status_description` | `str` | Optional | Status Description (Active, Temporarily Blocked, etc.,) |
| `driver_name` | `str` | Optional | Driver name<br>Example:  ANDREW GILBERRY |
| `vrn` | `str` | Optional | Vehicle registration number<br>Example: MV65YLH |
| `issue_date` | `str` | Optional | Issue date<br>Format: yyyyMMdd<br>Note: Clients to convert this to appropriate DateTime type. |
| `issue_number` | `int` | Optional | Issue Number |
| `account_id` | `int` | Optional | Account ID<br>Example: 29484 |
| `account_number` | `str` | Optional | Account Number<br>Example: GB99215176 |
| `account_name` | `str` | Optional | Account Name<br>Example: MATTHEW ALGIE & COMPANY LIMITED |
| `account_short_name` | `str` | Optional | Account Short Name |
| `currency_code` | `str` | Optional | ISO currency code of the Customer Currency<br>Example: GBP |
| `col_co_currency_code` | `str` | Optional | ISO currency code of the country.<br>Example: GBP |
| `col_co_currency_symbol` | `str` | Optional | Currency symbol of the country.<br>Example: £, $ |
| `restriction_currency_code` | `str` | Optional | ISO currency code of the country.<br>Example: GBP |
| `restriction_currency_symbol` | `str` | Optional | Currency symbol of the country.<br>Example: £, $ |
| `purchase_category_id` | `str` | Optional | Purchase category Id<br>Example: 123, 124, etc., |
| `purchase_category_code` | `str` | Optional | Purchase category code<br>Example:<br>0 - All Fuels (without VP) and Lubricants<br>1 - FuelSave only<br>2 - FuelSave and Lubricants<br>3 - No Restrictions<br>4 - VP and FuelSave<br>5 - Diesel ONLY<br>6 - Diesel and Lubricants<br>7 - VP and Lubricants<br>8 - VP and FuelSave and Lubricants |
| `purchase_category_name` | `str` | Optional | Purchase category name<br>Example:<br>0 - All Fuels (without VP) and Lubricants<br>1 - FuelSave only<br>2 - FuelSave and Lubricants<br>3 - No Restrictions<br>4 - VP and FuelSave<br>5 - Diesel ONLY<br>6 - Diesel and Lubricants<br>7 - VP and Lubricants<br>8 - VP and FuelSave and Lubricants |
| `is_superseded` | `bool` | Optional | True/False<br>True if a new card is issued with the same PAN, else false |
| `is_virtual_card` | `bool` | Optional | True/False<br>True if it is a virtual card, else false |
| `is_national` | `bool` | Optional | True/False<br>True if it is a national card, else false |
| `is_international` | `bool` | Optional | True/False<br>True if it is an international card, else false |
| `is_crt` | `bool` | Optional | True/False<br>True if it is a CRT type card, else false |
| `is_fleet` | `bool` | Optional | True/False<br>True if it is a Fleet type card, else false |
| `is_shell_sites_only` | `bool` | Optional | True/False<br>True if it is only allowed at Shell sites, else false |
| `is_partner_sites_included` | `bool` | Optional | True/False<br>True if it is allowed at all partner sites, else false |
| `card_type_id` | `int` | Optional | Card Type ID<br>Example Id & Description:<br>1 - Philippines CRT 7077861<br>2- Philippines Fleet 7002861<br>5-SHELL FLEET- HONG KONG 7002821<br>6-SHELL NHF- HONG KONG 7002821<br>7-SHELL CRT- HONG KONG 7077821 |
| `card_type_code` | `str` | Optional | ISO code of the card i.e. first 7 digits of the PAN |
| `card_type_name` | `str` | Optional | Card Type Name<br>Example Id & Description:<br>1 - Philippines CRT 7077861<br>2- Philippines Fleet 7002861<br>5-SHELL FLEET- HONG KONG 7002821<br>6-SHELL NHF- HONG KONG 7002821<br>7-SHELL CRT- HONG KONG 7077821 |
| `bundle_id` | `str` | Optional | Bundle Id associated with card in the Gateway.<br>This field will have a null value if the card is not associated with any bundle of IncludeBundleDetails in request is false.<br>If the search is based on a bundle Id, the same will be returned. |
| `medium_type_id` | `int` | Optional | Id of the medium type identifier.<br>Example: 1,2,4<br>Full list below:<br>1 - Fuel Card<br>2 - Fuel Card with EV<br>4 - Fuel Card and Key fob Card<br>5 - Key fob<br>6 - Virtual Card<br>7 - NPII Token<br>8 – Smartpay |
| `medium_type` | `str` | Optional | Name of the medium type identifier.<br><br>Example: Fuel Card, Fuel Card with EV, Key fob  <br>Full list below:<br>1 - Fuel Card<br>2 - Fuel Card with EV<br>4 - Fuel Card and Key fob Card<br>5 - Key fob<br>6 - Virtual Card<br>7 - NPII Token<br>8 - Smartpay |

## Example (as JSON)

```json
{
  "CardId": 110,
  "PAN": "PAN8",
  "ExpiryDate": "ExpiryDate8",
  "StatusId": 178,
  "StatusDescription": "StatusDescription4"
}
```

