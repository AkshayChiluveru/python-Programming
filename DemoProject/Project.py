class TicketInfo:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.user_details = {}

    def option(self,options):
        if options == 1:
            self.show_seats()

        elif options == 2:
            self.buy_tickets()

        elif options == 3:
            self.statistics()

        elif options == 4:
            self.user_info()
        else:
            print("Enter a valid option")

    
    def show_seats(self):
        for i in range(self.row + 1):
            for j in range(self.col + 1):
                # row =0
                if i == 0:
                    # col =0
                    if j == 0:
                        print(" ",end = " ")
                        # row 0 and col 1 -> n 
                    else:
                        print(j,end = " ")
                else:
                    # col 0 and row 1 -> n
                    if j == 0:
                        print(i,end = " ")
                        # row and col !=0
                    else:
                        if self.seat_status(i, j):
                            print("B",end = " ")
                        else:
                            print("S",end = " ")
            print()

    def buy_tickets(self):
        row = int(input("For which row are you planning to book the ticket: "))
        col = int(input("For which column are you planning to buy the ticket: "))
        seat_id = str(row) + "-" + str(col)
        total_seats = self.row * self.col
        half_seats = total_seats // 2
        if total_seats < 60 or (total_seats > 60 and row <= half_seats):
            price = 10
        else:
            price = 8
        
        if self.seat_status(row,col):
            print("That seat is already reserved")
        else:
            print("Prince of the selected seat is: ",price,'$')
            choice = input("Enter yes to continue to purchase the ticket")
            if choice.lower() == 'yes':
                name = input("Enter your name: ")
                gender = input("Enter your Gender ")
                age = input("Enter your age")
                mobile_number = input("Enter your mobile number")
                self.user_details[seat_id] = [name,gender,age,mobile_number]
                print('Your ticket is now reserved, seating id is: ' , seat_id)
            else:
                print('No problem visit back soon ..........')

    
    def statics(self):
        reserved_ticket = len(self.user_details)
        percentage = (reserved_ticket / (self.row *self.col)) * 100
        total = 0
        for price in self.user_details.values():
            total += price[4]
        seats = self.row * self.col 
        income = 0
        if seats <= 60:
            income = seats * 10
        else:
            half_seats = (self.row //2) * self.col
            income = half_seats * 10 + (seats - half_seats) * 8
        s = 'Number of purchased tickets { } \npercentage of tickets booked'
        print(s)
         