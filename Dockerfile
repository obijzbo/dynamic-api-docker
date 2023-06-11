FROM python:3.10

WORKDIR /var/app

COPY . /var/app

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]