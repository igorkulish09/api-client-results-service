from typing import List, Optional


class ResultService:
    def __init__(self):
        self.results: List[Optional[dict]] = []

    def save_result(self, result: dict):
        self.results.append(result)

    def get_all_results(self) -> List[dict]:
        return self.results
