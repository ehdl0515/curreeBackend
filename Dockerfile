FROM python:3.12.2-slim
LABEL authors="donghee"

RUN apt-get update && \
    apt-get install -y sudo && \
    apt-get install -y net-tools && \
    apt-get install -y procps && \
    apt-get install -y pkg-config && \
    apt-get install -y python3-dev && \
    apt-get install -y default-libmysqlclient-dev && \
    apt-get install -y build-essential && \
    apt-get install -y vim


RUN echo 'root:ehdl1234' | chpasswd
RUN useradd -ms /bin/bash admin
RUN echo "admin:1234" | chpasswd
USER admin

RUN mkdir -p /home/admin/logs
RUN mkdir -p /home/admin/backend

WORKDIR /home/admin/backend
COPY . .

RUN pip3 install --no-cache -r ./requirements.txt

CMD ["sleep", "10"]
CMD ["/home/admin/.local/bin/gunicorn", "curreeBackend_config.wsgi:application", "-b", "0.0.0.0:8000"]
#CMD ["sleep", "infinity"]