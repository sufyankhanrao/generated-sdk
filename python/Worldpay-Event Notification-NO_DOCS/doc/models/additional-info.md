
# Additional Info

## Structure

`AdditionalInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_tracking_id` | `str` | Optional | Tracking ID of Client<br><br>**Constraints**: *Maximum Length*: `255` |
| `partner_lead_type` | `str` | Optional | Type of Partner Lead<br><br>**Constraints**: *Maximum Length*: `255` |
| `partner_promotion_campaign` | `str` | Optional | Partner Promotion Campaign Code<br><br>**Constraints**: *Maximum Length*: `255` |
| `partner_vip_indicator` | `bool` | Optional | Indicator for VIP |
| `partner_market_region` | `str` | Optional | Partner Market Region<br><br>**Constraints**: *Maximum Length*: `255` |
| `partner_employee_officer_code` | `str` | Optional | Partner employee officer code<br><br>**Constraints**: *Maximum Length*: `50` |
| `partner_employee_type` | `str` | Optional | Partner Employee Type<br><br>**Constraints**: *Maximum Length*: `80` |
| `partner_employee_id` | `str` | Optional | Partner employee ID<br><br>**Constraints**: *Maximum Length*: `16` |
| `partner_employee_name` | `str` | Optional | Name of the partner employee<br><br>**Constraints**: *Maximum Length*: `80` |
| `partner_employee_region` | `str` | Optional | Partner Employee Region<br><br>**Constraints**: *Maximum Length*: `80` |
| `partner_employee_branch` | `str` | Optional | Partner Employee Branch<br><br>**Constraints**: *Maximum Length*: `80` |
| `partner_employee_cost_center` | `str` | Optional | Partner Employee Cost Center<br><br>**Constraints**: *Maximum Length*: `80` |
| `partner_employee_officer_code_2` | `str` | Optional | Partner employee officer code<br><br>**Constraints**: *Maximum Length*: `50` |
| `partner_employee_type_2` | `str` | Optional | Partner Employee Type<br><br>**Constraints**: *Maximum Length*: `255` |
| `partner_employee_name_2` | `str` | Optional | Name of the partner employee<br><br>**Constraints**: *Maximum Length*: `80` |
| `partner_employee_id_2` | `str` | Optional | Partner employee ID<br><br>**Constraints**: *Maximum Length*: `16` |
| `partner_employee_region_2` | `str` | Optional | Partner Employee Region<br><br>**Constraints**: *Maximum Length*: `80` |
| `partner_employee_branch_2` | `str` | Optional | Partner Employee Branch<br><br>**Constraints**: *Maximum Length*: `80` |
| `partner_employee_cost_center_2` | `str` | Optional | Partner Employee Cost Center<br><br>**Constraints**: *Maximum Length*: `80` |
| `partner_employee_industry` | `str` | Optional | Partner Employee Industry<br><br>**Constraints**: *Maximum Length*: `80` |
| `partner_employee_ref` | `str` | Optional | Partner Employee Reference<br><br>**Constraints**: *Maximum Length*: `80` |
| `partner_custom_1` | `str` | Optional | Partner Custom Data 1<br><br>**Constraints**: *Maximum Length*: `255` |
| `partner_custom_2` | `str` | Optional | Partner Custom Data 2<br><br>**Constraints**: *Maximum Length*: `255` |
| `partner_custom_3` | `str` | Optional | Partner Custom Data 3<br><br>**Constraints**: *Maximum Length*: `255` |
| `partner_custom_4` | `str` | Optional | Partner Custom Data 4<br><br>**Constraints**: *Maximum Length*: `255` |
| `partner_custom_5` | `str` | Optional | Partner Custom Data 5<br><br>**Constraints**: *Maximum Length*: `255` |
| `partner_group_id` | `str` | Optional | Partner Group ID<br><br>**Constraints**: *Maximum Length*: `16` |
| `partner_lead_id` | `str` | Optional | Partner Lead ID<br><br>**Constraints**: *Maximum Length*: `50` |
| `partner_method` | `str` | Optional | Partner Method<br><br>**Constraints**: *Maximum Length*: `80` |
| `partner_source_details` | `str` | Optional | Partner Source Details<br><br>**Constraints**: *Maximum Length*: `80` |
| `partner_sales_agent_id` | `str` | Optional | Partner Sales Agent ID<br><br>**Constraints**: *Maximum Length*: `80` |
| `partner_sales_agent_name` | `str` | Optional | Name of Partner Sales Agent<br><br>**Constraints**: *Maximum Length*: `80` |

## Example (as JSON)

```json
{
  "clientTrackingId": "1234",
  "partnerLeadType": "Bank Lead",
  "partnerPromotionCampaign": "Code234",
  "partnerVipIndicator": true,
  "partnerMarketRegion": "Arizona",
  "partnerEmployeeOfficerCode": "Officer Code 1",
  "partnerEmployeeType": "Employee Type 1",
  "partnerEmployeeId": "1234",
  "partnerEmployeeName": "John Doe",
  "partnerEmployeeRegion": "ABC 123",
  "partnerEmployeeBranch": "Atlanta",
  "partnerEmployeeCostCenter": "Cost Center 1",
  "partnerEmployeeOfficerCode2": "Officer Code 2",
  "partnerEmployeeType2": "Employee Type 2",
  "partnerEmployeeName2": "Jane Doe",
  "partnerEmployeeId2": "4321",
  "partnerEmployeeRegion2": "Atlanta",
  "partnerEmployeeBranch2": "Atlanta",
  "partnerEmployeeCostCenter2": "Cost Center 2",
  "partnerEmployeeIndustry": "Services",
  "partnerEmployeeRef": "Reference 1",
  "partnerCustom1": "data 1",
  "partnerCustom2": "data 2",
  "partnerCustom3": "data 3",
  "partnerCustom4": "data 4",
  "partnerCustom5": "data 5",
  "partnerGroupID": "group 1",
  "partnerLeadId": "NA00123456",
  "partnerMethod": "Method 1",
  "partnerSourceDetails": "Source 1",
  "partnerSalesAgentId": "A001234",
  "partnerSalesAgentName": "John R John"
}
```

