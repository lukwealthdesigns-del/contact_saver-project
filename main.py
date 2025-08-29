from pathlib import Path
import os
import file_ops 
from file_ops import save_participant
from  file_ops import load_participants


# Ensure the workspace directory exists
workspace = Path("participant_pkg")
workspace.mkdir(exist_ok=True)

from file_ops import save_participant, load_participants

# --- Validation functions ---
def validate_name(value):
    return len(value.strip()) > 0

def validate_age(value):
    return value.isdigit()

def validate_phone(value):
    return value.isdigit() and len(value) == 11

def validate_track(value):
    return len(value.strip()) > 0

def main():
    # Define CSV file path
    path = Path("participant_pkg/contacts.csv")

    print("\n--- Enter New Participant Details ---")

    participant_dict = {}

    # --- Name ---
    try:
        name = input("Enter Name: ").strip()
        if validate_name(name):
            participant_dict["Name"] = name
        else:
            print("Invalid name. It cannot be empty.")
            participant_dict["Name"] = None
    except Exception as e:
        print(f"Error reading name: {e}")
        participant_dict["Name"] = None

    # --- Age ---
    try:
        age_input = input("Enter Age: ").strip()
        if validate_age(age_input):
            participant_dict["Age"] = int(age_input)
        else:
            print("Invalid age. Must be a number.")
            participant_dict["Age"] = None
    except Exception as e:
        print(f"Error reading age: {e}")
        participant_dict["Age"] = None

    # --- Phone ---
    try:
        phone = input("Enter Phone (11 digits): ").strip()
        if validate_phone(phone):
            participant_dict["Phone"] = phone
        else:
            print("Invalid phone. Must be exactly 11 digits.")
            participant_dict["Phone"] = None
    except Exception as e:
        print(f"Error reading phone: {e}")
        participant_dict["Phone"] = None

    # --- Track ---
    try:
        track = input("Enter Track: ").strip()
        if validate_track(track):
            participant_dict["Track"] = track
        else:
            print("Invalid track. It cannot be empty.")
            participant_dict["Track"] = None
    except Exception as e:
        print(f"Error reading track: {e}")
        participant_dict["Track"] = None

    # --- Save participant ---
    try:
        save_participant(path, participant_dict)
        print("Participant saved successfully!")
    except Exception as e:
        print(f"Error saving participant: {e}")

    # --- Summary ---
    try:
        participants = load_participants(path)
        print(f"\nTotal participants saved: {len(participants)}")
        if len(participants) > 0:
            print(participant_dict)
        else:
            print("No participants available to show.")
    except Exception as e:
        print(f"Error loading participants: {e}")

main()
