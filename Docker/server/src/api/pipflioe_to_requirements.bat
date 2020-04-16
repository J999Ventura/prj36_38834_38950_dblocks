@echo off
pipenv lock
pipenv lock -r > requirements_lock.txt
more +1 requirements_lock.txt > requirements.txt
del /f requirements_lock.txt
move requirements.txt ..\..\