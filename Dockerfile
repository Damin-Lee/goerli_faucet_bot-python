# syntax=docker/dockerfile:1

# Python 버전 선택
FROM python:3.9.6-slim-buster

# 디폴트 폴더 변경
WORKDIR /app

# Pip 패키지 설치
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# 필요한 파일을 복사
COPY index.py index.py
CMD [ "python3", "index.py", "--echo=Hello, goerli_faucet-pyhon in docker container."]
