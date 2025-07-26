from flask import Flask, request, render_template_string

app = Flask(__name__)

# مسیر فایل دیتای ساده
DATA_FILE = 'data.txt'

# تابع برای خواندن وزن شکلات از فایل
def get_chocolate_weight(name):
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                if '=' in line:
                    chocolate, weight = line.strip().split('=')
                    if chocolate.strip().lower() == name:
                        return weight.strip()
        return 'پیدا نشد.'
    except FileNotFoundError:
        return 'فایل داده پیدا نشد.'

html_code = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>شکلات‌ها</title>
</head>
<body>
  <h2>اسم شکلات را وارد کن:</h2>
  <form method="POST">
    <input type="text" name="choco" placeholder="مثلاً kuş">
    <button type="submit">نمایش وزن</button>
  </form>
  <p><strong>وزن:</strong> {{ weight }}</p>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    weight = ''
    if request.method == 'POST':
        name = request.form['choco'].strip().lower()
        weight = get_chocolate_weight(name)
    return render_template_string(html_code, weight=weight)

if __name__ == '__main__':
    app.run(debug=True)
