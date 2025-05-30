TITLE: Basic FastAPI Application
DESCRIPTION: This code defines a simple FastAPI application with a single endpoint that returns a JSON response. It imports FastAPI, creates an app instance, and defines a route that returns a dictionary.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/zh-hant/docs/tutorial/first-steps.md#_snippet_0

LANGUAGE: Python
CODE:
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

```

----------------------------------------

TITLE: Defining a Common Dependency Function (Python)
DESCRIPTION: This snippet defines an asynchronous function `common_parameters` that serves as a dependency. It accepts optional query parameters `q` (string), `skip` (integer, default 0), and `limit` (integer, default 100), then returns them as a dictionary. This function encapsulates reusable logic for handling common request parameters.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/en/docs/tutorial/dependencies/index.md#_snippet_0

LANGUAGE: Python
CODE:
```
async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}
```

----------------------------------------

TITLE: Initializing FastAPI Application in Python
DESCRIPTION: This code snippet initializes a basic FastAPI application and defines a single endpoint that returns a JSON response. It imports the FastAPI class, creates an instance of it, and defines a path operation function decorated with `@app.get("/")` to handle GET requests to the root path.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/vi/docs/tutorial/first-steps.md#_snippet_0

LANGUAGE: Python
CODE:
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

----------------------------------------

TITLE: Importing FastAPI
DESCRIPTION: This code snippet shows how to import the FastAPI class from the fastapi package. This is the first step in creating a FastAPI application.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/ru/docs/tutorial/first-steps.md#_snippet_1

LANGUAGE: Python
CODE:
```
from fastapi import FastAPI
```

----------------------------------------

TITLE: Initializing a Basic FastAPI Application with Async Functions
DESCRIPTION: This code initializes a basic FastAPI application with two GET endpoints: one for the root path ('/') and another for '/items/{item_id}'.  It uses `async def` to define the route functions, indicating that they can handle asynchronous operations. The '/items/{item_id}' endpoint takes an integer item_id and an optional string query parameter q.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/tr/docs/index.md#_snippet_3

LANGUAGE: Python
CODE:
```
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

----------------------------------------

TITLE: Creating a Basic FastAPI Application with GET Routes (Python)
DESCRIPTION: This snippet demonstrates how to create a minimal FastAPI application. It shows importing the FastAPI class, creating an app instance, and defining two GET endpoints ('/' and '/items/{item_id}') using the `@app.get` decorator. It illustrates handling path parameters with type hints and optional query parameters, returning JSON responses.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/fa/docs/index.md#_snippet_0

LANGUAGE: Python
CODE:
```
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

LANGUAGE: Python
CODE:
```
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
```

----------------------------------------

TITLE: Creating a Simple FastAPI Application with async def (Python)
DESCRIPTION: Shows an alternative version of the basic FastAPI application example. This snippet uses `async def` for the endpoint functions, which is suitable for applications performing asynchronous operations or I/O-bound tasks. The functionality remains the same as the synchronous version, defining a root and an item endpoint.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/en/docs/index.md#_snippet_2

LANGUAGE: Python
CODE:
```
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

----------------------------------------

TITLE: Installing ASGI Server (Uvicorn) - Console
DESCRIPTION: Command to install an ASGI server like Uvicorn, which is necessary to run a FastAPI application. The `[standard]` extra includes commonly used dependencies for the server.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/he/docs/index.md#_snippet_1

LANGUAGE: Console
CODE:
```
$ pip install "uvicorn[standard]"
```

----------------------------------------

TITLE: Installing FastAPI with Standard Dependencies
DESCRIPTION: This command installs the FastAPI library along with its standard dependencies, including Uvicorn and Pydantic, which are necessary for running a FastAPI application. The "[standard]" extra ensures all common requirements are met for a typical FastAPI project.
SOURCE: https://github.com/fastapi/fastapi/blob/master/README.md#_snippet_0

LANGUAGE: Shell
CODE:
```
$ pip install "fastapi[standard]"
```

----------------------------------------

TITLE: Using `Annotated` for Metadata (Python 3.9+)
DESCRIPTION: Demonstrates the use of `Annotated` from the standard `typing` module in Python 3.9+ to add additional metadata to type hints. The first parameter to `Annotated` is the actual type, while subsequent parameters provide metadata for tools like FastAPI or Pydantic's `Field`.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/en/docs/python-types.md#_snippet_30

LANGUAGE: Python
CODE:
```
from typing import Annotated
from pydantic import BaseModel, Field

class ModelWithAnnotated(BaseModel):
    item_name: Annotated[str, Field(min_length=3, max_length=50)]
```

----------------------------------------

TITLE: Building a FastAPI Docker Image
DESCRIPTION: This Dockerfile defines the steps to build a Docker image for a FastAPI application. It starts from a Python 3.9 base image, sets the working directory, copies `requirements.txt`, installs dependencies, copies the application code, and sets the default command to run the FastAPI application using `fastapi run`. It also includes a commented-out line for running behind a proxy.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/en/docs/deployment/docker.md#_snippet_0

LANGUAGE: Dockerfile
CODE:
```
FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["fastapi", "run", "app/main.py", "--port", "80", "--proxy-headers"]
```

----------------------------------------

TITLE: Basic Dockerfile Configuration for FastAPI
DESCRIPTION: This Dockerfile sets up a FastAPI application within a Docker container. It starts from a Python base image, sets the working directory, copies the requirements file, installs dependencies, copies the application code, and defines the command to run the Uvicorn server.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/ja/docs/deployment/docker.md#_snippet_4

LANGUAGE: Dockerfile
CODE:
```
FROM python:3.9
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
```

----------------------------------------

TITLE: Defining a Basic Endpoint with FastAPI
DESCRIPTION: This code snippet defines a basic FastAPI application with a single endpoint that returns a JSON response. It imports the FastAPI class, creates an instance of it, and defines a route using a decorator.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/pt/docs/tutorial/first-steps.md#_snippet_0

LANGUAGE: Python
CODE:
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

```

----------------------------------------

TITLE: Defining Multiple Pydantic User Models in FastAPI
DESCRIPTION: Demonstrates defining separate Pydantic models for different stages of user data handling (input, output, database). It shows a FastAPI endpoint accepting `UserIn`, hashing the password, creating a `UserInDB` object (using dictionary unpacking), saving it, and returning a `UserOut` object, thus controlling which fields are exposed. This approach is common for handling sensitive data like passwords differently based on context.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/de/docs/tutorial/extra-models.md#_snippet_0

LANGUAGE: Python
CODE:
```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: str
    full_name: str | None = None

class UserOut(BaseModel):
    username: str
    email: str
    full_name: str | None = None

class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: str
    full_name: str | None = None

# Helper functions (fake)
def fake_password_hasher(password: str):
    return "fakehashed" + password

def fake_save_user(user_in_db: UserInDB):
    print(f"Saving user {user_in_db.username} to DB")
    # Simulate saving to DB
    return user_in_db

@app.post("/users/", response_model=UserOut)
def create_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    user_out = fake_save_user(user_in_db)
    return user_out
```

----------------------------------------

TITLE: Installing FastAPI with Standard Dependencies
DESCRIPTION: This command installs FastAPI along with a set of commonly used standard optional dependencies, such as Uvicorn for the server and Pydantic for data validation. It is recommended to execute this command within an activated Python virtual environment to manage project dependencies effectively.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/en/docs/tutorial/index.md#_snippet_1

LANGUAGE: console
CODE:
```
$ pip install "fastapi[standard]"

---> 100%
```

----------------------------------------

TITLE: Including Routers in Main App (Python)
DESCRIPTION: Uses app.include_router() to integrate path operations from APIRouter instances (users.router, items.router) defined in imported modules into the main FastAPI application.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/en/docs/tutorial/bigger-applications.md#_snippet_18

LANGUAGE: Python
CODE:
```
app.include_router(users.router)
app.include_router(items.router)
```

----------------------------------------

TITLE: Creating a Simple FastAPI Application (Python)
DESCRIPTION: Demonstrates a basic FastAPI application structure. It imports necessary components, initializes the app, and defines two simple GET endpoints using decorators: a root path '/' returning a JSON object and an item path '/items/{item_id}' that takes a path parameter and an optional query parameter, using type hints.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/en/docs/index.md#_snippet_1

LANGUAGE: Python
CODE:
```
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

----------------------------------------

TITLE: Creating a FastAPI Instance
DESCRIPTION: This Python code snippet shows how to create an instance of the FastAPI class, which serves as the main entry point for building all APIs. The 'app' variable will be an instance of the FastAPI class.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/id/docs/tutorial/first-steps.md#_snippet_3

LANGUAGE: Python
CODE:
```
app = FastAPI()
```

----------------------------------------

TITLE: Creating a Basic FastAPI Application with Async Endpoints
DESCRIPTION: This Python code illustrates a FastAPI application where endpoint functions are defined using `async def`. This approach is beneficial for I/O-bound operations, allowing the server to handle multiple requests concurrently without blocking, thereby improving performance and responsiveness. It includes a root endpoint and an item endpoint, both asynchronous.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/em/docs/index.md#_snippet_3

LANGUAGE: Python
CODE:
```
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

----------------------------------------

TITLE: Running FastAPI in Development Mode with CLI
DESCRIPTION: This snippet demonstrates how to start a FastAPI application in development mode using the `fastapi dev` command. It shows the console output, including server startup details, documentation links, and the auto-reload feature. This mode is suitable for development due to auto-reloading and listening on localhost.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/en/docs/fastapi-cli.md#_snippet_0

LANGUAGE: Shell
CODE:
```
$ fastapi dev main.py

  FastAPI   Starting development server 🚀

             Searching for package file structure from directories with
             __init__.py files
             Importing from /home/user/code/awesomeapp

    module   🐍 main.py

      code   Importing the FastAPI app object from the module with the
             following code:

             from main import app

       app   Using import string: main:app

    server   Server started at http://127.0.0.1:8000
    server   Documentation at http://127.0.0.1:8000/docs

       tip   Running in development mode, for production use:
             fastapi run

             Logs:

      INFO   Will watch for changes in these directories:
             ['/home/user/code/awesomeapp']
      INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to
             quit)
      INFO   Started reloader process [383138] using WatchFiles
      INFO   Started server process [383153]
      INFO   Waiting for application startup.
      INFO   Application startup complete.
```

----------------------------------------

TITLE: Initializing FastAPI Application
DESCRIPTION: Creates an instance of the FastAPI class, which serves as the main entry point for building the API. This instance is then used to define path operations and handle incoming requests.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/pl/docs/tutorial/first-steps.md#_snippet_2

LANGUAGE: python
CODE:
```
app = FastAPI()
```

----------------------------------------

TITLE: Creating FastAPI Instance
DESCRIPTION: This snippet creates an instance of the FastAPI class, assigning it to the variable app. This app instance serves as the main entry point for creating and interacting with the API.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/uk/docs/tutorial/first-steps.md#_snippet_2

LANGUAGE: python
CODE:
```
app = FastAPI()
```

----------------------------------------

TITLE: Importing FastAPI
DESCRIPTION: This code snippet demonstrates how to import the FastAPI class, which provides the core functionality for building APIs.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/de/docs/tutorial/first-steps.md#_snippet_1

LANGUAGE: Python
CODE:
```
from fastapi import FastAPI
```

----------------------------------------

TITLE: Declaring Basic Path Parameters in FastAPI
DESCRIPTION: This snippet demonstrates how to declare a simple path parameter `item_id` in a FastAPI GET route. The value from the URL path is automatically passed as an argument to the asynchronous function, allowing the API to respond with the received ID.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/en/docs/tutorial/path-params.md#_snippet_0

LANGUAGE: Python
CODE:
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```

----------------------------------------

TITLE: Creating a Basic FastAPI Application
DESCRIPTION: This Python code defines a simple FastAPI application with two HTTP GET endpoints. The root endpoint ('/') returns a basic 'Hello: World' JSON response, while the '/items/{item_id}' endpoint demonstrates how to define path parameters (item_id) and optional query parameters (q), returning them in the response.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/em/docs/index.md#_snippet_2

LANGUAGE: Python
CODE:
```
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

----------------------------------------

TITLE: Annotated Dockerfile for FastAPI
DESCRIPTION: This Dockerfile provides a step-by-step guide to building a FastAPI Docker image, with inline comments explaining each command. It covers selecting a base image, setting the working directory, copying dependencies, installing Python packages, and copying the application code.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/em/docs/deployment/docker.md#_snippet_4

LANGUAGE: Dockerfile
CODE:
```
# (1)
FROM python:3.9

# (2)
WORKDIR /code

# (3)
COPY ./requirements.txt /code/requirements.txt

# (4)
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# (5)
COPY ./app /code/app
```

----------------------------------------

TITLE: Defining a Route with GET Operation
DESCRIPTION: This code snippet demonstrates how to define a route using the @app.get() decorator. This decorator associates a function with a specific URL path ('/') and the HTTP GET operation, indicating that the function should handle GET requests to that path.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/pt/docs/tutorial/first-steps.md#_snippet_3

LANGUAGE: python
CODE:
```
@app.get("/")
async def read_root():
    return {"Hello": "World"}
```

----------------------------------------

TITLE: Running FastAPI Development Server
DESCRIPTION: This command initiates the FastAPI development server, automatically reloading the application upon code changes in `main.py`. It provides a local URL for accessing the API and displays server logs, indicating successful startup and watch directories.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/en/docs/tutorial/index.md#_snippet_0

LANGUAGE: console
CODE:
```
$ fastapi dev main.py

  FastAPI   Starting development server 🚀

             Searching for package file structure from directories
             with __init__.py files
             Importing from /home/user/code/awesomeapp

   module   🐍 main.py

     code   Importing the FastAPI app object from the module with
             the following code:

             from main import app

      app   Using import string: main:app

   server   Server started at http://127.0.0.1:8000
   server   Documentation at http://127.0.0.1:8000/docs

      tip   Running in development mode, for production use:
             fastapi run

             Logs:

     INFO   Will watch for changes in these directories:
             ['/home/user/code/awesomeapp']
     INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C
             to quit)
     INFO   Started reloader process [383138] using WatchFiles
     INFO   Started server process [383153]
     INFO   Waiting for application startup.
     INFO   Application startup complete.
```

----------------------------------------

TITLE: Defining a Path Operation Decorator
DESCRIPTION: This code snippet demonstrates how to define a path operation using the @app.get() decorator, which associates a function with a specific path and HTTP method (GET in this case).
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/de/docs/tutorial/first-steps.md#_snippet_3

LANGUAGE: Python
CODE:
```
@app.get("/")
async def read_root():
    return {"Hello": "World"}
```

----------------------------------------

TITLE: Define Synchronous Path Operation Function
DESCRIPTION: This code snippet defines a synchronous path operation function `def root():` that will be called by FastAPI when it receives a GET request to the `/` URL. It returns a dictionary that FastAPI automatically converts to JSON.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/es/docs/tutorial/first-steps.md#_snippet_6

LANGUAGE: python
CODE:
```
def root():
    return {"message": "Hello World"}
```

----------------------------------------

TITLE: Creating a Basic FastAPI Application
DESCRIPTION: Creates a basic FastAPI application with two endpoints: `/` and `/items/{item_id}`. The `/` endpoint returns a simple JSON response, and the `/items/{item_id}` endpoint returns the item ID and an optional query parameter.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/es/docs/deployment/docker.md#_snippet_3

LANGUAGE: Python
CODE:
```
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

----------------------------------------

TITLE: Type Hinting Optional Values (Union with None)
DESCRIPTION: Shows how to specify that a variable or parameter can be of a certain type or `None`. This is done using `Optional[SomeType]` from `typing` (equivalent to `Union[SomeType, None]`) or `SomeType | None` in Python 3.10+.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/em/docs/python-types.md#_snippet_8

LANGUAGE: Python
CODE:
```
from typing import Optional

def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}")
    else:
        print("Hello World")
```

LANGUAGE: Python
CODE:
```
def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}")
    else:
        print("Hello World")
```

----------------------------------------

TITLE: Creating SQLModel Database Model
DESCRIPTION: Defines a Hero class inheriting from SQLModel, representing a database table. Includes fields for id (primary key), name, secret_name, age, and indexes for optimized querying. The table=True argument specifies that this model represents a database table.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/pt/docs/tutorial/sql-databases.md#_snippet_0

LANGUAGE: Python
CODE:
```
from typing import Optional

from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)
```

----------------------------------------

TITLE: Simple FastAPI App
DESCRIPTION: This is a minimal FastAPI application that defines a single endpoint at the root path ('/'). When accessed, it returns a JSON response containing the message 'Hello World'.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/id/docs/tutorial/first-steps.md#_snippet_0

LANGUAGE: Python
CODE:
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

```

----------------------------------------

TITLE: Importing FastAPI
DESCRIPTION: This code snippet imports the FastAPI class, which is essential for creating a FastAPI application. It provides the core functionality for defining API endpoints and handling requests.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/tr/docs/tutorial/first-steps.md#_snippet_1

LANGUAGE: Python
CODE:
```
from fastapi import FastAPI
```

----------------------------------------

TITLE: Pydantic Model Example (Python 3.9+)
DESCRIPTION: This example demonstrates a Pydantic model definition with type annotations. Pydantic validates data, converts it to the appropriate type, and provides an object with all the data. This snippet is designed for Python 3.9 and above.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/bn/docs/python-types.md#_snippet_21

LANGUAGE: Python
CODE:
```
{!> ../../docs_src/python_types/tutorial011_py39.py!}
```

----------------------------------------

TITLE: Creating a Basic FastAPI Application - Python
DESCRIPTION: Defines a minimal FastAPI application instance and sets up two basic GET endpoints: a root path and an item path that accepts an integer path parameter and an optional string query parameter. Demonstrates using type hints for automatic data validation and documentation. Includes both synchronous (`def`) and asynchronous (`async def`) versions.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/he/docs/index.md#_snippet_2

LANGUAGE: Python
CODE:
```
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

LANGUAGE: Python
CODE:
```
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

----------------------------------------

TITLE: Defining Python Types and Pydantic Models
DESCRIPTION: This snippet demonstrates how to use standard Python type hints for function parameters and define a data model using Pydantic's BaseModel. Pydantic models provide data validation and serialization, leveraging Python's type annotations. It shows a simple function with a typed argument and a `User` model with `int`, `str`, and `date` fields.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/em/docs/features.md#_snippet_0

LANGUAGE: Python
CODE:
```
from datetime import date

from pydantic import BaseModel

# Declare a variable as a str
# and get editor support inside the function
def main(user_id: str):
    return user_id


# A Pydantic model
class User(BaseModel):
    id: int
    name: str
    joined: date
```

----------------------------------------

TITLE: Defining an Asynchronous Path Operation Function
DESCRIPTION: This code snippet defines an asynchronous path operation function that handles GET requests to the root path ('/'). It returns a dictionary, which FastAPI automatically converts to JSON. This function is decorated with @app.get("/") to associate it with the GET operation on the root path.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/ru/docs/tutorial/first-steps.md#_snippet_5

LANGUAGE: Python
CODE:
```
async def root():
    return {"message": "Hello World"}
```

----------------------------------------

TITLE: Installing FastAPI with pip
DESCRIPTION: This command installs the FastAPI library using pip, the Python package installer. It allows you to start developing web APIs with FastAPI.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/ru/docs/index.md#_snippet_0

LANGUAGE: console
CODE:
```
$ pip install fastapi
```

----------------------------------------

TITLE: Creating an Asynchronous FastAPI Application
DESCRIPTION: This code snippet demonstrates how to create an asynchronous FastAPI application using `async def` for the route functions. This is useful when dealing with I/O-bound operations. It includes two GET endpoints: one for the root path ('/') and another for '/items/{item_id}'. The '/items/{item_id}' endpoint includes a path parameter 'item_id' and an optional query parameter 'q'.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/nl/docs/index.md#_snippet_2

LANGUAGE: Python
CODE:
```
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

----------------------------------------

TITLE: Installing FastAPI with Standard Dependencies (Shell)
DESCRIPTION: Installs FastAPI along with its 'standard' group of optional dependencies, which include packages like `email-validator` for Pydantic, `httpx`, `jinja2`, `python-multipart` for Starlette, and `uvicorn` for serving the application.
SOURCE: https://github.com/fastapi/fastapi/blob/master/README.md#_snippet_9

LANGUAGE: Shell
CODE:
```
pip install "fastapi[standard]"
```

----------------------------------------

TITLE: Initializing FastAPI App with Basic Endpoints
DESCRIPTION: This code initializes a FastAPI application and defines two GET endpoints: one for the root path ('/') that returns a simple JSON response, and another for '/items/{item_id}' that accepts an integer path parameter 'item_id' and an optional string query parameter 'q'.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/ru/docs/index.md#_snippet_2

LANGUAGE: Python
CODE:
```
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

----------------------------------------

TITLE: Running FastAPI Application with Uvicorn
DESCRIPTION: This command starts the FastAPI application using Uvicorn, a fast ASGI server. The `--reload` flag enables automatic server reloading upon code changes, which is highly beneficial during development. The application typically becomes accessible at `http://127.0.0.1:8000`.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/em/docs/tutorial/index.md#_snippet_0

LANGUAGE: Shell
CODE:
```
uvicorn main:app --reload
```

----------------------------------------

TITLE: Running FastAPI Application with Uvicorn
DESCRIPTION: This command starts the FastAPI application using Uvicorn, a fast ASGI server. `main:app` specifies the `app` instance from `main.py`. The `--reload` flag enables automatic server restart on code changes, which is highly useful for development.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/em/docs/tutorial/first-steps.md#_snippet_0

LANGUAGE: console
CODE:
```
$ uvicorn main:app --reload

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
<span style="color: green;">INFO</span>:     Started reloader process [28720]
<span style="color: green;">INFO</span>:     Started server process [28722]
<span style="color: green;">INFO</span>:     Waiting for application startup.
<span style="color: green;">INFO</span>:     Application startup complete.
```

----------------------------------------

TITLE: Defining a GET path operation in FastAPI
DESCRIPTION: This snippet shows how to define a GET path operation in FastAPI using the `@app.get()` decorator. It demonstrates how to create an endpoint that returns a JSON response.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/ru/docs/alternatives.md#_snippet_1

LANGUAGE: Python
CODE:
```
@app.get("/some/url")
def read_url():
    return {"message": "Hello World"}
```

----------------------------------------

TITLE: Defining Path Operation Decorator with FastAPI
DESCRIPTION: This code snippet demonstrates how to define a path operation decorator using `@app.get("/")` in FastAPI. It associates the function below with handling GET requests to the root path ("/").
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/uk/docs/tutorial/first-steps.md#_snippet_4

LANGUAGE: Python
CODE:
```
@app.get("/")
```

----------------------------------------

TITLE: Running FastAPI Dev Server (Console)
DESCRIPTION: This command starts the FastAPI application in development mode using Uvicorn. It automatically detects the FastAPI app object in the specified file and enables auto-reloading on code changes.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/es/docs/index.md#_snippet_0

LANGUAGE: console
CODE:
```
$ fastapi dev main.py

 ╭────────── FastAPI CLI - Development mode ───────────╮
 │                                                     │
 │  Serving at: http://127.0.0.1:8000                  │
 │                                                     │
 │  Running in development mode, for production use:   │
 │                                                     │
 │  fastapi run                                        │
 │                                                     │
 ╰─────────────────────────────────────────────────────╯

INFO:     Will watch for changes in these directories: ['/home/user/code/awesomeapp']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2248755] using WatchFiles
INFO:     Started server process [2248757]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

----------------------------------------

TITLE: Running FastAPI Application in Development Mode
DESCRIPTION: This console command starts the FastAPI development server. The `fastapi dev` command automatically reloads the application on code changes, making it convenient for development. The server typically runs on `http://127.0.0.1:8000`.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/en/docs/advanced/websockets.md#_snippet_4

LANGUAGE: console
CODE:
```
$ fastapi dev main.py
```

----------------------------------------

TITLE: Setting a Dependency Override in FastAPI for Testing
DESCRIPTION: This snippet demonstrates how to set a dependency override in a FastAPI application. It assigns a new override function to an original dependency within the `app.dependency_overrides` dictionary, ensuring the override is used instead of the original during tests.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/en/docs/advanced/testing-dependencies.md#_snippet_0

LANGUAGE: Python
CODE:
```
app.dependency_overrides[original_dependency_function] = override_dependency_function
```

----------------------------------------

TITLE: Creating a basic FastAPI application
DESCRIPTION: This code creates a basic FastAPI application with two endpoints: `/` which returns a simple greeting, and `/items/{item_id}` which returns the item ID and an optional query parameter. It demonstrates the basic structure of a FastAPI application, including importing FastAPI, creating an app instance, and defining routes using decorators.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/zh/docs/index.md#_snippet_2

LANGUAGE: Python
CODE:
```
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

----------------------------------------

TITLE: Creating an async FastAPI application
DESCRIPTION: This code defines a basic FastAPI application with two asynchronous endpoints: `/` which returns a simple JSON response, and `/items/{item_id}` which takes an item ID as a path parameter and an optional query parameter `q`.  It uses `async def` to define the functions.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/ja/docs/index.md#_snippet_3

LANGUAGE: Python
CODE:
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

----------------------------------------

TITLE: Installing FastAPI with Standard Extras (Shell)
DESCRIPTION: Provides the command-line instruction to install the FastAPI library using pip, including the '[standard]' extra which typically pulls in necessary dependencies like an ASGI server (e.g., Uvicorn) for running the application. The command needs to be run in a virtual environment.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/en/docs/index.md#_snippet_0

LANGUAGE: Shell
CODE:
```
pip install "fastapi[standard]"

---> 100%
```

----------------------------------------

TITLE: Creating an Asynchronous FastAPI Application
DESCRIPTION: This code defines a simple FastAPI application with two asynchronous endpoints: `/` which returns a greeting, and `/items/{item_id}` which returns an item ID and an optional query parameter. It demonstrates the basic structure of a FastAPI application, including importing necessary modules, creating an app instance, and defining API endpoints using decorators.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/ko/docs/index.md#_snippet_3

LANGUAGE: Python
CODE:
```
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

----------------------------------------

TITLE: Initializing FastAPI App with Async Endpoints
DESCRIPTION: This code initializes a FastAPI application and defines two GET endpoints using `async def`: one for the root path ('/') that returns a simple JSON response, and another for '/items/{item_id}' that accepts an integer path parameter 'item_id' and an optional string query parameter 'q'. The use of `async def` allows for asynchronous request handling.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/ru/docs/index.md#_snippet_3

LANGUAGE: Python
CODE:
```
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

----------------------------------------

TITLE: Running FastAPI Application with Uvicorn
DESCRIPTION: This console command initiates the FastAPI application using fastapi dev, which internally uses Uvicorn. It starts a development server, making the application accessible at http://127.0.0.1:8000. This command is essential for testing and running FastAPI applications locally.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/en/docs/advanced/sub-applications.md#_snippet_3

LANGUAGE: Console
CODE:
```
fastapi dev main.py
```

----------------------------------------

TITLE: Sub-dependencies with Yield (Python 3.9+)
DESCRIPTION: Illustrates how to create nested dependencies with `yield`, where one dependency relies on another. FastAPI ensures that the exit code in each dependency with `yield` is executed in the correct order. This example uses Python 3.9+ syntax with Annotated.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/pt/docs/tutorial/dependencies/dependencies-with-yield.md#_snippet_2

LANGUAGE: python
CODE:
```
from typing import Annotated, Generator

from fastapi import Depends, FastAPI

app = FastAPI()


async def dependency_a() -> Generator[str, None, None]:
    yield "dependency_a"


async def dependency_b(dep_a: Annotated[str, Depends(dependency_a)]) -> Generator[str, None, None]:
    yield f"dependency_b with {dep_a}"


async def dependency_c(dep_b: Annotated[str, Depends(dependency_b)]) -> str:
    return f"dependency_c with {dep_b}"


@app.get("/items/")
async def read_items(dep_c: Annotated[str, Depends(dependency_c)]):
    return dep_c
```

----------------------------------------

TITLE: Install Uvicorn with standard extras using pip
DESCRIPTION: This command installs Uvicorn, an ASGI server, using pip. The `[standard]` extra installs commonly used dependencies for Uvicorn.
SOURCE: https://github.com/fastapi/fastapi/blob/master/docs/de/docs/index.md#_snippet_1

LANGUAGE: console
CODE:
```
$ pip install "uvicorn[standard]"
```