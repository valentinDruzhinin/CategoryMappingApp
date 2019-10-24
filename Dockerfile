FROM python:3.7-slim
ADD . /category-mapping
WORKDIR /category-mapping
RUN pip install -r requirements.txt
