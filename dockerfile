FROM python:3.13-slim

WORKDIR /errors

COPY . .

CMD ["python", "main.py"]