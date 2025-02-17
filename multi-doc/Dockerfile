FROM python:3.9-slim AS build

ARG APP_VERSION=1.0.0

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --user -r requirements.txt 

RUN echo "Building app version ${APP_VERSION}"
RUN echo "Pip install location:"


RUN ls -la /root/.local


FROM python:3.9-slim 

ENV APP_NAME="My Multi-stage Python App"
ENV APP_VERSION=${APP_VERSION}

WORKDIR /app

COPY --from=build /root/.local /root/.local

COPY . .

ENV PATH=/root/.local/bin:$PATH

CMD ["python", "app.py"]
