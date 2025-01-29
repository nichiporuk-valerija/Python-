from smartphone1 import Smartphone


catalog = []
catalog.append(Smartphone("Samsung", "Galaxy11", "8-999-123-45-67"))
catalog.append( Smartphone ("Iphone", "14 ProMax", "8-999-698-85-96"))
catalog.append( Smartphone ("Xiaomi", "Ilite", "8-916-745-74-74"))
catalog.append(Smartphone ("Mi", "I10", "8-926-745-75-75"))
catalog.append( Smartphone ("Redmi", "XR", "8-909-858-86-74"))


for phone in catalog:
    print (f"{phone.phone_brand},{phone.phone_model},{phone.number}")
