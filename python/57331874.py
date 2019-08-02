info = [
    ['Price: 5000', 'In warranty', 'Weight: 8 kg'], 
    ['Refundable', 'Price: 2800', 'Weight: 5.5 kg', 'Extra battery power'], 
    ['Price: 9000', 'Non-exchangeable', 'Weight: 8 kg', 'High-Quality']
]

keywords = ['Price', 'Weight']

l = map(lambda sub_list: list(filter(lambda element: any(map(lambda keyword: keyword in element, keywords)), sub_list)), info)

print(list(l))