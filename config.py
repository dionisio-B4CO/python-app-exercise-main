from src.Services.ApiService import ApiService

api_service = ApiService(
    api_url='https://jsonplaceholder.typicode.com/todos/',
    storage_path='storage/')
