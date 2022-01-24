# Base python docker image
FROM python:3.9.5-buster

# Import Code
ADD . /Code

# Changing the directory
WORKDIR /Code


# Installing lib
RUN pip install flask

# Exposing the poert
EXPOSE 5001

# Running python file
CMD python main.py