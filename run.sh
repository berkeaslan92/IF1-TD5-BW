pip install -r requirements.txt

source .v/bin/activate

FILE=main.py

if test -f "$FILE"; then
	echo "$FILE exists."
	#!/bin/sh
	python main.py
fi
