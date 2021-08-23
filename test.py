events = []
topics = ['graduation','visit','other']
for i in range(10):
    events.append(
        {
            '_id':f'{i}',
            'title':f'{topics[i%3]} {i}',
            'topic':f'{topics[i%3]} {i}',
            'time':f'2021-6-{i}',
            'location':f''
        }
    )

class user:
    def __init__(self,name,email) -> None:
        self.name = name
        self.email = email
    def keys(self):
        return("name","email")
    def __getitem__(self,item):
        return getattr(self,item)
auser = user("aaa","aaa.com")
userdict = dict(auser)
print(userdict)