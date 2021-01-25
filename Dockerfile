FROM python:3.8.2-slim

ENV APP_HOME /app
WORKDIR ${APP_HOME}

COPY . ./

RUN apt-get update && apt-get install -y git && apt-get clean && cd ./nbs && git clone https://github.com/alanmatzumiya/engineering-basic.git && git clone https://github.com/alanmatzumiya/data_analysis.git

RUN pip install pip pipenv --upgrade
RUN pipenv install --skip-lock --system --dev

CMD ["./scripts/entrypoint.sh"]
