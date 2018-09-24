"""
Dummy storage for Users, Meals, Menus and Orders
"""

ALL_USERS = {}
USER_COUNT = 1

ALL_MEALS = {}
MEAL_COUNT = 1

ALL_MENU = {}
MENU_COUNT = 1

ALL_ORDERS = {}
ORDER_COUNT = 1


class User:
    """
    Contains the methods to add, update and delete a user
    """

    @staticmethod
    def create_user(username, email, password, admin=False, **kwargs):
        """
        Creates a new user and appends his information to all_users dictionary
        """
        global ALL_USERS
        global USER_COUNT
        ALL_USERS[USER_COUNT] = {
            "id" : USER_COUNT,
            "username" : username,
            "email" : email,
            "password" : password,
            "admin" : admin
        }
        new_user = ALL_USERS[USER_COUNT]
        USER_COUNT += 1
        return new_user

    @staticmethod
    def update_user(user_id, username, email, password, admin=False, **kwargs):
        """
        Updates user information
        """
        if user_id in ALL_USERS.keys():
            ALL_USERS[user_id] = {
                "id" : user_id,
                "username" : username,
                "email" : email,
                "password" : password,
                "admin" : admin
            }
            return ALL_USERS[user_id]
        return {"message" : "user does not exist"}

    @staticmethod
    def delete_user(user_id):
        """
        Deletes an existing user
        """
        try:
            del ALL_USERS[user_id]
            return {"message" : "user successfully deleted"}
        except KeyError:
            return {"message" : "user does not exist"}

class Meal:
    """
    Contains methods to add, update and delete meal item
    """

    @staticmethod
    def create_meal(meal_item, price, **kwargs):
        """
        Creates a new meal item and appends it to the all_meals dictionary
        """
        global ALL_MEALS
        global MEAL_COUNT
        ALL_MEALS[MEAL_COUNT] = {
            "id" : MEAL_COUNT,
            "meal_item" : meal_item,
            "price" : price
        }
        new_meal = ALL_MEALS[MEAL_COUNT]
        MEAL_COUNT += 1
        return new_meal

    @staticmethod
    def update_meal(meal_id, meal_item, price, **kwargs):
        """
        Updates meal item information
        """
        if meal_id in ALL_MEALS.keys():
            ALL_MEALS[meal_id] = {
                "id" : meal_id,
                "meal_item" : meal_item,
                "price" : price
            }
            return ALL_MEALS[meal_id]
        return {"message" : "meal item does not exist"}

    @staticmethod
    def delete_meal(meal_id):
        """
        Deletes a meal from the dictionary
        """
        try:
            del ALL_MEALS[meal_id]
            return {"message" : "meal item successfully deleted"}
        except KeyError:
            return {"message" : "meal item does not exist"}


class Menu:
    """
    Contains methods to add, update and delete menu options
    """

    @staticmethod
    def create_menu(menu_option, price, **kwargs):
        """
        Creates a new menu option and appends it to all_menu dictionary
        """
        global ALL_MENU
        global MENU_COUNT
        ALL_MENU[MENU_COUNT] = {
            "id" : MENU_COUNT,
            "menu_option" : menu_option,
            "price" : price
        }
        new_menu_option = ALL_MENU[MENU_COUNT]
        MENU_COUNT += 1
        return new_menu_option

    @staticmethod
    def update_menu(menu_id, menu_option, price, **kwargs):
        """
        Updates menu option existing information
        """
        if menu_id in ALL_MENU.keys():
            ALL_MENU[menu_id] = {
                "id" : menu_id,
                "menu_option" : menu_option,
                "price" : price
            }
            return ALL_MENU[menu_id]
        return {"message" : "menu options does not exist"}

    @staticmethod
    def delete_menu(menu_id):
        """
        Deletes a menu option from the menu
        """

        try:
            del ALL_MENU[menu_id]
            return {"message" : "menu option successfully deleted"}
        except KeyError:
            return {"message" : "menu option does not exist"}


class Order:
    """
    Contains methods that add, update and delete orders
    """

    @staticmethod
    def create_order(order_item, price, status, **kwargs):
        """
        Creates a new order and appends this information to all_orders dictionary
        """
        global ALL_ORDERS
        global ORDER_COUNT
        ALL_ORDERS[ORDER_COUNT] = {
            "id" : ORDER_COUNT,
            "order_item" : order_item,
            "price" : price,
            "status": status
        }
        new_order = ALL_ORDERS[ORDER_COUNT]
        ORDER_COUNT += 1
        return new_order


    @staticmethod
    def update_order(order_id, status):
        """
        Updates order information
        """
        if order_id in ALL_ORDERS.keys():
            ALL_ORDERS[order_id]['status'] = status    
            return ALL_ORDERS[order_id]
        return {"message" : "order item does not exist"}

    @staticmethod
    def delete_order(order_id):
        """
        This methods allow deletion of orders
        """
        try:
            del ALL_ORDERS[order_id]
            return {"message" : "order item successfully deleted"}
        except KeyError:
            return {"message" : "order item does not exist"}
