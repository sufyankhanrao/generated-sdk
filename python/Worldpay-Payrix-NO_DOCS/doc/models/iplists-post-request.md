
# Iplists Post Request

## Structure

`IplistsPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `login` | `str` | Required | The Login that owns this resource. |
| `version` | [`VersionEnum`](../../doc/models/version-enum.md) | Required | Whether this IP List contains IPv4 addresses (for example, 198.51.100.113) or IPv6 addresses (for example, 2001:0db8:85a3:0000:0000:8a2e:0370:7334).<br><br>You can only use one type in each IP List resource.<br><br><details><br><summary>Valid Values</summary><br>- `4` - **IPv4 addresses.** (Example: 198.51.100.113)<br>- `6` - **IPv6 addresses.** (Example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)<br></details><br>**Default**: `4`<br> |
| `mtype` | [`IplistTypeEnum`](../../doc/models/iplist-type-enum.md) | Required | The type of this IP List.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Blacklisted IP address range.**<br>- `1` - **Whitelisted IP address range.**<br></details><br>**Default**: `0`<br> |
| `start` | `str` | Required | The lowest IP address that should be included in this IP List.<br>The valid data type for this field depends on whether the IP list is set to be an IPv4 or IPv6 list in the 'type' field.<br>For an IPv4 list, only IPv4 addresses such as 198.51.100.113 are permitted. For an IPv6 list, only IPv6 addresses such as 2001:0db8:85a3:0000:0000:8a2e:0370:7334 are permitted. |
| `finish` | `str` | Optional | The highest IP address that should be included in this IP List.<br>The valid values for this field depend on whether the IP list is set to be an IPv4 or IPv6 list in the 'type' field.<br>For an IPv4 list, only IPv4 addresses, such as '198.51.100.113', are permitted. For an IPv6 list, only IPv6 addresses, such as '2001:0db8:85a3:0000:0000:8a2e:0370:7334' are permitted. |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Required | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Required | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "login": "t1_log_61d874fe8b166d56672d0f9",
  "version": 4,
  "type": 1,
  "start": "1.1.1.1",
  "finish": "1.1.1.89",
  "inactive": 0,
  "frozen": 0
}
```

