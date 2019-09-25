# snapShotAlayzer30001
Demo project to manage EC2 instance snapshots


## About

This project is a demo, and uses boto3 to manage EC2 instance snapshots. Also do not use quotes around the pipenv run python shotty/shotty.py command. the ACG video tutorial instructs you to in error.

## Configuring

shotty uses the configuration file created bu the aws cli. e.g.

`aws configure --profile shotty`

## Running

`pipenv run python shotty/shotty.py <command> <--project=PROJECT>`

*command* is list, start, or stop_instances
*project* is optional
