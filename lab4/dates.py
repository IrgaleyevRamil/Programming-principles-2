"""
Practice - Dates and Time (datetime)

Topics:
1) datetime.now() and datetime.today()
2) Creating datetime/date objects
3) Formatting with strftime()
4) timedelta (adding/subtracting time)
5) Parsing strings with strptime()
"""

from datetime import datetime, date, time, timedelta


# =========================================================
# TOPIC 1: datetime.now() and datetime.today() (5 examples)
# =========================================================

# Example 1
now1 = datetime.now()
print("now1:", now1)

# Example 2
today1 = datetime.today()
print("today1:", today1)

# Example 3
print("Year:", datetime.now().year)

# Example 4
print("Hour:", datetime.now().hour)

# Example 5
now2 = datetime.now()
print("Date part:", now2.date(), "| Time part:", now2.time())


# =========================================================
# TOPIC 2: Creating datetime/date objects (5 examples)
# =========================================================

# Example 1
d1 = date(2026, 2, 26)
print("date:", d1)

# Example 2
t1 = time(14, 30, 0)
print("time:", t1)

# Example 3
dt1 = datetime(2025, 12, 31, 23, 59, 59)
print("datetime:", dt1)

# Example 4
dt2 = datetime.combine(date(2024, 9, 1), time(8, 0))
print("combined:", dt2)

# Example 5
d2 = date.today()
print("today date:", d2)


# =========================================================
# TOPIC 3: Formatting with strftime() (5 examples)
# =========================================================

# Example 1
dt = datetime.now()
print(dt.strftime("%Y-%m-%d"))

# Example 2
print(dt.strftime("%d/%m/%Y"))

# Example 3
print(dt.strftime("%H:%M:%S"))

# Example 4
print(dt.strftime("%A"))  # weekday name

# Example 5
print(dt.strftime("%Y-%m-%d %H:%M"))


# =========================================================
# TOPIC 4: timedelta (adding/subtracting time) (5 examples)
# =========================================================

# Example 1
now = datetime.now()
after_7_days = now + timedelta(days=7)
print("After 7 days:", after_7_days)

# Example 2
before_2_hours = now - timedelta(hours=2)
print("Before 2 hours:", before_2_hours)

# Example 3
after_90_minutes = now + timedelta(minutes=90)
print("After 90 minutes:", after_90_minutes)

# Example 4
tomorrow = date.today() + timedelta(days=1)
print("Tomorrow:", tomorrow)

# Example 5
diff = (datetime(2026, 3, 1) - datetime(2026, 2, 26))
print("Difference days:", diff.days)


# =========================================================
# TOPIC 5: Parsing strings with strptime() (5 examples)
# =========================================================

# Example 1
s1 = "2026-02-26"
dt1 = datetime.strptime(s1, "%Y-%m-%d")
print("Parsed:", dt1)

# Example 2
s2 = "26/02/2026"
dt2 = datetime.strptime(s2, "%d/%m/%Y")
print("Parsed:", dt2)

# Example 3
s3 = "2026-02-26 14:45"
dt3 = datetime.strptime(s3, "%Y-%m-%d %H:%M")
print("Parsed:", dt3)

# Example 4
s4 = "14:30:15"
t2 = datetime.strptime(s4, "%H:%M:%S").time()
print("Parsed time:", t2)

# Example 5
s5 = "Feb 26, 2026"
dt5 = datetime.strptime(s5, "%b %d, %Y")
print("Parsed:", dt5)