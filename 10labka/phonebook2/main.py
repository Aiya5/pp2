from phonebook import PhoneBook
from database import create_table

def main():
    # Create table first
    create_table()
    
    # Create PhoneBook instance
    pb = PhoneBook()
    
    while True:
        print("\n" + "="*50)
        print("PHONEBOOK APPLICATION")
        print("="*50)
        print("1. Upload data from CSV")
        print("2. Add contact from console")
        print("3. Query contacts")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            pb.insert_from_csv('contacts.csv')
        elif choice == '2':
            pb.insert_from_console()
        elif choice == '3':
            pb.query_data()
        elif choice == '4':
            pb.update_data()
        elif choice == '5':
            pb.delete_data()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-6")
    
    pb.close()

if __name__ == "__main__":
    main()