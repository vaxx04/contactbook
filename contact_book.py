import mysql.connector
#pip install mysql-connector-python
from mysql.connector import Error
from contact import Contact

class ContactBook:
    def __init__(self):
        self.connection = self.create_connection()

    def create_connection(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='contact_book',
                user='root',
                password='rashmi@0507'
            )
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"Error: {e}")
            return None

    def add_contact(self, contact):
        cursor = self.connection.cursor()
        query = "INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)"
        values = (contact.name, contact.phone, contact.email)
        cursor.execute(query, values)
        self.connection.commit()
        print("Contact added successfully!")

    def display_all_contacts(self):
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM contacts"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            contact = Contact(row['name'], row['phone'], row['email'])
            contact.display_contact()
            print("-----------------------")

    def search_contact(self, name):
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM contacts WHERE name = %s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        if result:
            return Contact(result['name'], result['phone'], result['email'])
        return None

    def update_contact(self, name, new_name=None, new_phone=None, new_email=None):
        cursor = self.connection.cursor()
        query = "UPDATE contacts SET name = %s, phone = %s, email = %s WHERE name = %s"
        values = (new_name if new_name else name,
                  new_phone if new_phone else self.search_contact(name).phone,
                  new_email if new_email else self.search_contact(name).email,
                  name)
        cursor.execute(query, values)
        self.connection.commit()
        print(f"Contact '{name}' has been updated.")

    '''def delete_contact(self, name):
        cursor = self.connection.cursor()
        query = "DELETE FROM contacts WHERE name = %s"
        cursor.execute(query, (name,))
        self.connection.commit()
        print(f"Contact '{name}' has been deleted.")'''

    def delete_contact(self, name):
        cursor = self.connection.cursor()
        query = "DELETE FROM contacts WHERE name = %s"
        cursor.execute(query, (name,))
        
        # Check the number of rows affected by the DELETE operation
        if cursor.rowcount == 0:
            print(f"No contact found with the name '{name}'.")
        else:
            self.connection.commit()
        print(f"Contact '{name}' has been deleted.")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed")
