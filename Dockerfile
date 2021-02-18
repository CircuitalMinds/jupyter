RUN apt-get update && apt-get install -y git && apt-get clean && git clone https://github.com/CircuitalMinds/manager.git
ENV APP_HOME ./manager
WORKDIR ${APP_HOME}
CMD ["python", "./manager/build.py"]
