"""Contacts to birthday calendar converter."""
from datetime import datetime, date
from icalendar import Calendar, Event
import vobject


def generate_birthday_event(
    name: str, event_title: str, birthday_date: datetime, age: int = None
) -> Event:
    """Creates a yearly birthday event.

    Args:
        name (str): Name of the person will be in the title.
        event_title (str): Text that will be added to the persons name.
        birthday_date (datetime): Date of the birthday.
        age (int, optional): Age will be added to event title if available. Defaults to None.

    Returns:
        Event: Birthday event that can be added to icalendar calendar.
    """
    event = Event()
    title = f"{name} {event_title}"
    if age:
        title += f" ({age})"
    event.add("summary", title)
    this_years_birthday = birthday_date.replace(year=date.today().year)
    event.add("dtstart", this_years_birthday, parameters={"VALUE": "DATE"})
    event.add("rrule", {"freq": "yearly"})
    return event


def convert(
    input_vcf_file_path: str, output_ics_file_path: str, event_title: str = "Geburtstag"
):
    """Converts a .vcf contacts file from Proton Mail to a birthday calendar
    .ics that can be imported into Proton Calendar.

    Args:
        input_vcf_file_path (str): Path to the contacts file.
        output_ics_file_path (str): Path to the output .ics file.
        event_title (str, optional): Text that will be added to the name in
            the event title. Defaults to "Geburtstag".

    Raises:
        Exception: If the date does not match expectations.
    """

    birthdays = Calendar()

    with open(file=input_vcf_file_path, mode="r", encoding="utf-8") as vcf_file:
        data = vcf_file.read()
        addressbook = vobject.readComponents(data)

        while (entry := next(addressbook, None)) is not None:
            if "fn" not in entry.contents:
                continue
            name = entry.contents["fn"][0].value
            if "bday" in entry.contents:
                birthday_string = entry.contents["bday"][0].value
                age = None
                if "." in birthday_string:
                    birthday_object = datetime.strptime(
                        birthday_string, "%d.%m."
                    ).date()
                    birthday_object = birthday_object.replace(year=date.today().year)
                    print(
                        f"Fixed date without year: {birthday_string} -> {birthday_object}"
                    )
                    age = None
                elif birthday_string.isdigit() and len(birthday_string) == 2 + 2 + 4:
                    birthday_object = datetime.strptime(
                        birthday_string, "%Y%m%d"
                    ).date()
                    print(birthday_object)
                    age = date.today().year - birthday_object.year
                elif re.match(r'--\d{2}\d{2}', birthday_string):
                    birthday_object = datetime.strptime(birthday_string, "--%m%d").date()
                    birthday_object = birthday_object.replace(year=date.today().year)
                    print(
                        f"Fixed date without year: {birthday_string} -> {birthday_object}"
                    )
                    age = None

                else:
                    raise Exception(f"Date {birthday_string} not implemented")

                event = generate_birthday_event(
                    name=name,
                    event_title=event_title,
                    birthday_date=birthday_object,
                    age=age,
                )
                print(event.get(key="SUMMARY"))
                birthdays.add_component(event)

    with open(output_ics_file_path, "wb") as ics_file:
        ics_file.write(birthdays.to_ical())


if __name__ == "__main__":
    convert(input_vcf_file_path="export.vcf", output_ics_file_path="birthdays.ics")
