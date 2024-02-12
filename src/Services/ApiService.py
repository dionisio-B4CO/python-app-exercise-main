from sys import stderr
import requests
import csv
from datetime import datetime
import logging


class ApiService:
    """
    Singleton class for managing API interactions and data storage.

    This class provides a single instance for interacting with an external API,
    fetching TODOs, and saving them to CSV files.

    Attributes:
        _instance (ApiService): The unique instance of the ApiService class.

    Methods:
        __new__(cls, *args, **kwargs): Overrides the creation of new instances.
            Ensures that only one instance of the class is created and shared.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ApiService, cls).__new__(cls)
            cls._instance.api_url = kwargs.get(
                'api_url', 'https://jsonplaceholder.typicode.com/todos/')
            cls._instance.storage_path = kwargs.get('storage_path', 'storage/')
            cls._instance.logger = logging.getLogger(__name__)
        return cls._instance

    def _fetch_todos(self):
        """
        Fetch TODOs from the API.

        Returns:
            list: List of TODOs.
        """
        response = requests.get(self.api_url)
        response.raise_for_status()
        return response.json()

    def _save_todo_to_csv(self, todo):
        """
        Save a TODO to a CSV file.

        Args:
            todo (dict): TODO data.

        Returns:
            str: Filename of the saved CSV file.
        """
        todo_id = todo['id']
        filename = f'{datetime.now().strftime("%Y_%m_%d")}_{todo_id}.csv'

        with open(
                f'{self.storage_path}{filename}', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['userId', 'id', 'title', 'completed'])
            csv_writer.writerow(
                [todo['userId'], todo['id'], todo['title'], todo['completed']])

        return filename

    def run(self):
        """
        Run the API service.

        This method is responsible for fetching TODOs from the API and saving them
        to CSV files. It logs relevant information about the process, including
        errors encountered during the API request or CSV file saving.

        Raises:
            requests.RequestException: If an error occurs during the API request.
        """
        self.logger.info('Running ApiService')

        try:
            todos = self._fetch_todos()

            for todo in todos:
                try:
                    filename = self._save_todo_to_csv(todo)
                    self.logger.info(f'TODO {todo["id"]} saved to {filename}')
                except Exception as save_error:
                    self.logger.error(f'Error saving TODO {todo["id"]} to CSV:\
                                      {save_error}')

        except requests.RequestException as e:
            self.logger.error(f'Error during API request: {e}')
            raise
