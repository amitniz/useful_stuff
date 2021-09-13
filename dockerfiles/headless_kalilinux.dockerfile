#Headless Kali linux container.

FROM kalilinux/kali-rolling
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt -y install kali-linux-headless
WORKDIR /root
ENTRYPOINT ["/bin/zsh"]

#Open Ports:
#EXPOSE
