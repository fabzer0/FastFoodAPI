[![Build Status](https://travis-ci.com/fabischolasi/fast-food-fast-v1.svg?branch=ch-test-orders-160876756)](https://travis-ci.com/fabischolasi/fast-food-fast-v1) [![Coverage Status](https://coveralls.io/repos/github/fabischolasi/fast-food-fast-v1/badge.svg?branch=ch-test-orders-160876756)](https://coveralls.io/github/fabischolasi/fast-food-fast-v1?branch=ch-test-orders-160876756) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Fast Food Fast

Fast Food Fast is an application that allows customers to make food orders online

![Home Image](https://raw.github.com/fabischolasi/fast-food-fast/develop/UI/static/css/img/pizza.jpg)

### Prerequisites

* Git
* Python 3.6.4
* Virtualenv
* Postgres

### Installation

1. Clone the repository:

```
$ git clone https://github.com/fabischolasi/fast-food-fast-v1.git
```

2. Initialize and activate a virtualenv

```
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

3. Install postgres together with its dependencies
```
$ sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
```

4. Install the dependencies

```
$ pip install -r requirements.txt
```

5. Initialize environment variables

```
$ export SECRET_KEY=<SECRET KEY>
$ export TESTING_URI=<PATH/TO/DB>
$ export DATABASE_URI=<PATH/TO/DB>
```

6. Run the development server. This will initialize db and create all tables

```
$ python run.py
```

5. Navigate to [http://localhost:5000](http://localhost:5000)

At the / endpoint you should see Welcome to Welcome to Fast Food Fast Version 2.

## Endpoints


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

1. On the root folder run:
```
$ pytest
```

## Pep 8 style guides

```
pylint app
```

## Deployment

Ensure you use ProductionEnv settings where DEBUG is False

## Built With

* CSS3
* Python 3.6.4
* Flask - The web framework used

## GitHub pages

[GitHub](https://fabischolasi.github.io/fast-food-fast/UI/index.html)

## Heroku

[Heroku](https://fast-food-fast-v2-api.herokuapp.com/)

## Version

 2

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
