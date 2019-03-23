FROM python:3.7

ADD . /tmp

RUN pip install --upgrade pip 
WORKDIR /tmp
#do the install
RUN pip install .

EXPOSE 10000

CMD run.py
