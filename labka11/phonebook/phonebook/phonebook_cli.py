import psycopg2
import csv
from config import load_config

config = load_config()

#добавляем контактик
def insert_contact_console():
    first_name = input("Enter first name: ").strip()
    phone = input("Enter phone: ").strip()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("CALL add_or_update_user(%s, %s);", (first_name, phone))
                conn.commit()
                print("Inserted/updated contact via add_or_update_user.")
    except Exception as e:
        print("Error inserting contact:", e)
#вставляем все из списка сиэсви
def insert_contacts_csv(file_path):
    try:
        rows = []
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader, None)
            for row in reader:
                if len(row) == 0:
                    continue
                rows.append(row)

        if not rows:
            print("No rows to insert.")
            return

        names = []
        phones = []

        for r in rows:
            names.append(r[0].strip())
            phones.append(r[-1].strip())

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT add_many_users(%s::TEXT[], %s::TEXT[]);", (names, phones))
                invalid = cur.fetchone()[0]
                conn.commit()

                print(f"Processed {len(rows)} rows via add_many_users.")
                if invalid:
                    print("\nIncorrect phones:")
                    for b in invalid:
                        print(" -", b)
                else:
                    print("No invalid rows reported.")

    except Exception as e:
        print("Error inserting CSV contacts:", e)

# обновляем контакики
def update_contact():
    first_name = input("Enter existing first name: ").strip()
    new_phone = input("Enter new phone: ").strip()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("CALL add_or_update_user(%s, %s);", (first_name, new_phone))
                conn.commit()
                print("Contact updated via add_or_update_user.")
    except Exception as e:
        print("Error updating contact:", e)

# поиск по чатям страничкам и все
def query_contacts():
    mode = input("Search mode - pattern or paged or all? (pattern/paged/all): ").strip().lower()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if mode == "pattern":
                    pattern = input("Enter pattern: ").strip()
                    cur.execute("SELECT * FROM search_contacts(%s);", (pattern,))
                elif mode == "paged":
                    limit = int(input("Enter limit: ").strip() or 10)
                    offset = int(input("Enter offset: ").strip() or 0)
                    cur.execute("SELECT * FROM paginate_contacts(%s, %s);", (limit, offset))
                elif mode == "all":
                    cur.execute("SELECT id, first_name, phone FROM contacts ORDER BY id;")
                else:
                    print("Invalid choice")
                    return

                rows = cur.fetchall()
                if not rows:
                    print("No contacts found.")
                else:
                    for r in rows:
                        print(r)
    except Exception as e:
        print("Error querying contacts:", e)
# Удаляем контакт номер
def delete_contact():
    choice = input("Delete by name or phone? (name/phone): ").strip().lower()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if choice == "name":
                    name = input("Enter first name: ").strip()
                    cur.execute("CALL delete_contact(%s, NULL);", (name,))
                elif choice == "phone":
                    phone = input("Enter phone: ").strip()
                    cur.execute("CALL delete_contact(NULL, %s);", (phone,))
                else:
                    print("Invalid choice")
                    return
                conn.commit()
                print("Deleted successfully.")
    except Exception as e:
        print("Error deleting contact:", e)

# добавляем юзеров 
def insert_many_users_console():
    n = int(input("How many users to insert? "))
    names = []
    phones = []

    for _ in range(n):
        names.append(input("Enter first name: ").strip())
        phones.append(input("Enter phone: ").strip())

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT add_many_users(%s, %s);", (names, phones))
                incorrect = cur.fetchone()[0]
                conn.commit()

        if incorrect:
            print("Incorrect entries:")
            for x in incorrect:
                print(" -", x)
        else:
            print("All data inserted successfully!")
    except Exception as e:
        print("Error:", e)

#простые страничкика
def paged_query():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM paginate_contacts(%s, %s);", (limit, offset))
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except Exception as e:
        print("Error:", e)

# Менюю опшоны
def menu():
    while True:
        print("\n1. Insert contact (console)")
        print("2. Insert contacts (CSV)")
        print("3. Update contact")
        print("4. Query contacts")
        print("5. Delete contact")
        print("6. Insert many users (console)")
        print("7. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            insert_contact_console()
        elif choice == "2":
            file_path = input("Enter CSV file path: ").strip()
            insert_contacts_csv(file_path)
        elif choice == "3":
            update_contact()
        elif choice == "4":
            query_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            insert_many_users_console()
        elif choice == "7":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
