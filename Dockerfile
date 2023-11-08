FROM python:slim AS builder
RUN apt update && apt install git gcc libssl-dev -y
WORKDIR /asksonic
RUN git clone https://github.com/BlinkersFr31/asksonic.git
RUN pip install --user wheel setuptools honcho
RUN pip install --user -r asksonic/requirements.txt

FROM python:slim
COPY --from=builder /asksonic /opt
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
WORKDIR /opt/asksonic
ENTRYPOINT ["honcho", "start", "-f", "Procfile.dev"]
