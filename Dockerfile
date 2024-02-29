FROM python:3.9-slim-buster AS builder
RUN apt update && apt install git gcc libssl-dev -y
WORKDIR /asksonic
RUN git clone https://github.com/BlinkersFr31/asksonic.git
RUN pip install --user wheel setuptools honcho
RUN pip install --use-pep517 --user git+https://github.com/srichter/flask-ask.git@flask2
RUN pip install --user gunicorn==20.1.0 py-sonic==0.7.9 requests==2.28.2 pyarr==5.2.0
#RUN pip install --user -r asksonic/requirements.txt

FROM python:3.9-slim-buster
COPY --from=builder /asksonic /opt
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
WORKDIR /opt/asksonic
ENTRYPOINT ["honcho", "start", "-f", "Procfile.dev"]
