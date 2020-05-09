"""
def hi(): 
    print ("Hi there!")
    print("How are you?")
hi()
def hi(name): 
    if name =="Jessy":
        print ("Hi Jessy")
    elif name == 'Sonja': 
        print ("Hi Sonja!")
    else : 
        print ("Hi anonymous!")
hi("Marc")
"""
def hi(name): 
    print ('hi ' + name + "!" )
girls = ["Julie", "Sophie", "Marie", "Jessy" ]
for name in girls :
    hi  (name)
    print ("next girl")
for i in range (1, 21): 
    print (i)