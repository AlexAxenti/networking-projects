# TCP Chat App

## Covered:

- Basic socket connections between server and client
- Simple threading to manage multiple clients

## Potential Features For Fun

1. Private Messaging - DONE
Allow users to send direct messages to each other by typing a command like /msg username message.

2. User List Command - DONE
Implement a command (e.g., /users) that shows all connected nicknames.

3. Message History
Store and display the last N messages when a user joins.

4. Colored Output
Use ANSI escape codes to color usernames or system messages for better readability.

6. Authentication
Require users to log in with a password or register an account.

5. User Roles
Add regular/admin roles as well as admin commands (e.g., /kick username).

7. GUI Client
Build a graphical client using Tkinter or PyQt for a more user-friendly experience.

### Current Todos

1. Refactor server.py into a class. Then clean up commands.py to not pass in nicknames and clients as parameters.