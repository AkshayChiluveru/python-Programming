import json
import datetime
import uuid

def load_data(Organizer):
    with open(Organizer, 'r') as file:
        data = json.load(file)
    return data

def save_data(data, Organizer):
    with open(Organizer, 'w') as file:
        json.dump(data, file, indent=4)

# Register a user as an Organizer or Member
def register_user(user_type):
    full_name = input("Enter your full name: ")
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    
    user_data = load_data('Organizers.json') if user_type == 'Organizer' else load_data('members.json')
    
    user_data.append({
        'Full Name': full_name,
        'Email': email,
        'Password': password
    })
    
    if user_type == 'Organizer':
        save_data(user_data, 'Organizers.json')
    else:
        save_data(user_data, 'members.json')
    
    print("Registration successful!")

# Login functionality
def login():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    
    organizer_data = load_data('Organizers.json')
    member_data = load_data('members.json')
    
    for organizer in organizer_data:
        if organizer['Email'] == email and organizer['Password'] == password:
            print("Login successful!")
            show_organizer_menu()
            return
    
    for member in member_data:
        if member['Email'] == email and member['Password'] == password:
            print("Login successful!")
            show_member_menu()
            return
    
    print("Invalid email or password. Please try again.")

# Show menu for organizers
def show_organizer_menu():
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

# Show menu for members
def show_member_menu():
    while True:
        print("\nMember Menu:")
        print("1. View Registered Events")
        print("2. Register for an Event")
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
def create_event(organizer_email):
    event_data = load_data('events.json')
    organizer_data = load_data('organizers.json')

    # Check if the organizer exists
    organizer = next((o for o in organizer_data if o['Email'] == organizer_email), None)
    if not organizer:
        print("Organizer not found.")
        return

    event_name = input("Enter the name of the event: ")
    start_date = input("Enter the start date of the event (YYYY-MM-DD): ")
    start_time = input("Enter the start time of the event (HH:MM:SS): ")
    end_date = input("Enter the end date of the event (YYYY-MM-DD): ")
    end_time = input("Enter the end time of the event (HH:MM:SS): ")
    total_seats = int(input("Enter the total seats available for the event: "))

    # Generate a unique EventID using UUID
    event_id = str(uuid.uuid4())

    # Create the event object
    event = {
        "ID": event_id,
        "Name": event_name,
        "Organizer": organizer["Full Name"],
        "Start Date": start_date,
        "Start Time": start_time,
        "End Date": end_date,
        "End Time": end_time,
        "Users Registered": [],
        "Capacity": total_seats,
        "Seats Available": total_seats
    }

    # Add the event to the event_data list
    event_data.append(event)
    save_data(event_data, 'events.json')

    print("Event created successfully.")

# View the list of all events
def view_event_list():
    event_data = load_data('events.json')

    current_datetime = datetime.datetime.now()

    print("\nEvent List:")
    for event in event_data:
        event_start_datetime = datetime.datetime.strptime(
            f"{event['Start Date']} {event['Start Time']}", "%Y-%m-%d %H:%M:%S"
        )
        event_end_datetime = datetime.datetime.strptime(
            f"{event['End Date']} {event['End Time']}", "%Y-%m-%d %H:%M:%S"
        )

        # Check if the event is ongoing or upcoming
        if event_start_datetime <= current_datetime <= event_end_datetime:
            event_status = "Ongoing"
        elif event_start_datetime > current_datetime:
            event_status = "Upcoming"
        else:
            continue  # Skip past events

        # Display event details
        print("EventID:", event['ID'])
        print("Name:", event['Name'])
        print("Organizer:", event['Organizer'])
        print("Start Date:", event['Start Date'])
        print("Start Time:", event['Start Time'])
        print("End Date:", event['End Date'])
        print("End Time:", event['End Time'])
        print("Total Users Registered:", len(event['Users Registered']))
        print("Seats Available:", event['Seats Available'])
        print("Status:", event_status)
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
            print("Total Seats:", event['Total Seats'])
            print("Seats Available:", event['Seats Available'])
            print("------------------------------")
            return
    
    print("Event not found.")

# Update event details based on EventID
def update_event(event_id):
    event_data = load_data('events.json')
    
    for event in event_data:
        if event['ID'] == event_id:
            name = input("Enter the new event name: ")
            start_date = input("Enter the new start date (YYYY-MM-DD): ")
            start_time = input("Enter the new start time (HH:MM:SS): ")
            end_date = input("Enter the new end date (YYYY-MM-DD): ")
            end_time = input("Enter the new end time (HH:MM:SS): ")
            
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

# View the list of registered events for a member
def view_registered_events():
    event_data = load_data('events.json')
    
    print("\nRegistered Events:")
    for event in event_data:
        if event['ID'] in current_user['Registered Events']:
            print("EventID:", event['ID'])
            print("Name:", event['Name'])
            print("Organizer:", event['Organizer'])
            print("Start Date:", event['Start Date'])
            print("Start Time:", event['Start Time'])
            print("End Date:", event['End Date'])
            print("End Time:", event['End Time'])
            print("Total Seats:", event['Total Seats'])
            print("Seats Available:", event['Seats Available'])
            print("------------------------------")

# Register for an event
def register_for_event(event_id):
    event_data = load_data('events.json')
    
    for event in event_data:
        if event['ID'] == event_id:
            if event['Seats Available'] > 0:
                event['Seats Available'] -= 1
                event['Users Registered'].append(current_user['Full Name'])
                save_data(event_data, 'events.json')
                print("Registration successful!")
            else:
                print("All seats for this event are filled.")
            return
    
    print("Event not found.")

# Update password for the current user
def update_password():
    new_password = input("Enter your new password: ")
    current_user['Password'] = new_password
    
    user_data = load_data('Organizers.json') if current_user_type == 'Organizer' else load_data('members.json')
    
    for user in user_data:
        if user['Email'] == current_user['Email']:
            user['Password'] = new_password
            save_data(user_data, 'Organizers.json') if current_user_type == 'Organizer' else save_data(user_data, 'members.json')
            print("Password updated successfully.")
            return
    
    print("User not found.")

def main():
    while True:
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
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


