# -*- coding: utf-8 -*-
#use with GNU Make for windows
#Author: Denis Dzíbela xdzibe00

PY = python3

.PHONY: all pack clean test doc run profile help sphinx

#runs the program
all: run

#requires powershell 5.0 or higher
#pack for WIS
pack: doc clean
	-mkdir ..\..\src
	-robocopy /MIR ..\src ..\..\src
	-copy ..\uzivatelska_prirucka.pdf ..\..
	-copy ..\hodnoceni.txt ..\..
	-echo %time% %date% > ..\..\odevzdani.txt
#hold my breath as I wish for death//oh please god help me
	-powershell /C Compress-Archive -Path "..\..\src", "..\..\uzivatelska_prirucka.pdf", "..\..\hodnoceni.txt", "..\..\odevzdani.txt" -DestinationPath ..\..\xmicek09_xmojze00_xdzibe00_xdemsk00.zip -CompressionLevel Optimal -Force
	-rmdir /s /q %cd%\..\..\src
	-del /q %cd%\..\..\uzivatelska_prirucka.pdf
	-del /q %cd%\..\..\hodnoceni.txt
	-del /q %cd%\..\..\odevzdani.txt
#now the world is gone, I'm just one//oh god wake me

#removes files that are not needed
clean:
	-rmdir /s /q %cd%\..\doc
	-rmdir /s /q %cd%\__pycache__
	-del /q %cd%\..\calculathor.exe
#some other stuff?

#runs math library unit tests
test: mathlib_unittest.py math_lib.py
	$(PY) -m unittest $<

#runs script to generate project documentation
doc:
	-cd sphinx && make html
	-mkdir ..\doc 
	-robocopy /MIR sphinx\_build\html ..\doc
	-cd sphinx && make clean

#installs sphinx
sphinx:
	-pip install sphinx

#runs the calculator
run: calculathor.py math_lib.py
	$(PY) $<

#runs profiling script
profile: stddev.py math_lib.py
	$(PY) $< < data.txt

#explains limitations of this makefile
help:
	-@echo Written using GNU Make for Windows 10 32bit
	-@echo Implementation limitations:
	-@echo 1.   Target "pack" requires powershell 5.0 or higher (5.0 comes preinstalled on Windows 10 systems)
	-@echo      Only wanting to use built-in tools the powershell utility Compress-Archive is used to create a zip file,
	-@echo      this utility features undocumented behaviour wherein hidden folders are ommited from the resulting archive.
	-@echo      It was decided that make pack will thus prepare a zip file for WIS in accordance with https://discordapp.com/channels/461541385204400138/493514738484117514/704681361147035750