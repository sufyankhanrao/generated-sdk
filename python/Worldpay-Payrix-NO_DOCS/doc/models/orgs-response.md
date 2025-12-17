
# Orgs Response

## Structure

`OrgsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `login` | str \| [loginsResponse4](../../doc/models/logins-response-4.md) \| None | Optional | This is a container for any-of cases. |
| `name` | `str` | Optional | The name of this Org.<br>This field is stored as a text string and must be between 0 and 100 characters long. |
| `description` | `str` | Optional | A description of this Org.<br>This field is stored as a text string and must be between 0 and 100 characters long. |
| `default_fee_from_entity` | `str` | Optional | This is used to specify a default fee for a group. |
| `aggregations` | [`List[AggregationsResponse]`](../../doc/models/aggregations-response.md) | Optional | - |
| `billing_modifiers` | [`List[BillingModifiersResponse]`](../../doc/models/billing-modifiers-response.md) | Optional | - |
| `billings` | [`List[BillingsResponse]`](../../doc/models/billings-response.md) | Optional | - |
| `decisions` | [`List[DecisionsResponse]`](../../doc/models/decisions-response.md) | Optional | - |
| `embedded_finance` | [`List[DivisionsResponse2]`](../../doc/models/divisions-response-2.md) | Optional | - |
| `fee_modifiers` | [`List[FeeModifiersResponse]`](../../doc/models/fee-modifiers-response.md) | Optional | - |
| `fees` | [`List[FeesResponse]`](../../doc/models/fees-response.md) | Optional | - |
| `invoice_parameters` | [`List[InvoiceParametersResponse]`](../../doc/models/invoice-parameters-response.md) | Optional | - |
| `org_entities` | [`List[OrgEntitiesResponse]`](../../doc/models/org-entities-response.md) | Optional | - |
| `omni_tokens` | [`List[OmniTokensResponse]`](../../doc/models/omni-tokens-response.md) | Optional | - |
| `payout_flows` | [`List[PayoutFlowsResponse]`](../../doc/models/payout-flows-response.md) | Optional | - |
| `profit_shares` | [`List[ProfitSharesResponse]`](../../doc/models/profit-shares-response.md) | Optional | - |
| `reserves` | [`List[ReservesResponse]`](../../doc/models/reserves-response.md) | Optional | - |
| `revenue_boosts` | [`List[RevenueBoostsResponse]`](../../doc/models/revenue-boosts-response.md) | Optional | - |
| `secrets` | [`List[SecretsResponse]`](../../doc/models/secrets-response.md) | Optional | - |
| `safer_payments` | [`List[SaferPaymentsResponse]`](../../doc/models/safer-payments-response.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": "id4",
  "created": "created4",
  "modified": "modified2",
  "creator": "String3",
  "modifier": "modifier8"
}
```

