FROM python:3.10-slim-bullseye

ENV FLASK_CONTEXT=development
ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/home/flask/.local/bin

RUN groupadd flaskgroup && useradd -m -g flaskgroup -s /bin/bash flask
RUN chown -R flask:flaskgroup /home/flask
RUN apt-get update
RUN apt-get install -y python3-dev build-essential libpq-dev
RUN apt-get install -y build-essential curl iputils-ping
RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
RUN rm -rf /var/lib/apt/lists/*
RUN ln -sf /user/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN echo "flask ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN mkdir -p /home/flask/app/ms-purchases/
ADD . /home/flask/app/ms-purchases/

RUN mkdir -p /home/flask/app/ms-purchases/app/Logs
RUN chown -R flask:flaskgroup /home/flask/app/ms-purchases/app/Logs
RUN chmod 777 -R /home/flask/app/ms-purchases/app/Logs

WORKDIR /home/flask/app/ms-purchases

USER flask
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gevent==24.10.3 gunicorn==23.0.0

EXPOSE 5002

CMD ["gunicorn", "--workers", "2", "--threads", "4","--log-level", "INFO", "--bind", "0.0.0.0:5002", "app:create_app()"]

