
# Orgs Post Request

## Structure

`OrgsPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `login` | `str` | Required | The Login that owns this Org. |
| `name` | `str` | Optional | The name of this Org.<br>This field is stored as a text string and must be between 0 and 100 characters long. |
| `description` | `str` | Optional | A description of this Org.<br>This field is stored as a text string and must be between 0 and 100 characters long. |
| `billings` | [`List[BillingsPostRequest]`](../../doc/models/billings-post-request.md) | Optional | - |
| `fee_modifiers` | [`List[FeeModifiersPostRequest]`](../../doc/models/fee-modifiers-post-request.md) | Optional | - |
| `fees` | [`List[FeesPostRequest]`](../../doc/models/fees-post-request.md) | Optional | - |
| `invoice_parameters` | [`List[InvoiceParametersPostRequest]`](../../doc/models/invoice-parameters-post-request.md) | Optional | - |
| `org_entities` | [`List[OrgEntitiesPostRequest]`](../../doc/models/org-entities-post-request.md) | Optional | - |
| `payout_flows` | [`List[PayoutFlowsPostRequest]`](../../doc/models/payout-flows-post-request.md) | Optional | - |
| `pinless_debit_conversions` | [`List[PinlessDebitConversionsPostRequest]`](../../doc/models/pinless-debit-conversions-post-request.md) | Optional | - |
| `profit_shares` | [`List[ProfitSharesPostRequest]`](../../doc/models/profit-shares-post-request.md) | Optional | - |
| `reserves` | [`List[ReservesPostRequest]`](../../doc/models/reserves-post-request.md) | Optional | - |
| `secrets` | [`List[SecretsPostRequest]`](../../doc/models/secrets-post-request.md) | Optional | - |

## Example (as JSON)

```json
{
  "login": "t1_log_656d51cd565edf13a27c494",
  "name": "Leora44",
  "description": "description of Org",
  "billings": [
    {
      "login": "login8",
      "entity": "entity6",
      "forentity": "forentity0",
      "org": "org4",
      "division": "division8",
      "partition": "partition0",
      "description": "description8",
      "schedule": "days",
      "scheduleFactor": 214,
      "start": 18,
      "collection": "collection4",
      "collectionFactor": "days",
      "collectionOffset": 154,
      "collectionIncludeCurrent": 0,
      "currency": "MWK",
      "inactive": 0,
      "frozen": 0
    }
  ],
  "feeModifiers": [
    {
      "fee": "fee4",
      "entity": "entity0",
      "org": "org8",
      "fromentity": "fromentity4",
      "markupUm": 1,
      "markupAmount": 38,
      "inactive": 0,
      "frozen": 0
    },
    {
      "fee": "fee4",
      "entity": "entity0",
      "org": "org8",
      "fromentity": "fromentity4",
      "markupUm": 1,
      "markupAmount": 38,
      "inactive": 0,
      "frozen": 0
    },
    {
      "fee": "fee4",
      "entity": "entity0",
      "org": "org8",
      "fromentity": "fromentity4",
      "markupUm": 1,
      "markupAmount": 38,
      "inactive": 0,
      "frozen": 0
    }
  ],
  "fees": [
    {
      "entity": "entity2",
      "forentity": "forentity8",
      "org": "org6",
      "type": 1,
      "name": "name0",
      "description": "description0",
      "schedule": 266,
      "scheduleFactor": 86,
      "start": 146,
      "finish": 34,
      "collectionFactor": 172,
      "collectionOffset": 230,
      "um": 1,
      "amount": 54.88,
      "currency": "CHW",
      "txnFee": 0,
      "inactive": 0,
      "frozen": 0
    },
    {
      "entity": "entity2",
      "forentity": "forentity8",
      "org": "org6",
      "type": 1,
      "name": "name0",
      "description": "description0",
      "schedule": 266,
      "scheduleFactor": 86,
      "start": 146,
      "finish": 34,
      "collectionFactor": 172,
      "collectionOffset": 230,
      "um": 1,
      "amount": 54.88,
      "currency": "CHW",
      "txnFee": 0,
      "inactive": 0,
      "frozen": 0
    }
  ]
}
```

