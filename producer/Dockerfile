FROM python:3.10

WORKDIR /app/

COPY producer/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]