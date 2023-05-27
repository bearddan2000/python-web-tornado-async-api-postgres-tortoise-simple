# python-web-tornado-async-api-postgres-tortoise-simple

## Description
Simple web app that serves an api
for a tornado project as a frontend 
and remote calling a fastapi backend.

Uses async functions and tortoise oem to query a table `dog`.

Remotely tested with *testify*.

## Tech stack
- python
  - tornado
  - fastapi
  - sqlalchemy
  - testify
  - requests
- postgresql

## Docker stack
- python:latest
- postgres:alpine

## To run
`sudo ./install.sh -u`
- Get all dogs: http://localhost/dog

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credit
- [HTTPServer config](https://phrase.com/blog/posts/tornado-web-framework-i18n/)
- [Code based on](https://www.tornadoweb.org/en/stable/)
- [Sqlalchemy code](https://medium.com/swlh/tornado-and-sqlalchemy-847eecbc0445)