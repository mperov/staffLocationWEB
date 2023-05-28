FROM python:3.8-slim

RUN useradd -m runner

COPY --chown=runner:runner ./informant.py /home/runner/staffLocation.py
RUN mkdir -p /home/runner/getLinuxUserLocation
COPY --chown=runner:runner ./getLinuxUserLocation/getLocation.py /home/runner/getLinuxUserLocation/getLocation.py
RUN mkdir -p /home/runner/templates
COPY --chown=runner:runner ./templates/base.html /home/runner/templates/base.html
COPY --chown=runner:runner ./templates/server1.html /home/runner/templates/server1.html
COPY --chown=runner:runner ./templates/server2.html /home/runner/templates/server2.html
RUN mkdir -p /home/runner/static/css
COPY --chown=runner:runner ./static/css/load.css /home/runner/static/css/load.css

ENV PYTHONPATH /home/runner

WORKDIR /home/runner

RUN /usr/local/bin/python -m pip install --upgrade pip \
    && pip install -r requirements \
    && chmod 755 /home/runner/staffLocation.py

USER runner

CMD ["/home/runner/staffLocation.py"]
