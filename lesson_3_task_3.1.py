from Mailing1 import mailing
from Address1 import Address

to_address = Address ("140103", "Раменское", "Крымская", "75", "55")
from_address = Address("140109", "Москва", "Гурьева", "82", "99")

mailing = mailing("5454", from_address, to_address,"650" )
print(mailing)