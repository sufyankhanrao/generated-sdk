
# Entity Refs Response

## Structure

`EntityRefsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `entity` | `str` | Optional | The identifier of the Entity that owns this entityRefs resource. |
| `member` | `str` | Optional | The identifier of the Member associated with this entityRefs resource. |
| `entity_route` | `str` | Optional | The original 'entity_route' that routed the merchant onto the platform which then returned this reference information, if applicable |
| `ref` | `str` | Optional | The reference code itself.<br>This field is stored as a text string and must be between 0 and 50 characters long. |
| `stage` | [`EntityRefStageEnum`](../../doc/models/entity-ref-stage-enum.md) | Optional | An indicator showing what this terminalRef refers to.<br><br><details><br><summary>Valid Values</summary><br>- `amexCharge` - **Amex Charge.**<br>- `batch` - **Batch.**<br>- `batchSuffix` - **Batch Suffix.**<br>- `boarding` - **Boarding.**<br>- `chain` - **The store chain ID for this Merchant.**<br>- `chargeback` - **Chargeback.**<br>- `companyDebit` - **Company Debit.**<br>- `companyCredit` - **Company Credit.**<br>- `create` - **Terminal Creation.**<br>- `disbursement` - **Disbursement.**<br>- `entity` - **The Entity ID.**<br>- `batchFile` - **Batch File.**<br>- `payoutFile` - **Payout File.**<br>- `frontend` - **Frontend.**<br>- `funding` - **The Payout funding ID for this Merchant.**<br>- `member` - **The member ID for this Member.**<br>- `merchant` - **The Merchant ID.**<br>- `mid` - **The transaction Merchant ID (MID).**<br>- `origId` - **Original ID.**<br>- `store` - **The store ID for this Merchant.**<br>- `software` - **Software.**<br>- `terminal` - **Terminal.**<br>- `displayName` - **Display Name.**<br>- `domain` - **Domain.**<br>- `expressCreds` - **Express Credentials.**<br></details><br> |
| `staging` | [`StagingEnum`](../../doc/models/staging-enum.md) | Optional | Allows a merchant to transact under the Staging environment while boarding is in progress, and allows for configuration with valid values such as **Disabled** or **Enabled**.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Disabled**<br>- `1` - **Enabled**<br></details><br> |
| `platform` | [`EntityPlatformEnum`](../../doc/models/entity-platform-enum.md) | Optional | The processor that issued this terminalTxnRef.<br><br><details><br><summary>Valid Values</summary><br>- `APPLE` - **APPLE**<br>- `ELAVON` - **ELAVON**<br>- `FIRSTDATA` - **FIRSTDATA**<br>- `GOOGLE` - **GOOGLE**<br>- `VANTIV` - **VANTIV**<br>- `VCORE` - **VCORE**<br>- `WELLSACH` - **WELLSACH**<br>- `WELLSFARGO` - **WELLSFARGO**<br>- `WFSINGLE` - **WFSINGLE**<br>- `WORLDPAY` - **WORLDPAY**<br>- `TDBANKCA` - **TDBANKCA**<br></details><br> |
| `currency` | [`CurrencyEnum`](../../doc/models/currency-enum.md) | Optional | The currency of the entityRef. See <a href="https://www.iban.com/currency-codes" target="_blank">Currency codes</a>  for all valid values. |
| `funding_currency` | [`FundingCurrencyEnum`](../../doc/models/funding-currency-enum.md) | Optional | The currency for which this entityRefs resource was funded on. See <a href="https://www.iban.com/currency-codes" target="_blank">Currency codes</a>  for all valid values. |
| `options` | `str` | Optional | A string-JSON of options for this reference value. |
| `default` | [`EntityRefsDefaultEnum`](../../doc/models/entity-refs-default-enum.md) | Optional | Whether this entityRef is the default one. Default entityRefs will have priority when processing transactions with no MID or Platform set.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not default**<br>- `1` - **Default**<br></details><br> |
| `fbo` | `str` | Optional | The FBO from which this entity refers to. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "platform": "VCORE",
  "currency": "USD",
  "fundingCurrency": "USD",
  "inactive": 0,
  "frozen": 0,
  "id": "id0",
  "created": "created0",
  "modified": "modified2",
  "creator": "String9",
  "modifier": "modifier6"
}
```

