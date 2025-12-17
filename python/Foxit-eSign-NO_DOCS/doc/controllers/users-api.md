# Users API

```python
users_api_controller = client.users_api
```

## Class Name

`UsersAPIController`

## Methods

* [Create User](../../doc/controllers/users-api.md#create-user)
* [Update User](../../doc/controllers/users-api.md#update-user)
* [Delete User](../../doc/controllers/users-api.md#delete-user)
* [List All Users](../../doc/controllers/users-api.md#list-all-users)


# Create User

This endpoint allows you to create a User in any account by using the API.

```python
def create_user(self,
               user_creation_object)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_creation_object` | [`UserCreationObject`](../../doc/models/user-creation-object.md) | Body, Required | object to create users |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
user_creation_object = UserCreationObject(
    user=UserCreation(
        first_name='eSign',
        last_name='Demo',
        email_id='esigndemo@foxitsoftware.com',
        user_role=UserRolesEnum.ADMIN,
        active=True,
        send_mail_for_password_reset=True,
        allow_advanced_email_validation=True,
        address='Miami, Florida',
        department='DEV',
        title='Tech Lead',
        login_password='TXxgjjezFLAqnR'
    )
)

result = users_api_controller.create_user(user_creation_object)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response

```
{
  "result": "success",
  "message": "new user successfully added",
  "user": {
    "partyId": 54,
    "firstName": "eSign",
    "lastName": "Demo",
    "emailId": "esigndemo@foxitsoftware.com",
    "address": "Miami, Florida",
    "dateCreated": null,
    "companyId": 32567,
    "userRole": "Admin",
    "userAddedDate": null,
    "department": "DEV",
    "title": "Tech Lead",
    "active": true,
    "requestLocale": "auto"
  }
}
```


# Update User

This endpoint allows you to update the User's profile parameters using the API.

```python
def update_user(self,
               user_update_object)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_update_object` | [`UserUpdateObject`](../../doc/models/user-update-object.md) | Body, Required | object to update a user |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
user_update_object = UserUpdateObject(
    user=UserUpdate(
        party_id='54',
        first_name='eSign',
        last_name='Demo',
        user_role=UserRolesEnum.SUPER_ADMIN,
        active=False,
        address='Miami, Florida',
        department='DEV',
        title='Tech Lead'
    )
)

result = users_api_controller.update_user(user_update_object)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete User

This endpoint allows you to delete a user via API.

```python
def delete_user(self,
               user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `str` | Query, Required | Party Id for that user |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
user_id = '54'

result = users_api_controller.delete_user(user_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response

```
{
  "result": "success",
  "message": "user 54 deleted successfully"
}
```


# List All Users

This endpoint allows you to list all of the users under a specific account via API.

```python
def list_all_users(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
result = users_api_controller.list_all_users()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response

```
{
  "usersList": [
    {
      "partyId": 54,
      "firstName": "Steve",
      "lastName": "Rogers",
      "emailId": "abc@gmail.com",
      "address": "New Delhi, India",
      "dateCreated": 1492662823000,
      "companyId": 32567,
      "userRole": "Admin",
      "userAddedDate": 1504778908000,
      "department": "DEV",
      "title": "Tech Lead",
      "active": true,
      "requestLocale": "auto",
      "managerId": null
    },
    {
      "partyId": 123,
      "firstName": "Sandra",
      "lastName": "Smith",
      "emailId": "san_smith@esigngenie.com",
      "address": "East Delhi, India",
      "dateCreated": 1492662823000,
      "companyId": 32567,
      "userRole": "Super-Administrator",
      "userAddedDate": 1504779092000,
      "department": "Testing",
      "title": "Test Lead",
      "active": true,
      "requestLocale": "auto",
      "managerId": null
    },
    {
      "partyId": 456,
      "firstName": "Amanda",
      "lastName": "Williams",
      "emailId": "williams_ama@esigngenie.com",
      "address": "",
      "dateCreated": 1492662824000,
      "companyId": 32567,
      "userRole": "super_admin",
      "userAddedDate": 1504777539000,
      "department": null,
      "title": null,
      "active": true,
      "requestLocale": "auto",
      "managerId": null
    },
    {
      "partyId": 789,
      "firstName": "Hannah",
      "lastName": "Pitt",
      "emailId": "pitthannah@esigngenie.com",
      "address": null,
      "dateCreated": 1492662824000,
      "companyId": 32567,
      "userRole": "super_admin",
      "userAddedDate": 1504785081000,
      "department": "",
      "title": "",
      "active": true,
      "requestLocale": "auto",
      "managerId": null
    }
  ],
  "allActiveUsers": 4,
  "allInactiveUsers": 0
}
```

