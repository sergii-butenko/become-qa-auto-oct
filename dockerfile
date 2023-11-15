# PYTHON
FROM python:3.7-slim-bullseye

#JAVA
# FROM openjdk:22-slim-bullseye

# install dependencies 
# COPY requirements file ONLY
RUN pip install pytest requests selenium pytest-html 

# mkdri /tests && cd /tests
WORKDIR /tests

# stands for 
# COPY EVERYTHING from LOCALFOLDER to CURRENT FODLER IN CONTAINER(which is /tests)
COPY . .

# specidfy command to run
ENTRYPOINT [ "pytest" ]
CMD ["--html=reports/report.html", "--self-contained-html"]
