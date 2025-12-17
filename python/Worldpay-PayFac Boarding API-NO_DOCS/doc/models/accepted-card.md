
# Accepted Card

## Structure

`AcceptedCard`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attributes` | [`List[Attribute]`](../../doc/models/attribute.md) | Optional | Only the attributes corresponding to the type selected, needs to be included.<br><br>1) For Visa, MasterCard, no attributes are allowed. If any attributes are passed, they will be ignored.<br><br>2) For Discover, following 2 attributes are allowed.Discover Account Number is only required when Discover Acquired is 'No'<br>   a) Name - Acquired<br>   Values- Yes or No<br>   b) Name- AccountNumber<br>   Values- Discover Account Number<br><br>3) For AmericanExpress, following 3 attributes are allowed. ESA is the direct processing program<br>   a) Name- AmexProgram<br>   Values- OptBlue,ESA<br>   b) Name- ReceiveOptBlueMarketing<br>   Values- Yes or No<br>   c) Name- AccountNumber<br>   Values- Amex Account Number<br><br>4) For Debit following  attribute is allowed<br>   a) Name - PINless<br>   Values - Yes or No<br>   Default value is 'No'<br><br>5) For JCB (Japan Credit Bureau) the following attribute is allowed.<br>   a) Name - JCBCardNumber<br>   Value - JCB Credit Card Number<br><br>6) For EBT (Electronic Benefit transfer) the following attributes are allowed.<br>   a) Name - EBTType<br>   Values - FOOD & CASH, FOOD STAMPS, CASH BENEFITS<br>   b) Name - FNSNumberCardPresent<br>   Values - FNS Number<br>   example: '1234567'<br>   c) Name - FNSNumberCardNotPresent<br>   Values - FNS Number<br>   example: '1234567'<br>   <br>       Note: For EBTType - 'CASH BENEFITS' the FNSNumberCardPresent and FNSNumberCardNotPresent are 0000000<br><br>7) For WIC (Special Supplemental Nutrition Program for Women, Infants, and Children) the following attributes are allowed.<br>   a) Name - WICProgram<br>   Values - WIC KENTUCKY, WIC MICHIGAN, WIC NEVADA, WIC VIRGINIA, WIC WEST VIRGINIA, WIC FLORIDA, WIC OREGON, WIC INTRTRBL, COUNCIL NV, WIC CHICKASAW NATION, WIC OKLAHOMA, WIC MASSACHUSETTS, WIC WISCONSIN, WIC VERMONT, WIC IOWA, WIC MAINE, WIC CONNECTICUT, WIC INDIANA, WIC DELAWARE, WIC COLORADO, WIC MONTANA, WIC SOUTH DAKOTA, WIC MARYLAND, WIC ARIZONA, WIC NAVAJO NATION, WIC N MARIANA ISLAND, WIC GUAM, WIC CHOCTAW NATION OF OK, WIC POTOWOTAMI NATION OK, WIC VIRGIN ISLANDS, WIC WCD ENTERPRISES, WIC AMERICAN SAMOA, WIC KANSAS, WIC OTOE MISSOURIA TRIBE, WIC MUSCOGEE CREEK NATION, WIC INTER-TRIBAL CNCL OK, WIC INTER-COUNCIL ARIZON, WIC OSAGE NATION, WIC NORTH CAROLINA, WIC TENNESSEE XEROX, WIC ALASKA, WIC WASHINGTON, WIC NEBRASKA, WIC IDAHO, WIC NEW YORK, WIC MINNESOTA, WIC NEW HAMPSHIR, WIC ALABAMA, WIC SOUTH CAROLINA, WIC CALIFORNIA, WIC HAWAII, WIC MISSISSIPPI, WIC ILLINOIS, WIC RHODE ISLAND, WIC CHOCTAW MISSISSIPPI, MAINE WIC, NORTH DAKOTA WIC, WIC - TEN TRIBES, WIC NEW JERSEY, WIC PUERTO RICO, WIC D OF COLUMBIA, WIC GEORGIA<br>   example: 'KENTUCKY'<br>   b) Name - WICId<br>   Values - WIC Number<br><br>8) For Fleet, no attributes are allowed. If any attributes are passed, they will be ignored. |
| `mtype` | [`Type3Enum`](../../doc/models/type-3-enum.md) | Required | Method of Payment or Accepted Card Type |

## Example (as JSON)

```json
{
  "type": "AmericanExpress",
  "attributes": [
    {
      "name": "name4",
      "value": "value6"
    },
    {
      "name": "name4",
      "value": "value6"
    },
    {
      "name": "name4",
      "value": "value6"
    }
  ]
}
```

