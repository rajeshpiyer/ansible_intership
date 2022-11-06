From ubuntu
MAINTAINER <your name>
RUN apt-get update
RUN apt-get install -y apache2
RUN apt-get clean

ENV APACHE_RUN_USER www-data
ENV APACHE_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
EXPOSE 80
CMD [“/usr/sbin/apache2”, “-D”, “FOREGROUND”]

