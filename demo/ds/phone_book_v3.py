data = ['Bill,9494944444', 'Tom,8484848333', 'Mark,3939822222',
        'Tom,7654545333', 'Scott-657574444', 'Tom,8484848333',
        'Bill,39992223323']

phones = {}

for entry in data:
    parts = entry.split(',')
    if len(parts) != 2:
        continue

    name, phone = parts
    if name not in phones:
        phones[name] = {phone}
    else:
        phones[name].add(phone)

for name, values in sorted(phones.items()):
    print(f"{name:15} {','.join(values)}")
