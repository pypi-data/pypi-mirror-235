from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

from .auth import get_auth_token


# BE_HOST = "http://localhost:8000"
# FE_HOST = "http://localhost:3000"
FE_HOST = "https://dev.playgroundrl.com"
BE_HOST = "https://devbe.playgroundrl.com"

client_ = None


def get_client():
    global client_
    if client_ is None:
        transport = AIOHTTPTransport(
            url=f"{BE_HOST}/graphql/",
            headers={"Authorization": get_auth_token()},
            ssl=True,
        )
        client_ = Client(transport=transport, fetch_schema_from_transport=True)
    return client_
