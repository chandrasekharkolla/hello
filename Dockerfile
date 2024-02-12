FROM amd64/python:3.9-buster
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "index.py"]