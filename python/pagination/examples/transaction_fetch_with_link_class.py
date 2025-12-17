from paginationtester.configuration import Environment
from paginationtester.exceptions.api_exception import APIException
from paginationtester.paginationtester_client import PaginationtesterClient

client = PaginationtesterClient(
    environment=Environment.PRODUCTION
)

transaction_controller = client.transaction
page = 1

size = 10

try:
    result = transaction_controller.fetch_with_link(
        page=page,
        size=size
    )

    # Iterating over items in all pages.
    try:
        for _item in result:
            print(_item)
    except APIException as e:
        print(e)

    # Iterating over pages in the paginated response.
    try:
        for _page in result.pages():
            print(_page.body)
            # Iterating over items in the current page.
            for _item in _page.items():
                print(_item)
    except APIException as e:
        print(e)

except APIException as e: 
    print(e)

