
data = ['Bill,9494944444', 'Tom,8484848333', 'Mark,3939822222',
        'Tom,7654545333', 'Scott,657574444']

phones = {}

for entry in data:
    name, phone = entry.split(',')
    if name not in phones:
        phones[name] = phone

for name, phone in sorted(phones.items()):
    print(f"{name:15} {phone}")