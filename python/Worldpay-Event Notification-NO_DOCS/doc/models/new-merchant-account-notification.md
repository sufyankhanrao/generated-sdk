
# New Merchant Account Notification

## Structure

`NewMerchantAccountNotification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_type` | `str` | Required | Name of the event<br><br>**Constraints**: *Maximum Length*: `50` |
| `notification_id` | `int` | Required | The identifier associated with the event notification |
| `event_count` | `int` | Required | The count associated with the notification |
| `version` | `str` | Optional | The version of the event framework<br><br>**Constraints**: *Maximum Length*: `3` |
| `created_at` | `str` | Optional | Notification created date and time<br><br>**Constraints**: *Minimum Length*: `20`, *Maximum Length*: `20` |
| `data` | [`Data`](../../doc/models/data.md) | Required | This aggregate field includes details of merchantAccounts |

## Example (as JSON)

```json
{
  "eventType": "merchant.accounts.created",
  "notificationId": 12345,
  "eventCount": 1,
  "version": "2.0",
  "data": {
    "merchantAccounts": [
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
      },
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
    ]
  },
  "createdAt": "createdAt8"
}
```

