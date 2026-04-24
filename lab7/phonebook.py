from connect import connect
import csv

def insert_contact(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def show_contacts():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

def update_contact(name, new_phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE contacts SET phone=%s WHERE name=%s", (new_phone, name))
    conn.commit()
    cur.close()
    conn.close()

def delete_contact(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE name=%s", (name,))
    conn.commit()
    cur.close()
    conn.close()

def search_by_prefix(prefix):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", (prefix + "%",))
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

def import_csv():
    conn = connect()
    cur = conn.cursor()
    with open("lab7/contacts.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
          cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (row[0], row[1]))
        conn.commit()
    conn.commit()
    cur.close()
    conn.close()
    

while True:
    print("\n1 Add")
    print("2 Show")
    print("3 Update")
    print("4 Delete")
    print("5 Search by prefix")
    print("6 Import CSV")
    print("0 Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        insert_contact(name, phone)

    elif choice == "2":
        show_contacts()

    elif choice == "3":
        name = input("Name: ")
        new_phone = input("New phone: ")
        update_contact(name, new_phone)

    elif choice == "4":
        name = input("Name: ")
        delete_contact(name)

    elif choice == "5":
        prefix = input("Prefix: ")
        search_by_prefix(prefix)

    elif choice == "6":
        import_csv()

    elif choice == "0":
        break
