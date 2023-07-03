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