class mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track
        
    def __str__(self):
        return (f"отправление{self.track}, из{self.from_address}, в{self.to_address}, стоимость {self.cost} руб")
