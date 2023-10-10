FROM debian:bullseye

WORKDIR /workdir

COPY Makefile.in Makefile

RUN apt update && \
    apt install wget unzip default-jre -y && \
    wget https://repo1.maven.org/maven2/net/java/dev/javacc/javacc/7.0.12/javacc-7.0.12.jar && \
    echo "java -classpath javacc-7.0.12.jar javacc \"\$@\"" > javacc && \
    chmod +x javacc
