#!/bin/bash
brew upgrade python
cp .load_env.example .load_env
pip3 install virtualenvwrapper
virtualenv load_test
source load_test/bin/activate
cd load_test
printf 'locustio\npython-dotenv'>requirements.txt
pip3 install -r requirements.txt
locust 