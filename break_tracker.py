SECONDS_PER_MINUTE = 60


def check_average_break(break_lengths, goal_minutes):
    """Compare the average break length to the user's goal."""
    if not break_lengths:
        return "No breaks logged yet"

    average = sum(break_lengths) / len(break_lengths)

    if average >= goal_minutes:
        return "Good job"
    return "Take more breaks"


def minutes_to_seconds(minutes):
    """Convert break minutes to seconds for the timer."""
    if minutes < 0:
        raise ValueError("Minutes cannot be negative")
    return minutes * SECONDS_PER_MINUTE


break_lengths = [5, 10, 15]
print(check_average_break(break_lengths, 10))
print(minutes_to_seconds(5))
