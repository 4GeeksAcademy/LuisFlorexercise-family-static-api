
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # Self es el equivalente al this en Javascript, y siempre hay que pasarle el self 
        # example list of members
        self._members = [
            {
                "id":self._generateId(),
                "name":"John",
                "last_name":self.last_name,
                "age":33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id":self._generateId(),
                "name":"Jane",
                "last_name":self.last_name,
                "age":35,
                "lucky_numbers": [10, 7, 23]
            },
            {
                "id":self._generateId(),
                "name":"Jimmy",
                "last_name":self.last_name,
                "age":5,
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        add_member = {
            **member,
            "id": self._generateId(),
            "last_name":self.last_name
        }
        return self._members.append(add_member)

    def delete_member(self, id):
        # fill this method and update the return. Me toca meterle una función lambda
         for i in self._members:
            if i["id"] == id:
                self._members.remove(i)

    def get_member(self, id):
        # fill this method and update the return
        # Este NO nos funcionó: filter_member = list((filter(lambda item:item["id"]==id,self._members)))
        # print(filter_member)
        
        for i in self._members:
            if i["id"] == id:
                return i

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
