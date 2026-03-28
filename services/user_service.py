# services/user_service.py
"""
User Service Module

This module provides authentication and user management operations.
It handles user registration, login, and user data storage in Firebase
Firestore and Firebase Authentication services.
"""

from config.firebase_config import auth, db
from models.user import User


class UserService:
    """Service class for managing user authentication and profile operations."""

    @staticmethod
    def register(email, password):
        """
        Register a new user with email and password.
        
        Creates a new Firebase Authentication account and stores the user
        information in the Firestore database.
        
        Args:
            email (str): The user's email address
            password (str): The user's password
            
        Returns:
            User: A User object containing the newly created user's information
            
        Raises:
            Exception: If email is already registered or password is invalid
        """
        user = auth.create_user_with_email_and_password(email, password)
        user_id = user['localId']

        new_user = User(user_id, email)
        db.collection("users").document(user_id).set(new_user.to_dict())

        return new_user

    @staticmethod
    def login(email, password):
        """
        Authenticate a user with email and password.
        
        Validates the user's credentials against Firebase Authentication
        and returns authentication tokens for the session.
        
        Args:
            email (str): The user's email address
            password (str): The user's password
            
        Returns:
            dict: Authentication response containing user ID, token, and session information
            
        Raises:
            Exception: If email/password combination is invalid or user doesn't exist
        """
        return auth.sign_in_with_email_and_password(email, password)