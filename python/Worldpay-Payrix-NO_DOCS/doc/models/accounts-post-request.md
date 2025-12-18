
# Accounts Post Request

A request body for creating new bank account information for one or more entities.

## Structure

`AccountsPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entity` | `str` | Required | The identifier of the Entity associated with this Account. |
| `account` | [`AccountsAccount`](../../doc/models/accounts-account.md) | Required | An object representing details of the Account, including the type of Account (method), Account number, and routing code. |
| `name` | `str` | Optional | A client-supplied name for this bank account.<br>This field is stored as a string and must be between 0 and 100 characters long. |
| `description` | `str` | Optional | A client-supplied description for this bank account.<br>This field is stored as a string and must be between 0 and 100 characters long. |
| `primary` | [`AccountPrimaryEnum`](../../doc/models/account-primary-enum.md) | Required | Indicates whether the Account is the primary Account for the associated Entity.<br>Only one Account associated with each Entity can be the primary Account.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not primary**<br>- `1` - **Primary**<br></details><br> |
| `mtype` | [`AccountTypeEnum`](../../doc/models/account-type-enum.md) | Required | The type of financial account: debit, credit, or both.<br><br><details><br><summary>Valid Values</summary><br>- `all` - **Debit/checking and credit**<br>- `credit` - **Credit only**<br>- `debit` - **Debit/checking only**<br></details><br>**Default**: `'all'`<br> |
| `status` | [`AccountStatusEnum`](../../doc/models/account-status-enum.md) | Required | The status of the Account.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Ready.**<br>- `1` - **Ready.**<br>- `2` - **Challenged.**<br>- `3` - **Verified.**<br>- `4` - **Manual.**<br></details><br>**Default**: `0`<br> |
| `expiration` | `str` | Optional | The expiration date of the related debit account. The date is specified as a four-digit string in MMYY format, for example, `0118` for January 2018. |
| `currency` | [`CurrencyEnum`](../../doc/models/currency-enum.md) | Required | The currency of this Account. The default is `USD`. See <a href="https://www.iban.com/currency-codes" target="_blank">Currency codes</a>  for all valid values. |
| `public_token` | `str` | Optional | The token received from the Plaid account connection process. |
| `mask` | `str` | Optional | The account number mask, showing the last four digits of the account number. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |
| `payouts` | [`List[PayoutPostRequest]`](../../doc/models/payout-post-request.md) | Optional | - |

## Example (as JSON)

```json
{
  "entity": "t1_ent_5a1pf5a1234531155a12345",
  "primary": 1,
  "name": "Bank Account Name",
  "description": "Bank account description",
  "account": {
    "method": 8,
    "routing": "1",
    "number": "2"
  },
  "currency": "USD",
  "type": "all",
  "status": 1,
  "expiration": "0118",
  "publicToken": "public-test-a12eeba1-1234-4567-af1g-d80cc1bfd713",
  "mask": "2345",
  "inactive": 0,
  "frozen": 0
}
```

