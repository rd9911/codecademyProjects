from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, array_size=0):
    self.array_size = array_size
    self.array = [LinkedList() for i in range(self.array_size)]
  
  def hash(self, key):
    hash_code = sum(key.encode())
    return hash_code
  
  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for i in list_at_array:
      if i[0] == key:
        i[1] = value  
    list_at_array.insert(payload)




  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    list_at_index = self.array[array_index]
    payload = self.array[array_index]

    for i in list_at_index:
      if i[0] == key:
        return i[1]
      else:
        return None
      

hash_map = HashMap(len(flower_definitions))
for defs in flower_definitions:
  hash_map.assign(defs[0], defs[1])
print(hash_map.retrieve("daisy"))





