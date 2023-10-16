import requests
from requests.structures import CaseInsensitiveDict


class ReachApiGatewayV2:
    def __init__(self, base_url, access_token):
        self.base_url = base_url
        self.headers = CaseInsensitiveDict(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "authorization": f"Bearer {access_token}",
            }
        )

    def stripe_create_subscription(self, user_id, business_id):
        resp = requests.post(
            f"{self.base_url}/stripe/user/{user_id}/business/{business_id}/subscription",
            headers=self.headers
        )
        return resp

    def stripe_create_booking_guarantee(self, business_id, booking_price):
        resp = requests.post(
            f"{self.base_url}/stripe/business/{business_id}/booking-guarantee/",
            headers=self.headers,
            params={'booking_price': booking_price}
        )
        return resp

    def stripe_get_customer(self, user_id):
        resp = requests.get(
            f"{self.base_url}/stripe/user/{user_id}/customer",
            headers=self.headers
        )
        return resp
