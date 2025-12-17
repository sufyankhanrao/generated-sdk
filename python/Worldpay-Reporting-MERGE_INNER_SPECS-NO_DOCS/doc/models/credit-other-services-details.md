
# Credit Other Services Details

This object provides information on other services related information

## Structure

`CreditOtherServicesDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dcc_indicator` | `str` | Optional | Provides dynamic currency conversion information to the merchant. Applicable for credit (master credit card).<br><br>**Constraints**: *Maximum Length*: `1` |
| `level_indicator` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Level code and description of the code |
| `re_authorization_attempts_count` | `str` | Optional | Indicates count of authorization re-attempts.<br><br>**Constraints**: *Maximum Length*: `256` |
| `signature_capabilities_indicator` | `str` | Optional | Indicator of signature capabilities.<br><br>**Constraints**: *Maximum Length*: `256` |
| `signature_compression` | `str` | Optional | Indicates signature compression.<br><br>**Constraints**: *Maximum Length*: `256` |
| `signature_encrypt_key` | `str` | Optional | Indicates key of signature encryption.<br><br>**Constraints**: *Maximum Length*: `256` |
| `signature_encrypt_method` | `str` | Optional | It is used to verify the encryption method.<br><br>**Constraints**: *Maximum Length*: `256` |
| `signature_pen` | `str` | Optional | Pinless transaction.<br><br>**Constraints**: *Maximum Length*: `256` |

## Example (as JSON)

```json
{
  "dccIndicator": "Y",
  "reAuthorizationAttemptsCount": "6",
  "signatureCapabilitiesIndicator": "NO, SIGNATURE WAS NOT CAPTURED",
  "signatureCompression": "GEHG",
  "signatureEncryptKey": "FYJGDT",
  "signatureEncryptMethod": "EJYUH",
  "signaturePen": "GEBD",
  "levelIndicator": {
    "code": "code4",
    "shortDescription": "shortDescription8",
    "longDescription": "longDescription6"
  }
}
```

