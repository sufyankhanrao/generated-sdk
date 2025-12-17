
# Tax Rates 2

Consists of tax rates applicable pre & post-retirement.

*This model accepts additional fields of type Any.*

## Structure

`TaxRates2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ltcg_pre_retirement` | `float` | Required | Pre-retirement Long Term Capital Gains tax on profits & qualified dividends due to capital appreciation. <br>                        LTCG is applicable only on taxable accounts.<br><br>**Constraints**: `>= 0`, `<= 1` |
| `ltcg_post_retirement` | `float` | Required | Pre-retirement Long Term Capital Gains tax on profits & qualified dividends due to capital appreciation. <br>                        LTCG is applicable only on taxable accounts.<br><br>**Constraints**: `>= 0`, `<= 1` |
| `etr_pre_retirement` | `float` | Required | Pre-retirement Effective tax rate applicable on profits due to: <br>                     Unqualified Dividend <br>                     Interest Income <br>                     Social Security Income< br>                     TDA Withdrawal<br><br>**Constraints**: `>= 0`, `<= 1` |
| `etr_post_retirement` | `float` | Required | Post-retirement Effective tax rate applicable on profits due to: <br>                     Unqualified Dividend <br>                     Interest Income <br>                     Social Security Income <br>                     TDA Withdrawal (including RMD)<br><br>**Constraints**: `>= 0`, `<= 1` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "LTCGPreRetirement": 0.15,
  "LTCGPostRetirement": 0.15,
  "ETRPreRetirement": 0.15,
  "ETRPostRetirement": 0.15,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

