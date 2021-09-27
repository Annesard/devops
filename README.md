# DevOps Course Labs

[![CI to Docker Hub](https://github.com/Annesard/devops/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/Annesard/devops/actions/workflows/main.yml)

## Description
This project intend to provide information about the best practices on the practical example of the web application. The webapp is used to get the current time in Moscow, Russia

## Getting Started
### Dependencies
python 3

django framework

## Executing program
### To execute the webapp:

Clone the repository to your computer. After that please go to app_python/mysite.

Now inside this directory run ```python3 manage.py startproject```

Then open your browser and visit http://127.0.0.1:8000/

### To find out the best practices:

Please go to app_python/mysite and find there python.md file, docker.md and CI.md

## Docker
My repository name on docker hub is anessard/lab1

In order to run the image please use following command:

```docker run -it -p 8020:8020 anessard/lab1```

Then visit: http://127.0.0.1:8020/

## Unit test

There is a unit test that ensures corectness of the time displayed

It is located app_python/my_site/time2/tests.py

Please go to app_python/mysite.

To run it, execute the following comand:
```python3 manage.py test```

## Ansible

In order to run the playbook please cd to ansible then run

'''ansible-playbook -i inventory/aws_ec2.yaml  playbooks/playbook.yaml -u ubuntu -vvv'''

## Author
Anastassiya Ryabkova

BS18SE-02

Innopolis University

a.ryabkova@innopolis.university

## Lab 12

my app "/" show current time
"/visits" show visitor
