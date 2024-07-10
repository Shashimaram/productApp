FROM python:3.10-slim
RUN pip install --upgrade pip

WORKDIR /app

COPY ./requirements.txt .
RUN pip install psycopg2-binary
RUN pip3 install -r requirements.txt

COPY ./main.py .

ARG dbUsername
ARG dbPassword
ARG dbDatabase
ARG dbHost

ENV dbUsername=$dbUsername
ENV dbPassword=$dbPassword
ENV dbHost=$dbHost
ENV dbDatabase=$dbDatabase

EXPOSE 8000

ENTRYPOINT ["fastapi", "run", "./main.py"]