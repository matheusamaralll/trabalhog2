from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,ValidationError
from wtforms.validators import InputRequired, Email
from email_validator import validate_email, EmailNotValidError
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://trabg2:12345@localhost/trabg2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'chave_secreta_aleatoria'
db = SQLAlchemy(app)

class ResumeForm(FlaskForm):
    nome = StringField('Nome', validators=[InputRequired()])
    telefone = StringField('Telefone')
    email = StringField('Endereço de E-mail', validators=[InputRequired(), Email()])
    endereco_web = StringField('Endereço Web')
    experiencia_profissional = TextAreaField('Experiência Profissional', validators=[InputRequired()])

    def validate_email(form, field):
        try:
            v = validate_email(field.data)
            field.data = v.email
        except EmailNotValidError as e:
            raise ValidationError(str(e))


class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(20))
    email_address = db.Column(db.String(120), nullable=False, unique=True)
    endereco_web = db.Column(db.String(200))
    experiencia_profissional = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    resumes = Resume.query.all()
    return render_template('listagem.html', resumes=resumes)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    form = ResumeForm()
    if form.validate_on_submit():
        new_resume = Resume(
            nome=form.nome.data,
            telefone=form.telefone.data,
            email_address=form.email.data,
            endereco_web=form.endereco_web.data,
            experiencia_profissional=form.experiencia_profissional.data
        )
        db.session.add(new_resume)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('cadastrar.html', form=form)

@app.route('/consultar/<int:resume_id>')
def consultar(resume_id):
    resume = Resume.query.get_or_404(resume_id)
    return render_template('consultar.html', resume=resume)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(ssl_context=('cert.pem','key.pem'),debug=True)
