FROM python:3.12-bullseye

WORKDIR /workdir

COPY Makefile.in Makefile

RUN apt update && \
    apt install default-jre -y && \
    pip3 install antlr4-python3-runtime && \
    curl -O https://www.antlr.org/download/antlr-4.13.1-complete.jar
