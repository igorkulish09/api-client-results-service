"""Module for interacting with the Cat API."""

import httpx
from pydantic import BaseModel


class CatImage(BaseModel):

    """Represents a cat image.

    Attributes:
        url (str): The URL of the cat image.
    """
    url: str


class CatAPIClient:
    """
    Client for interacting with the Cat API.

    Attributes:
        base_url (str): The base URL of the Cat API.
        client (httpx.Client): HTTP client for making requests to the Cat API.
    """

    def __init__(self, base_url: str = 'https://api.thecatapi.com/v1'):
        """
        Initialize CatAPIClient.

        :param base_url: The base URL of the Cat API.
        """
        self.base_url = base_url
        self.client = httpx.Client()

    def get_random_cat_image(self) -> CatImage:
        """
        Get a random cat image from the Cat API.

        :return: CatImage object representing the random cat image.
        """
        url = f'{self.base_url}/images/search'
        response = self.client.get(url)
        response.raise_for_status()
        image_url = response.json()[0]['url']
        return CatImage(url=image_url)

    def close(self):
        """Close the HTTP client."""
        self.client.close()
