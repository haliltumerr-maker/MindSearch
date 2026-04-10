FROM continuumio/miniconda3

ENV PATH=/opt/conda/bin:$PATH

WORKDIR /app

COPY . .

RUN conda create --name fastapi python=3.10 -y && \
    conda run -n fastapi pip install janus && \
    conda run -n fastapi pip install -r requirements.txt && \
    conda clean --all -f -y

EXPOSE 8002

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "fastapi"]
CMD ["python3", "-m", "mindsearch.app", "--asy", "--host", "0.0.0.0", "--port", "8002"]
