import json
from datetime import datetime

# Helper function to load data from JSON files
def load_data(Organizer):
    with open(Organizer ,'r') as file:
        data = json.load(file)
    return data

# Helper function to save data to JSON files
def save_data(data, Organizer):
    with open(Organizer ,'w') as file:
        json.dump(data, file, indent=4)

# Register a new user
def register_user(user_type):
    full_name = input("Enter your full name: ")
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    
    if user_type == 'Organizer':
        organizer_data = load_data('organizers.json')
        organizer_data.append({
            'Full Name': full_name,
            'Email': email,
            'Password': password
        })
        save_data(organizer_data, 'organizers.json')
        print("Organizer registration successful!")
    elif user_type == 'Member':
        member_data = load_data('members.json')
        member_data.append({
            'Full Name': full_name,
            'Email': email,
            'Password': password
        })
        save_data(member_data, 'members.json')
        print("Member registration successful!")

# User login
def login():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    
    # Check if user is an organizer
    organizer_data = load_data('organizers.json')
    for organizer in organizer_data:
        if organizer['Email'] == email and organizer['Password'] == password:
            print("Organizer login successful!")
            # Call organizer menu function
            organizer_menu()
            return
    
    # Check if user is a member
    member_data = load_data('members.json')
    for member in member_data:
        if member['Email'] == email and member['Password'] == password:
            print("Member login successful!")
            # Call member menu function
            member_menu()
            return
    
    print("Invalid credentials. Please try again.")

# Organizer menu
def organizer_menu():
    while True:
        print("\nOrganizer Menu:")
        print("1. Create Event")
        print("2. View Event List")
        print("3. View Event Details")
        print("4. Update Event")
        print("5. Delete Event")
        print("6. Logout")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            create_event()
        elif choice == '2':
            view_event_list()
        elif choice == '3':
            event_id = input("Enter the EventID: ")
            view_event_details(event_id)
        elif choice == '4':
            event_id = input("Enter the EventID: ")
            update_event(event_id)
        elif choice == '5':
            event_id = input("Enter the EventID: ")
            delete_event(event_id)
        elif choice == '6':
            print("Logged out successfully!")
            break
        else:
            print("Invalid choice. Please try again.")

# Member menu
def member_menu():
    while True:
        print("\nMember Menu:")
        print("1. View Registered Events")
        print("2. Register for Event")
        print("3. View Event Details")
        print("4. Update Password")
        print("5. Logout")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            view_registered_events()
        elif choice == '2':
            event_id = input("Enter the EventID: ")
            register_for_event(event_id)
        elif choice == '3':
            event_id = input("Enter the EventID: ")
            view_event_details(event_id)
        elif choice == '4':
            update_password()
        elif choice == '5':
            print("Logged out successfully!")
            break
        else:
            print("Invalid choice. Please try again.")

# Create a new event
def create_event():
    event_data = load_data('events.json')
    
    event_id = input("Enter the EventID: ")
    name = input("Enter the event name: ")
    organizer = input("Enter the organizer name: ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    start_time = input("Enter the start time (HH:MM:SS): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    end_time = input("Enter the end time (HH:MM:SS): ")
    total_seats = int(input("Enter the total seats: "))
    
    event_data.append({
        'ID': event_id,
        'Name': name,
        'Organizer': organizer,
        'Start Date': start_date,
        'Start Time': start_time,
        'End Date': end_date,
        'End Time': end_time,
        'Users Registered': [],
        'Capacity': total_seats,
        'Seats Available': total_seats
    })
    
    save_data(event_data, 'events.json')
    print("Event created successfully!")

# View the list of events created by the logged-in organizer
def view_event_list():
    organizer = input("Enter the organizer name: ")
    event_data = load_data('events.json')
    
    print("\nEvents created by", organizer, ":")
    for event in event_data:
        if event['Organizer'] == organizer:
            print("EventID:", event['ID'])
            print("Name:", event['Name'])
            print("Start Date:", event['Start Date'])
            print("Start Time:", event['Start Time'])
            print("End Date:", event['End Date'])
            print("End Time:", event['End Time'])
            print("------------------------------")

# View event details based on EventID
def view_event_details(event_id):
    event_data = load_data('events.json')
    
    for event in event_data:
        if event['ID'] == event_id:
            print("\nEvent Details:")
            print("EventID:", event['ID'])
            print("Name:", event['Name'])
            print("Organizer:", event['Organizer'])
            print("Start Date:", event['Start Date'])
            print("Start Time:", event['Start Time'])
            print("End Date:", event['End Date'])
            print("End Time:", event['End Time'])
            print("Total Seats:", event['Capacity'])
            print("Seats Available:", event['Seats Available'])
            return
    
    print("Event not found.")

# Update event details based on EventID
def update_event(event_id):
    event_data = load_data('events.json')
    
    for event in event_data:
        if event['ID'] == event_id:
            name = input("Enter the updated event name: ")
            start_date = input("Enter the updated start date (YYYY-MM-DD): ")
            start_time = input("Enter the updated start time (HH:MM:SS): ")
            end_date = input("Enter the updated end date (YYYY-MM-DD): ")
            end_time = input("Enter the updated end time (HH:MM:SS): ")
            
            event['Name'] = name
            event['Start Date'] = start_date
            event['Start Time'] = start_time
            event['End Date'] = end_date
            event['End Time'] = end_time
            
            save_data(event_data, 'events.json')
            print("Event updated successfully.")
            return
    
    print("Event not found.")

# Delete an event based on EventID
def delete_event(event_id):
    event_data = load_data('events.json')
    
    for event in event_data:
        if event['ID'] == event_id:
            event_data.remove(event)
            save_data(event_data, 'events.json')
            print("Event deleted successfully.")
            return
    
    print("Event not found.")

# View registered events by the logged-in member
def view_registered_events():
    member = input("Enter the member name: ")
    event_data = load_data('events.json')
    
    print("\nRegistered events for", member, ":")
    for event in event_data:
        if member in event['Users Registered']:
            print("EventID:", event['ID'])
            print("Name:", event['Name'])
            print("Organizer:", event['Organizer'])
            print("Start Date:", event['Start Date'])
            print("Start Time:", event['Start Time'])
            print("End Date:", event['End Date'])
            print("End Time:", event['End Time'])
            print("------------------------------")

# Register for an event
def register_for_event(event_id):
    event_data = load_data('events.json')
    
    for event in event_data:
        if event['ID'] == event_id:
            if event['Seats Available'] > 0:
                member = input("Enter your name: ")
                event['Users Registered'].append(member)
                event['Seats Available'] -= 1
                save_data(event_data, 'events.json')
                print("Registration successful.")
                return
            else:
                print("Sorry, all seats are filled.")
                return
    
    print("Event not found.")

# Update password for the logged-in member
def update_password():
    member_data = load_data('members.json')
    email = input("Enter your email address: ")
    new_password = input("Enter your new password: ")
    
    for member in member_data:
        if member['Email'] == email:
            member['Password'] = new_password
            save_data(member_data, 'members.json')
            print("Password updated successfully.")
            return
    
    print("Member not found.")

# Entry point of the application
def main():
    while True:
        print("\nWelcome to the Event Management App!")
        print("1. Register as Organizer")
        print("2. Register as Member")
        print("3. Login")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            register_user('Organizer')
        elif choice == '2':
            register_user('Member')
        elif choice == '3':
            login()
        elif choice == '4':
            print("Thank you for using the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == '__main__':
    main()
