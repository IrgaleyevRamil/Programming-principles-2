from datetime import datetime, date, timedelta

# =========================================================
# TASK 1: Subtract five days from current date
# =========================================================

now = datetime.now()
five_days_earlier = now - timedelta(days=5)

print("Current datetime:", now)
print("Five days earlier:", five_days_earlier)


# =========================================================
# TASK 2: Print yesterday, today, tomorrow
# =========================================================

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


# =========================================================
# TASK 3: Drop microseconds from datetime
# =========================================================

current_time = datetime.now()
no_microseconds = current_time.replace(microsecond=0)

print("Original datetime:", current_time)
print("Without microseconds:", no_microseconds)


# =========================================================
# TASK 4: Calculate two date difference in seconds
# =========================================================

date1 = datetime(2026, 2, 26, 10, 0, 0)
date2 = datetime(2026, 2, 27, 15, 30, 0)

difference = date2 - date1
seconds = difference.total_seconds()

print("Difference in seconds:", seconds)