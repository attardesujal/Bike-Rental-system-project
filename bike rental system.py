class BikeRental:
    def __init__(self, name, no_of_bikes) -> None:
        self.name = name
        self.no_of_bikes = no_of_bikes
        self.users = {}

    def rent_bike_hourly(self, name:str, bikes:int):
        if bikes > self.no_of_bikes:
            print(f"Bike shortage! Max {self.no_of_bikes} bikes available.")
        else:
            self.users.update({name:{"hourly":bikes}})
            self.no_of_bikes -= bikes

    def rent_bike_daily(self, name:str, bikes:int):
        if bikes > self.no_of_bikes:
            print(f"Bike shortage! Max {self.no_of_bikes} bikes available.")
        else:
            self.users.update({name:{"daily":bikes}})
            self.no_of_bikes -= bikes

    def rent_bike_weekly(self, name:str, bikes:int):
        if bikes > self.no_of_bikes:
            print(f"Bike shortage! Max {self.no_of_bikes} bikes available.")
        else:
            self.users.update({name:{"weekly":bikes}})
            self.no_of_bikes -= bikes

    def issue_bill(self, name:str):
        if name in self.users:
            record = self.users[name]
            for mode in record:
                qty = record[mode]
                if mode == "hourly":
                    price = 5 * qty
                    if 1 < qty < 6:
                        price *= 0.7
                elif mode == "daily":
                    price = 20 * qty
                    if 3 < qty < 6:
                        price *= 0.7
                elif mode == "weekly":
                    price = 60 * qty
                    if 3 < qty < 6:
                        price *= 0.7
                print(f"{name} rented {qty} bikes on {mode} basis. Bill: ${price}")
                self.no_of_bikes += qty
            self.users.pop(name)
        else:
            print("Customer not found!")
