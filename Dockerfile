# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.7

ENV APP_HOME /app
WORKDIR $APP_HOME

# Install manually all the missing libraries
RUN apt-get update

# Install Python dependencies.
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

#Set timezone
ENV TZ=America/Bogota
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV API_URL="https://dsapi-maa3kukuyq-ue.a.run.app/api/v1/"
ENV GOOGLE_APPLICATION_CREDENTIALS="credentials.json"

# Copy local code to the container image.
COPY . .

ENV APP_HOME /app/news_crawler_scraper
WORKDIR $APP_HOME

# Run the web service on container startup. 
EXPOSE 8080
CMD uvicorn --host=0.0.0.0 --port 8080 main:app