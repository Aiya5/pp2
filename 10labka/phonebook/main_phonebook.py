from phonebook import PhoneBook
from database import create_tables

def main():
    create_tables()
    pb = PhoneBook()
    
    while True:
        print("\n=== PhoneBook Menu ===")
        print("1. Upload from CSV")
        print("2. Add contact from console")
        print("3. Update contact")
        print("4. Show all contacts")
        print("5. Delete contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            pb.insert_from_csv('contacts.csv')
        elif choice == '2':
            pb.insert_from_console()
        elif choice == '3':
            pb.update_contact()
        elif choice == '4':
            pb.query_contacts()
        elif choice == '5':
            pb.delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice!")
    
    pb.close()

if __name__ == "__main__":
    main()
    