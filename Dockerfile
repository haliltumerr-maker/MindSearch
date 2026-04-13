Tüm docker file yazFROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir janus && \
    pip install --no-cache-dir -r requirements.txt

RUN grep -n "plugin_executor\|interpreter_executor" /usr/local/lib/python3.10/site-packages/lagent/agents/stream.py

EXPOSE 8002

CMD ["python3", "-m", "mindsearch.app", "--lang", "en", "--model_format", "groq", "--search_engine", "GoogleSearch"]
