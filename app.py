import keyboard

# خواندن عدد از فایل HTML (اگر وجود دارد)
def read_number_from_file():
    try:
        with open("index.html", "r") as file:
            for line in file:
                if "kg =" in line:
                    return int(line.strip().split("kg =")[1].split("<")[0])
    except:
        return 0

# نوشتن عدد جدید داخل HTML
def write_number_to_html(number):
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>kg counter</title>
</head>
<body>
    <h1>وزن:</h1>
    <p>kg = {number}</p>
</body>
</html>
"""
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(html_content)

# مقدار اولیه
number = read_number_from_file()

print("با زدن Space عدد 5 تا زیاد میشه و در index.html ذخیره میشه. برای خروج esc رو بزن.")

while True:
    if keyboard.is_pressed("space"):
        number += 5
        print("عدد فعلی:", number)
        write_number_to_html(number)
        while keyboard.is_pressed("space"):
            pass
    elif keyboard.is_pressed("esc"):
        print("خروج از برنامه.")
        break
                                               
