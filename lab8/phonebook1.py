from connect import connect


def search_pattern(pattern):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_contacts(%s);", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


def show_paginated(limit, offset):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


def upsert_user(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL upsert_contact(%s, %s);", (name, phone))
    conn.commit()
    cur.close()
    conn.close()


def delete_user(value):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_contact(%s);", (value,))
    conn.commit()
    cur.close()
    conn.close()


def insert_many_users():
    n = int(input("How many users: "))
    names = []
    phones = []

    for i in range(n):
        print(f"User {i + 1}")
        name = input("Name: ")
        phone = input("Phone: ")
        names.append(name)
        phones.append(phone)

    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_many_contacts(%s, %s);", (names, phones))
    conn.commit()
    cur.close()
    conn.close()


while True:
    print("\n1 Add or update user")
    print("2 Search by pattern")
    print("3 Show paginated")
    print("4 Delete by name or phone")
    print("5 Insert many users")
    print("0 Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        upsert_user(name, phone)
        print("Done")

    elif choice == "2":
        pattern = input("Pattern: ")
        search_pattern(pattern)

    elif choice == "3":
        limit = int(input("Limit: "))
        offset = int(input("Offset: "))
        show_paginated(limit, offset)

    elif choice == "4":
        value = input("Name or phone: ")
        delete_user(value)
        print("Done")

    elif choice == "5":
        insert_many_users()
        print("Done")

    elif choice == "0":
        break

    else:
        print("Invalid choice")