import requests
import os
import sseclient
from datetime import datetime
import urllib.parse
import urllib3
import ssl


class RKClient:
    """Main class for interacting with IDM. See Documentation for details."""

    def __init__(
        self,
        token: str,
        creds: dict,
        server: str = "https://idm.robokami.com",
        **kwargs
    ) -> None:
        """Initializes the client.

        Args:
            creds: Dictionary containing credentials. Required keys are: username and password.
            server: Server address. Defaults to https://idm.robokami.com.
            initiate_login: If True, initiates login upon initialization. Defaults to True.
            initiate_stream: If True, initiates stream upon initialization. Defaults to False.
        """
        self.token = token
        self.server = server
        self.creds = creds

        if kwargs.get("use_ssl_legacy"):
            self.ssl_legacy()
        else:
            self.req = requests

        if kwargs.get("initiate_login", True):
            self.authorize()

        if kwargs.get("initiate_stream", False) and self.session_token is not None:
            self.stream()

    def authorize(self):
        """
        Authorizes the client to IDM. If successful, session_token is set. If not, session_token is set to None.
        """
        res = self.req.get(
            urllib.parse.urljoin(self.server, "login"),
            json={"credentials": self.creds, "token": self.token},
            timeout=15,
        )

        if res.status_code == 200:
            self.session_token = res.json()["session_token"]
            self.iat = datetime.now().timestamp()
        else:
            print("Login failed")
            self.session_token = None

    def renew_session(self):
        """
        Renews the session token.
        """
        self.authorize()

    def place_order(self, d: dict) -> dict:
        """
        Places an order to IDM. Order details are given as a dictionary. Wrapper to trade_command function.

        Args:
            d: Dictionary containing order details. Required keys are: c (contract), position ('bid' or 'ask'), price, and lots. order_status and order_note are optional.
        """
        d["order_status"] = d.get("order_status", "active")
        d["order_note"] = d.get("order_note", "RK-TRADER")
        return self.trade_command("place_order", d)

    def update_order(self, d) -> dict:
        """
        Updates an order existing in IDM. Update details are given as a dictionary. Wrapper to trade_command function.

        Args:
            d: Dictionary containing order update details. Required keys are: order_id and c.
        """
        if "order_id" not in d.keys():
            return {"status": "error", "message": "order_id is required"}
        d["contract_type"] = "hourly" if d["c"].startswith("PH") else "block"
        d["order_note"] = d.get("order_note", "RK-TRADER")
        return self.trade_command("update_order", d)

    def get_net_positions(self, is_block: bool = False) -> dict:
        """
        Gets the net positions of the user. Wrapper to trade_command function.

        Args:
            is_block: If True, returns block positions. If False, returns hourly positions. Defaults to False.
        """
        return self.trade_command(
            "net_positions", {"contract_type": "block" if is_block else "hourly"}
        )

    def trade_command(self, command: str, d: dict) -> dict:
        """
        Main trade commands function. See Documentation for details.

        Args:
            command: Name of the command.
            d: Dictionary containing command details.

        Returns:
            Dictionary containing the response from IDM.
        """
        command_phrase = urllib.parse.urljoin(self.server, ("trade/" + command))
        res = self.req.post(
            command_phrase,
            headers={"Authorization": self.session_token},
            json=d,
        )

        if res.status_code == 200:
            return res.json()
        else:
            print("Failed response code: " + str(res.status_code))
            print(res.json())
            return res.json()

    def stream(self):
        """
        Initiates a stream connection to IDM. Stream is available at self.stream_client.
        """
        response = self.req.get(
            urllib.parse.urljoin(self.server, "stream"),
            headers={"Authorization": self.session_token},
            stream=True,
        )

        self.stream_client = sseclient.SSEClient(response)

    def ssl_legacy(self):
        class CustomHttpAdapter(requests.adapters.HTTPAdapter):
            # "Transport adapter" that allows us to use custom ssl_context.

            def __init__(self, ssl_context=None, **kwargs):
                self.ssl_context = ssl_context
                super().__init__(**kwargs)

            def init_poolmanager(self, connections, maxsize, block=False):
                self.poolmanager = urllib3.poolmanager.PoolManager(
                    num_pools=connections,
                    maxsize=maxsize,
                    block=block,
                    ssl_context=self.ssl_context,
                )

        def get_legacy_session():
            ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
            ctx.options |= 0x4  # OP_LEGACY_SERVER_CONNECT
            session = requests.session()
            session.mount("https://", CustomHttpAdapter(ctx))
            return session

        self.req = get_legacy_session()
