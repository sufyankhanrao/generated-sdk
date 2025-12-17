
# Checkout Item

## Structure

`CheckoutItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | The type of item. Possible values are:<br><br>* Service - Indicates that this item is a pricing option.<br>* Product - Indicates that this item is a retail product.<br>* Package - Indicates that this item is a package.<br>* Tip - Indicates that this item is a tip. |
| `metadata` | `Dict[str, Any]` | Optional | Contains information about the item to be purchased. See [Cart Item Metadata](https://developers.mindbodyonline.com/PublicDocumentation/V6#cart-item-metadata) for more information. |

## Example (as JSON)

```json
{
  "Type": "Type2",
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

