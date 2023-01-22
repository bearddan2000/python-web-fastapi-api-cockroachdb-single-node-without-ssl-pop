# python-web-fastapi-api-cockroachdb-single-node-without-ssl-pop

## Description
Creates an api of `pop` for a fastapi project.

A python flask build, that connects to single node cluster
cockroach database without ssl.

## Tech stack
- python
  - fastapi
  - sqlalchemy
- bootstrap
- jquery
- dataTable
- cockroachdb

## Docker stack
- python:latest
- cockroachdb/cockroach:v19.2.4

## To run
`sudo ./install.sh -u`
- Endpoints
  - [Select all](http://localhost/pop)
- [Webui](http://localhost:8000)

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credit
- [Cockroach setup](https://github.com/s0rg/cockroach-compose)
