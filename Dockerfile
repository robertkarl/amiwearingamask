FROM ubuntu:18.10 as base
ENV BUILD_DATE "1/31/2019"

####
# Python environment setup
RUN apt-get update && apt-get upgrade -yq
RUN apt-get update && apt-get install -yq man htop iftop curl lsof pdftk
RUN apt-get install -yq software-properties-common 
RUN apt-get install -yq python3-pip
RUN python3 -V
RUN apt-get update
RUN apt-get install -yq virtualenv
RUN pip3 install --upgrade setuptools
RUN pip3 install --upgrade pip
RUN pip3 install -q uwsgi
ADD requirements.txt .
RUN pip3 install -q -r requirements.txt


####
# Application dependencies and setup
EXPOSE 80

WORKDIR /aiwam/code/src
ADD src .
WORKDIR /aiwam/code/model
ADD model .
WORKDIR /aiwam/code/
ADD README.md .
ADD setup.py .
RUN pip3 install .

# Required by click, a flask dep
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENV FLASK_ENV=production
ENV PYTHONPATH=src

ENTRYPOINT ["uwsgi", "--ini", "src/amiwearingamask/wsgi-80.ini"]
