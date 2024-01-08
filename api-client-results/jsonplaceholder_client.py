from typing import List

from pydantic import BaseModel
import httpx


class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class Comment(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str


class JsonPlaceholderClient:
    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com"):
        self.base_url = base_url
        self.client = httpx.Client()

    def get_all_posts(self) -> List[Post]:
        response = self.client.get(f"{self.base_url}/posts")
        response.raise_for_status()
        return [Post(**post) for post in response.json()]

    def get_all_comments(self) -> List[Comment]:
        response = self.client.get(f"{self.base_url}/comments")
        response.raise_for_status()
        return [Comment(**comment) for comment in response.json()]

    def close(self):
        self.client.close()
