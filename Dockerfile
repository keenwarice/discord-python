FROM python:3.11.6-slim

WORKDIR /app
COPY . /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN pip install -U discord.py


CMD ["poetry", "run", "python", "bot.py"]
