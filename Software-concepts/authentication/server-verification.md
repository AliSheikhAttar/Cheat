To address your query about how a server verifies a token's signature and expiration in the context of JSON Web Tokens (JWT), and whether it uses its private key, let’s break it down step-by-step.

### How the Server Verifies the Token Signature and Expiration

A JWT consists of three parts: a **header**, a **payload**, and a **signature**, separated by dots (e.g., `header.payload.signature`). The header specifies the token type and signing algorithm, the payload contains claims (data like user ID and expiration), and the signature ensures the token’s integrity.

#### Signature Verification
The server verifies the signature to confirm that the token hasn’t been tampered with. The method of verification depends on the signing algorithm used when the token was created:

- **Symmetric Signing (e.g., HMAC)**: 
  - The token is signed using a **secret key** known only to the server.
  - To verify, the server uses the same secret key. It recomputes the signature by applying the HMAC algorithm to the `header.payload` portion of the token and compares it to the provided signature. If they match, the token is valid.
  
- **Asymmetric Signing (e.g., RSA)**:
  - The token is signed using the server’s **private key**.
  - To verify, the server (or any party) uses the corresponding **public key**. The public key decrypts the signature to validate that it matches the hash of the `header.payload`. If it does, the token is authentic.

Thus, for signature verification:
- Symmetric signing uses the secret key.
- Asymmetric signing uses the public key, not the private key.

#### Expiration Verification
The expiration is checked independently of the signature. The payload typically includes an **`exp` claim**, a timestamp (in seconds since the Unix epoch) indicating when the token expires. The server:
- Extracts the `exp` value from the payload.
- Compares it to the current time.
- If the current time is past the `exp` timestamp, the token is considered expired and invalid.

This process doesn’t involve any keys—it’s a simple comparison.

### Does the Server Use Its Private Key to Verify the Token?
Not exactly—it depends on the signing method:

- **Symmetric Signing (HMAC)**:
  - The server uses a **secret key** for both signing and verifying. This key is symmetric (the same for both operations). While you might think of it as a “private key” because it’s kept secret, in cryptography, “private key” typically refers to asymmetric key pairs. So, technically, it’s a secret key, not a private key in the asymmetric sense.
  
- **Asymmetric Signing (RSA)**:
  - The server signs the token with its **private key** when issuing it.
  - For verification, it uses the **public key**, not the private key. The private key’s role is limited to signing; verification relies on the public key, which can be shared publicly.

So, to directly answer: **No, the server does not use its private key to verify the token’s signature in the standard sense.** For HMAC, it uses a secret key (symmetric), and for RSA, it uses the public key (asymmetric). The private key is used only for signing in the asymmetric case.

### Does the Server Use the Same Private Key for Every User?
Since your second question assumes the private key is used for verification, let’s clarify this in the context of signing (where the private key is actually used):

- **Symmetric Signing (HMAC)**:
  - The server uses the same **secret key** to sign tokens for all users. This key is server-specific, not user-specific. The uniqueness of each token comes from the payload (e.g., user ID), not the key.
  
- **Asymmetric Signing (RSA)**:
  - The server uses the same **private key** to sign tokens for all users and the same corresponding **public key** to verify them. Like the secret key in HMAC, this key pair is tied to the server, not individual users.

In standard JWT authentication:
- **Yes, the server uses the same key (or key pair) for all users.** Whether it’s a secret key (HMAC) or a private/public key pair (RSA), the key material is consistent across all tokens issued by the server. User-specific data is embedded in the payload, and the signature ensures its integrity, but the signing key remains the same.

### Summary
- **Signature Verification**: The server uses the secret key (for HMAC) or the public key (for RSA), not the private key directly for verification.
- **Expiration Check**: The server compares the `exp` claim to the current time, no keys involved.
- **Same Key for All Users**: Yes, the server typically uses the same secret key (HMAC) or private key (RSA) to sign tokens for all users, ensuring consistency and scalability.

This approach is standard in JWT-based authentication, though in rare, advanced cases (e.g., multi-tenant systems), different keys might be used—but that’s not typical for a single application.