# -*- coding: utf-8 -*-
#use with GNU Make for windows
#Author: Denis Dzíbela xdzibe00

PY = python3

.PHONY: all clean pack

all:

pack: doc clean
	-mkdir ..\..\doc
	-mkdir ..\..\install
	-mkdir ..\..\repo
#-robocopy /MIR ..\..\ivs-project-2 ..\..\repo
	robocopy /MIR ..\install ..\..\install
#-robocopy /MIR ..\doc ..\..\doc
#zip

clean:
	-rmdir /s /q %cd%\__pycache__
	-del /q %cd%\..\calculathor.exe
#some other stuff

test: mathlib_unittest.py math_lib.py
	$(PY) -m unittest $<

doc:
#spustit script od Elišky

run: calculathor.py math_lib.py
	$(PY) $<

profile: stddev.py math_lib.py
	$(PY) $< < data.txt