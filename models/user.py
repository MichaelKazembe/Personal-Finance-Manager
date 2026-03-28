# models/user.py
"""
User Model Module

This module defines the User class which represents a user in the Personal
Finance Manager application. It stores basic user information including
identification and contact details.
"""


class User:
    """
    User model class representing an application user.
    
    Attributes:
        user_id (str): The unique identifier for the user (Firebase UID)
        email (str): The user's email address used for authentication
    """
    def __init__(self, user_id, email):
        """
        Initialize a new User instance.
        
        Args:
            user_id (str): The unique identifier for the user (typically from Firebase)
            email (str): The user's email address for authentication and communication
        """
        self.user_id = user_id
        self.email = email

    def to_dict(self):
        """
        Convert the User object to a dictionary for storage or serialization.
        
        Returns:
            dict: A dictionary containing all user attributes:
                - user_id: The user's unique identifier
                - email: The user's email address
        """
        return {
            "user_id": self.user_id,
            "email": self.email
        }