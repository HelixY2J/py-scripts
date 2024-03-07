# py_scripts

This repository contains various smol python projects

## honeySSH

The honeypot system is implemented using Python's paramiko library to create an SSH server. The server listens for incoming connections and simulates a fake UNIX filesystem. When attackers connect to the honeypot, their actions and commands are logged.

## Installation

Install the dependencies 

```python
    pip install -r requirements.txt
```

**Note**: If you encounter SSH key verification issues due to generating a new key every time the server starts, consider using a static key for the server. You can generate a static key using the `ssh-keygen` command. After generating the static key, use it in your server code:

```python
server_key = paramiko.RSAKey.from_private_key_file('static_key')
``` 

## Current Progress

- Implemented SSH server using paramiko.
- Created a basic fake UNIX filesystem structure.
- Handling of basic commands such as `ls` and `cd`,but there are some bugs that need to be addressed.
- Every failed attempt of attacker will be logged 

## Usage

1. Run the `honeypot_server.py` script to start the honeypot server.
2. Connect to the server using an SSH client to simulate attacker interactions.


Client unsuccessful login attempts & succesful login on password "qwerty": 

Server logging attempts from attackers:


## Future Work

- Implement additional commands and functionality to further simulate a real UNIX environment.
- Improve security measures to prevent attackers from detecting the honeypot.


