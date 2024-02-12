from src.Application.App import App
from src.Services.ApiService import ApiService
import unittest
from unittest.mock import patch


class TestIntegration(unittest.TestCase):
    """
    Integration tests for the application.

    These tests ensure that the application components work together correctly.

    Methods:
        test_app_run_calls_api_service_run:
            Verifies that the 'run' method of ApiService is called when 'run' \
            method of App is executed.
    """
    @patch('src.Services.ApiService.requests.get')
    def test_app_run_calls_api_service_run(self, mock_requests_get):
        """
        Test if the 'run' method of ApiService is called when 'run' method of \
        App is executed.

        Args:
            mock_requests_get: \
                Mock object for ApiService's 'requests.get' method.

        Returns:
            None
        """

        app = App(ApiService())

        with app._app.test_client() as client:
            client.get('/api/fetch_todos')

        # Assert that the 'requests.get' method of ApiService is called once,
        # indirectly verifying that the 'run' method of ApiService is invoked.
        mock_requests_get.assert_called_once()


if __name__ == '__main__':
    unittest.main()
