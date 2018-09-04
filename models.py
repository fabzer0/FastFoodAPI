"""
Dummy storage for Users, Meals and Orders
"""

all_users = {}
user_count = 1

all_meals = {}
meal_count = 1

all_menu = {}
menu_count = 1

all_orders = {}
order_count = 1


class User(object):
    """
    Contains the methods to add, update and delete a user
    """

    @staticmethod
    def create_user(username, email, password, admin=False, **kwargs):
        """
        Creates a new user and appends his information to all_users dictionary
        """
        global all_users
        global user_count
        all_users[user_count] = {
             "id" : user_count,
             "username" : username,
             "email" : email,
             "password" : password,
             "admin" : admin
        }
        new_user = all_users[user_count]
        user_count += 1
        return new_user

    @staticmethod
    def update_user(user_id, username, email, password, admin=False, **kwargs):
        """
        Updates user information
        """
        if user_id in all_users.keys():
            all_users[user_id] = {
                "id" : user_id,
                "username" : username,
                "email" : email,
                "password" : password,
                "admin" : admin
            }
            return all_users[user_id]
        return {"message" : "user does not exist"}

    @staticmethod
    def delete_user(user_id):
        """
        Deletes an existing user
        """
        try:
            del all_users[user_id]
            return {"message" : "user successfully deleted"}
        except KeyError:
            return {"message" : "user does not exist"}
