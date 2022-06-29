# Install base image
FROM gitlab/gitlab-runner:latest

# Update base image
RUN apt update
RUN apt upgrade -y

# Install vim
RUN apt install vim -y

# Install Python3
RUN apt install python3 -y
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install pip
RUN apt install pip -y

# Install required Python modules
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Update installed applications
RUN pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U 
RUN apt update
RUN apt upgrade -y

# Copy necessary files
COPY /secrets/secrets.json /etc/.secrets/secrets.json
