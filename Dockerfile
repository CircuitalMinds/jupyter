FROM python:3.8.2-slim


ENV APP_HOME .
WORKDIR ${APP_HOME}
COPY . ./

RUN apt-get update && apt-get clean
RUN pip install pip pipenv --upgrade
RUN pipenv install --skip-lock --system --dev

CMD ["./scripts/entrypoint.sh"]

RUN apt-get update && apt-get install -y git && apt-get clean && git clone https://github.com/CircuitalMinds/manager.git
RUN pip install -r ./manager/requirements.txt
CMD ["python", "./manager/circuitflow.py"]

