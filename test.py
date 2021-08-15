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

print(events)