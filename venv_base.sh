#!/usr/bin/env bash

DIR="venv_base"

if [ -d "$DIR" ]; then
  echo -e "\nUpdating virtualenv ${DIR} ...\n"
else
  echo -e "\nInstalling virtualenv ${DIR} ...\n"
  python3 -m venv $DIR
fi

. $DIR/bin/activate
pip install -r requirements.txt

echo -e "\nDone.\n\nActivate with \". ${DIR}/bin/activate\"\n"
