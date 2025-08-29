
from pathlib import Path
import csv

def save_participant(path, participant_dict):

# Save a participant to a CSV file.
#  If the file does not exist, create it and add a header.
# If it exists, just append the new participant.
   

    # Ensure directory exists
    parent_dir = path.parent
    exists = parent_dir.exists()
    if exists:
        pass
    else:
        parent_dir.mkdir(parents=True)

    file_exists = path.exists()

    f = path.open("a", newline="", encoding="utf-8")
    writer = csv.DictWriter(f, fieldnames=["Name", "Age", "Phone", "Track"])

    if file_exists:
        writer.writerow(participant_dict)
    else:
        writer.writeheader()
        writer.writerow(participant_dict)

    f.close()


def load_participants(path):

    # Load all participants from CSV into a list of dictionaries.
    # Return an empty list if the file does not exist.
    
    exists = path.exists()
    if exists:
        f = path.open()
        reader = csv.DictReader(f)
        data = list(reader)
        f.close()
        return data
    else:
        return []