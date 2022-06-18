
FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN python3 -m pip install --upgrade pip

#RUN echo $(ls)

#RUN pip install -e .

RUN pip install -r requirements.txt

#CMD [ "python3", "main.py"]