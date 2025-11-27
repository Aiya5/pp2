import psycopg2
import csv
import os
from database import connect_db

class PhoneBook:
    def __init__(self):
        self.conn = connect_db()
    
    def insert_from_csv(self, filename):
        if not os.path.exists(filename):
            print(f"Error: File {filename} not found!")
            return
        
        cur = self.conn.cursor()
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    cur.execute("""
                        INSERT INTO contacts (first_name, last_name, phone, email)
                        VALUES (%s, %s, %s, %s)
                        ON CONFLICT (phone) DO NOTHING
                    """, (row['first_name'], row['last_name'], row['phone'], row['email']))
            self.conn.commit()
            print("Data from CSV imported successfully!")
        except Exception as e:
            print(f"Error: {e}")
            self.conn.rollback()
    
    def insert_from_console(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        
        cur = self.conn.cursor()
        try:
            cur.execute("""
                INSERT INTO contacts (first_name, last_name, phone, email)
                VALUES (%s, %s, %s, %s)
            """, (first_name, last_name, phone, email))
            self.conn.commit()
            print("Contact added successfully!")
        except psycopg2.IntegrityError:
            print("Error: Phone number already exists!")
        except Exception as e:
            print(f"Error: {e}")
    
    def query_data(self):
        print("\nQuery options:")
        print("1. Show all contacts")
        print("2. Search by name")
        print("3. Search by phone")
        
        choice = input("Enter choice (1-3): ")
        cur = self.conn.cursor()
        
        if choice == '1':
            cur.execute("SELECT * FROM contacts ORDER BY first_name")
        elif choice == '2':
            name = input("Enter name to search: ")
            cur.execute("SELECT * FROM contacts WHERE first_name ILIKE %s OR last_name ILIKE %s", 
                       (f'%{name}%', f'%{name}%'))
        elif choice == '3':
            phone = input("Enter phone to search: ")
            cur.execute("SELECT * FROM contacts WHERE phone ILIKE %s", (f'%{phone}%',))
        else:
            print("Invalid choice!")
            return
        
        results = cur.fetchall()
        self.display_results(results)
    
    def display_results(self, contacts):
        if not contacts:
            print("No contacts found!")
            return
        
        print("\nID  First Name  Last Name   Phone         Email")
        print("-" * 50)
        for contact in contacts:
            print(f"{contact[0]:<3} {contact[1]:<11} {contact[2]:<11} {contact[3]:<13} {contact[4]}")
    
    def update_data(self):
        phone = input("Enter phone number of contact to update: ")
        new_first_name = input("Enter new first name: ")
        new_phone = input("Enter new phone: ")
        
        cur = self.conn.cursor()
        cur.execute("""
            UPDATE contacts 
            SET first_name = %s, phone = %s 
            WHERE phone = %s
        """, (new_first_name, new_phone, phone))
        
        self.conn.commit()
        if cur.rowcount > 0:
            print("Contact updated successfully!")
        else:
            print("Contact not found!")
    
    def delete_data(self):
        phone = input("Enter phone number to delete: ")
        
        cur = self.conn.cursor()
        cur.execute("DELETE FROM contacts WHERE phone = %s", (phone,))
        
        self.conn.commit()
        if cur.rowcount > 0:
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")
    
    def close(self):
        self.conn.close()