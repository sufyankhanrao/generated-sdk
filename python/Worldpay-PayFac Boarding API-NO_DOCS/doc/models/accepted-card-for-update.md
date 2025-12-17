
# Accepted Card for Update

## Structure

`AcceptedCardForUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attributes` | [`List[Attribute]`](../../doc/models/attribute.md) | Optional | Only the attributes corresponding to the type selected, needs to be included.<br><br>1) For Visa, MasterCard no attributes are allowed. If any attributes are passed, they will be ignored.<br><br>2) The following are the attributes for Discover and American Express<br>   <br>   a) Discover<br>   Attribute 1 (mandatory)<br>   name - Acquired<br>   value - Yes or No<br>   Attribute 2 (Include if and only if Acquired = No)<br>   name - AccountNumber<br>   value - the account number associated with the card<br>   <br>   b) AmericanExpress<br>   <br>   Attribute 1 (mandatory)<br>   name - AmexProgram<br>   values - ESA or OptBlue<br>   Attribute 2 (Include if and only if AmexProgram = ESA)<br>   name - AccountNumber<br>   value - the account number associated with the card<br>   Attribute 3 (Optionally included if AmexProgram = OptBlue. Defaults to Yes.)<br>   name - ReceiveOptBlueMarketing<br>   value - Yes or No<br><br>3) For Debit following  attribute is allowed<br>   a) Name - PINless<br>   Values - Yes or No<br><br>4) For JCB (Japan Credit Bureau) the following attribute is allowed.<br>   a) Name - JCBCardNumber<br>   Value - JCB Credit Card Number<br><br>5) For EBT (Electronic Benefit transfer) the following attributes are allowed.<br>   a) Name - EBTType<br>   Values - FOOD & CASH, FOOD STAMPS, CASH BENEFITS<br>   b) Name - FNSNumberCardPresent<br>   Values - FNS Number<br>   example: '1234567'<br>   c) Name - FNSNumberCardNotPresent<br>   Values - FNS Number<br>   example: '1234567'<br>   <br>        Note: For EBTType - 'CASH BENEFITS' the FNSNumberCardPresent and FNSNumberCardNotPresent are 0000000<br><br>6) For WIC (Special Supplemental Nutrition Program for Women, Infants, and Children) the following attributes are allowed.<br>   a) Name - WICProgram<br>   Values - Name of a WIC eligible state in the United States of America<br>   example: 'KENTUCKY'<br>   b) Name - WICId<br>   Values - WIC Number<br><br>7) For Fleet, no attributes are allowed. If any attributes are passed, they will be ignored. |

## Example (as JSON)

```json
{
  "attributes": [
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

