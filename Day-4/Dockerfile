FROM python:3-alpine3.15
EXPOSE 3000
WORKDIR /app1
COPY ./requirements.txt /app1/
RUN pip install -r requirements.txt
COPY . /app1
CMD ["python","./app1.py"]
