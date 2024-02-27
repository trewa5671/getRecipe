FROM python:3.11.7-slim-bullseye

WORKDIR /app
COPY . .

RUN pip install requests
RUN pip install uvicorn
RUN pip install fastapi


#RM if loading to yandex
EXPOSE 80

CMD ["python", "main.py"]
