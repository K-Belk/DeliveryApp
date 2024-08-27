App Description
  An app to manage product deliveries and distribution.


Key features
  CRUD users
  CRUD delivery locations
    - When creating a location do a google places call to get all the info you can
    - Give a place to specify what type of place it is i.e. school, grocery store, ect.
    - Give a way to break up by region of town
  CRUD products
  CRUD individual deliveries of products to location by user

  User can login

  User can get best directions biased on the selected delivery locations

  

  
https://github.com/zhanymkanov/fastapi-best-practices


structure

DeliveryApp
├── backend/
│   ├── src/
│   │   ├── auth/
│   │   │   ├── router.py
│   │   │   ├── schemas.py  # pydantic models
│   │   │   ├── models.py  # db models
│   │   │   ├── dependencies.py
│   │   │   ├── config.py  # local configs
│   │   │   ├── constants.py
│   │   │   ├── exceptions.py
│   │   │   ├── service.py
│   │   │   └── utils.py
│   │   └── deliveries/
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   ├── models.py
│   │   │   ├── dependencies.py
│   │   │   ├── constants.py
│   │   │   ├── exceptions.py
│   │   │   ├── service.py
│   │   │   └── utils.py
│   │   └── delivery_locations/
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   ├── models.py
│   │   │   ├── dependencies.py
│   │   │   ├── constants.py
│   │   │   ├── exceptions.py
│   │   │   ├── service.py
│   │   │   └── utils.py
│   │   └── products/
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   ├── models.py
│   │   │   ├── dependencies.py
│   │   │   ├── constants.py
│   │   │   ├── exceptions.py
│   │   │   ├── service.py
│   │   │   └── utils.py
│   │   ├── database.py  # db connection related stuff
│   │   └── main.py
│   ├── tests/
│   ├── requirements.txt
│   ├── .env
|
├── Frontend/