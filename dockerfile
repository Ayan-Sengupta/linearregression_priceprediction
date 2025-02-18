# python3 is the env we need 
FROM python:3

# set the working directory in the container
WORKDIR /app

# install the required packages from the requirements.txt
COPY requirements.txt /tmp/requirements.txt
RUN pip install --requirement /tmp/requirements.txt

# copy the content of the local src directory to the working directory
COPY . /app

# command to run on container start
CMD [ "python", "./main.py" ]

