FROM ushuz/python:2

COPY requirements.txt /opt/code/

RUN set -ex \
    && virtualenv /opt/venv \
    && /opt/venv/bin/pip install --no-cache-dir -r /opt/code/requirements.txt

COPY . /opt/code/

ENV ENV prod
ENV ENVELOPE_STATIC_URL_PREFIX https://objects.ushuz.im/envelope/

EXPOSE 8888

CMD ["/opt/venv/bin/python", "/opt/code/app.py"]
