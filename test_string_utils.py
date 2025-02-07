from typing import Literal
import pytest
from StringUtils import StringUtils
utils=StringUtils


# 1 capitilize
@pytest.mark.parametrize("string,result",[
   #positiv
   ("skypro","Skypro"),("LESSON","Lesson"),
   #negativ
   ("mother","mother")])


#2 trim
def test_capitilize(string,result):
   utils = StringUtils()
   assert utils.capitilize(string) == result
@pytest.mark.parametrize ("string,result",[
   #Positiv
   (" Lera","Lera"),("   Taras","Taras"),
   #Negativ
   (" Misha"," Misha")
   ])
def test_trim(string,result):
   utils = StringUtils()
   assert utils.trim(string) == result
   


#3 to_list
@pytest.mark.parametrize("input,delimeter,result",[
   #pozitive
   ("1:2:3", ":", ["1","2","3"]),("L.e.r.a",".", ["L","e","r","a"]), 
    #negativ
                                                   ("lera", " ",["L","e","r","a"])
                                                   ])
def test_to_list(input: Literal['1:2:3'] | Literal['L.e.r.a'] | Literal['lera'],delimeter: Literal[':'] | Literal['.'] | Literal[' '],result: list[str]):
    utils = StringUtils()
    assert utils.to_list(input,delimeter) == result



#4 contains     
@pytest.mark.parametrize("input_text,sumbol,result",
                         #positive
                         [("Cat","a", True), ("Dog","g", False),
                          #negativ
                          ("Skypro","m",True)
                          ])
def test_contain (input_text,sumbol,result):
    utils = StringUtils()
    assert utils.contains(input_text,sumbol) == result

#5 delete_symbol
@pytest.mark.parametrize ("string,symbol,result", [
  #positiv
   ("SkySmart","Smart","Sky"),("Skyeng","eng","Sky"),
   #negativ
   ("Skysmart","Sky","Sky")])
def test_delete_symbol (string,symbol,result):
 utils = StringUtils()
 assert utils.delete_symbol(string,symbol) == result


#6 starts_with
@pytest.mark.parametrize ("string,symbol,result", [
   #Positiv
   ("Lera","L",True),("House","H",True),("Bar","R",False),
    #negativ
   ("Mouse","O",True),("Desk","D",False)
   ])
def test_starts_with(string,symbol,result):
   utils = StringUtils()
   assert utils.starts_with(string,symbol) == result


#7 end_with
# pytest.mark.parametrize ("string,symbol,result",[
#    ("Mama","a",True),("DOM","M",True),("Dog","G",True),("Brother","U",False)])
# def test_end_with(string,symbol,result):
#  utils = StringUtils()
#  assert utils.end_with(string,symbol) == result



#8 is_empty
@pytest.mark.parametrize ("string,result", [
   #Positiv
   ("",True),("  ",True),("AA",False),
    #negativ
   ("O",True),(" ",False)
   ])
def test_is_empty(string,result):
   utils = StringUtils()
   assert utils.is_empty(string) == result


#9 list_to_string
@pytest.mark.parametrize ("lst,joiner,result", [
   #Positiv
   (["8,4,9"],",","8,4,9"),(["Sky", "Pro"],"-","Sky-Pro"),
   #negativ
   (["Sky", "Pro"],"-",["Sky-Pro"])
   ])
def test_list_to_string(lst,joiner,result):
   utils = StringUtils()
   assert utils.list_to_string(lst,joiner) == result







