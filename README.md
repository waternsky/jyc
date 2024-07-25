# JSON-YAML Converter

Tool to quickly covert json to yaml and vice-versa.
Some people (usually web-dev), who are unfamiliar with yaml,
find json easier to read than yaml.

# Installation

```shell
git clone https://github.com/waternsky/jyc.git
```
# Usage

jyc comes with two sub command 
* ui
* cli

## UI

<img width="1278" alt="Screenshot 2024-07-12 at 10 00 03 PM" src="https://github.com/user-attachments/assets/82cde4b6-f0bf-4710-8cd9-3d0d55be788f">

```shell
./jyc ui
```
Checkout [localhost](http://localhost:7860) at port 7860.
You can share public link as well by passing --public flag.

## CLI

<img width="707" alt="Screenshot 2024-07-12 at 9 55 38 PM" src="https://github.com/user-attachments/assets/70e0e7f2-fdd0-4be3-a0b4-af28b8183e42">

```shell
./jyc cli <filepath>
```
Checkout --help option for more information.

# Docker

```shell
docker pull waternsky/jyc
```
Start the container by running
```shell
docker run -it -p 7860:7860 waternsky/jyc /bin/bash
```
Can use all the above [mentioned](#Usage) commands inside container.

# Useful tips

1. Clean up the containers using following:
```shell
docker ps -a -q --filter ancestor=waternsky/jyc | xargs docker container rm
```
