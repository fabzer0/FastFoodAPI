[![Build Status](https://travis-ci.com/fabischapeli/fast-food-fast-v1.svg?branch=develop-v1)](https://travis-ci.com/fabischapeli/fast-food-fast-v1) [![Coverage Status](https://coveralls.io/repos/github/fabischapeli/fast-food-fast-v1/badge.svg?branch=develop-v1)](https://coveralls.io/github/fabischapeli/fast-food-fast-v1?branch=develop-v1) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



# Fast-Food-Fast

Fast-Food-Fast is an application that allows users(customers) order their favorite meals online and get deliveries in time

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
$ git clone https://github.com/fabischapeli/fast-food-fast-v1.git
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
$ python app.py
```

5. Navigate to [http://localhost:5000](http://localhost:5000)

At the / endpoint you should see Welcome to Fast-Food-Fast API displayed in your browser.

## API Endpoints

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

## Running the tests

```
<top-dir> pytest
```

### And coding style tests

Coding styles tests are tests that ensure conformity to coding style guides. In our case, they test conformity to
PEP 8 style guides

```
pylint app.py
```

## Deployment

Ensure you use Production config settings where DEBUG=False

## Built With

* HTML5
* CSS3
* Python 3.6.6
* Flask - Server

## GitHub pages

https://fabischapeli.github.io/fast-food-fast/UI/index.html

## Heroku

https://fast-food-fast-api-97.herokuapp.com

## Versioning

Version 1

## Authors

Fabisch Enock

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
