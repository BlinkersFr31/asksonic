FROM python:slim AS builder
RUN apt update && apt install git gcc libssl-dev -y
WORKDIR /asksonic
RUN git clone https://github.com/BlinkersFr31/asksonic.git
RUN pip install --user wheel setuptools honcho
RUN pip install --user git+https://github.com/srichter/flask-ask.git@flask2
RUN pip install --user gunicorn==20.1.0 py-sonic==0.7.9 requests==2.25.1 pyarr==5.2.0

FROM python:slim
COPY --from=builder /asksonic /opt
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
WORKDIR /opt/asksonic
ENTRYPOINT ["honcho", "start", "-f", "Procfile.dev"]
