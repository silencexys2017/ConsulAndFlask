FROM python:2-alpine

WORKDIR /consuls

RUN pip install requests 
RUN pip install consulate 
RUN pip install flask 

EXPOSE 8001 8002 8500 22
COPY . .

ENTRYPOINT ["python","server.py"]

