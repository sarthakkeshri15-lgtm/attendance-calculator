from data_handler import load_subjects, save_subjects


def get_subjects_data():
    subjects = load_subjects()

    print("\nCurrent saved subjects:", list(subjects.keys()) if subjects else "None")

    while True:
        raw_name = input("\nEnter subject name to add/update (or type 'done' to finish): ").strip()
        if raw_name.lower() == "done":
            break

        # Check if this subject already exists, ignoring case
        existing_key = None
        for key in subjects:
            if key.lower() == raw_name.lower():
                existing_key = key
                break

        name = existing_key if existing_key else raw_name

        try:
            total = int(input(f"Total classes held for {name}: "))
            attended = int(input(f"Classes attended for {name}: "))
            if total <= 0 or attended < 0 or attended > total:
                print("Invalid numbers, try this subject again.")
                continue
        except ValueError:
            print("Please enter valid numbers.")
            continue

        subjects[name] = {"total": total, "attended": attended}

    save_subjects(subjects)
    return subjects