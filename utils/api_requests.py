import requests

class ApiRequests:
    BASE_URL = "https://api.restful-api.dev/objects"

    @staticmethod
    def get_all_phones():
        return requests.get(ApiRequests.BASE_URL)

    @staticmethod
    def get_phones_by_ids(ids):
        params = {'id': ids}
        return requests.get(ApiRequests.BASE_URL, params=params)

    @staticmethod
    def create_phone(data):
        return requests.post(ApiRequests.BASE_URL, json=data)

    @staticmethod
    def update_phone(id, data):
        return requests.put(f"{ApiRequests.BASE_URL}/{id}", json=data)

    @staticmethod
    def delete_phone(id):
        return requests.delete(f"{ApiRequests.BASE_URL}/{id}")
