#!/usr/bin/python3
"""
Task 00 - Simple templating program.

Provides a function generate_invitations(template, attendees) that:
- Validates input types
- Handles empty template and empty attendees list
- Fills placeholders with attendee data or 'N/A'
- Writes output files named output_X.txt (starting from 1)
"""

import os


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and a list
    of attendee dictionaries.

    Args:
        template (str): Template string with placeholders:
                        {name}, {event_title}, {event_date}, {event_location}
        attendees (list[dict]): List of dictionaries with attendee data.
    """
    # --- Type checks ---
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # --- Empty checks ---
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # --- Process each attendee ---
    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        content = template

        # Replace each placeholder with provided data or "N/A"
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value_str = "N/A"
            else:
                value_str = str(value)
            content = content.replace("{" + key + "}", value_str)

        filename = f"output_{index}.txt"

        # Optional: check if file exists (we overwrite silently, but check is there)
        if os.path.exists(filename):
            pass

        # Write the filled template to file
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
        except OSError as e:
            print(f"Error: could not write to {filename}: {e}")
