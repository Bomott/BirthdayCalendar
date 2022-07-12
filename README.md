# BirthdayCalendar
Script for turning a Proton contacts export into a birthday calendar.

## Requirements:
 - Python >= 3.9 (see Pipfile)
 - Pipenv

## Setup:
 1. Install requirements: `pipenv install`

## Use it 
to convert downloaded contacts (.vcf) into birthday calendar (.ics):

 1. Make sure your shell is in the parent directory of `convert.py`.
 2. Put downloaded contacts file as `export.vcf` in the directory next to `convert.py`.
 3. Run `convert.py` using Pipenv: `pipenv run python convert.py`
 4. (OPTIONAL: Delete old birthday calendar if you are updating the calendar.)
 5. Create new birthday calendar in Proton calendar.
 6. Upload newly created `birthdays.ics` to Proton calendar under settings.
 