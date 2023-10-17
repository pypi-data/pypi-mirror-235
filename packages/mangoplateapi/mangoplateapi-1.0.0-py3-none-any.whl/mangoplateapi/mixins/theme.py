import requests


class ThemeMixin:
    def get_themes(self, page_no: int, page_size: int):
        url = f"https://stage.mangoplate.com/api/v5/top_lists/list.json"
        data = {
            "language": "kor",
            "start_index": page_no,
            "request_count": page_size,
            # "filter": {"subcuisine_codes":[],"metro_codes":[],"price_codes":[],"cuisine_codes":[],"is_parking_available":0},
            # "order_by": "2"
        }
        response = requests.get(url, data=data)
        themes = response.json()
        # ID 설정
        for theme in themes:
            id = theme['link_key']
            theme['id'] = id
            theme['_id'] = id
        return themes

    def get_theme(self, code: str,page_no:int, page_size:int):
        url = f"https://stage.mangoplate.com/api/v2/web/top_lists/{code}/restaurants.json"
        data = {
            "language": "kor",
            "start_index": page_no,
            "request_count": page_size,
        }
        response = requests.get(url, data=data)
        response_dict = response.json()
        # ID 설정
        for item in response_dict:
            _id = item['restaurant']['restaurant_uuid']
            item['_id'] = _id
            item['id'] = _id
            item['key'] = item['restaurant']['restaurant_key']
        return response_dict

