def update_chocolate_weight(name, new_weight):
    name = name.lower()
    updated = False
    lines = []

    try:
        with open('data.txt', 'r', encoding='utf-8') as f:
            for line in f:
                if '=' in line:
                    choco, weight = line.strip().split('=')
                    if choco.strip().lower() == name:
                        lines.append(f'{choco.strip()} = {new_weight}\n')
                        updated = True
                    else:
                        lines.append(line)
                else:
                    lines.append(line)
    except FileNotFoundError:
        print("فایل پیدا نشد. ایجاد می‌کنم...")
    
    if not updated:
        lines.append(f'{name} = {new_weight}\n')

    with open('data.txt', 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print(f"وزن شکلات '{name}' به {new_weight} تغییر کرد.")

# مثال استفاده:
# update_chocolate_weight("kuş", "600kg")
