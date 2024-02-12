from src.Services.ApiService import ApiService
import unittest
from unittest.mock import patch, MagicMock


class TestApiService(unittest.TestCase):

    @patch('src.Services.ApiService.requests.get')
    def test_run_fetch_todos(self, mock_requests_get):
        # Configuring the behaviour of the mock
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {"userId": 1, "id": 1, "title": "Todo test", "completed": False}]
        mock_requests_get.return_value = mock_response

        api_service = ApiService()
        api_service.run()

        import os
        files_in_storage = os.listdir("storage")
        assert any(file.endswith(".csv")
                   for file in files_in_storage), "No CSV files found in the \
                    'storage' directory"

        # Ensure that the content of the CSV file is correct.
        with open(
                os.path.join("storage", files_in_storage[0]), "r") as csvfile:
            lines = csvfile.readlines()
            assert "userId,id,title,completed\n" in lines
            assert 2 == len(lines)
            assert 4 == len(lines[1].split(','))


if __name__ == '__main__':
    unittest.main()
