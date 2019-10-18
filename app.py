from flask import Flask, render_template
from forms import user

app = Flask(__name__)

app.config['SECRET_KEY'] = "key"

@app.route('/', methods=['GET', 'POST'])
def index():
    form=user.SampleForm()
    if form.validate_on_submit():
        return render_template('index.html', name=form.name.data, age=form.age.data, form=form)
    return render_template('index.html', text="eiei", form=form)

@app.route('/about')
def about():
    return 'this is about page'

# @app.route('/add_user', methods=['GET', 'POST'])
# def add_user():
#     form = UserForm
#     new

if __name__ == "__main__":
    app.run(debug=True)