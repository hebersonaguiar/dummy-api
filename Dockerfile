FROM python:3.4.9

RUN apt-get update -y ; \
	    apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev

WORKDIR /opt

#ADD requirements.txt /opt
#RUN pip install -r requirements.txt

#ADD static /opt/static
ADD templates /opt/templates
ADD server.py /opt/
ADD people.py /opt/
ADD swagger.yml /opt/

#COPY docker-entrypoint.sh /entrypoint.sh

#RUN chmod +x /entrypoint.sh

EXPOSE 5000

#ENTRYPOINT ["/entrypoint.sh"]

#CMD celery -A app.celery worker --loglevel=info