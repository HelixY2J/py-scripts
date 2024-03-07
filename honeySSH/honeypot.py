
import paramiko
import socket
import threading
import os,sys

file_system = {
    "/": {
        "bin": {
            "files": {
                "ls",
                "cp",
                "rm",
                "mv",
                "apt," "apt-add-repository",
                "apt-cache",
                "apt-config",
                "apt-get",
                "apt-key",
                "aria_dump_log",
                "base32",
                "base58",
                "base64",
                "basename",
                "basenc",
                "bash",
                "bdftruncate",
                "besside-ng-crawler",
            },
            "dir": {},
        },
        "home": {
            "userIV": {
                "files": {"vpn.txt", "python101.pdf"},
                "dir": {
                    "Desktop": {},
                    "Documents": {},
                    "Downloads": {},
                    "Music": {},
                    "Pictures": {},
                    "Public": {},
                    "Templates": {},
                    "Videos": {},
                },
            },
        },
        "lib32": {
            "files": {
                "lib32_1.so",
                "lib32_2.so",
                "lib32_3.so",
                "lib32_4.so",
                "lib32_5.so",
                "lib32_6.so",
                "lib32_7.so",
                "lib32_8.so",
                "lib32_9.so",
            },
            "dir": {},
        },
        "media": {
            "files": {},
            "dir": {"userIV"},
        },
        "root": {
            "files": {},
            "dir": {},
        },
        "srv": {
            "files": {},
            "dir": {},
        },
        "var": {
            "log": {
                "files": {"app.log", "system.log"},
                "dir": {},
            },
            "tmp": {
                "files": {},
                "dir": {},
            },
        },
        "boot": {
            "files": {"vmlinuz"},
            "dir": {},
        },
        "lib64": {
            "files": {"lib64_1.so", "lib64_2.so"},
            "dir": {},
        },
        "mnt": {
            "files": {},
            "dir": {},
        },
        "run": {
            "files": {},
            "dir": {},
        },
        "sys": {
            "files": {},
            "dir": {},
        },
        "vmlinuz": {
            "files": {},
            "dir": {},
        },
        "dev": {
            "files": {},
            "dir": {},
        },
        "opt": {
            "files": {},
            "dir": {},
        },
        "sbin": {
            "files": {"service1", "service2"},
            "dir": {},
        },
        "tmp": {
            "files": {},
            "dir": {},
        },
        "etc": {
            "files": {"config1", "config2"},
            "dir": {},
        },
        "lib": {
            "files": {"lib1.so", "lib2.so", "lib3.so"},
            "dir": {},
        },
        "usr": {
            "files": {},
            "dir": {},
        },
    },
}

class sshServer(paramiko.ServerInterface):
    def check_channel_request(self, kind: str, chanid: int) -> int:
         if kind == "session":
              return paramiko.OPEN_SUCCEEDED
         return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    
    def check_auth_password(self, username: str, password: str) -> int:
        # return super().check_auth_password(username, password)
        if password == "qwerty":
             return paramiko.AUTH_SUCCESSFUL
        else:
            print(f"{username}:{password}")

            return paramiko.AUTH_FAILED
    def check_channel_pty_request(self, channel: paramiko.Channel, term: bytes, width: int, height: int, pixelwidth: int, pixelheight: int, modes: bytes) -> bool:
        #  return super().check_channel_pty_request(channel, term, width, height, pixelwidth, pixelheight, modes)
         return True
    
    def check_channel_shell_request(self, channel: paramiko.Channel) -> bool:
        #  return super().check_channel_shell_request(channel)
         return True

def is_complete_command(command):
    # Modify this function based on your criteria for a complete command
    # For example, return True if the command ends with a newline, space followed by another character, etc.
    # You can also use regular expressions for more complex patterns
    return command.endswith("\n") or (" " in command and len(command.split()) > 1)

def handle_connection(client_sock):
    transport = paramiko.Transport(client_sock)
    # server_key = paramiko.RSAKey.generate(2048) 
            # creating the host key evrytime seems bad practice
            # get a static for server by ssh-keygen

    server_key = paramiko.RSAKey.from_private_key_file('key')
    transport.add_server_key(server_key)
    transport.set_gss_host(socket.getfqdn(""))
    transport.load_server_moduli()
    ssh = sshServer()

    transport.start_server(server=ssh)
    channel = transport.accept(50)

    if channel is None:
        print("> No channel was found")
        sys.exit(1)
    
    print("> Gotcha ! one bad guy...\n")
    
    buffer = ""  # Initialize a buffer to collect characters
    # channel.send("> Enter 'help' for more info".encode())
    
    while True:
        try:
            channel.send("$ ".encode())  
            cmd = channel.recv(1).decode("utf-8").strip()  

            # Append received command to the buffer
            buffer += cmd


            if( '\n' in buffer):
                complete_cmd, buffer = buffer.split('\n',1)
            # if not buffer.strip():
            #     break  # Handle empty commands
            
            # Process the complete command only if it's not empty
                if complete_cmd:
                    normalized_cmd = complete_cmd.lower().replace("\t", "")

                    if normalized_cmd.lower() in ("exit", "quit", "logout"):
                        channel.send("Goodbye!\n".encode())
                        channel.close()
                        break
                    elif normalized_cmd == "a":
                        response = "hiiii\n"
                        channel.send(response.encode())

                    elif normalized_cmd == "ls":
                        response = "\n".join(
                            file_system["/"]["home"]["userIV"]["dir"]
                            + [""]
                            + file_system["/"]["home"]["userIV"]["files"]
                        )
                        channel.send(response.encode())
                        # response = "\n".join(file_system["/"]["bin"]["files"])
                        # channel.send(response.encode())

                    elif normalized_cmd.startswith("cd "):
                        target_dir = cmd[3:]
                        if target_dir in file_system["/"]["home"]["userIV"]["dir"]:
                            channel.send(f"Directory changed to {target_dir}\n".encode())
                        else:
                            channel.send("No such directory\n".encode())

                    else:
                        channel.send(f"Unknown command: {cmd}\n".encode())  # Handle invalid commands
                    buffer = ""


        except Exception as e:
            print(f"> Error receiving command: {e}")
            break

def main():
    server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server_sock.bind(('',2222))
    server_sock.listen(100)

    while True:
        client_sock, client_addr = server_sock.accept()
        print(f"> CoNnection from the {client_addr[0]} : {client_addr[1]} ")
        # client_sock.send(b"heloooo, I am elmo \n")
        t = threading.Thread(target=handle_connection,args=(client_sock,))
        t.start()
    


if __name__ == "__main__":
    main()