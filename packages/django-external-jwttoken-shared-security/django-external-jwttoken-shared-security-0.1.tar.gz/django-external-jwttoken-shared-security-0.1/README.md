
# External JWT Token Shared Security


This django app is used to manage django auth using a token from a external source.
Like a auth microservice


## Quick start

1. Add "shared_security" to your INSTALLED_APPS setting like this:
    ```
    INSTALLED_APPS = [
        ...
        'shared_security',
    ]
    ```

2. Add on your django projects settings a var named JWT_SECRET_KEY with the secret key of your external jwt generator source. We recommend using
   a environment variable instead of writing to code directly on settings.py for security reasons

3. Include the shared_security URLconf in your project urls.py like this:

    `path('token/', include('shared_security.api.urls')),`

4. Start the django development server.



5. To use the authentication on your API

    * Add the authentication class on REST_FRAMEWORK variable on django rest framework settings as:
    
        ```
        REST_FRAMEWORK = {
            ...

            'DEFAULT_AUTHENTICATION_CLASSES': [
                "shared_security.authentication.ExternalTokenAuthentication",
            ],
            ...
        }
        ```

    * Add to specific django rest view as:
        ```
        from shared_security.authentication import ExternalTokenAuthentication

        class YourView(viewsets.ViewSet):
        """
        A awesome view
        """

        authentication_classes = [ExternalTokenAuthentication,]

        ...
        ```

6. Visit http://127.0.0.1:8000/security/user passing on header Authentication Bearer <external_jwt_token> to get user 
    info using decode data from token.


## Configuration Vars

**SECURITY_USE_PERSISTENT_USERS:** Boolean var to specify if you want to use your auth with the creation and update of users 
on the database. Important to use the django admin application the vars need to be set to true.