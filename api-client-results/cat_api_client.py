from typing import List

import httpx


class CatImage:
    def __init__(self, url: str):
        self.url = url


class CatAPIClient:
    def __init__(self, base_url: str = "https://api.thecatapi.com/v1"):
        self.base_url = base_url
        self.client = httpx.Client()

    def get_random_cat_image(self) -> CatImage:
        response = self.client.get(f"{self.base_url}/images/search")
        response.raise_for_status()
        return CatImage(url=response.json()[0]['url'])

    def close(self):
        self.client.close()
