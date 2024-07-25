FROM python:3.12

WORKDIR /opt/jyc/bin

ENV PATH="$PATH:/opt/jyc/bin"
EXPOSE 7860

SHELL ["/bin/bash", "-c"]
RUN python3.12 -m venv .venv

COPY . .
RUN source .venv/bin/activate && pip3.12 install -r requirements.txt
