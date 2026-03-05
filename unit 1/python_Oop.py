# Python OOP - object oreinted programing

# object - A represenation 
# of some complex data structure 
# *data types (... and functions in this case)
# Although they maybe the same thing, objectively, onjects
# can different characteristics / featuers

# class - is a constructor / blueprint for creating
# objects

# properties = the data type values of a object. 

class computers:
    def _init_(self, color, shape, storage, protability, camera, ram,):
        self.color = color'
        self.shape = shape
        self.storage = storage
        self.protability = protability
        self.camera = camera
        self.ram = ram




class phones:
    def _init_(self, storage, carrier, size, color, camera, name, warrenty, price, brand ):
        self. storage = storage # int storage 
        self. carrier = carrier #str carrier 
        self. size = size
        self. color = color
        self. camera = camera
        self. name = name
        self. warrenty = warrenty
        self. price = price
        self. brand = brand 

phone1 = phones(16, 'att', 13.00,'yellow', False, ' brick pro', False, 100.00,'Brick')
phone1 = phones(32, 'verzion',)
#apple_1 = computers("apple m4", 'black', 10.00, 320, true, true, 60, 'm4')
#apple_2 = computers("apple m4", "white", 10.00, 320, true, true, 80, 'm4')

print(apple_1.ram)
print(apple_2.ram)