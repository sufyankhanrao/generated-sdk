# GOE

Find out more here: [content/API-overview.md](content/API-overview.md)

```python
goe_api = client.goe
```

## Class Name

`GoeApi`

## Methods

* [Run Pipe](../../doc/controllers/goe.md#run-pipe)
* [Unified Portfolio Advice](../../doc/controllers/goe.md#unified-portfolio-advice)
* [Initial Wealth Splitter](../../doc/controllers/goe.md#initial-wealth-splitter)
* [Goal Discovery](../../doc/controllers/goe.md#goal-discovery)
* [Goal Discovery Paginated Results](../../doc/controllers/goe.md#goal-discovery-paginated-results)
* [Goe for Decumulation](../../doc/controllers/goe.md#goe-for-decumulation)
* [GOE Simulation Engine](../../doc/controllers/goe.md#goe-simulation-engine)
* [Goal Calculator](../../doc/controllers/goe.md#goal-calculator)
* [GOE for Taxes](../../doc/controllers/goe.md#goe-for-taxes)
* [Goe With Annuities](../../doc/controllers/goe.md#goe-with-annuities)


# Run Pipe

```python
def run_pipe(self,
            body,
            version='4')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`RunPipeInputModel`](../../doc/models/run-pipe-input-model.md) | Body, Required | - |
| `version` | `str` | Header, Optional | **Default**: `'4'` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`RunPipeResponseModelV4`](../../doc/models/run-pipe-response-model-v4.md).

## Example Usage

```python
body = RunPipeInputModel(
    is_new_goal_priority=True,
    is_new_investment_tenure=True,
    is_new_risk_profile=True,
    is_new_goal=True,
    get_path=True,
    reallocation_freq=ReallocationFreq.YEARLY,
    goal_amount=1000000,
    initial_investment=95027,
    current_wealth=95027,
    start_date='13-01-2021',
    end_date='10-10-2055',
    goal_priority=GoalPriority.NEED,
    current_portfolio_id=None,
    infusions=[
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
    ],
    risk_profile=RiskProfile6.MODERATE,
    scenario_type=ScenarioType1.REGULAR,
    infusion_type=InfusionType.YEARLY,
    cashflow_date='11-10-2020',
    curr_date='13-01-2021',
    use_age_based_cap=False,
    additional_properties={
        'lastReallocatedDate': jsonpickle.decode('"01-01-2020"'),
        'isNearTermVolatility': jsonpickle.decode('true'),
        'calibrateRecommendations': jsonpickle.decode('true')
    }
)

version = '4'

result = goe_api.run_pipe(
    body,
    version=version
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`MessageException`](../../doc/models/message-exception.md) |
| 404 | Not Found | [`ValidationMessageOneException`](../../doc/models/validation-message-one-exception.md) |
| 500 | Internal Server Error | [`InternalServerMessageException`](../../doc/models/internal-server-message-exception.md) |


# Unified Portfolio Advice

```python
def unified_portfolio_advice(self,
                            body,
                            detailed_response=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`UnifiedPortfolioAdviceInputModelV4`](../../doc/models/unified-portfolio-advice-input-model-v4.md) | Body, Required | - |
| `detailed_response` | `str` | Header, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UpAv4ResponseModel`](../../doc/models/up-av-4-response-model.md).

## Example Usage

```python
body = UnifiedPortfolioAdviceInputModelV4(
    is_new_goal_priority=True,
    is_new_risk_profile=True,
    is_new_investment_tenure=True,
    is_new_goal=True,
    get_path=True,
    reallocation_freq=ReallocationFreq5.YEARLY,
    initial_investment=86000,
    current_wealth=None,
    current_portfolio_id=None,
    infusions=[
        0,
        4000,
        4000,
        4000,
        4000,
        4000,
        4000,
        4000,
        4000,
        4000,
        -21000,
        -19000,
        -75000,
        -23000,
        -23000,
        -23000
    ],
    risk_profile=RiskProfile7.AGGRESSIVE,
    infusion_type='yearly',
    goal_profile_list=[
        GoalProfile(
            goal_id='Goal1',
            goal_amt=[
                25000
            ],
            start_date='01-01-2021',
            end_date='01-01-2031',
            priority='Need',
            scenario_type='regular'
        ),
        GoalProfile(
            goal_id='Goal2',
            goal_amt=[
                52000
            ],
            start_date='01-01-2021',
            end_date='01-01-2033',
            priority='Need',
            scenario_type='regular'
        ),
        GoalProfile(
            goal_id='Goal3',
            goal_amt=[
                2000,
                2000,
                2000,
                2000,
                2000,
                2000,
                2000,
                2000,
                2000,
                2000,
                2000,
                2000,
                2000,
                2000,
                2000
            ],
            start_date='01-01-2022',
            end_date='01-01-2036',
            priority='Need',
            scenario_type='retirement'
        ),
        GoalProfile(
            goal_id='Goal4',
            goal_amt=[
                21000,
                21000,
                21000,
                21000,
                21000
            ],
            start_date='01-01-2032',
            end_date='01-01-2036',
            priority='Need',
            scenario_type='retirement'
        )
    ],
    is_near_term_volatility=False,
    cashflow_date='01-01-2021',
    curr_date='04-01-2021',
    additional_properties={
        'calibrateGoalRec': jsonpickle.decode('true')
    }
)

result = goe_api.unified_portfolio_advice(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ValidationMessageOneException`](../../doc/models/validation-message-one-exception.md) |
| 404 | Not Found | [`MessageException`](../../doc/models/message-exception.md) |
| 500 | Internal Server Error | [`InternalServerMessageException`](../../doc/models/internal-server-message-exception.md) |


# Initial Wealth Splitter

```python
def initial_wealth_splitter(self,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`WealthSplitterInputModel`](../../doc/models/wealth-splitter-input-model.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`WealthSplitterOutputModel`](../../doc/models/wealth-splitter-output-model.md).

## Example Usage

```python
body = WealthSplitterInputModel(
    start_date='1-01-2020',
    risk_profile=RiskProfile8.CONSERVATIVE,
    goal_profile_list=[
        GoalProfileListWealthSplitterModel(
            goal_id='Goal_1',
            goal_value=1000000,
            purpose='Saving',
            curr_wealth=141412,
            goal_priority=WeathSplitterGoalPriorityAttribute.NEED,
            cashflow_type='monthly',
            cashflow=[
                0,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                400,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                -15000,
                0
            ],
            end_date='10-10-2080',
            scenario_type='retirement',
            cashflow_date='15-06-2020',
            loss_threshold=None,
            additional_properties={
                'goal_priority_prob': jsonpickle.decode('0.85')
            }
        ),
        GoalProfileListWealthSplitterModel(
            goal_id='Goal_2',
            goal_value=1000000,
            purpose='Fixed',
            curr_wealth=897494,
            goal_priority=WeathSplitterGoalPriorityAttribute.DREAM,
            cashflow_type='yearly',
            cashflow=[
                0,
                4000,
                -30000,
                0
            ],
            end_date='10-10-2023',
            scenario_type='retirement',
            cashflow_date='11-10-2020',
            loss_threshold=None,
            additional_properties={
                'goal_priority_prob': jsonpickle.decode('0.5')
            }
        )
    ],
    curr_date='13-01-2021'
)

result = goe_api.initial_wealth_splitter(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ValidationMessageOneException`](../../doc/models/validation-message-one-exception.md) |
| 404 | Not Found | [`MessageException`](../../doc/models/message-exception.md) |
| 500 | Internal Server Error | [`InternalServerMessageException`](../../doc/models/internal-server-message-exception.md) |


# Goal Discovery

```python
def goal_discovery(self,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GoalDiscoveryInputModel`](../../doc/models/goal-discovery-input-model.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GoalDiscoveryOutputModel`](../../doc/models/goal-discovery-output-model.md).

## Example Usage

```python
body = GoalDiscoveryInputModel(
    goal_type=GoalType.RETIREMENT,
    risk_profile=RiskProfile1.MODERATE,
    initial_investment=InitialInvestment2(
        min=100000,
        max=77.92
    ),
    goal_priority=[
        GoalDiscoveryGoalPriorityAttribute.NEED
    ],
    infusion_type=InfusionType1.YEARLY,
    infusions=Infusions2(
        min=102,
        max=20
    ),
    goal_tenure=GoalTenure2(
        min=120,
        max=38
    ),
    target_wealth=TargetWealth2(
        min=100000,
        max=35.54
    ),
    page_size=12000
)

result = goe_api.goal_discovery(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ValidationMessageOneException`](../../doc/models/validation-message-one-exception.md) |
| 404 | Not Found | [`MessageException`](../../doc/models/message-exception.md) |
| 500 | Internal Server Error | [`InternalServerMessageException`](../../doc/models/internal-server-message-exception.md) |


# Goal Discovery Paginated Results

```python
def goal_discovery_paginated_results(self,
                                    request_id,
                                    page_index=500)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Query, Required | - |
| `page_index` | `int` | Query, Optional | **Default**: `500` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GoalDiscoveryOutputModel`](../../doc/models/goal-discovery-output-model.md).

## Example Usage

```python
request_id = 'requestId2'

page_index = 500

result = goe_api.goal_discovery_paginated_results(
    request_id,
    page_index=page_index
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ValidationMessageOneException`](../../doc/models/validation-message-one-exception.md) |
| 500 | Internal Server Error | [`InternalServerMessageException`](../../doc/models/internal-server-message-exception.md) |


# Goe for Decumulation

```python
def goe_for_decumulation(self,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GoeForDecumulationInputModel`](../../doc/models/goe-for-decumulation-input-model.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DecumulationResponseModel`](../../doc/models/decumulation-response-model.md).

## Example Usage

```python
body = GoeForDecumulationInputModel(
    future_annuity_proj=True,
    risk_profile=RiskProfile.AGGRESSIVE,
    current_portfolio_id=None,
    date_of_birth='15-06-2020',
    db_income=[
        1000,
        1000,
        1000,
        1000,
        1000,
        1000
    ],
    other_guaranteed_income=[
        1000,
        1000,
        1000,
        1000,
        1000,
        1000
    ],
    existing_annuities_income=[
        1000,
        1000,
        1000,
        1000,
        1000,
        1000
    ],
    state_income=[
        1000,
        1000,
        1000,
        1000,
        1000,
        1000
    ],
    target_expenditures=[
        20400,
        20808,
        21224.2,
        21648.7,
        22081.7
    ],
    fixed_expense_fact=[
        158.68,
        158.69
    ],
    current_wealth=10000,
    initial_investment=100000,
    include_annuities=True,
    infusion_type=InfusionType.YEARLY,
    start_date='01-01-2023',
    end_date='01-01-2052',
    annuity_rate=0.0865,
    reallocation_freq=ReallocationFreq1.YEARLY,
    is_new_goal_priority=True,
    is_new_risk_profile=True,
    is_new_investment_tenure=True,
    is_new_goal=True,
    loss_threshold=100000,
    gender='unisex',
    health_status=0,
    cashflow_date='01-01-2024',
    retirement_age=65,
    reallocate=False
)

result = goe_api.goe_for_decumulation(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "statusCode": 200,
  "message": "Success",
  "body": {
    "wealthPath": [
      89716,
      91018,
      78018,
      64508,
      51157,
      37804,
      23502,
      7865,
      9
    ],
    "riskThreshold": "High",
    "goalProbability": 0.3448,
    "currentGoalProbability": 0.2947,
    "allocationAnnuity": 0,
    "allocationGOE": 89716,
    "goalProbabilityLongevityAdjusted": 0.6138,
    "payoutGOE": [
      10284,
      13000,
      13510,
      14030.2,
      14560.8,
      15102,
      15654,
      7865,
      9
    ],
    "recommendedPortfolioId": 11,
    "fundedness": "UnderFunded",
    "guaranteedIncomePercent": 0.5,
    "isGoalRealistic": false,
    "bankruptcyMessage": "NA",
    "additionalPayoutAnnuity": 0,
    "portfolioPath": [
      11,
      11,
      11,
      11,
      11,
      11,
      11,
      8
    ],
    "payoutAnnuity": [
      1000,
      1000,
      1000,
      1000,
      1000,
      1000,
      1000,
      1000,
      1000
    ],
    "consumptionGoal": [
      12500,
      13000,
      13510,
      14030.2,
      14560.8,
      15102,
      15654,
      16217.1,
      16791.4
    ],
    "recommendedConsumption": [
      22784,
      25500,
      26010,
      26530.2,
      27060.8,
      27602,
      28154,
      20365,
      12509
    ]
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ValidationMessageOneException`](../../doc/models/validation-message-one-exception.md) |
| 404 | Not Found | [`MessageException`](../../doc/models/message-exception.md) |
| 500 | Internal Server Error | [`InternalServerMessageException`](../../doc/models/internal-server-message-exception.md) |


# GOE Simulation Engine

```python
def goe_simulation_engine(self,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GoeSimulationEngineInputModel`](../../doc/models/goe-simulation-engine-input-model.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GoeSimulationEngineOutputModel`](../../doc/models/goe-simulation-engine-output-model.md).

## Example Usage

```python
body = GoeSimulationEngineInputModel(
    reallocation_freq=ReallocationFreq.YEARLY,
    current_portfolio_id=None,
    risk_profile=RiskProfile4.AGGRESSIVE,
    compute_social_security=True,
    use_social_security_for_goals=True,
    is_new_risk_profile=True,
    infusion_type=InfusionType3.YEARLY,
    cola_rate=0.02,
    tax_rates=TaxRates2(
        ltcg_pre_retirement=0.15,
        ltcg_post_retirement=0.15,
        etr_pre_retirement=0.15,
        etr_post_retirement=0.15
    ),
    household=Household2(
        household_id='house_1',
        member_list=[
            Member(
                member_type=MemberType1.PRIMARY,
                member_id='1234',
                dob='12-1968',
                current_age=55,
                retirement_age=65,
                current_salary=50000,
                social_security_start_age=62,
                existing_monthly_social_security_amount=1000,
                tda_balance_for_rmd=10000,
                rmd_utilized=2000
            )
        ],
        state_of_residence='CA'
    ),
    accounts=[
        Account(
            account_id='5',
            account_type='401k',
            taxability_type='T',
            member_i_ds=[
                'memberIDs0'
            ],
            current_balance=14589,
            current_holdings=[
                Category(
                    category_name='CASH',
                    category_id='10',
                    category_price=1,
                    quantity=200000,
                    cost_basis=14589
                )
            ],
            cashflow_details=CashflowDetails2(
                start_date='01-03-2024',
                end_date='01-11-2032',
                cashflow_amt=[
                    2500,
                    2575
                ]
            )
        )
    ],
    goal_profile_list=[
        GoalProfileSimulationEngine(
            goal_id='Goal1',
            start_date='01-12-2059',
            end_date='01-12-2067',
            priority='Need',
            goal_purpose='Non-education',
            goal_amt=[
                2215916.68281757,
                2282394.1833021,
                2350866.00880116,
                2421391.9890652,
                2494033.74873716,
                2568854.76119927,
                2645920.40403525,
                2725298.01615631,
                2807056.95664099,
                2891268.66534022
            ],
            scenario_type='retirement',
            additional_properties={
                'bequest': jsonpickle.decode('false')
            }
        ),
        GoalProfileSimulationEngine(
            goal_id='Goal2',
            start_date='01-01-2023',
            end_date='01-01-2025',
            priority='Want',
            goal_purpose='Non-education',
            goal_amt=[
                10600
            ],
            scenario_type='regular',
            additional_properties={
                'bequest': jsonpickle.decode('false')
            }
        ),
        GoalProfileSimulationEngine(
            goal_id='Goal3',
            start_date='01-01-2023',
            end_date='01-01-2028',
            priority='Want',
            goal_purpose='Non-education',
            goal_amt=[
                31907.039
            ],
            scenario_type='regular',
            additional_properties={
                'bequest': jsonpickle.decode('false')
            }
        ),
        GoalProfileSimulationEngine(
            goal_id='Goal4',
            start_date='01-01-2023',
            end_date='02-04-2025',
            priority='Dream',
            goal_purpose='Non-education',
            goal_amt=[
                5061.361
            ],
            scenario_type='regular',
            additional_properties={
                'bequest': jsonpickle.decode('false')
            }
        ),
        GoalProfileSimulationEngine(
            goal_id='Goal5',
            start_date='01-01-2023',
            end_date='02-01-2048',
            priority='Dream',
            goal_purpose='Non-education',
            goal_amt=[
                407057.448
            ],
            scenario_type='regular',
            additional_properties={
                'bequest': jsonpickle.decode('false')
            }
        ),
        GoalProfileSimulationEngine(
            goal_id='Goal6',
            start_date='01-01-2023',
            end_date='06-02-2024',
            priority='Want',
            goal_purpose='Non-education',
            goal_amt=[
                5024.45469099256
            ],
            scenario_type='regular',
            additional_properties={
                'bequest': jsonpickle.decode('false')
            }
        )
    ],
    reallocate=False,
    is_new_goal_priority=False,
    curr_date='01-01-2023',
    cashflow_date='01-01-2023;',
    is_new_investment_tenure=False,
    is_new_goal=False
)

result = goe_api.goe_simulation_engine(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | [`MessageException`](../../doc/models/message-exception.md) |
| 500 | Internal Server Error | [`InternalServerMessageGeneralException`](../../doc/models/internal-server-message-general-exception.md) |


# Goal Calculator

```python
def goal_calculator(self,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GoalCalculatorInputModel`](../../doc/models/goal-calculator-input-model.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GoalCalculatorOutputModel`](../../doc/models/goal-calculator-output-model.md).

## Example Usage

```python
body = GoalCalculatorInputModel(
    is_new_goal=True,
    is_new_risk_profile=True,
    is_new_investment_tenure=True,
    is_new_goal_priority=True,
    reallocation_freq=ReallocationFreq.YEARLY,
    get_path=True,
    current_portfolio_id=None,
    loss_threshold=None,
    scenario_type=ScenarioType.REGULAR,
    risk_profile=RiskProfile.AGGRESSIVE,
    initial_investment=100000,
    current_wealth=100000,
    goal_priority=GoalCalculatorGoalPriorityAttribute.NEED,
    goal_amount=0,
    start_date='19-09-2023',
    end_date='01-11-2032',
    infusion_type=InfusionType.YEARLY,
    infusions=[
        0,
        5000,
        5000,
        5000,
        5000,
        5000,
        5000,
        5000,
        5000,
        5000,
        0
    ],
    reallocate=False,
    use_age_based_cap=False,
    curr_date='19-09-2023',
    calibrate_recommendations=True,
    stepup_date='01-01-2024',
    inflation=0
)

result = goe_api.goal_calculator(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ValidationMessageOneException`](../../doc/models/validation-message-one-exception.md) |
| 404 | Not Found | [`MessageException`](../../doc/models/message-exception.md) |
| 500 | Internal Server Error | [`InternalServerMessageException`](../../doc/models/internal-server-message-exception.md) |


# GOE for Taxes

```python
def goe_for_taxes(self,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GoeForTaxesInputModel`](../../doc/models/goe-for-taxes-input-model.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GoeForTaxesOutputModel`](../../doc/models/goe-for-taxes-output-model.md).

## Example Usage

```python
body = GoeForTaxesInputModel(
    is_new_risk_profile=False,
    is_new_investment_tenure=False,
    is_new_goal_priority=False,
    is_new_goal=False,
    get_path=True,
    reallocation_freq=ReallocationFreq.YEARLY,
    current_portfolio_id=None,
    risk_profile=RiskProfile3.AGGRESSIVE,
    compute_social_security=False,
    use_social_security_for_goals=True,
    infusion_type=InfusionType3.YEARLY,
    cola_rate=0.03,
    tax_rates=TaxRatesDic2(
        ltcg_pre_retirement=0.15,
        ltcg_post_retirement=0.1,
        etr_pre_retirement=0.15,
        etr_post_retirement=0.2
    ),
    household=HouseholdGoeForTaxesObj2(
        household_id='1',
        member_list=[
            MemberGoeForTaxesObj(
                member_type=MemberType.PRIMARY,
                member_id='eff63fdb-1ed8-41be-a0f8-7788fdac728c',
                dob='02-1959',
                current_age=66,
                retirement_age=93,
                current_salary=400,
                social_security_start_age=65,
                existing_monthly_social_security_amount=10,
                additional_properties={
                    'lifeExpectancy': jsonpickle.decode('93')
                }
            )
        ],
        state_of_residence='KS'
    ),
    accounts=[
        GoeToAccountAttr(
            account_id='dbcd5e3d-55fb-45f6-a654-d720f056a071',
            account_type='IRA',
            taxability_type='D',
            member_i_ds=[
                'eff63fdb-1ed8-41be-a0f8-7788fdac728c'
            ],
            current_balance=2,
            current_holdings=[
                GoeToCategory(
                    category_name='CASH',
                    category_id='10',
                    category_price=1,
                    quantity=2,
                    cost_basis=2
                )
            ],
            cashflow_details=GoeToCashflowDetails2(
                start_date='02-05-2025',
                end_date='02-05-2051',
                cashflow_amt=[
                    2500,
                    2575,
                    2652,
                    2732,
                    2814,
                    2898,
                    2985,
                    3075,
                    3167,
                    3262,
                    3360,
                    3461,
                    3564,
                    3671,
                    3781,
                    3895,
                    4012,
                    4132,
                    4256,
                    4384,
                    4515,
                    4651,
                    4790,
                    4934,
                    5082,
                    5234,
                    5391
                ]
            ),
            additional_properties={
                'lockExpiry': jsonpickle.decode('0'),
                'meanReturn': jsonpickle.decode('0.03'),
                'standardDeviation': jsonpickle.decode('0.04')
            }
        )
    ],
    goal_profile_list=[
        GoalProfileGoeForTaxesAttr(
            goal_id='39623865346539642d366234362d343639362d393332332d356134356563653030336130',
            start_date='02-05-2052',
            end_date='02-05-2052',
            priority='Need',
            goal_purpose='non-education',
            goal_amt=[
                666
            ],
            scenario_type='retirement'
        )
    ],
    reallocate=False,
    is_near_term_volatility=False,
    curr_date='02-05-2025',
    cashflow_date='02-05-2025',
    loss_threshold=0,
    additional_properties={
        'targetPortfolio': jsonpickle.decode('{"meanReturn":0.03,"standardDeviation":0.04}')
    }
)

result = goe_api.goe_for_taxes(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | [`MessageException`](../../doc/models/message-exception.md) |
| 500 | Internal Server Error | [`InternalServerMessageGeneralException`](../../doc/models/internal-server-message-general-exception.md) |


# Goe With Annuities

```python
def goe_with_annuities(self,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GoeWithAnnuitiesInputModel`](../../doc/models/goe-with-annuities-input-model.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AnnuitiesResponseModel`](../../doc/models/annuities-response-model.md).

## Example Usage

```python
body = GoeWithAnnuitiesInputModel(
    include_annuities=True,
    date_of_birth='01-01-1981',
    retirement_age=61,
    drawdown_age=66,
    planning_age=82,
    current_salary=350000,
    total_account_balance=1260000,
    balance_proportion=0.1,
    periodic_contributions=8750,
    contribution_freq=ContributionFreq.MONTHLY,
    outside_assets=210000,
    current_portfolio_id=None,
    current_date='01-01-2024',
    risk_profile=RiskProfile5.AGGRESSIVE,
    annuity_type=AnnuityType.DEFERRED,
    annuity_price=[
        AnnuityPrice(
            age=43,
            value=[
                Value(
                    year=2024,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=44,
            value=[
                Value(
                    year=2025,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=45,
            value=[
                Value(
                    year=2026,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=46,
            value=[
                Value(
                    year=2027,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=47,
            value=[
                Value(
                    year=2028,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=48,
            value=[
                Value(
                    year=2029,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=49,
            value=[
                Value(
                    year=2030,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=50,
            value=[
                Value(
                    year=2031,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=51,
            value=[
                Value(
                    year=2032,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=52,
            value=[
                Value(
                    year=2033,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=53,
            value=[
                Value(
                    year=2034,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=54,
            value=[
                Value(
                    year=2035,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=55,
            value=[
                Value(
                    year=2036,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=56,
            value=[
                Value(
                    year=2037,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=57,
            value=[
                Value(
                    year=2038,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=58,
            value=[
                Value(
                    year=2039,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=59,
            value=[
                Value(
                    year=2040,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=60,
            value=[
                Value(
                    year=2041,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=61,
            value=[
                Value(
                    year=2042,
                    rate=10
                )
            ]
        )
    ],
    annuity_payout_freq=AnnuityPayoutFreq.YEARLY,
    marital_status=MaritalStatus.MARRIED,
    spousal_salary=250000,
    job_tenure=31,
    current_annuity_balance=35000,
    retirement_income_goal=25000,
    drawdown_age_ss=64,
    income_from_ss=10000,
    other_income=25000,
    other_income_freq=OtherIncomeFreq.YEARLY,
    calculate_retirement_income_goal=True,
    additional_properties={
        'currAge': jsonpickle.decode('43')
    }
)

result = goe_api.goe_with_annuities(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "statusCode": 200,
  "message": "Success",
  "body": {
    "retirementGoal": 60000,
    "retirementGoalMin": 50000,
    "retirementGoalMax": 75000,
    "incomeFromOutsideAssets": 2000,
    "incomeFromSS": 2000,
    "incomeFromOthers": 10000,
    "allocationToAnnuities": 1000,
    "allocationToGOE": 20000,
    "recommendedPortfolioID": 8,
    "retirementGoalProbability": 0.8513,
    "recommendedConsumption": 60000
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ValidationMessageOneException`](../../doc/models/validation-message-one-exception.md) |
| 404 | Not Found | [`MessageException`](../../doc/models/message-exception.md) |
| 500 | Internal Server Error | [`InternalServerMessageException`](../../doc/models/internal-server-message-exception.md) |

