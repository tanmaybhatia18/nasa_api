class crow:
    species='bird'
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=crow('blu',10)
woo=crow('woo',15)
print('blu is a {}'.format(blu.__class__.species))
print('woo is a {}'.format(woo.__class__.species))
