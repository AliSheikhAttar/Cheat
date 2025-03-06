Yes, that's correct! In token-based authentication, such as with JSON Web Tokens (JWT), the client doesn’t change the token—it simply receives it from the server and sends it along with every request. Here’s how it works:

- **Receiving the Token**: When the client logs in with valid credentials (like a username and password), the server generates a token and sends it back to the client.
- **Storing the Token**: The client stores the token securely, often in local storage, session storage, or a cookie.
- **Sending the Token**: For every subsequent request to the server, the client includes the token, typically in the `Authorization` header (e.g., `Authorization: Bearer <token>`).
- **No Modification**: The client does not modify the token. The token is designed to be a secure credential that the server can verify. If the client changes it, the server’s verification process (which checks the token’s signature) would fail, and the request would be rejected.

In short, the client’s job is to receive the token and send it unchanged with each request, allowing the server to authenticate the user without requiring credentials every time.