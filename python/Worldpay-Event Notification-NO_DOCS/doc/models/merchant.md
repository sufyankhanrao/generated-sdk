
# Merchant

This aggregate field includes hierarchy, business, location and additional information related data of merchant

## Structure

`Merchant`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hierarchy` | [`Hierarchy`](../../doc/models/hierarchy.md) | Optional | This aggregate field includes hierarchy data |
| `business` | [`Business`](../../doc/models/business.md) | Optional | This aggregate field includes business data |
| `location` | [`Location`](../../doc/models/location.md) | Optional | This aggregate field includes location data |
| `additional_info` | [`AdditionalInfo`](../../doc/models/additional-info.md) | Optional | This aggregate field includes additional information |

## Example (as JSON)

```json
{
  "hierarchy": {
    "salesOrganizationCode": "salesOrganizationCode2",
    "salesOrganizationName": "salesOrganizationName0",
    "salesChannelCode": "salesChannelCode4",
    "salesChannelName": "salesChannelName2",
    "partnerGroupId": "partnerGroupId4"
  },
  "business": {
    "chainCode": "chainCode2",
    "chainAcro": "chainAcro2",
    "createdDate": "2016-03-13",
    "legalName": "legalName6",
    "dbaName": "dbaName8",
    "partners": [
      [
        {
          "type": "type2",
          "id": "id2",
          "name": "name2"
        },
        {
          "type": "type2",
          "id": "id2",
          "name": "name2"
        },
        {
          "type": "type2",
          "id": "id2",
          "name": "name2"
        }
      ],
      [
        {
          "type": "type2",
          "id": "id2",
          "name": "name2"
        },
        {
          "type": "type2",
          "id": "id2",
          "name": "name2"
        },
        {
          "type": "type2",
          "id": "id2",
          "name": "name2"
        }
      ],
      [
        {
          "type": "type2",
          "id": "id2",
          "name": "name2"
        },
        {
          "type": "type2",
          "id": "id2",
          "name": "name2"
        },
        {
          "type": "type2",
          "id": "id2",
          "name": "name2"
        }
      ]
    ]
  },
  "location": {
    "storeNumber": "storeNumber2",
    "storeName": "storeName6",
    "merchantId": "merchantId0",
    "hostMerchantNumber": "hostMerchantNumber8",
    "billingDescriptor": "billingDescriptor4"
  },
  "additionalInfo": {
    "clientTrackingId": "clientTrackingId4",
    "partnerLeadType": "partnerLeadType6",
    "partnerPromotionCampaign": "partnerPromotionCampaign0",
    "partnerVipIndicator": false,
    "partnerMarketRegion": "partnerMarketRegion2"
  }
}
```

