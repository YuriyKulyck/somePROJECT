import sqlite3
from flask import *
from werkzeug.security import generate_password_hash, check_password_hash
import DBmanager
from DBmanager import DBManager

app = Flask(__name__)

app.secret_key = "9919"

# Підключення до бази даних через DBManager
dbmanager = DBManager("db_name.sql")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about_us")
def about_us():
    return render_template("about_us.html")


@app.route("/confidence")
def confidence():
    return render_template("confidence.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = dbmanager.get_user_by_email(email)

        if user and check_password_hash(user[3], password):  # Перевірка паролю
            session['user'] = email
            flash('Вхід виконано успішно!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Невірний email або пароль.', 'danger')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form.get('fullName')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirmPassword')  # Додано підтвердження паролю

        # Перевірка, чи не порожні поля
        if not full_name or not email or not password or not confirm_password:
            flash('Будь ласка, заповніть усі поля.', 'danger')
            return render_template('register.html')

        # Перевірка на збіг паролів
        if password != confirm_password:
            flash('Паролі не співпадають.', 'danger')
            return render_template('register.html')

        # Перевірка наявності користувача в базі
        if dbmanager.get_user_by_email(email):
            flash('Користувач з таким email вже існує.', 'danger')
            return render_template('register.html')

        # Збереження нового користувача в базі даних
        hashed_password = generate_password_hash(password)
        dbmanager.add_user(full_name, email, hashed_password)
        flash('Реєстрація успішна! Тепер ви можете увійти.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user' not in session:
        flash('Спочатку увійдіть у систему.', 'warning')
        return redirect(url_for('login'))

    email = session['user']
    user = dbmanager.get_user_by_email(email)
    profile = dbmanager.get_profile(user[0])  # user[0] — це user_id

    if request.method == 'POST':
        # Оновлення профілю
        phone = request.form.get('phone', '')
        address = request.form.get('address', '')
        dbmanager.update_profile(user[0], phone, address)  # Оновлюємо профіль у базі
        flash('Профіль оновлено успішно!', 'success')

    return render_template(
        'profile.html',
        name=user[1],  # user[1] — це full_name
        email=email,
        phone=profile[1] if profile else 'Пусто',  # profile[1] — телефон
        address=profile[2] if profile else 'Пусто'  # profile[2] — адреса
    )


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Ви вийшли із системи.', 'info')
    return redirect(url_for('login'))


@app.route('/cart')
def cart():
    return render_template("cart.html")


@app.route("/products_by_catagory/<int:id_category>")
def product(id_category):
    dbmanager = DBmanager.DBManager("db_name.sql")
    articles = dbmanager.get_products_by_catalog(id_category)
    return render_template("product.html", items=articles)


@app.route("/product_page/<item_id>")
def product_page(item_id):
    dbmanager = DBmanager.DBManager("db_name.sql")
    article = dbmanager.get_products_by_id(item_id)
    is_registered = True
    return render_template("product_page.html", article=article, is_registered=is_registered)


if __name__ == '__main__':
    app.run(debug=True)