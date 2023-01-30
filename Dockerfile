FROM python:3.9-slim
LABEL maintainer="Texas A&M Blockchain (Ishan Dhanani)"
LABEL version="0.1"
LABEL description="A utility program to automate adding entries to our mailing list"

COPY requirements.txt /tmp/ 
COPY ./src /src
WORKDIR "/src"

# WORKDIR /src
# COPY requirements.txt /tmp/ 
# COPY ./src /src
RUN apt-get update -y && apt-get install -y gcc
RUN pip install -r /tmp/requirements.txt 

CMD [ "python", "automated_mailing_list.py"]


