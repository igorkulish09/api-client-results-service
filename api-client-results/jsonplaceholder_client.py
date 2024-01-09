"""Module to interact with the JSONPlaceholder API."""

from typing import List

import httpx


class JsonPlaceholderClient:
    """Client for the JSONPlaceholder API."""

    base_url = 'https://jsonplaceholder.typicode.com'

    def __init__(self, base_url: str = base_url):
        """Initialize JsonPlaceholderClient."""
        self.base_url = base_url
        self.client = httpx.Client()

    def get_posts(self, user_id: int = None) -> List[dict]:
        """
        Get a list of posts.

        :param user_id: Optional user ID to filter posts.
        :type user_id: int or None
        :return: A list of post dictionaries.
        :rtype: list[dict]
        """
        url = f'{self.base_url}/posts'
        query_parameters = {'userId': user_id} if user_id else {}

        response = self.client.get(url, params=query_parameters)
        response.raise_for_status()

        return response.json()

    def get_comments(self, post_id: int) -> List[dict]:
        """
        Get a list of comments for a specific post.

        :param post_id: The ID of the post to get comments for.
        :return: A list of comment dictionaries.
        """
        url = f'{self.base_url}/comments'
        query_parameters = {'postId': post_id}

        response = self.client.get(url, params=query_parameters)
        response.raise_for_status()

        return response.json()

    def close(self):
        """Close the HTTP client."""
        self.client.close()
