"""
Dummy storage for Users, Meals, Menus and Orders
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

class Meal(object):
    """
    Contains methods to add, update and delete meal item
    """

    @staticmethod
    def create_meal(meal_item, price, **kwargs):
        """
        Creates a new meal item and appends it to the all_meals dictionary
        """
        global all_meals
        global meal_count
        all_meals[meal_count] = {
            "id" : meal_count,
            "meal_item" : meal_item,
            "price" : price
        }
        new_meal = all_meals[meal_count]
        meal_count += 1
        return new_meal

    @staticmethod
    def update_meal(meal_id, meal_item, price, **kwargs):
        """
        Updates meal item information
        """
        if meal_id in all_meals.keys():
            all_meals[meal_id] = {
                "id" : meal_id,
                "meal_item" : meal_item,
                "price" : price
            }
            return all_meals[meal_id]
        return {"message" : "meal item does not exist"}

    @staticmethod
    def delete_meal(meal_id):
        """
        Deletes a meal from the dictionary
        """
        try:
            del all_meals[meal_id]
            return {"message" : "meal item successfully deleted"}
        except KeyError:
            return {"message" : "meal item does not exist"}


class Menu(object):
    """
    Contains methods to add, update and delete menu options
    """

    @staticmethod
    def create_menu(menu_option, price, **kwargs):
        """
        Creates a new menu option and appends it to all_menu dictionary
        """
        global all_menu
        global menu_count
        all_menu[menu_count] = {
            "id" : menu_count,
            "menu_option" : menu_option,
            "price" : price
        }
        new_menu_option = all_menu[menu_count]
        menu_count += 1
        return new_menu_option

    @staticmethod
    def update_menu(menu_id, menu_option, price, **kwargs):
        """
        Updates menu option existing information
        """
        if menu_id in all_menu.keys():
            all_menu[menu_id] = {
                "id" : menu_id,
                "menu_option" : menu_option,
                "price" : price
            }
            return all_menu[menu_id]
        return {"message" : "menu options does not exist"}

    @staticmethod
    def delete_menu(menu_id):
        """
        Deletes a menu option from the menu
        """

        try:
            del all_menu[menu_id]
            return {"message" : "menu option successfully deleted"}
        except KeyError:
            return {"message" : "menu option does not exist"}


class Order(object):
    """
    Contains methods that add, update and delete orders
    """

    @staticmethod
    def create_order(order_item, price, **kwargs):
        """
        Creates a new order and appends this information to all_orders dictionary
        """
        global all_orders
        global order_count
        all_orders[order_count] = {
            "id" : order_count,
            "order_item" : order_item,
            "price" : price
        }
        new_order = all_orders[order_count]
        order_count += 1
        return new_order


    @staticmethod
    def update_order(order_id, order_item, price, **kwargs):
        """
        Updates order information
        """
        if order_id in all_orders.keys():
            all_orders[order_id] = {
                "id" : order_id,
                "order_item" : order_item,
                "price" : price
            }
            return all_orders[order_id]
        return {"message" : "order item does not exist"}

    @staticmethod
    def delete_order(order_id):
        try:
            del all_orders[order_id]
            return {"message" : "order item successfully deleted"}
        except KeyError:
            return {"message" : "order item does not exist"}
