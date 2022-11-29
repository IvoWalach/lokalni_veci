def soubor(cesta):
    try:
        souborek = open(cesta, "r")
    except FileNotFoundError:
        print(f"Soubor {cesta} nebyl nalezen")
        return []
    return souborek.readlines()

print(soubor("C:\learn\local_stuff\sth.txt"))




def dictsearch(key, value, dictio):
    if type(dictio) is not dict:
        return "Third value must be a dictionary"
    
    if dictio.get(key) == None:
        print("no such key")
        return False
    
    return dictio.get(key) == value

a= "b"
b=1
c={"a":2}
print(dictsearch(a,b,c))