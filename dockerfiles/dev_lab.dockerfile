# Ubuntu container with development tools.

FROM ubuntu 

#Install softwares
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y git build-essential gdb valgrind \
 python2 python3 python3-pip zsh wget curl

#Install python3 modules
RUN pip3 install numpy pillow matplotlib twisted pycrypto pycryptodome pipenv


#Setup the shell 

#replace zsh's config file 
RUN curl https://raw.githubusercontent.com/AmitNiz/.dotfiles/master/zsh/custom_zshrc > ~/.zshrc
#Working Directory
#WORKDIR

#Default shell
ENTRYPOINT ["/bin/zsh"]

WORKDIR /root


#Enviroments Variables
#ENV

#Open ports 
#EXPOSE


