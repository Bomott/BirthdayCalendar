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
 2. Run `convert.py` using Pipenv: `pipenv run python convert.py --title "title for events"[^1] PATH_TO_VCF PATH_TO_EXPORTED_ICS`
 3. (OPTIONAL: Delete old birthday calendar if you are updating the calendar.)
 4. Create new birthday calendar in Proton calendar.
 5. Upload newly created `birthdays.ics` to Proton calendar under settings. You can also drag-and-drop the file into your browser when your calendar is open.
 
[^1]: if you do not specify a title, it will default to "Geburtstag"