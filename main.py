from subject_manager import get_subjects_data
from analytics import generate_report

REQUIRED_PERCENTAGE = 75


def main():
    print("=== Attendance Safety Calculator ===")
    while True:
        subjects = get_subjects_data()
        if subjects:
            generate_report(subjects, REQUIRED_PERCENTAGE)
        else:
            print("No subjects entered.")

        again = input("\nRun again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()