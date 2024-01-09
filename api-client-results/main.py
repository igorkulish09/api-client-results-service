"""This script initializes clients and services, performs various actions, and prints the results."""

import asyncio
from typing import List, Optional

import httpx


class JSONPlaceholderClient:
    """
    Client for interacting with the JSONPlaceholder API.

    Attributes:
        base_url (str): The base URL of the JSONPlaceholder API.
        success_status_code (int): The expected HTTP status code for successful responses.
    """

    def __init__(self, base_url: Optional[str] = 'https://jsonplaceholder.typicode.com'):
        """
        Initialize the JSONPlaceholderClient.

        Args:
            base_url (Optional[str]): The base JSONPlaceholder API. Defaults to 'https://jsonplaceholder.typicode.com'.
        """
        self.base_url = base_url
        self.success_status_code = 200  # Expected HTTP status code for successful responses

    async def get_posts(self) -> List[dict]:
        """Get a list of posts from the JSONPlaceholder API."""
        endpoint = f'{self.base_url}/posts'

        async with httpx.AsyncClient() as client:
            response = await client.get(endpoint)

        return response.json() if response.status_code == self.success_status_code else []

    async def get_comments(self) -> List[dict]:
        """Get a list of comments from the JSONPlaceholder API."""
        endpoint = f'{self.base_url}/posts'

        async with httpx.AsyncClient() as client:
            response = await client.get(endpoint)

        return response.json() if response.status_code == self.success_status_code else []


async def main():
    """
    Main function to demonstrate the usage of JSONPlaceholderClient.

    This function creates an instance of JSONPlaceholderClient,
    retrieves the list of posts and comments, and prints the results.
    """
    jsonplaceholder_client = JSONPlaceholderClient()

    # Get the list of posts
    posts = await jsonplaceholder_client.get_posts()
    print('Posts:', posts)

    # Get the list of comments
    comments = await jsonplaceholder_client.get_comments()
    print('Comments:', comments)


if __name__ == '__main__':
    asyncio.run(main())
