# CTFd API Documentation

## Getting Started

The CTFd REST API is the underlying resource that powers almost all CTFd interactions. Most behaviors that are available within CTFd can be done using the REST API.

The REST API is considered stable however the ergonomics of certain behaviors can be improved and some endpoints may change in format to improve performance (e.g. adding pagination).

The following document discusses how to begin interacting with the CTFd API.

## API Access

The API can be used by any user but only admin level users can perform most management actions. To begin interacting with the API it's recommended to have an Admin CTFd user.

## API Request Requirements

In order to communicate with the REST API your request must have:

- a **valid method**
- an **available API endpoint**
- an **admin access token**
- the correct **request headers**
- the appropriate **payload structure** (if applicable)

### Endpoint Methods

In general the API uses the following HTTP request methods:

- **GET** - To access resource data
- **POST** - To create resource data
- **PATCH** - To edit resource data
- **DELETE** - To delete a resource

## API Endpoint Documentation

The list of available endpoints along with their responses and error codes is available in the official CTFd API documentation.

## Access Token

The CTFd API expects the access token on every request it receives. It should be appended on the **Authorization** header in this format: `Authorization: Token <access token>`. For example:

```bash
curl -X GET https://demo.ctfd.io/api/v1/challenges \
  --header "Authorization: Token e8v6d87f6ef9hhe3a0k976g3d7h6d5d9j7g56h7g9h9h8j4qs0b9g" \
  --header "Content-Type: application/json" \
```

### Generating an Admin Access Token

1. Go to the "Settings" page of your user, `/settings`.

2. Click on the "Access Tokens" tab.

3. Set an expiration for the token (the default is 30 days) and click "Generate".

4. You will receive an Access Token that you should copy and save.

## Request Headers

The CTFd API expects the following headers:

- **Authorization** header with `Token {access_token}`. For example: `Authorization: Token <access token>`

- **Content-Type** representation header set to `application/json` (only required if the request has a JSON payload)

## Request Payload

For endpoints that require a payload, refer to the API endpoint documentation on how to add the appropriate JSON payload structure.

## API Usage

You can send requests to the API using different HTTP tools. Check out the tutorial on how to use the CTFd API using **curl** and the **requests** Python library.

---

*Last Updated: 2025*
