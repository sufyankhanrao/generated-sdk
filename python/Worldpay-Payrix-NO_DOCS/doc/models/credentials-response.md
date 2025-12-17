
# Credentials Response

## Structure

`CredentialsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `entity` | `str` | Optional | The identifier of the Entity that this Credential resource belongs to. |
| `name` | `str` | Optional | The name of this Credential resource.<br>This field is stored as a text string and must be between 1 and 100 characters long. |
| `description` | `str` | Optional | A description of this Credential resource.<br>This field is stored as a text string and must be between 1 and 100 characters long. |
| `username` | `str` | Optional | The username to use when authenticating to the integration associated with this Credential resource.<br>This field is stored as a text string and must be between 1 and 50 characters long. |
| `password` | `str` | Optional | The password to use when authenticating to the integration associated with this Credential resource.<br>This field is stored as a text string and must be between 1 and 50 characters long. |
| `connect_username` | `str` | Optional | The username to use when connecting to the integration associated with this Credential resource.<br>This field is stored as a text string and must be between 1 and 50 characters long.<br>This field is only necessary when it is required by the integration. |
| `connect_password` | `str` | Optional | The password to use when connecting to the integration associated with this Credential resource.<br>This field is stored as a text string and must be between 1 and 50 characters long.<br>This field is only necessary when it is required by the integration. |
| `integration` | [`CredentialIntegrationEnum`](../../doc/models/credential-integration-enum.md) | Optional | The payment platform integration using credential logins.<br><br><details><br><summary>Valid Values</summary><br>- `APPLE` - **Apple API.**<br>- `ELAVON` - **Elavon API.**<br><br>- `FEDACH` - **FedACH Account Integration.**<br><br>- `FIRSTDATA` - **FirstData / Clover Integration.**<br><br>- `NEUTRINO` - **Neutrino eCommerce Integration.**<br><br>- `OFAC` - **Office of Foreign Assets Control Sanctions.**<br><br>- `PAYRIX` - **Payrix API.**<br><br>- `PLAID` - **Plaid Account Integration.**<br><br>- `SIFT` - **Sift Fraud Management.**<br><br>- `SOCURE` - **Socure ID Verification.**<br><br>- `SOUNDPAYMENTS` - **Sound Payments POS.**<br><br>- `TDBANK` - **TD Bank Platform.**<br><br>- `VANTIV` - **WorldPay / Vantiv eComm Platform.**<br><br>- `VCORE` - **WorldPay / Vantiv Core Platform.**<br><br>- `WEBSHIELD` - **Web Shield Merchant Monitoring.**<br><br>- `WELLSACH` - **Wells Fargo Merchant Services ACH Processor.**<br><br>- `WELLSFARGO` - **Wells Fargo Merchant Services Payment Processor.**<br><br>- `WFSINGLE` - **Wells Fargo Single Payment Processors.**<br><br></details><br> |
| `mtype` | [`CredentialTypeEnum`](../../doc/models/credential-type-enum.md) | Optional | The type of Transaction.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **Credit Card Only:** Sale Transaction. Processes a sale and charges the customer.<br>- `2` - **Credit Card Only:** Auth Transaction. Authorizes and holds the requested total on the credit card.<br>- `3` - **Credit Card Only:** Capture Transaction. Finalizes a prior Auth Transaction and charges the customer.<br>- `4` - **Credit Card Only:** Reverse Authorization. Reverses a prior Auth or Sale Transaction and releases the credit hold.<br>- `5` - **Credit Card Only:** Refund Transaction. Refunds a prior Capture or Sale Transaction (total may be specified for a partial refund).<br>- `7` - **Echeck Only:** Echeck Sale Transaction. Sale Transaction for ECheck payment.<br>- `8` - **ECheck Only:** ECheck Refund Transaction. Refund Transaction for prior ECheck Sale Transaction.<br>- `11` - **Echeck Only:** Echeck Redeposit Transaction. Attempt to redeposit a prior failed eCheck Sale Transaction.<br>- `12` - **Echeck Only:** Echeck Account Verification Transaction. Attempt to verify eCheck payment details.<br></details><br> |
| `secret` | `str` | Optional | The secret resource identifier to use when connecting using this Credential.<br>This field is only necessary when a private key is required by the integration. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "inactive": 0,
  "frozen": 0,
  "id": "id4",
  "created": "created4",
  "modified": "modified2",
  "creator": "String3",
  "modifier": "modifier8"
}
```

