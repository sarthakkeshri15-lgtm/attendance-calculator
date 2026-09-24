from attendance_tracker import calculate_percentage, safe_bunks, classes_needed


def generate_report(subjects, required=75):
    print("\n===== ATTENDANCE REPORT =====")
    total_attended_all = 0
    total_classes_all = 0
    at_risk = []

    for name, data in subjects.items():
        total = data["total"]
        attended = data["attended"]
        percentage = calculate_percentage(total, attended)

        total_attended_all += attended
        total_classes_all += total

        if percentage >= required:
            bunks = safe_bunks(total, attended, required)
            print(f"{name}: {percentage:.2f}% ✅ Safe — can miss {bunks} more class(es)")
        else:
            needed = classes_needed(total, attended, required)
            print(f"{name}: {percentage:.2f}% ⚠️  At risk — attend {needed} more class(es)")
            at_risk.append(name)

    if total_classes_all > 0:
        overall = calculate_percentage(total_classes_all, total_attended_all)
        print(f"\nOverall attendance across all subjects: {overall:.2f}%")

    if at_risk:
        print(f"Subjects needing attention: {', '.join(at_risk)}")
    else:
        print("All subjects are in safe zone. 🎉")