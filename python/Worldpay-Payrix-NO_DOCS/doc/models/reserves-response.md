
# Reserves Response

## Structure

`ReservesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `login` | `str` | Optional | The Login that owns this resource. |
| `org` | `str` | Optional | The identifier of the Org that this Reserve's resource applies to. If you set this field, then the Reserve applies to all Entities in the Org. |
| `division` | `str` | Optional | The division on which this reserve applies. |
| `partition` | `str` | Optional | The partition on which this reserve applies. |
| `level` | [`LevelEnum`](../../doc/models/level-enum.md) | Optional | The hierarchical level for this reserve setting.<br><br><details><br><summary>Valid Values</summary><br>- `admin` - **Admin User.**<br>- `division` - **Division-level User.**<br>- `merchant` - **Merchant-level User.**<br>- `partition` - **Partition-level User.**<br></details><br> |
| `entity` | `str` | Optional | The identifier of the Entity that this Reserve applies to. |
| `hold` | `str` | Optional | The entity hold from which this reserve was generated. |
| `name` | `str` | Optional | The name of this Reserve. This field is stored as a text string and must be between 1 and 100 characters long. |
| `description` | `str` | Optional | A description of this Reserve. This field is stored as a text string and must be between 0 and 100 characters long. |
| `percent` | `int` | Optional | The percentage of funds to reserve, expressed in basis points. For example, 25.3% is expressed as '2530'. |
| `release` | [`ReleaseEnum`](../../doc/models/release-enum.md) | Optional | The schedule that determines when the funds in this Reserve should be released, which can have valid values such as never, days, weeks, months, or years.<br><br><details><br><summary>Valid Values</summary><br>- `never` - **Never.**<br>- `days` - **Daily. The funds are released every day.**<br>- `weeks` - **Weekly. The funds are released every week.**<br>- `months` - **Monthly. The funds are released every month.**<br>- `years` - **Annually. The funds are released every year.**<br></details><br> |
| `release_factor` | `int` | Optional | A multiplier that you can use to adjust the schedule set in the 'release' field, which is specified as an integer and its value determines how the schedule is multiplied. |
| `start` | `int` | Optional | The date on which this Reserve resource should start reserving funds from the Entity or Org. The date is specified as an eight digit string in YYYYMMDD format, for example, '20160120' for January 20, 2016. |
| `finish` | `int` | Optional | The date on which this Reserve resource should stop reserving funds from the Entity or Org. The date is specified as an eight digit string in YYYYMMDD format, for example, '20160120' for January 20, 2016. |
| `max` | `int` | Optional | The maximum amount to reserve. |
| `status` | [`Status1Enum`](../../doc/models/status-1-enum.md) | Optional | The status of reserve.<br><br><details><br><summary>Valid Values</summary><br>- `1` - **The reserve is active.**<br>- `2` - **The reserve is under review.**<br>- `3` - **The reserve is inactive.**<br></details><br> |
| `inactive` | [`InactiveEnum`](../../doc/models/inactive-enum.md) | Optional | Whether this resource is marked as inactive.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Active**<br>- `1` - **Inactive**<br></details><br>**Default**: `0`<br> |
| `frozen` | [`FrozenEnum`](../../doc/models/frozen-enum.md) | Optional | Whether this resource is marked as frozen.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not Frozen**<br>- `1` - **Frozen**<br></details><br>**Default**: `0`<br> |

## Example (as JSON)

```json
{
  "inactive": 0,
  "frozen": 0,
  "id": "id0",
  "created": "created0",
  "modified": "modified8",
  "creator": "String9",
  "modifier": "modifier4"
}
```

