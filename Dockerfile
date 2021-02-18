FROM python:3.8.2-slim

ENV APP_HOME /app
WORKDIR ${APP_HOME}
RUN apt-get update && apt-get install -y git && apt-get clean && git clone https://github.com/CircuitalMinds/manager.git
COPY . ./
RUN pip install pip pipenv --upgrade
CMD ["python", "./manager/build.py"]
RUN pipenv install --skip-lock --system --dev
CMD ["./scripts/entrypoint.sh"]
