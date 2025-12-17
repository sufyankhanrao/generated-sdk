from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.exceptions.error_object_exception import ErrorObjectException
from shellcardmanagementapis.http.auth.bearer_token import BearerTokenCredentials
from shellcardmanagementapis.models.filters import Filters
from shellcardmanagementapis.models.search_card import SearchCard
from shellcardmanagementapis.models.search_card_request import SearchCardRequest
from shellcardmanagementapis.shell_card_management_ap_is_client import ShellCardManagementApIsClient

client = ShellCardManagementApIsClient(
    bearer_token_credentials=BearerTokenCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    ),
    environment=Environment.SIT
)

card_controller = client.card
request_id = 'RequestId8'

body = SearchCardRequest(
    filters=Filters(
        card_status=[
            'ACTIVE',
            'BLOCKED'
        ],
        account_id=1223,
        account_number='CZ00000923',
        card_group_id=424,
        card_group_name='CARDGRP1',
        card_segment='Fleet',
        card_type_code='7077327',
        col_co_code=32,
        col_co_id=32,
        coverage='National',
        creation_date='20211222',
        driver_name=[
            'JAN KOLLER',
            'DRIVER23',
            'DRIVER25'
        ],
        effective_date='20211222',
        exclude_cancelled_cards=True,
        exclude_card_group_id=425,
        exclude_card_group_name='CARDGRP2',
        exclude_cards=[
            SearchCard(
                card_id=466907,
                pan='7077327290224795811'
            )
        ],
        exclude_fraud_cards=False,
        exclude_pending_renewal_cards=True,
        exclude_replaced_cards=False,
        expiry_month='052022',
        include_cards=[
            SearchCard(
                card_id=466906,
                pan='7077327290224795801'
            )
        ],
        include_intermediate_status=False,
        issued_after='20211123',
        network='ShellSitesOnly',
        pan_ends_with='1284',
        payer_id=1223,
        payer_number='CZ00000923',
        purchase_category_code='3',
        sort_order='1,3,7',
        include_scheduled_card_blocks=False,
        token_type_id=107,
        token_type_name='CZ CRT Int MultiNetwork - CHIP',
        vehicle_registration_number=[
            '5A2 7512',
            '5A2 7514'
        ],
        exclude_old_cards=False,
        exclude_expiring_cards=False,
        reissue_setting='true',
        request_id='233e4567-e89b-12d3-a456-426614174000'
    ),
    page_size='50',
    page='1'
)

try:
    result = card_controller.searchcard(
        request_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorObjectException as e: 
    print(e)
except APIException as e: 
    print(e)

