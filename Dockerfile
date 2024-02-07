FROM ubuntu
RUN apt-get clean
RUN apt-get update && apt-get install -y python-is-python3 python3-pip
RUN pip3 install flask
COPY app.py /opt/
COPY /templates/about.html /opt/templates/
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080
