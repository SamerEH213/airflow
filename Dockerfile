FROM apache/airflow:latest-python3.8
USER root
ENV DISPLAY=:99
ENV TIME_CHNAGE_IP=60
ENV MANY_TIME_CHNAGE_IP=0
RUN apt-get update && apt-get install -y firefox-esr xvfb
RUN apt-get install -y xvfb xauth
ARG AIRFLOW_HOME=/opt/airflow
ADD dags /opt/airflow/dags
USER airflow
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org boto3 selenium 
USER ${AIRFLOW_UID}
