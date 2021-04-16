FROM ubuntu:latest
# Install cron & python 
RUN apt-get update
#RUN apt-get -y install cron python3.8 python3-pip
RUN apt-get -y install python3.8 python3-pip
RUN pip3 install --upgrade pip

# Add crontab file in the cron directory
#ADD crontab /etc/cron.d/purge-file-cron
# Add shell script and grant execution rights
#ADD purge.sh /purge.sh
#RUN chmod +x /purge.sh
# Give execution rights on the cron job
#RUN chmod 0644 /etc/cron.d/purge-file-cron
# Run the command on container startup
#CMD cron 
# 
WORKDIR /appli
ADD ./appli/ .

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN pip install -r requirements.txt

ENTRYPOINT ["flask", "run"]