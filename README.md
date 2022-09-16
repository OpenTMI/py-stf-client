# stf-client
Control and manages real Smartphone devices from browser and restful apis

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.4.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [http://openstf.io/](http://openstf.io/)

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import stf_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import stf_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import stf_client
from pprint import pprint
from stf_client.api import admin_api
from stf_client.model.device_list_response import DeviceListResponse
from stf_client.model.device_payload import DevicePayload
from stf_client.model.device_response import DeviceResponse
from stf_client.model.devices_payload import DevicesPayload
from stf_client.model.group_list_response import GroupListResponse
from stf_client.model.remote_connect_user_device_response import RemoteConnectUserDeviceResponse
from stf_client.model.response import Response
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.user_access_token_response import UserAccessTokenResponse
from stf_client.model.user_access_tokens_response import UserAccessTokensResponse
from stf_client.model.user_response import UserResponse
from stf_client.model.users_payload import UsersPayload
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stf_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accessTokenAuth
configuration.api_key['accessTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with stf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)
    serial = "serial_example" # str | Device identifier (serial)
    id = "id_example" # str | Group identifier

    try:
        # Adds a device into an origin group
        api_response = api_instance.add_origin_group_device(serial, id)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->add_origin_group_device: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminApi* | [**add_origin_group_device**](docs/AdminApi.md#add_origin_group_device) | **PUT** /devices/{serial}/groups/{id} | Adds a device into an origin group
*AdminApi* | [**add_origin_group_devices**](docs/AdminApi.md#add_origin_group_devices) | **PUT** /devices/groups/{id} | Adds devices into an origin group
*AdminApi* | [**add_user_device_v3**](docs/AdminApi.md#add_user_device_v3) | **POST** /users/{email}/devices/{serial} | Places a device under user control
*AdminApi* | [**create_user**](docs/AdminApi.md#create_user) | **POST** /users/{email} | Creates a user
*AdminApi* | [**create_user_access_token**](docs/AdminApi.md#create_user_access_token) | **POST** /users/{email}/accessTokens | Create an access token for a user
*AdminApi* | [**delete_device**](docs/AdminApi.md#delete_device) | **DELETE** /devices/{serial} | Removes a device
*AdminApi* | [**delete_devices**](docs/AdminApi.md#delete_devices) | **DELETE** /devices | Removes devices
*AdminApi* | [**delete_user**](docs/AdminApi.md#delete_user) | **DELETE** /users/{email} | Removes a user
*AdminApi* | [**delete_user_access_token**](docs/AdminApi.md#delete_user_access_token) | **DELETE** /users/{email}/accessTokens/{id} | Removes an access token of a user
*AdminApi* | [**delete_user_access_tokens**](docs/AdminApi.md#delete_user_access_tokens) | **DELETE** /users/{email}/accessTokens | Remove the access tokens of a user
*AdminApi* | [**delete_user_device**](docs/AdminApi.md#delete_user_device) | **DELETE** /users/{email}/devices/{serial} | Remove a device from the user control
*AdminApi* | [**delete_users**](docs/AdminApi.md#delete_users) | **DELETE** /users | Removes users
*AdminApi* | [**get_device_groups**](docs/AdminApi.md#get_device_groups) | **GET** /devices/{serial}/groups | Gets the groups to which the device belongs
*AdminApi* | [**get_user_access_token**](docs/AdminApi.md#get_user_access_token) | **GET** /users/{email}/accessTokens/{id} | Gets an access token of a user
*AdminApi* | [**get_user_access_tokens_v2**](docs/AdminApi.md#get_user_access_tokens_v2) | **GET** /users/{email}/accessTokens | Gets the access tokens of a user
*AdminApi* | [**get_user_device**](docs/AdminApi.md#get_user_device) | **GET** /users/{email}/devices/{serial} | Gets a device controlled by a user
*AdminApi* | [**get_user_devices_v2**](docs/AdminApi.md#get_user_devices_v2) | **GET** /users/{email}/devices | Gets the devices controlled by a user
*AdminApi* | [**put_device_by_serial**](docs/AdminApi.md#put_device_by_serial) | **PUT** /devices/{serial} | Adds device informatin
*AdminApi* | [**remote_connect_user_device**](docs/AdminApi.md#remote_connect_user_device) | **POST** /users/{email}/devices/{serial}/remoteConnect | Allows to remotely connect to a device controlled by a user
*AdminApi* | [**remote_disconnect_user_device**](docs/AdminApi.md#remote_disconnect_user_device) | **DELETE** /users/{email}/devices/{serial}/remoteConnect | Forbids to remotely connect to a device controlled by a user
*AdminApi* | [**remove_origin_group_device**](docs/AdminApi.md#remove_origin_group_device) | **DELETE** /devices/{serial}/groups/{id} | Removes a device from an origin group
*AdminApi* | [**remove_origin_group_devices**](docs/AdminApi.md#remove_origin_group_devices) | **DELETE** /devices/groups/{id} | Removes devices from an origin group
*AdminApi* | [**update_default_user_groups_quotas**](docs/AdminApi.md#update_default_user_groups_quotas) | **PUT** /users/groupsQuotas | Updates the default groups quotas of users
*AdminApi* | [**update_user_groups_quotas**](docs/AdminApi.md#update_user_groups_quotas) | **PUT** /users/{email}/groupsQuotas | Updates the groups quotas of a user
*DevicesApi* | [**get_device_bookings**](docs/DevicesApi.md#get_device_bookings) | **GET** /devices/{serial}/bookings | Gets the bookings to which the device belongs
*DevicesApi* | [**get_device_by_serial**](docs/DevicesApi.md#get_device_by_serial) | **GET** /devices/{serial} | Device Information
*DevicesApi* | [**get_devices**](docs/DevicesApi.md#get_devices) | **GET** /devices | Device List
*GroupsApi* | [**add_group_device**](docs/GroupsApi.md#add_group_device) | **PUT** /groups/{id}/devices/{serial} | Adds a device into a transient group
*GroupsApi* | [**add_group_devices**](docs/GroupsApi.md#add_group_devices) | **PUT** /groups/{id}/devices | Adds devices into a transient group
*GroupsApi* | [**add_group_user**](docs/GroupsApi.md#add_group_user) | **PUT** /groups/{id}/users/{email} | Adds a user into a group
*GroupsApi* | [**add_group_users**](docs/GroupsApi.md#add_group_users) | **PUT** /groups/{id}/users | Adds users into a group
*GroupsApi* | [**create_group**](docs/GroupsApi.md#create_group) | **POST** /groups | Creates a group
*GroupsApi* | [**delete_group**](docs/GroupsApi.md#delete_group) | **DELETE** /groups/{id} | Removes a group
*GroupsApi* | [**delete_groups**](docs/GroupsApi.md#delete_groups) | **DELETE** /groups | Removes groups
*GroupsApi* | [**get_group**](docs/GroupsApi.md#get_group) | **GET** /groups/{id} | Gets a group
*GroupsApi* | [**get_group_device**](docs/GroupsApi.md#get_group_device) | **GET** /groups/{id}/devices/{serial} | Gets a device of a group
*GroupsApi* | [**get_group_devices**](docs/GroupsApi.md#get_group_devices) | **GET** /groups/{id}/devices | Gets the devices of a group
*GroupsApi* | [**get_group_user**](docs/GroupsApi.md#get_group_user) | **GET** /groups/{id}/users/{email} | Gets a user of a group
*GroupsApi* | [**get_group_users**](docs/GroupsApi.md#get_group_users) | **GET** /groups/{id}/users | Gets the users of a group
*GroupsApi* | [**get_groups**](docs/GroupsApi.md#get_groups) | **GET** /groups | Gets groups
*GroupsApi* | [**remove_group_device**](docs/GroupsApi.md#remove_group_device) | **DELETE** /groups/{id}/devices/{serial} | Removes a device from a transient group
*GroupsApi* | [**remove_group_devices**](docs/GroupsApi.md#remove_group_devices) | **DELETE** /groups/{id}/devices | Removes devices from a transient group
*GroupsApi* | [**remove_group_user**](docs/GroupsApi.md#remove_group_user) | **DELETE** /groups/{id}/users/{email} | Removes a user from a group
*GroupsApi* | [**remove_group_users**](docs/GroupsApi.md#remove_group_users) | **DELETE** /groups/{id}/users | Removes users from a group
*GroupsApi* | [**update_group**](docs/GroupsApi.md#update_group) | **PUT** /groups/{id} | Updates a group
*UserApi* | [**add_adb_public_key**](docs/UserApi.md#add_adb_public_key) | **POST** /user/adbPublicKeys | Adb public keys
*UserApi* | [**add_user_device**](docs/UserApi.md#add_user_device) | **POST** /user/devices | Add a device to a user
*UserApi* | [**add_user_device_v2**](docs/UserApi.md#add_user_device_v2) | **POST** /user/devices/{serial} | Places a device under user control
*UserApi* | [**create_access_token**](docs/UserApi.md#create_access_token) | **POST** /user/accessTokens | Create an access token
*UserApi* | [**delete_access_token**](docs/UserApi.md#delete_access_token) | **DELETE** /user/accessTokens/{id} | Removes an access token
*UserApi* | [**delete_access_tokens**](docs/UserApi.md#delete_access_tokens) | **DELETE** /user/accessTokens | Removes your access tokens
*UserApi* | [**delete_user_device_by_serial**](docs/UserApi.md#delete_user_device_by_serial) | **DELETE** /user/devices/{serial} | Delete User Device
*UserApi* | [**get_access_token**](docs/UserApi.md#get_access_token) | **GET** /user/accessTokens/{id} | Gets an access token
*UserApi* | [**get_access_tokens**](docs/UserApi.md#get_access_tokens) | **GET** /user/fullAccessTokens | Gets your access tokens
*UserApi* | [**get_user**](docs/UserApi.md#get_user) | **GET** /user | User Profile
*UserApi* | [**get_user_access_tokens**](docs/UserApi.md#get_user_access_tokens) | **GET** /user/accessTokens | Access Tokens
*UserApi* | [**get_user_device_by_serial**](docs/UserApi.md#get_user_device_by_serial) | **GET** /user/devices/{serial} | User Device
*UserApi* | [**get_user_devices**](docs/UserApi.md#get_user_devices) | **GET** /user/devices | User Devices
*UserApi* | [**remote_connect_user_device_by_serial**](docs/UserApi.md#remote_connect_user_device_by_serial) | **POST** /user/devices/{serial}/remoteConnect | Remote Connect
*UserApi* | [**remote_disconnect_user_device_by_serial**](docs/UserApi.md#remote_disconnect_user_device_by_serial) | **DELETE** /user/devices/{serial}/remoteConnect | Remote Disconnect
*UsersApi* | [**get_user_by_email**](docs/UsersApi.md#get_user_by_email) | **GET** /users/{email} | Gets a user
*UsersApi* | [**get_users**](docs/UsersApi.md#get_users) | **GET** /users | Gets users


## Documentation For Models

 - [AccessTokensResponse](docs/AccessTokensResponse.md)
 - [AddAdbPublicKeyRequest](docs/AddAdbPublicKeyRequest.md)
 - [AddUserDevicePayload](docs/AddUserDevicePayload.md)
 - [Conflict](docs/Conflict.md)
 - [ConflictDate](docs/ConflictDate.md)
 - [ConflictOwner](docs/ConflictOwner.md)
 - [ConflictsResponse](docs/ConflictsResponse.md)
 - [DeviceListResponse](docs/DeviceListResponse.md)
 - [DevicePayload](docs/DevicePayload.md)
 - [DeviceResponse](docs/DeviceResponse.md)
 - [DevicesPayload](docs/DevicesPayload.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [GroupListResponse](docs/GroupListResponse.md)
 - [GroupPayload](docs/GroupPayload.md)
 - [GroupResponse](docs/GroupResponse.md)
 - [GroupsPayload](docs/GroupsPayload.md)
 - [RemoteConnectUserDeviceResponse](docs/RemoteConnectUserDeviceResponse.md)
 - [Response](docs/Response.md)
 - [Token](docs/Token.md)
 - [UnexpectedErrorResponse](docs/UnexpectedErrorResponse.md)
 - [UserAccessTokenResponse](docs/UserAccessTokenResponse.md)
 - [UserAccessTokensResponse](docs/UserAccessTokensResponse.md)
 - [UserListResponse](docs/UserListResponse.md)
 - [UserResponse](docs/UserResponse.md)
 - [UsersPayload](docs/UsersPayload.md)


## Documentation For Authorization


## accessTokenAuth

- **Type**: API key
- **API key parameter name**: authorization
- **Location**: HTTP header


## Author

contact@openstf.io


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in stf_client.apis and stf_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from stf_client.api.default_api import DefaultApi`
- `from stf_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import stf_client
from stf_client.apis import *
from stf_client.models import *
```

