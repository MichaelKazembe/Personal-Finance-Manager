# models/budget.py
"""
Budget Model Module

This module defines the Budget class which represents a spending budget
for a specific category. It allows users to set spending limits for different
expense categories and helps track their financial goals.
"""


class Budget:
    """
    Budget model class representing a spending budget for a category.
    
    Attributes:
        user_id (str): The ID of the user who owns this budget
        category (str): The budget category (e.g., "Food", "Transport", "Entertainment")
        limit (float): The maximum spending limit for this budget category
    """
    def __init__(self, user_id, category, limit):
        """
        Initialize a new Budget instance.
        
        Args:
            user_id (str): The unique identifier of the user creating this budget
            category (str): The spending category to set a budget for (e.g., "Food", "Transport")
            limit (float): The maximum amount allowed to spend in this category
        """
        self.user_id = user_id
        self.category = category
        self.limit = limit

    def to_dict(self):
        """
        Convert the Budget object to a dictionary for storage or serialization.
        
        Returns:
            dict: A dictionary containing all budget attributes:
                - user_id: The user's ID
                - category: The budget category
                - limit: The spending limit for this budget
        """
        return {
            "user_id": self.user_id,
            "category": self.category,
            "limit": self.limit
        }