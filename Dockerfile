FROM python:3.8.2-slim

COPY . /app
ENV APP_HOME /app
WORKDIR ${APP_HOME}

RUN apt-get update && apt-get install -y git && apt-get clean
RUN pip install pip pipenv --upgrade
RUN pipenv install --skip-lock --system --dev
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
