from Collections.MyList import MyList

foo = MyList(['hey','i\'m','r4bit\'s','script'])
foo.append(2)
foo.append(3)
foo.append(4)
foo.append(5)
foo.append(6)
print(len(foo))
print(foo.pop())
print(len(foo))
print(foo)
foo.reverse()
print(foo)
print(foo.pop(0))
print(foo)
