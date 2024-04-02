#!/bin/zsh
VERSION=dev

pip3 freeze > requirements.txt

docker build -t curree_backend:$VERSION .