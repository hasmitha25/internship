FROM python:3.8
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install Flask
COPY . /app
CMD ["python3", "app.py"]
