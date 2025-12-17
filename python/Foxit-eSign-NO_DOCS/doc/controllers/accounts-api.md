# Accounts API

```python
accounts_api_controller = client.accounts_api
```

## Class Name

`AccountsAPIController`

## Methods

* [Create New Account](../../doc/controllers/accounts-api.md#create-new-account)
* [Change Plan](../../doc/controllers/accounts-api.md#change-plan)
* [Cancel Account](../../doc/controllers/accounts-api.md#cancel-account)
* [Reactivate Account](../../doc/controllers/accounts-api.md#reactivate-account)
* [Change Licenses](../../doc/controllers/accounts-api.md#change-licenses)


# Create New Account

This endpoint allows you to create a new account as a partner by using the API.

*Note:* instead of providing the `access_token` Authorization header from your partner portal, you will instead provide the `client_id` and `client_secret` as part of the body parameters of this call.

:information_source: **Note** This endpoint does not require authentication.

```python
def create_new_account(self,
                      account_creationobject)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_creationobject` | [`AccountCreationObject`](../../doc/models/account-creation-object.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
account_creationobject = AccountCreationObject(
    client_id='123456789012345678901234567890',
    client_secret='123456789012345678901234567890',
    company=AccountCreationCompanyObject(
        company_name='Wayne Tech',
        company_address='LA, US'
    ),
    user=AccountCreationUserObject(
        first_name='Bruce',
        last_name='Wayne',
        email_id='esigndemo@foxitsoftware.com',
        login_password='Welcome@123!'
    ),
    plan_name=PlanNamesEnum.PROFESSIONAL,
    account_type='partner-pay',
    partner_code='WAYNE_TECH'
)

result = accounts_api_controller.create_new_account(account_creationobject)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response

```
{
  "refresh_token": "12345678901234567890123456789012",
  "access_token": "12345678901234567890123456789012",
  "token_type": "bearer",
  "expires_in": 31535999,
  "result": "success",
  "message": "new company registration successfull",
  "company": {
    "companyId": 30,
    "companyName": "Wayne Tech",
    "companyAddress": "LA, US",
    "companyTimeZone": "America/Los_Angeles",
    "companyDateFormat": "MM/DD/YYYY",
    "creationDate": 1504696542000,
    "companyReferer": "test",
    "accountType": "partner-pay",
    "accountStatus": "active",
    "accountOwner": 1147,
    "passwordProtectEnvelopes": false,
    "attachCertificateToDocs": false,
    "defaultSignOption": "TYPE",
    "sendNotificationToOwner": false,
    "sendPDFWithMail": true,
    "defaultFieldNavigation": "ALL",
    "defaultDisplayIndicators": true,
    "allowRecipientsToDelegate": false,
    "allFeatures": [
      "Reports",
      "Digitally Certified Pdf",
      "Upload to Cloud",
      "Attachments"
    ],
    "signatureFont": null,
    "viewOnlyDefaulSignOption": false,
    "customSenderName": null,
    "customSenderEmail": null
  }
}
```


# Change Plan

This endpoint allows you to change the plan type for a specific account.

**Note:** please provide the `access_token` Authorization header from the account which you are looking to change the plan type for.

```python
def change_plan(self,
               new_number_of_licenses,
               new_plan)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `new_number_of_licenses` | `str` | Query, Required | The new required number of licences for the account in the new plan |
| `new_plan` | [`PlanNamesEnum`](../../doc/models/plan-names-enum.md) | Query, Required | Name of plan that you want to subscribe to |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
new_number_of_licenses = '20'

new_plan = PlanNamesEnum.BUSINESS_PREMIUM

result = accounts_api_controller.change_plan(
    new_number_of_licenses,
    new_plan
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response

```
{
  "result": "success",
  "message": "company 32567 plan changed to Business Premium"
}
```


# Cancel Account

This endpoint allows you to cancel a specific account.

`Note:` please provide the `access_token` Authorization header from the account which you are looking to cancel.

```python
def cancel_account(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
result = accounts_api_controller.cancel_account()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response

```
{
  "result": "success",
  "message": "company 32567 cancelled successfully"
}
```


# Reactivate Account

This endpoint allows you to reactivate a specific account.

`Note:` please provide the `access_token` Authorization header from the account which you are looking to reactivate.

```python
def reactivate_account(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
result = accounts_api_controller.reactivate_account()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response

```
{
  "result": "success",
  "message": "company 32567 reactivated successfully"
}
```


# Change Licenses

This endpoint allows you to edit the number of licenses available in a a specific account.

`Note:` please provide the `access_token` Authorization header from the account which you are looking to reactivate.

```python
def change_licenses(self,
                   new_number_of_licences,
                   partner_code)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `new_number_of_licences` | `str` | Query, Required | The new required number of licences for the account |
| `partner_code` | `str` | Query, Required | Enter the unique partner code assigned to the partner to link this account with the specified partner |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
new_number_of_licences = '20'

partner_code = 'partnerCode0'

result = accounts_api_controller.change_licenses(
    new_number_of_licences,
    partner_code
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response

```
{
  "result": "success",
  "message": "company 32567 licence number changed to 3"
}
```

