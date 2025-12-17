class sibi:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return self.name + " says hello!"
    

s=sibi("Sibi")
s2=sibi("kavin")

print(id(s))
print(id(s2))
print(id(s.name))
print(id(s2.name))

#    ❌ Misconception: You might think s.name "is part of" s, so they should share the same ID.
 #   ✅ Reality: The instance s contains a reference to the string object s.name, but they are distinct objects in memory.