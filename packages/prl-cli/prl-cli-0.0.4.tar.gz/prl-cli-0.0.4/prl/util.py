from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import os

from .auth import get_auth_token

PLAYGROUND_ENV = os.getenv("PLAYGROUND_ENV")
endpoints = {
    "LOCAL": ("http://localhost:8000", "http://localhost:3000"),
    "DEV": ("https://dev.playgroundrl.com", "https://devbe.playgroundrl.com"),
    "PROD": ("https://playgroundrl.com", "https://prodbe.playgroundrl.com"),
}
FE_HOST, BE_HOST = (
    endpoints[PLAYGROUND_ENV] if PLAYGROUND_ENV in endpoints else endpoints["PROD"]
)

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
