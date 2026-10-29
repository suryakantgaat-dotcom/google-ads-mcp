# Copyright 2026 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for multi-account credentials and login-method selection."""

import json
import os
import unittest
from unittest.mock import MagicMock, patch

from fastmcp.exceptions import ToolError
from google.oauth2.credentials import Credentials

from ads_mcp import utils

_ACCOUNTS = [
    {
        "name": "qura",
        "developer_token": "dev-qura",
        "login_customer_id": "111-222-3333",
        "refresh_token": "rt-qura",
        "client_id": "cid",
        "client_secret": "secret",
    },
    {"name": "nocreds", "developer_token": "dev-x"},
    {
        "name": "notoken",
        "refresh_token": "rt",
        "client_id": "c",
        "client_secret": "s",
    },
]


def _env(**extra):
    env = {"GOOGLE_ADS_ACCOUNTS_CONFIG": json.dumps(_ACCOUNTS)}
    env.update(extra)
    return patch.dict(os.environ, env, clear=True)


class TestAccountClients(unittest.TestCase):

    def test_account_uses_its_own_refresh_token_and_settings(self):
        with _env(GOOGLE_ADS_LOGIN_CUSTOMER_ID="999"):
            with patch("ads_mcp.utils.GoogleAdsClient") as mock_client:
                utils._get_googleads_client(account_name="qura")
                _, kwargs = mock_client.call_args
        creds = kwargs["credentials"]
        self.assertIsInstance(creds, Credentials)
        self.assertEqual(creds.refresh_token, "rt-qura")
        self.assertEqual(kwargs["developer_token"], "dev-qura")
        self.assertEqual(kwargs["login_customer_id"], "1112223333")

    def test_explicit_login_customer_id_overrides_account(self):
        with _env():
            with patch("ads_mcp.utils.GoogleAdsClient") as mock_client:
                utils._get_googleads_client(
                    login_customer_id="444-555-6666", account_name="qura"
                )
                _, kwargs = mock_client.call_args
        self.assertEqual(kwargs["login_customer_id"], "4445556666")

    def test_unknown_account_lists_available_accounts(self):
        with _env():
            with self.assertRaises(ToolError) as cm:
                utils._get_googleads_client(account_name="missing")
        self.assertIn("qura", str(cm.exception))

    def test_account_without_credentials_does_not_fall_back(self):
        with _env():
            with patch("google.auth.default") as mock_adc:
                with self.assertRaises(ToolError):
                    utils._get_googleads_client(account_name="nocreds")
                mock_adc.assert_not_called()

    def test_account_without_developer_token_fails(self):
        with _env():
            with self.assertRaises(ToolError):
                utils._get_googleads_client(account_name="notoken")

    def test_account_service_account_json(self):
        accounts = [
            {"name": "sa", "developer_token": "d", "credentials_json": "{}"}
        ]
        with patch.dict(
            os.environ,
            {"GOOGLE_ADS_ACCOUNTS_CONFIG": json.dumps(accounts)},
            clear=True,
        ):
            with patch(
                "ads_mcp.utils.service_account.Credentials.from_service_account_info"
            ) as mock_sa:
                with patch("ads_mcp.utils.GoogleAdsClient"):
                    utils._get_googleads_client(account_name="sa")
                mock_sa.assert_called_once()


class TestDefaultCredentials(unittest.TestCase):

    def test_no_default_credentials_never_calls_adc_or_token(self):
        with _env():
            with (
                patch("google.auth.default") as mock_adc,
                patch(
                    "fastmcp.server.dependencies.get_access_token"
                ) as mock_token,
            ):
                with self.assertRaises(ToolError) as cm:
                    utils._create_credentials()
                mock_adc.assert_not_called()
                mock_token.assert_not_called()
        self.assertIn("account_name", str(cm.exception))

    def test_default_refresh_token(self):
        with _env(
            GOOGLE_ADS_REFRESH_TOKEN="rt",
            GOOGLE_ADS_MCP_OAUTH_CLIENT_ID="c",
            GOOGLE_ADS_MCP_OAUTH_CLIENT_SECRET="s",
        ):
            with patch(
                "fastmcp.server.dependencies.get_access_token",
                return_value=None,
            ):
                creds = utils._create_credentials()
        self.assertEqual(creds.refresh_token, "rt")

    def test_mcp_oauth_token_used_when_login_enabled(self):
        with _env(
            GOOGLE_ADS_MCP_OAUTH_CLIENT_ID="c",
            GOOGLE_ADS_MCP_OAUTH_CLIENT_SECRET="s",
        ):
            with patch(
                "fastmcp.server.dependencies.get_access_token",
                return_value=MagicMock(token="user-token"),
            ):
                creds = utils._create_credentials()
        self.assertEqual(creds.token, "user-token")

    def test_adc_only_when_explicitly_allowed(self):
        with _env(GOOGLE_ADS_MCP_ALLOW_ADC="true"):
            with patch(
                "google.auth.default", return_value=(MagicMock(), "p")
            ) as mock_adc:
                utils._create_credentials()
                mock_adc.assert_called_once()


if __name__ == "__main__":
    unittest.main()
