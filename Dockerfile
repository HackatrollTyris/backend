
FROM ubuntu:latest

RUN apt update
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt install -y tzdata
RUN apt install -y python3-pip git

RUN git clone https://github.com/HackatrollTyris/backend
WORKDIR /app
COPY . /app
RUN python3 -m pip install --upgrade pip

#RUN echo $(ls)

#RUN pip install -e .

RUN pip install -r requirements.txt

CMD [ "python3", "main.py"]
