
# Checkout Payment Info

## Structure

`CheckoutPaymentInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | The type of payment. Possible values are:<br><br>* CreditCard - Indicates that this payment item is a credit card.<br>* StoredCard - Indicates that this payment item is a credit card stored on the client’s account.<br>* DirectDebit - Indicates that this payment item is a direct debit.<br>* EncryptedTrackData - Indicates that this payment item is a swiped credit card.<br>* TrackData - Indicates that this payment item is a swiped credit card.<br>* DebitAccount - Indicates that funds should be debited from the client’s account.<br>* Custom - Indicates that this payment item is a custom payment method configured by the business.<br>* Comp - Indicates that this payment item is making all or part of the cart’s total complementary.<br>* Cash - Indicates that this payment item is cash.<br>* Check - Indicates that this payment item is a check.<br>* GiftCard - Indicates that this payment item is a gift card. |
| `metadata` | `Dict[str, Any]` | Optional | Contains information about the cart’s payments. Possible values vary according to the Type property, as below:<br><br>* CreditCard Keys - amount, creditCardNumber, expMonth, expYear, cvv, billingName, billingAddress, billingCity, billingState, billingPostalCode, saveInfo, cardId<br>* StoredCard Keys - amount, lastFour<br>* DirectDebit Keys - amount<br>* EncryptedTrackData Keys - amount, trackData<br>* TrackData Keys - amount, trackData<br>* DebitAccount Keys - amount<br>* Custom Keys - amount, id<br>* Comp Keys - amount<br>* Cash Keys - amount, notes<br>* Check Keys - amount, notes<br>* GiftCard - amount, notes, cardNumber |

## Example (as JSON)

```json
{
  "Type": "Type0",
  "Metadata": {
    "key0": {
      "key1": "val1",
      "key2": "val2"
    },
    "key1": {
      "key1": "val1",
      "key2": "val2"
    }
  }
}
```

