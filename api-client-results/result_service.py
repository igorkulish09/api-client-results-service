"""Module containing the ResultService class."""

from typing import List, Optional


class ResultService:
    """
    This class represents a service for managing results.

    Attributes:
        saved_results (List[Optional[dict]]): A list to store results as dictionaries.
    """

    def __init__(self):
        """Initialize ResultService."""
        self.saved_results: List[Optional[dict]] = []

    def save_result(self, result_dict: dict):
        """
        Save a result to the service.

        :param result_dict: A dictionary representing the result.
        """
        self.saved_results.append(result_dict)

    def get_all_results(self) -> List[dict]:
        """
        Get all saved results.

        :return: A list of dictionaries representing the results.
        """
        return self.saved_results
