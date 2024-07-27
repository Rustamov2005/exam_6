FROM python:slim	
WORKDIR /app
COPY . /app
EXPOSE 81
CMD ["sleep", "30"]
