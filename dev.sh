#!/bin/bash
if [ "$(which nodemon)" != ""];
then
  echo "Nodemon is required. Use 'npm i -g nodemon' to install nodemon"
  exit 1
fi

nodemon -w **/*.py --exec "python3" app.py
