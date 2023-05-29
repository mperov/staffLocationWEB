FROM python:3.8-slim

RUN useradd -m runner

COPY --chown=runner:runner ./staffLocation.py /home/runner/staffLocation.py
COPY --chown=runner:runner ./requirements /home/runner/requirements
RUN mkdir -p /home/runner/getLinuxUserLocation
COPY --chown=runner:runner ./getLinuxUserLocation/getLocation.py /home/runner/getLinuxUserLocation/getLocation.py
COPY --chown=runner:runner ./getLinuxUserLocation/requirements /home/runner/getLinuxUserLocation/requirements
RUN mkdir -p /home/runner/templates/location
COPY --chown=runner:runner ./templates/location/base.html /home/runner/templates/location/base.html
COPY --chown=runner:runner ./templates/location/server1.html /home/runner/templates/location/server1.html
COPY --chown=runner:runner ./templates/location/server2.html /home/runner/templates/location/server2.html
RUN mkdir -p /home/runner/static/css
COPY --chown=runner:runner ./static/css/load.css /home/runner/static/css/load.css
RUN mkdir -p /home/runner/.ssh

ENV PYTHONPATH /home/runner

WORKDIR /home/runner

RUN /usr/local/bin/python -m pip install --upgrade pip \
    && pip install -r /home/runner/requirements \
    && pip install -r /home/runner/getLinuxUserLocation/requirements \
    && chmod 755 /home/runner/staffLocation.py

USER runner

ENTRYPOINT ["python3", "-u", "/home/runner/staffLocation.py"]
