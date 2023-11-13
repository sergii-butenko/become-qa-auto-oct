# PYTHON
FROM python:3.7-slim-bullseye

#JAVA
# FROM openjdk:22-slim-bullseye

# install dependencies 
# COPY requirements file ONLY
RUN pip install pytest requests selenium

# mkdri /tests && cd /tests
WORKDIR /tests

# stands for 
# COPY EVERYTHING from LOCALFOLDER to CURRENT FODLER IN CONTAINER(which is /tests)
COPY . .

# specidfy command to run
CMD [ "pytest", "-k", "test_search_for_existing_repo"]