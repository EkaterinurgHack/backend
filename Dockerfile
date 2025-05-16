FROM python:3.13 AS packagebuilder
COPY ./requirements.txt ./requirements.txt
RUN pip3 wheel -r requirements.txt

FROM python:3.13-slim
EXPOSE 8000


# Setup user
ENV UID=2000
ENV GID=2000

RUN groupadd -g "${GID}" python \
  && useradd --create-home --no-log-init --shell /bin/bash -u "${UID}" -g "${GID}" python

USER python
WORKDIR /home/python

RUN mkdir ./wheels
COPY --from=packagebuilder ./*.whl ./wheels/
RUN pip3 install ./wheels/*.whl --no-warn-script-location

COPY setup.py ./
COPY ./app ./app
COPY ./.env ./.env
RUN pip3 install .


CMD PATH=$PATH:/home/python/.local/bin && \
    uvicorn app.main:app --host 0.0.0.0 --port 8000