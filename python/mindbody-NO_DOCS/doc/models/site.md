
# Site

## Structure

`Site`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accepts_american_express` | `bool` | Optional | When `true`, indicates that this site accepts American Express cards.<br /><br>When `false`, indicates that this site does not accept American Express credit cards. |
| `accepts_discover` | `bool` | Optional | When `true`, indicates that this site accepts Discover cards.<br /><br>When `false`, indicates that this site does not accept Discover credit cards. |
| `accepts_master_card` | `bool` | Optional | When `true`, indicates that this site accepts MasterCard cards.<br /><br>When `false`, indicates that this site does not accept MasterCard credit cards. |
| `accepts_visa` | `bool` | Optional | When `true`, indicates that this site accepts Visa cards.<br /><br>When `false`, indicates that this site does not accept Visa credit cards. |
| `allows_dashboard_access` | `bool` | Optional | When `true`, indicates that this site allows access to its dashboard.<br /><br>When `false`, indicates that this site does not allow access to its dashboard. |
| `contact_email` | `str` | Optional | The site’s email address. |
| `description` | `str` | Optional | A description of the site. |
| `id` | `int` | Optional | The site ID. |
| `logo_url` | `str` | Optional | The URL to the site’s logo. |
| `name` | `str` | Optional | The name of the site. |
| `page_color_1` | `str` | Optional | A hex code for a color the business owner uses in marketing. This color can be used to set a theme for an integration so that it matches the configured color-scheme for the business. |
| `page_color_2` | `str` | Optional | The hex code for a second color, to be used in the same manner as `pageColor1`. |
| `page_color_3` | `str` | Optional | The hex code for a third color, to be used in the same manner as `pageColor1`. |
| `page_color_4` | `str` | Optional | The hex code for a fourth color, to be used in the same manner as `pageColor1`. |
| `pricing_level` | `str` | Optional | The MINDBODY pricing level for the business. Possible values are:<br>Accelerate - The business is on MINDBODY’s Accelerate pricing tier.<br>Grow - The business is on MINDBODY’s Essential pricing tier.<br>Legacy - The business is on an older MINDBODY pricing tier that is no longer offered.<br>Listing - The business is on an older MINDBODY pricing tier that is no longer offered.<br>Pro - The business is on an older MINDBODY pricing tier that is no longer offered.<br>Solo - The business is on an older MINDBODY pricing tier that is no longer offered.<br>Ultimate - The business is on MINDBODY’s Ultimate pricing tier. |
| `sms_package_enabled` | `bool` | Optional | When `true`, indicates that the business uses SMS text messages to communicate with its clients.<br /><br>When `false`, indicates that the business does not use SMS text messages to communicate with its clients. |
| `tax_inclusive_prices` | `bool` | Optional | When `true`, indicates that the total includes tax.<br /><br>When `false`, indicates that the total does not include tax. |
| `currency_iso_code` | `str` | Optional | The currency ISO code for the site. |
| `country_code` | `str` | Optional | The country code for the site. |
| `time_zone` | `str` | Optional | The time zone the site is located in. |
| `accepts_direct_debit` | `bool` | Optional | When `true`, indicates that direct debit can be used by clients at this site.<br /><br>When `false`, indicates that direct debit can not by used by clients at this site. |
| `lead_channels` | [`List[LeadChannel]`](../../doc/models/lead-channel.md) | Optional | The list of lead channels available for a subscriber/studio. |

## Example (as JSON)

```json
{
  "AcceptsAmericanExpress": false,
  "AcceptsDiscover": false,
  "AcceptsMasterCard": false,
  "AcceptsVisa": false,
  "AllowsDashboardAccess": false,
  "ContactEmail": null,
  "Description": null,
  "Id": null,
  "LogoUrl": null,
  "Name": null,
  "PageColor1": null,
  "PageColor2": null,
  "PageColor3": null,
  "PageColor4": null,
  "PricingLevel": null,
  "SmsPackageEnabled": null,
  "TaxInclusivePrices": null,
  "CurrencyIsoCode": null,
  "CountryCode": null,
  "TimeZone": null,
  "AcceptsDirectDebit": null,
  "LeadChannels": [
    {
      "UniversalCustomerId": "00000000-0000-0000-0000-000000000000"
    }
  ]
}
```

