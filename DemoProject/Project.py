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
    