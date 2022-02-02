FROM python:3.8
WORKDIR /source
RUN pip install pipenv
COPY . .
RUN pipenv install
CMD ["pipenv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]