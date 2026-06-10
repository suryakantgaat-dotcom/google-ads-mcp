#!/usr/bin/env python

# Copyright 2026 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Common utilities used by the MCP server."""

from typing import Any
import json
import proto
import logging
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.v24.services.services.google_ads_service import (
    GoogleAdsServiceClient,
)

from google.ads.googleads.util import get_nested_attr
import google.auth
from google.oauth2 import service_account
from ads_mcp.mcp_header_interceptor import MCPHeaderInterceptor
import os
import importlib.resources

# filename for generated field information used by search
_GAQL_FILENAME = "gaql_resources.txt"

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# OAuth scope for the Google Ads API.
_ADS_SCOPE = "https://www.googleapis.com/auth/adwords"

def _create_credentials() -> google.auth.credentials.Credentials:
    """Returns credentials: FastMCP token > stored refresh token > Application Default Credentials."""
    from fastmcp.server.dependencies import get_access_token
    from google.oauth2.credentials import Credentials

    token_obj = get_access_token()
    if token_obj and token_obj.token:
        return Credentials(token=token_obj.token)

    refresh_token = os.environ.get("GOOGLE_ADS_REFRESH_TOKEN")
    client_id = os.environ.get("GOOGLE_ADS_MCP_OAUTH_CLIENT_ID")
    client_secret = os.environ.get("GOOGLE_ADS_MCP_OAUTH_CLIENT_SECRET")
    if refresh_token and client_id and client_secret:
        return Credentials(
            token=None,
            refresh_token=refresh_token,
            token_uri="https://oauth2.googleapis.com/token",
            client_id=client_id,
            client_secret=client_secret,
            scopes=[_ADS_SCOPE],
        )

    credentials, _ = google.auth.default(scopes=[_ADS_SCOPE])
    return credentials

def _get_developer_token() -> str:
    """Returns the developer token from the environment variable GOOGLE_ADS_DEVELOPER_TOKEN."""
    dev_token = os.environ.get("GOOGLE_ADS_DEVELOPER_TOKEN")
    if dev_token is None:
        raise ValueError(
            "GOOGLE_ADS_DEVELOPER_TOKEN environment variable not set."
        )
    return dev_token

def _get_login_customer_id() -> str | None:
    """Returns login customer id, if set, from the environment variable GOOGLE_ADS_LOGIN_CUSTOMER_ID."""
    return os.environ.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID")

def _get_googleads_client() -> GoogleAdsClient:
    args = {
        "credentials": _create_credentials(),
        "developer_token": _get_developer_token(),
        "use_proto_plus": True,
    }
    login_customer_id = _get_login_customer_id()
    if login_customer_id:
        args["login_customer_id"] = login_customer_id
    return GoogleAdsClient(**args)

# ---------------------------------------------------------------------------
# Multi-account support
# ---------------------------------------------------------------------------

def _get_account_configs() -> list:
    """Returns list of account configs from GOOGLE_ADS_ACCOUNTS_CONFIG env var.

    JSON array format:
    [
      {
        "name": "account_a",
        "developer_token": "TOKEN_A",
        "login_customer_id": "1234567890",
        "credentials_json": "{...service account JSON string...}"
      }
    ]
    credentials_json is optional; omit to use Application Default Credentials.
    """
    raw = os.environ.get("GOOGLE_ADS_ACCOUNTS_CONFIG")
    return json.loads(raw) if raw else []

def _create_credentials_for_account(account_config: dict) -> google.auth.credentials.Credentials:
    """Returns credentials for a specific account config.

    Priority: FastMCP token > per-account refresh token > service account JSON > ADC.
    Account config supports:
      refresh_token, client_id, client_secret  — OAuth user credentials
      credentials_json                          — service account JSON string
    """
    from fastmcp.server.dependencies import get_access_token
    from google.oauth2.credentials import Credentials

    token_obj = get_access_token()
    if token_obj and token_obj.token:
        return Credentials(token=token_obj.token)

    refresh_token = account_config.get("refresh_token")
    client_id = account_config.get("client_id")
    client_secret = account_config.get("client_secret")
    if refresh_token and client_id and client_secret:
        return Credentials(
            token=None,
            refresh_token=refresh_token,
            token_uri="https://oauth2.googleapis.com/token",
            client_id=client_id,
            client_secret=client_secret,
            scopes=[_ADS_SCOPE],
        )

    creds_json = account_config.get("credentials_json")
    if creds_json:
        info = json.loads(creds_json) if isinstance(creds_json, str) else creds_json
        return service_account.Credentials.from_service_account_info(
            info, scopes=[_ADS_SCOPE]
        )

    credentials, _ = google.auth.default(scopes=[_ADS_SCOPE])
    return credentials

def _get_googleads_client_for_account(account_config: dict) -> GoogleAdsClient:
    """Returns a GoogleAdsClient configured for the given account config dict."""
    dev_token = account_config.get("developer_token")
    if not dev_token:
        raise ValueError(
            f"Account config '{account_config.get('name')}' is missing 'developer_token'."
        )
    args = {
        "credentials": _create_credentials_for_account(account_config),
        "developer_token": dev_token,
        "use_proto_plus": True,
    }
    if account_config.get("login_customer_id"):
        args["login_customer_id"] = account_config["login_customer_id"]
    return GoogleAdsClient(**args)

def _resolve_client(account_name: str | None) -> GoogleAdsClient:
    """Returns the GoogleAdsClient for the given account name, or the default client."""
    if account_name:
        accounts = _get_account_configs()
        account = next((a for a in accounts if a["name"] == account_name), None)
        if account:
            return _get_googleads_client_for_account(account)
        raise ValueError(
            f"Account '{account_name}' not found in GOOGLE_ADS_ACCOUNTS_CONFIG. "
            f"Available accounts: {[a['name'] for a in accounts]}"
        )
    return _get_googleads_client()

def get_googleads_service(serviceName: str, account_name: str | None = None) -> GoogleAdsServiceClient:
    return _resolve_client(account_name).get_service(
        serviceName, interceptors=[MCPHeaderInterceptor()]
    )

def get_googleads_type(typeName: str, account_name: str | None = None):
    return _resolve_client(account_name).get_type(typeName)

def get_googleads_client(account_name: str | None = None):
    return _resolve_client(account_name)

def format_output_value(value: Any) -> Any:
    if isinstance(value, proto.Enum):
        return value.name
    elif isinstance(value, proto.Message):
        return proto.Message.to_dict(value)
    elif hasattr(value, "__iter__") and not isinstance(value, (str, bytes)):
        return [format_output_value(v) for v in value]
    else:
        return value

def format_output_row(row: proto.Message, attributes):
    return {
        attr: format_output_value(get_nested_attr(row, attr))
        for attr in attributes
    }

def get_gaql_resources_filepath():
    package_root = importlib.resources.files("ads_mcp")
    file_path = package_root.joinpath(_GAQL_FILENAME)
    return file_path