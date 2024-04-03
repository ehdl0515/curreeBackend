#!/bin/zsh
VERSION=dev

pip3 freeze > requirements.txt

docker build -t ehdl0515/curree_backend:$VERSION .