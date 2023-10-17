"""
Singleton Utility Module

This module provides a simple utility class for implementing the Singleton design pattern.
It ensures that only one instance of a class exists at any given time, and it provides a
mechanism to access that instance.
"""


class SingletonInstance:
    """
    A base class for implementing the Singleton design pattern.

    This utility ensures that only one instance of a class exists at any given time,
    and it provides a mechanism to access or create that instance.

    Usage:
    To make a class a Singleton, inherit from SingletonInstance, and then use the 'instance'
    class method to access or create the Singleton instance.

    Example:
        class MySingleton(SingletonInstance):
            # Your class implementation here

        my_instance = MySingleton.instance()
    """

    __instance = None

    @classmethod
    def __get_instance(cls):
        """
        Get the existing Singleton instance.

        Returns:
            object: The existing Singleton instance if it exists, or None if not.
        """
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kwargs):
        """
        Access or create the Singleton instance.

        If an instance already exists, it returns that instance; otherwise, it creates
        a new instance with the provided arguments.

        Args:
            *args: Positional arguments for the initialization of the Singleton class.
            **kwargs: Keyword arguments for the initialization of the Singleton class.

        Returns:
            object: The Singleton instance.
        """
        cls.__instance = cls(*args, **kwargs)
        cls.instance = cls.__get_instance
        return cls.__instance
