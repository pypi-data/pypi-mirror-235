from datetime import datetime, timedelta

from typing import Dict

import requests
from requests import RequestException
from requests.auth import HTTPBasicAuth

from investec_python.exception import InvestecError, InvestecAuthenticationError


class API:

    _api_url: str = "https://openapi.investec.com"

    _use_sandbox: bool = False
    _sandbox_x_api_token: str = "eUF4elFSRlg5N3ZPY3lRQXdsdUVVNkg2ZVB4TUE1ZVk6YVc1MlpYTjBaV010ZW1FdGNHSXRZV05qYjNWdWRITXRjMkZ1WkdKdmVBPT0="

    _client_id: str
    _client_secret: str

    _token: str
    _token_expires_at: datetime

    def __init__(
        self,
        use_sandbox: bool,
        client_id: str = "",
        client_secret: str = "",
    ):
        self._use_sandbox = use_sandbox
        self._client_id = client_id
        self._client_secret = client_secret

        if use_sandbox:
            self._setup_client_for_sandbox()

        if self._client_id == "":
            raise InvestecError(
                "You did not choose to use the sandbox but did not provide a client_id"
            )

        if self._client_secret == "":
            raise InvestecError(
                "You did not choose to use the sandbox but did not provide a client_secret"
            )

        self._refresh_token()

    def _setup_client_for_sandbox(self):
        self._api_url = "https://openapisandbox.investec.com"
        self._client_id = "yAxzQRFX97vOcyQAwluEU6H6ePxMA5eY"
        self._client_secret = "4dY0PjEYqoBrZ99r"

    def _refresh_token(self):
        try:
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            if self._use_sandbox:
                headers["x-api-key"] = self._sandbox_x_api_token

            response = requests.post(
                f"{self._api_url}/identity/v2/oauth2/token",
                headers=headers,
                auth=HTTPBasicAuth(self._client_id, self._client_secret),
                data={"grant_type": "client_credentials"},
            )

            if response.status_code >= 400:
                raise InvestecAuthenticationError("Failed to authenticate")

            response_data = response.json()
            if (
                "access_token" not in response_data.keys()
                or "expires_in" not in response_data.keys()
            ):
                raise InvestecAuthenticationError("Failed to authenticate")

            self._token = response_data["access_token"]
            self._token_expires_at = datetime.utcnow() + timedelta(
                seconds=response_data["expires_in"]
            )

        except RequestException:
            raise InvestecAuthenticationError("Failed to authenticate")

    def _is_token_valid(self):
        return self._token is not None and self._token_expires_at > datetime.utcnow()

    def _get_token(self) -> str:
        if not self._is_token_valid():
            self._refresh_token()

        return self._token

    def _get_headers(self) -> Dict:
        token = self._get_token()
        return {"Authorization": f"Bearer {token}"}

    @property
    def api_url(self) -> str:
        return self._api_url

    def get(self, resource_path: str) -> Dict:
        headers = self._get_headers()

        try:
            response = requests.get(f"{self._api_url}/{resource_path}", headers=headers)
            if response.status_code >= 400:
                raise InvestecError(f"Failed to get resource at {resource_path}")
            return response.json()
        except RequestException as e:
            raise InvestecError(f"Failed to get resource at {resource_path}")
