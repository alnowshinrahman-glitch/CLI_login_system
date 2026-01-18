# CLI Login & Registration System 

A simple command-line authentication system built in Python that demonstrates secure password handling, user registration, and login verification using cryptographic hashing.
This project focuses on security fundamentals rather than UI, making it a strong foundation for understanding real-world authentication flows.

--- 

## Features

- User registration with unique usernames
- Secure password hashing using SHA-256
- User login with hashed password verification
- Persistent storage using a JSON file
- Menu-driven CLI interface
- Clear separation of concerns (I/O, authentication, persistence)

---

## Technologies Used

 - hashlib : for cryptographic hashing
 - json : for data storage

---

## How Authentication Works: Registration Flow

1. User enters a username
2. Program checks for username uniqueness
3. User enters a password
4. Password is:
   - Converted to bytes
   - Hashed using SHA-256
   - Only the hashed password is stored in users.json

---

## Login Flow

1. User enters username
2. Program verifies the username exists
3. User enters password
4. Entered password is hashed
5. Hash is compared with the stored hash
6. Login succeeds only if the hashes match

----
 
## Security Considerations
- Passwords are never stored in plaintext
- Passwords are hashed before storage
- Authentication is done via hash comparison
- Separation between authentication logic and user input

---

## Known Limitations (By Design)
- Password input is visible in the terminal due to standard CLI input echo
- In production systems, password masking or secure input methods would be used
- No password salting (intentionally excluded to focus on hashing fundamentals)
- This was intentionally excluded to keep the focus on core hashing logic

These tradeoffs are documented intentionally to reflect real-world engineering decisions.
