FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/

#RUN pip install --upgrade pip
#RUN python -m pip install rasa

#WORKDIR /app
#COPY . /app
#COPY ./data /app/data
## COPY ./ssl /app/ssl

## RUN rasa train 

#VOLUME /app
#VOLUME /app/data
#VOLUME /app/models
#VOLUME /app/ssl

CMD [ "run","-m","/app/models","--enable-api","--cors","*","--debug" ]
