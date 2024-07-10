FROM python:3-alpine3.20

WORKDIR /app

# RUN apt install -y python3
# RUN apt install -y python3.12-venv

# RUN python3 -m venv myvenv
# RUN . myvenv/bin/activate

COPY requirements.txt .
# RUN pip install psycopg2-binary
RUN pip3 install -r requirements.txt

COPY . .

ARG db_url

ENV db_url=$db_url

EXPOSE 8000

ENTRYPOINT ["fastapi", "run", "main.py"]