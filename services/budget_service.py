# services/budget_service.py
"""
Budget Service Module

This module provides database operations for managing user budgets.
It handles CRUD operations (Create, Read, Update, Delete) for budget records
stored in Firebase Firestore.
"""

from config.firebase_config import db
from models.budget import Budget


class BudgetService:
    """Service class for managing budget-related database operations."""

    @staticmethod
    def create_budget(user_id, category, limit):
        """
        Create a new budget for a user.
        
        Args:
            user_id (str): The ID of the user creating the budget
            category (str): The budget category (e.g., "Food", "Transport")
            limit (float): The spending limit for this budget
        """
        budget = Budget(user_id, category, limit)
        db.collection("budgets").add(budget.to_dict())

    @staticmethod
    def get_user_budgets(user_id):
        """
        Retrieve all budgets for a specific user.
        
        Args:
            user_id (str): The ID of the user
            
        Returns:
            list: A list of budget dictionaries with their document IDs
        """
        docs = db.collection("budgets") \
            .where("user_id", "==", user_id) \
            .stream()
        budgets = []
        for doc in docs:
            data = doc.to_dict()
            data["id"] = doc.id
            budgets.append(data)
        return budgets

    @staticmethod
    def get_budget(bid):
        """
        Retrieve a specific budget by its ID.
        
        Args:
            bid (str): The budget document ID
            
        Returns:
            dict: The budget data with its ID, or None if not found
        """
        doc = db.collection("budgets").document(bid).get()
        if doc.exists:
            data = doc.to_dict()
            data["id"] = bid
            return data
        return None

    @staticmethod
    def update_budget(bid, **kwargs):
        """
        Update specific fields of an existing budget.
        
        Args:
            bid (str): The budget document ID
            **kwargs: Fields to update (e.g., limit=500, category="Food")
        """
        db.collection("budgets").document(bid).update(kwargs)

    @staticmethod
    def delete_budget(bid):
        """
        Delete a budget from the database.
        
        Args:
            bid (str): The budget document ID to delete
        """
        db.collection("budgets").document(bid).delete()
