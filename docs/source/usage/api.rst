API Usage
=========

The most up-to-date API usage can be found at `/docs/`. The following API shows how to use several of the endpoints for the backend and example `curl` calls to interact with the server.

User
----

Basic users can be added from the registration page on the frontend site. Users can alternatively interact with the REST API (which is what the frontend uses).

User login and resource access is based on the `access` and `refresh` strategy where both `access` and `refresh` tokens are used to verify the user. The `access` tokens are typically short-lived, expiring sooner,  and provide access to the server resources. The `refresh` tokens are a bit longer than the `access` tokens for their expiration date and are used to retrieve a new `access` token. The short-lived `access` token is setup for various security reasons, mainly if an attacker gets ahold of the token, the amount of time the attacker can use the token will be limited. Since both the `access` and `refresh` token can both expire, using the `Verification`_ API defined below can be used to check if a token is still valid. The `Refresh`_ API is used to refresh user `access` tokens if the `refresh` token is still valid.

Registration and Authentication
...............................

JSON Web Tokens (JWT) are used for authentication for user login and user actions. To login and perform actions the user must first register an account. The details to do so are listed below. To find out more information about JWT, read `here <https://jwt.io/introduction/>`_ and find the `standard located here <https://tools.ietf.org/rfc/rfc7519.txt>`_.

Registration
++++++++++++

To register users, send data to `/api/register/`.

The following POST format is used to register users.

.. code-block:: json
    :linenos:

    {
        "username": "user1",
        "password": "password1"
    }

Login
+++++

To login users, send data to `/api/login/` which will return an `access` and `refresh` token if the user is valid.

The following POST format is used to login users.

.. code-block:: json
    :linenos:

    {
        "username": "user1",
        "password": "password1"
    }

A valid response will return the following:

.. code-block:: json
    :linenos:

    {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU3NDEyNDg0NywianRpIjoiMDhiYjQxYTQ4ZWVhNDE4YWEzOTEwZWU1YWMxYjY2ZjciLCJ1c2VyX2lkIjoyfQ.cg7NQ8YwVbuX2mVEGg6AFkNVQc7PEs72ohDiOnr2ZPg",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc0MDM4NzQ3LCJqdGkiOiIxYzk4NTM2MGQ3NDA0OWFiYmZkNDQzMDliYjAyMzhkMCIsInVzZXJfaWQiOjJ9.Uz_X2sECClBkfT7p1GyCI8L9buJNVvJ2gxq0VJOBqaM"
    }

Verification
++++++++++++

Verfication is used to ensure that the provided token is still valid. The verification endpoint is located at `/api/verify/` which will return a `200` response if the provided token is valid.

The following POST format is used for token verification:

.. code-block:: json
    :linenos:

    {
        "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTczODg2ODQ0LCJqdGkiOiI5ZjI3MzQxZDIyNGQ0YWIwODRmM2YwYTZmYmNlNWQ4YSIsInVzZXJfaWQiOjJ9.wq9C-a1wJDojXUDGo73fhxQylWVgtmOYNhtEl0Up052"
    }

Refresh
+++++++
