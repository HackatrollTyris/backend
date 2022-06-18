
FROM ubuntu:latest

RUN apt update
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt install -y tzdata
RUN apt install -y python3-pip git zip curl htop screen libgl1-mesa-glx libglib2.0-0
RUN alias python=python3


RUN git clone https://github.com/HackatrollTyris/backend
WORKDIR /BACKEND

RUN python3 -m pip install --upgrade pip

RUN echo $(ls)

RUN pip install -e .

#RUN pip install -r requirements.txt

CMD [ "python3", "main.py"]