FROM python:3.7
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /root
COPY requirements.txt /root/

RUN pip install -r requirements.txt
COPY . /root