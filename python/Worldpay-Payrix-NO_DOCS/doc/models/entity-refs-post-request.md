
# Entity Refs Post Request

## Structure

`EntityRefsPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entity` | `str` | Required | The identifier of the Entity that owns this entityRefs resource. |
| `member` | `str` | Required | The identifier of the Member associated with this entityRefs resource. Default value is 'null' |
| `entity_route` | `str` | Optional | The original 'entity_route' that routed the merchant onto the platform which then returned this reference information, if applicable. |
| `ref` | `str` | Required | The reference code itself.<br>This field is stored as a text string and must be between 0 and 50 characters long. |
| `stage` | [`EntityRefStageEnum`](../../doc/models/entity-ref-stage-enum.md) | Required | An indicator showing what this terminalRef refers to.<br><br><details><br><summary>Valid Values</summary><br>- `amexCharge` - **Amex Charge.**<br>- `batch` - **Batch.**<br>- `batchSuffix` - **Batch Suffix.**<br>- `boarding` - **Boarding.**<br>- `chain` - **The store chain ID for this Merchant.**<br>- `chargeback` - **Chargeback.**<br>- `companyDebit` - **Company Debit.**<br>- `companyCredit` - **Company Credit.**<br>- `create` - **Terminal Creation.**<br>- `disbursement` - **Disbursement.**<br>- `entity` - **The Entity ID.**<br>- `batchFile` - **Batch File.**<br>- `payoutFile` - **Payout File.**<br>- `frontend` - **Frontend.**<br>- `funding` - **The Payout funding ID for this Merchant.**<br>- `member` - **The member ID for this Member.**<br>- `merchant` - **The Merchant ID.**<br>- `mid` - **The transaction Merchant ID (MID).**<br>- `origId` - **Original ID.**<br>- `store` - **The store ID for this Merchant.**<br>- `software` - **Software.**<br>- `terminal` - **Terminal.**<br>- `displayName` - **Display Name.**<br>- `domain` - **Domain.**<br>- `expressCreds` - **Express Credentials.**<br></details><br> |
| `staging` | [`StagingEnum`](../../doc/models/staging-enum.md) | Required | Allows a merchant to transact under the Staging environment while boarding is in progress, and allows for configuration with valid values such as **Disabled** or **Enabled**.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Disabled**<br>- `1` - **Enabled**<br></details><br>**Default**: `0`<br> |
| `platform` | [`EntityPlatformEnum`](../../doc/models/entity-platform-enum.md) | Required | The processor that issued this terminalTxnRef.<br><br><details><br><summary>Valid Values</summary><br>- `APPLE` - **APPLE**<br>- `ELAVON` - **ELAVON**<br>- `FIRSTDATA` - **FIRSTDATA**<br>- `GOOGLE` - **GOOGLE**<br>- `VANTIV` - **VANTIV**<br>- `VCORE` - **VCORE**<br>- `WELLSACH` - **WELLSACH**<br>- `WELLSFARGO` - **WELLSFARGO**<br>- `WFSINGLE` - **WFSINGLE**<br>- `WORLDPAY` - **WORLDPAY**<br>- `TDBANKCA` - **TDBANKCA**<br></details><br> |
| `currency` | [`CurrencyEnum`](../../doc/models/currency-enum.md) | Optional | The currency of the entityRef. See <a href="https://www.iban.com/currency-codes" target="_blank">Currency codes</a>  for all valid values. |
| `funding_currency` | [`FundingCurrencyEnum`](../../doc/models/funding-currency-enum.md) | Optional | The currency for which this entityRefs resource was funded on. See <a href="https://www.iban.com/currency-codes" target="_blank">Currency codes</a>  for all valid values. |
| `default` | [`Default4Enum`](../../doc/models/default-4-enum.md) | Required | Whether this entityRef is the default one. Default entityRefs will have priority when processing transactions with no MID or Platform set. <details> <summary>Valid Values</summary> - `0` - **Not default.** - `1` - **Default.** </details><br><br>**Default**: `0` |
| `fbo` | `str` | Optional | The FBO from which this entity refers to. |
| `options` | `str` | Optional | A string-JSON of options for this reference value. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Required | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Required | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "entity": "entity8",
  "member": "member6",
  "ref": "ref0",
  "stage": "chain",
  "staging": 0,
  "platform": "VCORE",
  "currency": "USD",
  "fundingCurrency": "USD",
  "default": 0,
  "inactive": 0,
  "frozen": 0,
  "entityRoute": "entityRoute6",
  "fbo": "fbo0",
  "options": "options8"
}
```

