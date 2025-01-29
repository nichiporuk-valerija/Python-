class User:
    def __init__(self, first_name, last_name):
        print("Мое имя и фамилия:")
        self.usefirst_name = first_name
        self.userlast_name = last_name

    def first_name(self):
        print ("мое имя",self.usefirst_name)

    def last_name(self):
        print("моя фамилия",self.userlast_name)
  
    def group(self):
       print ("мое имя и фамилия",self.userlast_name, self.usefirst_name)


