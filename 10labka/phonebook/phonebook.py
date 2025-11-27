import psycopg2
import csv
from database import get_connection

class PhoneBook:
    def __init__(self):
        self.conn = get_connection()
    
    def insert_from_csv(self, filename):
        try:
            cur = self.conn.cursor()
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    cur.execute("""
                        INSERT INTO phonebook (first_name, last_name, phone, email)
                        VALUES (%s, %s, %s, %s)
                    """, (row['first_name'], row['last_name'], row['phone'], row['email']))
            self.conn.commit()
            print("Data uploaded from CSV successfully!")
        except Exception as e:
            print(f"Error: {e}")
    
    def insert_from_console(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO phonebook (first_name, last_name, phone, email)
            VALUES (%s, %s, %s, %s)
        """, (first_name, last_name, phone, email))
        
        self.conn.commit()
        print("Contact added successfully!")
    
    def update_contact(self):
        phone = input("Enter phone number of contact to update: ")
        new_first_name = input("Enter new first name: ")
        
        cur = self.conn.cursor()
        cur.execute("UPDATE phonebook SET first_name = %s WHERE phone = %s", 
                   (new_first_name, phone))
        
        self.conn.commit()
        print("Contact updated successfully!")
    
    def query_contacts(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM phonebook ORDER BY first_name")
        results = cur.fetchall()
        
        if not results:
            print("No contacts found!")
            return
        
        print("\nContacts:")
        for contact in results:
            print(f"ID: {contact[0]}, Name: {contact[1]} {contact[2]}, Phone: {contact[3]}, Email: {contact[4]}")
    
    def delete_contact(self):
        phone = input("Enter phone number to delete: ")
        
        cur = self.conn.cursor()
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
        
        self.conn.commit()
        print("Contact deleted successfully!")
    
    def close(self):
        self.conn.close()