import psycopg2
import csv
from config import load_config

config = load_config()

#вводим данные
def insert_contact_console():
    first_name = input("Enter first name: ")
    phone = input("Enter phone: ")
    sql = "INSERT INTO contacts(first_name,phone) VALUES (%s,%s) RETURNING id;"
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (first_name, phone))
                contact_id = cur.fetchone()[0]
                conn.commit()
                print(f"Inserted contact with id {contact_id}")
    except Exception as e:
        print("Error inserting contact:", e)

#добавляем уже готовые данные
def insert_contacts_csv(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header
            data = [tuple(row) for row in reader]
        sql = "INSERT INTO contacts(first_name,phone) VALUES (%s,%s);"
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.executemany(sql, data)
                conn.commit()
                print(f"Inserted {len(data)} contacts from CSV")
    except Exception as e:
        print("Error inserting CSV contacts:", e)

# обноваляем все данные
def update_contact():
    phone = input("Enter the phone of contact to update: ")
    choice = input("Update first name or phone? (name/phone): ").strip().lower()
    if choice == "name":
        new_name = input("Enter new first name: ")
        sql = "UPDATE contacts SET first_name=%s WHERE phone=%s;"
        params = (new_name, phone)
    elif choice == "phone":
        new_phone = input("Enter new phone: ")
        sql = "UPDATE contacts SET phone=%s WHERE phone=%s;"
        params = (new_phone, phone)
    else:
        print("Invalid choice")
        return
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                conn.commit()
                print("Contact updated")
    except Exception as e:
        print("Error updating contact:", e)

# фильтруем данные
def query_contacts():
    filter_by = input("Filter by first name, or phone? (name/last/phone/all): ").strip().lower()
    if filter_by == "name":
        val = input("Enter first name: ")
        sql = "SELECT * FROM contacts WHERE first_name=%s;"
        params = (val,)
    elif filter_by == "phone":
        val = input("Enter phone: ")
        sql = "SELECT * FROM contacts WHERE phone=%s;"
        params = (val,)
    else:
        sql = "SELECT * FROM contacts;"
        params = ()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except Exception as e:
        print("Error querying contacts:", e)

# удаляем данные
def delete_contact():
    choice = input("Delete by first name or phone? (name/phone): ").strip().lower()
    if choice == "name":
        val = input("Enter first name: ")
        sql = "DELETE FROM contacts WHERE first_name=%s;"
    elif choice == "phone":
        val = input("Enter phone: ")
        sql = "DELETE FROM contacts WHERE phone=%s;"
    else:
        print("Invalid choice")
        return
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (val,))
                conn.commit()
                print("Contact deleted")
    except Exception as e:
        print("Error deleting contact:", e)

#меню общее
def menu():
    while True:
        print("\n1. Insert contact (console)")
        print("2. Insert contacts (CSV)")
        print("3. Update contact")
        print("4. Query contacts")
        print("5. Delete contact")
        print("6. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            insert_contact_console()
        elif choice == "2":
            file_path = input("Enter CSV file path: ")
            insert_contacts_csv(file_path)
        elif choice == "3":
            update_contact()
        elif choice == "4":
            query_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
