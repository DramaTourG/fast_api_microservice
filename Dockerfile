FROM python:3.9

WORKDIR .

RUN pip install --upgrade pip

RUN pip install pipenv

RUN apt-get -q update && apt-get -qy install netcat

COPY . .

RUN pipenv install --system --deploy --ignore-pipfile

RUN curl -OL https://raw.githubusercontent.com/mrako/wait-for/master/wait-for && chmod +x wait-for

EXPOSE 8000
