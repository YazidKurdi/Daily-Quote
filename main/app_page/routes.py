from flask import Blueprint,render_template
from main.util import quote_api

app_page = Blueprint('app_page',__name__)


@app_page.route("/")
def home():

    # if current_user.is_authenticated:
    #     return redirect(url_for('util.home'))
    #
    # form = RegistartionForm()
    # if form.validate_on_submit():
    #     hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    #     user = User(username = form.username.data,email = form.email.data, password = hashed_password)
    #     db.session.add(user)
    #     db.session.commit()
    #     flash('Your account has been created! You are now able to log in', 'success')
    #     return redirect(url_for('app_page.login'))
    quote,author = quote_api.content,quote_api.author
    return render_template('main_page.html', title='Register',author = author, quote = quote)


# @app_page.route("/login", methods=['GET', 'POST'])
# def login():
#
#     if current_user.is_authenticated:
#         return redirect(url_for('util.home'))
#
#     form = LoginForm()
#     if form.validate_on_submit():
#             user = User.query.filter_by(email = form.email.data).first()
#             if user and bcrypt.check_password_hash(user.password,form.password.data):
#                 login_user(user,remember=form.remember.data)
#                 next_page = request.args.get('next')
#                 return redirect(next_page) if next_page else redirect(url_for('util.home'))
#             else:
#                 flash('Login Unsuccessful. Please check email and password', 'danger')
#
#     return render_template('login.html', title='Login', form=form)
#
#
# @app_page.route("/logout")
# def logout():
#     logout_user()
#     return redirect(url_for("util.home"))
#
# @app_page.route("/account", methods = ["POST","GET"])
# @login_required
# def account():
#     form = UpdateAccountForm()
#     if form.validate_on_submit():
#         if form.picture.data:
#             picture_file = save_picture(form.picture.data)
#             current_user.image_file = picture_file
#
#         current_user.username = form.username.data
#         current_user.email = form.email.data
#         db.session.commit()
#         flash("Your account has been updated!","success")
#         return redirect(url_for('app_page.account'))
#     elif request.method == "GET":
#         form.username.data = current_user.username
#         form.email.data = current_user.email
#     image_file = url_for('static',filename = 'profile_pics/' + current_user.image_file)
#     return render_template("account.html",title = 'Account',image_file = image_file,form = form)
#
#
# @app_page.route("/user/<string:username>")
# def user_posts(username):
#     page = request.args.get('page', 1, type=int)
#     user = User.query.filter_by(username=username).first_or_404()
#     posts = Post.query.filter_by(author=user)\
#         .order_by(Post.date_posted.desc())\
#         .paginate(page=page, per_page=5)
#     return render_template('user_posts.html', posts=posts, user=user)