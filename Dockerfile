FROM python
MAINTAINER Gustavo Martins
COPY . /var/www
WORKDIR /var/www
RUN pip install flask
ENTRYPOINT python3 app.py
EXPOSE 5000
