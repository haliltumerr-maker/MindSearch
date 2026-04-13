FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir janus && \
    pip install --no-cache-dir -r requirements.txt

RUN sed -i 's/if not self.interpreter_executor:/if False:/' /usr/local/lib/python3.10/site-packages/lagent/agents/stream.py

EXPOSE 8002

CMD ["python3", "-m", "mindsearch.app", "--lang", "en", "--model_format", "groq", "--search_engine", "GoogleSearch"]
