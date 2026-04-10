FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir janus && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8002

CMD ["python3", "-m", "mindsearch.app", "--asy", "--host", "0.0.0.0", "--port", "8002"]
