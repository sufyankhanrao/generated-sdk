
# Get Client Contracts Response

## Structure

`GetClientContractsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `contracts` | [`List[ClientContract]`](../../doc/models/client-contract.md) | Optional | Contains the details of the client’s contract. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Contracts": [
    {
      "AgreementDate": "2016-03-13T12:52:32.123Z",
      "AutopayStatus": "Active",
      "ContractName": "ContractName8",
      "EndDate": "2016-03-13T12:52:32.123Z",
      "Id": 44
    },
    {
      "AgreementDate": "2016-03-13T12:52:32.123Z",
      "AutopayStatus": "Active",
      "ContractName": "ContractName8",
      "EndDate": "2016-03-13T12:52:32.123Z",
      "Id": 44
    },
    {
      "AgreementDate": "2016-03-13T12:52:32.123Z",
      "AutopayStatus": "Active",
      "ContractName": "ContractName8",
      "EndDate": "2016-03-13T12:52:32.123Z",
      "Id": 44
    }
  ]
}
```

