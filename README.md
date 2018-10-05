[![Build Status](https://travis-ci.com/fabischolasi/fast-food-fast-v1.svg?branch=ch-test-orders-160876756)](https://travis-ci.com/fabischolasi/fast-food-fast-v1) [![Coverage Status](https://coveralls.io/repos/github/fabischolasi/fast-food-fast-v1/badge.svg?branch=ch-test-orders-160876756)](https://coveralls.io/github/fabischolasi/fast-food-fast-v1?branch=ch-test-orders-160876756) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



# Fast-Food-Fast

Fast-Food-Fast is an application that allows users(customers) order their favorite meals online and get deliveries in time

![Home Image](https://raw.github.com/fabischolasi/fast-food-fast/develop/UI/static/css/img/pizza.jpg)

## Getting Started

This will give you guidance on how you can run the program on your machine and test it in development and testing mode configurations

### Prerequisites

* Git
* Python 3.6.6
* Virtualenv
* Flask

### Quick Start

1. Clone the repository

```
$ git clone https://github.com/fabischolasi/fast-food-fast-v1.git
$ cd <dir>
```

2. Initialize git and activate a virtualenv

```
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

3. Install the dependencies

```
$ pip install -r requirements.txt
```

4. Run the development server

```
$ python run.py
```

5. Navigate to [http://localhost:5000]

At the / endpoint you should see Welcome to Fast-Food-Fast API displayed in your browser.

## API Endpoints version 1

Here are the projects api endpoints

Endpoint | Functionality
------------ | -------------
POST   /api/v1/auth/signup | Register a user
POST   /api/v1/auth/login | Signin user
GET    /api/v1/users | Get all users
GET   /api/v1/users/id | Get unique user
PUT  /api/v1/users/id | Update unique user
DELETE   /api/v1/users/id | Delete  unique user
POST   /api/v1/meals | Create new meal
GET   /api/v1/meals | Get all meals
GET   /api/v1/meals/id | Get unique meal
PUT   /api/v1/meals/id | Update unique meal
DELETE   /api/v1/meals/id | Delete unique meal
POST   /api/v1/menu | Create new menu option
GET   /api/v1/menu | Get all menu options
GET   /api/v1/menu/id | Get a unique menu option
PUT   /api/v1/menu/id | Update a unique menu option
DELETE   /api/v1/menu/id | Delete a unique menu option
POST   /api/v1/orders | Create new order
GET   /api/v1/orders | Get all orders
GET   /api/v1/orders/id | Get a unique order
PUT   /api/v1/orders/id | Update a unique order
DELETE   /api/v1/orders/id | Delete unique order


## API Endpoints version 2


Endpoint                     | Functionality
---------------------------- | -------------------------------------------------
POST   /api/v2/auth/signup   | Register a user
POST   /api/v2/auth/login    | Log in user
GET    /api/v2/users         | Admin to view all users
PUT    /api/v2/users/id      | Admin to promote another user
POST   /api/v2/meals         | Admin to add meal in the system
GET    /api/v2/meals         | Admin to view all meals in the system
PUT    /api/v2/meals/id      | Admin to update a particular meal in the system
DELETE /api/v2/meals/id      | Admin to delete a particular meal from the system
POST   /api/v2/user/orders   | User to post an order
GET    /api/v2/user/orders   | User to view their orders
GET    /api/v2/user/orders/id| User to view a particular order
DELETE /api/v2/user/orders/id| User to delete a particular order
POST   /api/v2/menu          | Admin to add meal to menu
GET    /api/v2/menu          | Anyone to view menu
GET    /api/v2/menu/id       | Anyone to filter and view a particular menu
DELETE /api/v2/menu/id       | Admin to remove meal item from menu 
GET    /api/v2/orders        | Admin to view all orders
GET    /api/v2/orders/id     | Admin to view a particular order
PUT    /api/v2/orders/id     | Admin to update a particular order

## Running the tests

```
<top-dir> pytest
```

### And coding style tests

Coding styles tests are tests that ensure conformity to coding style guides. In our case, they test conformity to
PEP 8 style guides

```
pylint app
```

## Deployment

Ensure you use Production config settings where DEBUG=False

## Built With

* HTML5
* CSS3
* Python 3.6.6
* Flask - Server

## GitHub pages

[Github Pages](https://fabischolasi.github.io/fast-food-fast/UI/index.html)

## Heroku for version one

[Heroku](https://fast-food-fast-api-97.herokuapp.com)

## Heroku for version two

[Heroku](https://fast-food-fast-v2-api.herokuapp.com/)


## Versioning

Version 1 & 2Github Pages

## Authors

Fabisch Enock

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
