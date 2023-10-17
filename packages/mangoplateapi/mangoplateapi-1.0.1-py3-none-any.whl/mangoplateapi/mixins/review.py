import requests


class ReviewMixin:
    def get_reviews(self, restaurant_code, page_no: int, page_size: int):
        url = f"https://stage.mangoplate.com/api/v5/restaurants/{restaurant_code}/reviews.json"
        data = {
            "language": "kor",
            "start_index": page_no,
            "request_count": page_size,
        }
        response = requests.get(url, data=data)
        response_dict = response.json()
        
        # ID 값 설정
        for item in response_dict:
            _id = item['action_id']
            item['_id'] = _id
            item['id'] = _id

        return response_dict
