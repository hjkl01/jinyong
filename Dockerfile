FROM python:3.6.1
# RUN pip install --upgrade pip \
RUN pip install uwsgi -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
RUN mkdir /sockets
ADD requirements.txt /
RUN pip install -r /requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
COPY uwsgi.ini /etc/uwsgi/
COPY src/ /app
WORKDIR /app
CMD /usr/local/bin/uwsgi --ini /etc/uwsgi/uwsgi.ini --ini /app/uwsgi.ini
