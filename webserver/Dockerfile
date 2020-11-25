FROM nginx:1.19
COPY . /etc/nginx/conf.d/
RUN mkdir -p /etc/nginx/ssl-certs \
    && openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl-certs/mycert.key -out /etc/nginx/ssl-certs/mycert.crt -subj "/C=AD/ST=Andorra la Vella/L=Andorra la Vella/O=practice/CN=*.example.com"