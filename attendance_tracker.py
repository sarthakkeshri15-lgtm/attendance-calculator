def calculate_percentage(total, attended):
    return (attended / total) * 100


def safe_bunks(total, attended, required=75):
    return int((attended - required/100 * total) / (required/100))


def classes_needed(total, attended, required=75):
    needed = 0
    future_total = total
    future_attended = attended
    while (future_attended / future_total) * 100 < required:
        future_total += 1
        future_attended += 1
        needed += 1
    return needed