FROM python:3.8-slim-bullseye

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x run.sh
CMD [ "/app/run.sh" ]