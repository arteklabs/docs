# dev
FROM python:3.8

WORKDIR /workspaces/deps/
COPY dev.requirements.txt ../deps/
COPY requirements.txt ../deps/

# global deps
RUN pip install -r ../deps/dev.requirements.txt
RUN pip install -r ../deps/requirements.txt
