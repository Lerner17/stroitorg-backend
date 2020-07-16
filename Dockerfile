FROM python:3.7
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /root
COPY requirements.txt /root/

RUN pip install -r requirements.txt
COPY . /root
RUN mkdir -p /var/static
RUN cp -r /root/static/* /var/static
VOLUME /var/static

RUN apt-get update && apt-get install netcat -y

EXPOSE 8000

CMD ["sh", "start.sh"]
