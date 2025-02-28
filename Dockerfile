FROM jenkins/jenkins:latest
USER root
RUN mkdir /my_app
WORKDIR /my_app
RUN pwd
RUN ls -la
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    python3-venv && \
    rm -rf /var/lib/apt/lists/*