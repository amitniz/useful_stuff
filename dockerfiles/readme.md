# Dockerfiles :whale:

## DevLab - Ubuntu container with dev tools.
	+ includes: gcc, python2, python3 (with common modules),
	  pip3, git, gdb, valgrind, wget, curl.
## HeadLess KaliLinux - Kali linux container.
	+ includes: all headless tools.


## Build:
> docker build -t {tagname} -f {dockerfile} {pathtofile}

## Run:

#### -Examples:

simple run without mounting:
> docker run --rm -h {hostname} -it {imagename}

run with mount dir:
> docker run --rm -h {hostname} -p {host_path}:{guest_path} -w {guest_path} -it {imagename}

#### -Useful flags:
**--rm:** remove container after exit.

**-it:** interactive mode.

**-v:** mount.

**-w:** change working dir.

**-h:** change hostname.

