FROM python:3.5.5

RUN apt-get update -y

WORKDIR /opt

ADD requirements.txt /opt
RUN pip install -r requirements.txt

ADD app.py /opt/
ADD main.py /opt/
ADD config.py /opt/

COPY docker-entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/entrypoint.sh"]

CMD ["python","main.py"]