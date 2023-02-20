FROM python:3.10.3-slim

WORKDIR /usr/src/app

COPY . .

RUN apt update && apt install -y build-essential && apt install -y python3-xmltodict && pip3.10 install -r requirements.txt

RUN mypy && pytest --cov

EXPOSE 8080

CMD [ "uvicorn", "src.main:app", "--host=0.0.0.0", "--port=8080"]