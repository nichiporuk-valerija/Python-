class  Address:
    def __init__(self,index,city,street,house,apartment):
       self. index = index
       self.city = city
       self.street = street
       self.house = house
       self.apartament = apartment
    def __str__(self):
        return f"{self.index} индекс, {self.city} город, {self.street} улица, {self.house} дом, {self.apartament} квартира"
       
