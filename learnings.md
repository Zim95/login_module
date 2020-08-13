OAUTH Theory:
=============
1. Roles:
---------
Four roles:
    a. Resource Owner - End user (is called resource owner because he/she owns some resource. e.g. profile)
    b. Resource Server - Server hosting the resource.
    c. Client - The application which makes the request.
    d. Authorization Server - AUTH server (This is what we will be building)

2. Basic Idea:
--------------
Resource Owner uses Client to get access tokens. The client then makes a request to resource server using the access token
and get's the requested resource.

We are going to build AUTH server and register our Client on it.

This means the client is now able to retrieve access tokens. This access token is only available after successful authorization, therefore, if the access token is valid, it means that authorization was successful and that the resource can be accessed.

3. 