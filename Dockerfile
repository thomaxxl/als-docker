FROM python:3.10

COPY requirements.txt /
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt

EXPOSE 5000

