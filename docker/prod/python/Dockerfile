FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r /base/ dev.txt
COPY . /code/
CMD ["python","-u","main.py"]