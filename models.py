from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import jwt
from flask_login import LoginManager
from flask_login import UserMixin

database = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    return RegistrosSyP.query.get(int(user_id))

class RegistrosSyP(database.Model, UserMixin):
    __tablename__ = 'users'
    id = database.Column(database.Integer, primary_key=True,
                     unique=True, autoincrement=True)
    firstname = database.Column(database.String(255))
    lastname = database.Column(database.String(255))
    username = database.Column(database.BIGINT(), unique=True)
    email = database.Column(database.String(255), unique=True)
    password = database.Column(database.String(255))
    career = database.Column(database.String(255))
    education = database.relationship('Education')
    course = database.relationship('Course')
    publication = database.relationship('Publication')
    volunteering = database.relationship('Volunteering')
    experience = database.relationship('Experience')
    language = database.relationship('Language')
    create_date = database.Column(database.DateTime, default= datetime.datetime.now)
    rol = database.Column(database.String(10))
    photo = database.Column(database.String(255))
    cv = database.Column(database.String(255))
    age = database.Column(database.Integer)
    user_type = database.Column(database.String(50))
    contact = database.Column(database.String(100))
    mail_sec = database.Column(database.String(250))
    about_me = database.Column(database.String(1500))
    habilitie = database.Column(database.String(1500))
    interest = database.Column(database.String(1500))
    linkendin = database.Column(database.String(500))
    instagram = database.Column(database.String(500))
    facebook = database.Column(database.String(500))
    twitter = database.Column(database.String(500))

    def get_reset_token(self, expires=1800):
        return jwt.encode({'reset_password': self.username},
                           key='secret_key_ucemining')

    @staticmethod       
    def verify_reset_token(token):
        try:
            username = jwt.decode(token, key='secret_key_ucemining')['reset_password']
            print(username)
        except Exception as e:
            print(e)
            return
        return RegistrosSyP.query.filter_by(username=username).first()
 
    def __init__(self, firstname, lastname, username, email, password, career, rol, photo, cv):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = self.__create_password(password)
        self.career = career
        self.rol = rol
        self.photo = photo
        self.cv = cv
        
        
        
    def set_password(self, password, commit=False):
        self.password = generate_password_hash(password)

        if commit:
            database.session.commit()

    def __create_password(self, password):
        return generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)
    
class empresa(database.Model):
    __tablename__ = 'company'
    id = database.Column(database.Integer, primary_key=True)
    empresa = database.Column(database.String(255))
    email = database.Column(database.String(255))
    password = database.Column(database.String(255))
    rol = database.Column(database.String(10))

    def __init__(self, empresa, email, password, rol):
        self.empresa = empresa
        self.email = email
        self.password = self.__create_password(password)
        self.rol = rol
    

    def __create_password(self, password):
        return generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.password, password)


class Admin(database.Model):
    __tablename__ = 'admin'
    id = database.Column(database.Integer, primary_key=True)
    admin = database.Column(database.String(100))
    password = database.Column(database.String(255))
    rol = database.Column(database.String(10))

    

    def verify_password(self, password):
        return check_password_hash(self.password, password)



class Education(database.Model):
    __tablename__ = 'education'
    id = database.Column(database.Integer, primary_key=True,
                     unique=True, autoincrement=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))
    level_education = database.Column(database.Enum('Primaria','Secundaria','Preparatoria/Bachillerato','Universitaria/Tecnologia/Licenciatura','Especialidad','Maestria','Doctorado'),nullable=True)
    name_institution = database.Column(database.String(250),nullable=True)
    start_date = database.Column(database.Date,nullable=True)
    end_date = database.Column(database.Date)
    degree = database.Column(database.String(100),nullable=True)

class Course(database.Model):
    __tablename__ = 'course'
    id = database.Column(database.Integer, primary_key=True,
                     unique=True, autoincrement=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))
    description = database.Column(database.String(500),nullable=True)
    area = database.Column(database.Enum('Seguridad Minera','Software Técnico','Manejo Ambiental','Legislación Minera','Cierre de Minas','Auditoría Minera','Tratamiento de Aguas','Optimización de Procesos','Planificación Minera','Simulación de Procesos','Estimación de Reservas','QA/QC','Operaciones Unitarias','Geología','OTRA'),nullable=True)
    start_date = database.Column(database.Date)
    end_date = database.Column(database.Date, default= datetime.datetime.now)
    time = database.Column(database.Integer)

class Publication(database.Model):
    __tablename__ = 'publication'
    id = database.Column(database.Integer, primary_key=True,
                     unique=True, autoincrement=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))
    title = database.Column(database.String(255),nullable=True)
    pub_date = database.Column(database.Date,nullable=True)
    link = database.Column(database.String(500),nullable=True)
    description = database.Column(database.String(1000),nullable=True)

class Volunteering(database.Model):
    __tablename__ = 'volunteering'
    id = database.Column(database.Integer, primary_key=True,
                     unique=True, autoincrement=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))
    organization = database.Column(database.String(250),nullable=True)
    possition = database.Column(database.String(100),nullable=True)
    start_date = database.Column(database.Date,nullable=True)
    end_date = database.Column(database.Date,nullable=True)
    activities = database.Column(database.String(1000),nullable=True)

class Experience(database.Model):
    __tablename__ = 'experience'
    id = database.Column(database.Integer, primary_key=True,
                     unique=True, autoincrement=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))
    company = database.Column(database.String(250),nullable=True)
    area_e = database.Column(database.Enum('Seguridad Minera','Software Técnico','Manejo Ambiental','Legislación Minera','Cierre de Minas','Auditoría Minera','Tratamiento de Aguas','Optimización de Procesos','Planificación Minera','Simulación de Procesos','Estimación de Reservas','QA/QC','Operaciones Unitarias','Geología','OTRA'),nullable=True)
    possition = database.Column(database.String(100),nullable=True)
    start_date_e = database.Column(database.Date,nullable=True)
    end_date_e = database.Column(database.Date,nullable=True)
    time_e = database.Column(database.Integer)  

class Language(database.Model):
    __tablename__ = 'language'
    id = database.Column(database.Integer, primary_key=True,
                     unique=True, autoincrement=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))
    language = database.Column(database.Enum('Español','Inglés','Ruso','Alemán','Italiano','Chino Mandarín','Quichua'),nullable=True)
    level = database.Column(database.Enum('Lengua Materna','Elemental - A1','Elemental Superior - A2','Intermedio - B1','Intermedio Superior - B2','Avanzado - C1','Avanzando Superior - C2'),nullable=True)
    study_center = database.Column(database.String(250),nullable=True)


class ReferenceW(database.Model):
    __tablename__ = 'referencew'
    id = database.Column(database.Integer, primary_key=True,
                     unique=True, autoincrement=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))
    name_rw = database.Column(database.String(250),nullable=True)
    profession_rw = database.Column(database.String(250),nullable=True)
    company_rw = database.Column(database.String(250),nullable=True)
    position_rw = database.Column(database.String(250),nullable=True)
    number_rw = database.Column(database.String(250),nullable=True)
    mail_rw = database.Column(database.String(250),nullable=True)

class ReferenceP(database.Model):
    __tablename__ = 'referencep'
    id = database.Column(database.Integer, primary_key=True,
                     unique=True, autoincrement=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))
    name_rp = database.Column(database.String(250),nullable=True)
    profession_rp = database.Column(database.String(250),nullable=True)
    relation_rp = database.Column(database.String(250),nullable=True)
    number_rp = database.Column(database.String(250),nullable=True)
    mail_rp = database.Column(database.String(250),nullable=True)  

class Proyectos(database.Model):
    __tablename__ = 'proyectos'
    id = database.Column(database.Integer, primary_key=True,
                     unique=True, autoincrement=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))
    empresa_id = database.Column(database.Integer, database.ForeignKey('company.id'))