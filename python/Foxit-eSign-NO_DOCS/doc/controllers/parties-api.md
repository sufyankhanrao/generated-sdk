# Parties API

```python
parties_api_controller = client.parties_api
```

## Class Name

`PartiesAPIController`

## Methods

* [Create Email Group](../../doc/controllers/parties-api.md#create-email-group)
* [Get Email Group Details](../../doc/controllers/parties-api.md#get-email-group-details)


# Create Email Group

To create a new email group via API, please make a call to parties/createEmailGroup with the following parameters.

You can only pass up to 20 party details.

```python
def create_email_group(self,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `Any` | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
body = jsonpickle.decode('{"emailGroupName":"Email_Group_Name","emailGroupDescription":"Email_Group_Description","allowAdvancedEmailValidation":true,"parties":[{"firstName":"Sandra","lastName":"Smith","emailId":"san_smith@esigngenie.com"},{"firstName":"Hannah","lastName":"Pitt","emailId":"pitthannah@esigngenie.com"}]}')

result = parties_api_controller.create_email_group(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response

```
{
  "result": "success",
  "message": "new email group successfully added",
  "emailGroup": {
    "groupId": 230,
    "groupName": "Email_Group_Name",
    "groupDesc": "Email_Group_Description",
    "dateCreated": 1561549235000,
    "companyId": 11,
    "parties": [
      {
        "firstName": "Sandra",
        "lastName": "Smith",
        "emailId": "san_smith@esigngenie.com"
      },
      {
        "firstName": "Hannah",
        "lastName": "Pitt",
        "emailId": "pitthannah@esigngenie.com"
      }
    ]
  }
}
```


# Get Email Group Details

You can pool our API to get email group information.

You can pass this request with no parameters to get the details of all of the email groups in your account.

```python
def get_email_group_details(self,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`EmailGroupIdentifiers`](../../doc/models/email-group-identifiers.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
body = EmailGroupIdentifiers(
    email_group_names=[
        'Email_Group_1',
        'Email_Group_2'
    ]
)

result = parties_api_controller.get_email_group_details(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response

```
{
  "allEmailGroups": [
    {
      "groupId": 1,
      "groupName": "Email_Group_1",
      "groupDesc": "",
      "dateCreated": 1512677389000,
      "companyId": 11,
      "parties": [
        {
          "firstName": "Amanda",
          "lastName": "Williams",
          "emailId": "williams_ama@esigngenie.com"
        },
        {
          "firstName": "Hannah",
          "lastName": "Pitt",
          "emailId": "pitthannah@esigngenie.com"
        },
        ".."
      ]
    },
    {
      "groupId": 176,
      "groupName": "Email_Group_2",
      "groupDesc": "Email_Group_Description",
      "dateCreated": 1425120364000,
      "companyId": 11,
      "parties": [
        {
          "firstName": "Sandra",
          "lastName": "Smith",
          "emailId": "san_smith@esigngenie.com"
        },
        {
          "firstName": "Bruce",
          "lastName": "Wayne",
          "emailId": "bruce.wayne_as@esigngenie.com"
        },
        {
          "firstName": "Amanda",
          "lastName": "Williams",
          "emailId": "williams_ama@esigngenie.com"
        }
      ]
    }
  ]
}
```

