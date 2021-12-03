from wtforms import Form, HiddenField
from wtforms import StringField, PasswordField, SelectField, SubmitField, TextAreaField, DateField, IntegerField, TextAreaField
from wtforms.fields.html5 import EmailField, DateField
from wtforms import validators
from wtforms.validators import EqualTo
from models import RegistrosSyP, empresa


def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio')



class RegisForm(Form):
    firstname = StringField("First Name:",
                [
                    validators.Required()
                ]
                )
    lastname = StringField("Last Name:",
                [
                    validators.Required()
                ]
                )
    username = StringField("Username:",
                [
                    validators.Required()
                ]
                )
    email = StringField("Email:",
                [
                    validators.Email(message='El email ingresado no es valido'),
                    validators.Required()
                ]
                )
    password = PasswordField("Password:",
                [
                    validators.length(min=6, max=30, message='La contraseña debe tener entre 6 y 30 caracteres'),
                    validators.Required()
                ]
                )
    honeypot = HiddenField('',[length_honeypot])
    career = SelectField(label= "Carrera", choices=[('', ''), ('Ingeniería de Minas', 'Ingeniería de Minas'), ('Ingeniería en Geología', 'Ingeniería en Geología'), ('Ingeniería Ambiental', 'Ingeniería Ambiental'), ('Ingeniería en Petróleos', 'Ingeniería en Petróleos')], validators=[validators.Required()])

    
    def validate_username(form, field):
        username = field.data
        user = RegistrosSyP.query.filter_by(username = username).first()
        if user is not None:
            raise validators.ValidationError('Esa cédula ya se encuentra registrada')

    def validate_email(form, field):
        email = field.data
        mail = RegistrosSyP.query.filter_by(email = email).first()
        if mail is not None:
            raise validators.ValidationError('Ese correo electronico ya se encuentra registrado')
    
        



class LoginForm(Form):
    username = StringField("Username:",
                [
                    validators.Required()
                ]
                )
    password = PasswordField("Password:",
                [
                    validators.length(min=6, max=30, message='Ingrese una contraseña valida'),
                    validators.Required()
                ]
                )


class RequestResetForm(Form):
    username = StringField("Username:",
                [
                    validators.Required()
                ]
                )
    submit = SubmitField('Solicitar cambio de contraseña')

    def validate_email(form, field):
        username = field.data
        user = RegistrosSyP.query.filter_by(username = username).first()
        if user is None:
            raise validators.ValidationError('No se encuentra registrado')
            

class ResetPasswordForm(Form):
    password = PasswordField("Password:",
                [
                    validators.length(min=6, max=30, message='La contraseña debe tener entre 6 y 30 caracteres'),
                    validators.Required()
                ])
    confirm_password = PasswordField('Confirm Password', 
                [
                    EqualTo('password', message='Las contraseñas no coinciden'),
                    validators.Required()
                ])
    submit = SubmitField('Cambiar Contraseña')






class Empresas(Form):
    empresa = StringField("Username:",
                [
                    validators.length(min=4, max=10, message='El username debe tener entre 4 y 25 caracteres'),
                    validators.Required()
                ]
                )
    email = StringField("Email:",
                [
                    validators.Email(message='El email ingresado no es valido'),
                    validators.Required()
                ]
                )
    password = PasswordField("Password:",
                [
                    validators.length(min=6, max=30, message='La contraseña debe tener entre 6 y 30 caracteres'),
                    validators.Required()
                ]
                )
    honeypot = HiddenField('',[length_honeypot])
    
    
    
    def validate_username(form, field):
        username = field.data
        user = empresa.query.filter_by(username = username).first()
        if user is not None:
            raise validators.ValidationError('Ese username ya se encuentra registrado')

    def validate_email(form, field):
        email = field.data
        mail = empresa.query.filter_by(email = email).first()
        if mail is not None:
            raise validators.ValidationError('Ese correo electronico ya se encuentra registrado')

class ContactForm(Form):
    title = StringField('Información de Contacto:')
    age = IntegerField('Edad: ')
    user_type = SelectField('Tipo de Usuario:',choices=[('Estudiante','Estudiante'),('Egresado','Egresado'),('Profesional','Profesional')])
    contact = StringField('Teléfonos de Contacto:', render_kw={"placeholder": "(+333) 0999-999-999 / (+333) 0999-999-999"})
    mail_sec = StringField('Mail de Contacto: ', render_kw={"placeholder": "ejemplo@asasa.com / ejemplo1@asasa.edu.ec"})
    linkendin = StringField('Perfil de Linkendin: ', render_kw={"placeholder": "https://www.linkedin.com/in/usuario"})
    instagram = StringField('Perfil de Instagram: ', render_kw={"placeholder": "https://www.instagram.com/usuario/"})
    facebook = StringField('Perfil de Facebook: ', render_kw={"placeholder": "https://www.facebook.com/usuario/"})
    twitter = StringField('Perfil de Twitter: ', render_kw={"placeholder": "https://twitter.com/usuario"})
    about_me = TextAreaField('Sobre mi: ')
    habilitie = TextAreaField('Sobre mis habilidades: ', render_kw={"placeholder": "En que aspectos sobresales?"})
    interest = TextAreaField('Sobre mis intereses: ', render_kw={"placeholder": "Cuáles son tus intereses?"})
    submit = SubmitField('POST')

class EducationForm(Form):
    title = StringField('Nivel de Instrucción:')
    level_education = SelectField('Nivel de Instrucción:',
                                    choices=[('Primaria','Primaria'),('Secundaria','Secundaria'),('Preparatoria/Bachillerato','Preparatoria/Bachillerato'),('Universitaria/Tecnologia/Licenciatura','Universitaria/Tecnologia/Licenciatura'),('Especialidad','Especialidad'),('Maestria','Maestría'),('Doctorado','Doctorado')])
    name_institution = StringField('Nombre de la Institución:')
    start_date = DateField('Fecha de Inicio:', format='%Y-%m-%d', validators=(validators.DataRequired('Ingrese una fecha'),))
    end_date = DateField('Fecha de Culminación:', format='%Y-%m-%d')
    degree = StringField('Título/Mención Alcanzado:')
    submit = SubmitField('POST')   

class UEducationForm(Form):
    title = StringField('Nivel de Instrucción:')
    level_education = SelectField('Nivel de Instrucción:',
                                    choices=[('Primaria','Primaria'),('Secundaria','Secundaria'),('Preparatoria/Bachillerato','Preparatoria/Bachillerato'),('Universitaria/Tecnologia/Licenciatura','Universitaria/Tecnologia/Licenciatura'),('Especialidad','Especialidad'),('Maestria','Maestría'),('Doctorado','Doctorado')])
    name_institution = StringField('Nombre de la Institución:')
    start_date = DateField('Fecha de Inicio:', format='%Y-%m-%d', validators=(validators.DataRequired('Ingrese una fecha'),))
    end_date = DateField('Fecha de Culminación:', format='%Y-%m-%d')
    degree = StringField('Título/Mención Alcanzado:')
    submit = SubmitField('POST') 

class CourseForm(Form):
    description = StringField('Descripción del Curso/Capacitación:')
    area = SelectField('Área de Capacitación:',
                                    choices=[('Seguridad Minera','Seguridad Minera'),('Software Técnico','Software Técnico'),('Manejo Ambiental','Manejo Ambiental'),('Legislación Minera','Legislación Minera'),('Cierre de Minas','Cierre de Minas'),('Auditoría Minera','Auditoría Minera'),('Tratamiento de Aguas','Tratamiento de Aguas'),('Optimización de Procesos','Optimización de Procesos'),('Planificación Minera','Planificación Minera'),('Simulación de Procesos','Simulación de Procesos'),('Estimación de Reservas','Estimación de Reservas'),('QA/QC','QA/QC'),('Operaciones Unitarias','Operaciones Unitarias'),('Geología','Geología')])
    start_date = DateField('Fecha de Inicio:', format='%Y-%m-%d', validators=(validators.DataRequired('Ingrese una fecha'),))
    end_date = DateField('Fecha de Culminación:', format='%Y-%m-%d', validators=(validators.DataRequired('Ingrese una fecha'),))
    time = IntegerField('Horas de Capacitación:')
    submit = SubmitField('POST')   

class UCourseForm(Form):
    description = StringField('Descripción del Curso/Capacitación:')
    area = SelectField('Área de Capacitación:',
                                    choices=[('Seguridad Minera','Seguridad Minera'),('Software Técnico','Software Técnico'),('Manejo Ambiental','Manejo Ambiental'),('Legislación Minera','Legislación Minera'),('Cierre de Minas','Cierre de Minas'),('Auditoría Minera','Auditoría Minera'),('Tratamiento de Aguas','Tratamiento de Aguas'),('Optimización de Procesos','Optimización de Procesos'),('Planificación Minera','Planificación Minera'),('Simulación de Procesos','Simulación de Procesos'),('Estimación de Reservas','Estimación de Reservas'),('QA/QC','QA/QC'),('Operaciones Unitarias','Operaciones Unitarias'),('Geología','Geología')])
    start_date = DateField('Fecha de Inicio:', format='%Y-%m-%d', validators=(validators.DataRequired('Ingrese una fecha'),))
    end_date = DateField('Fecha de Culminación:', format='%Y-%m-%d', validators=(validators.DataRequired('Ingrese una fecha'),))
    time = IntegerField('Horas de Capacitación:', render_kw={"placeholder": "HORAS"})
    submit = SubmitField('POST')

class PublicationForm(Form):
    title = StringField('Tema de Investigación/Publicación:')
    pub_date = DateField('Fecha de Publicación:', format='%Y-%m-%d', validators=(validators.DataRequired('Ingrese una fecha'),))
    link = StringField('DOI de la publicación:')
    description = TextAreaField('Descripción de la Investigación:')
    submit = SubmitField('POST')   

class UPublicationForm(Form):
    title = StringField('Tema de Investigación/Publicación:')
    pub_date = DateField('Fecha de Publicación:', format='%Y-%m-%d', validators=(validators.DataRequired('Ingrese una fecha'),))
    description = StringField('Descripción del Curso/Capacitación:')
    link = StringField('DOI de la publicación:')
    description = TextAreaField('Descripción de la Investigación:')
    submit = SubmitField('POST')

class VolunteeringForm(Form):
    organization = StringField('Organización donde sirvió:')
    possition = StringField('Cargo/Puesto desempeñado en la Institución:')
    start_date = DateField('Fecha de Inicio:', format='%Y-%m-%d', validators=(validators.DataRequired('Ingrese una fecha'),))
    end_date = DateField('Fecha de Culminación:', format='%Y-%m-%d', validators=(validators.DataRequired('Ingrese una fecha'),))
    activities = TextAreaField('Actividades desempeñadas:')
    submit = SubmitField('POST')   

class UVolunteeringForm(Form):
    organization = StringField('Organización donde sirvió:')
    possition = StringField('Cargo/Puesto desempeñado en la Institución:')
    start_date = DateField('Fecha de Inicio:', format='%Y-%m-%d', validators=(validators.DataRequired('Ingrese una fecha'),))
    end_date = DateField('Fecha de Culminación:', format='%Y-%m-%d', validators=(validators.DataRequired('Ingrese una fecha'),))
    activities = TextAreaField('Actividades desempeñadas:')
    submit = SubmitField('POST')

class ExperienceForm(Form):
    company = StringField('Empresa donde trabajó:')
    area_e = SelectField('Área de Trabajo:',
                                    choices=[('Seguridad Minera','Seguridad Minera'),('Software Técnico','Software Técnico'),('Manejo Ambiental','Manejo Ambiental'),('Legislación Minera','Legislación Minera'),('Cierre de Minas','Cierre de Minas'),('Auditoría Minera','Auditoría Minera'),('Tratamiento de Aguas','Tratamiento de Aguas'),('Optimización de Procesos','Optimización de Procesos'),('Planificación Minera','Planificación Minera'),('Simulación de Procesos','Simulación de Procesos'),('Estimación de Reservas','Estimación de Reservas'),('QA/QC','QA/QC'),('Operaciones Unitarias','Operaciones Unitarias'),('Geología','Geología')])
    possition = StringField('Cargo desempeñado:')
    start_date_e = DateField('Fecha de Inicio:', format='%Y-%m-%d', validators=(validators.DataRequired('Ingrese una fecha'),))
    end_date_e = DateField('Fecha de Culminación:', format='%Y-%m-%d', validators=(validators.DataRequired('Ingrese una fecha'),))
    time_e = IntegerField('Años de experiencia:', render_kw={"placeholder": "AÑOS"})
    submit = SubmitField('POST')   

class UExperienceForm(Form):
    company = StringField('Empresa donde trabajó:')
    area_e = SelectField('Área de Trabajo:',
                                    choices=[('Seguridad Minera','Seguridad Minera'),('Software Técnico','Software Técnico'),('Manejo Ambiental','Manejo Ambiental'),('Legislación Minera','Legislación Minera'),('Cierre de Minas','Cierre de Minas'),('Auditoría Minera','Auditoría Minera'),('Tratamiento de Aguas','Tratamiento de Aguas'),('Optimización de Procesos','Optimización de Procesos'),('Planificación Minera','Planificación Minera'),('Simulación de Procesos','Simulación de Procesos'),('Estimación de Reservas','Estimación de Reservas'),('QA/QC','QA/QC'),('Operaciones Unitarias','Operaciones Unitarias'),('Geología','Geología')])
    possition = StringField('Cargo desempeñado:')
    start_date_e = DateField('Fecha de Inicio:', format='%Y-%m-%d', validators=(validators.DataRequired('Ingrese una fecha'),))
    end_date_e = DateField('Fecha de Culminación:', format='%Y-%m-%d', validators=(validators.DataRequired('Ingrese una fecha'),))
    time_e = IntegerField('Años de experiencia:', render_kw={"placeholder": "AÑOS"})
    submit = SubmitField('POST')

class LanguageForm(Form):
    language = SelectField('Lenguaje:',
                                    choices=[('Español','Español'),('Inglés','Inglés'),('Ruso','Ruso'),('Alemán','Alemán'),('Italiano','Italiano'),('Chino Mandarín','Chino Mandarín'),('Quichua','Quichua')])
    level = SelectField('Nivel alcanzado:',
                                    choices=[('Lengua Materna','Lengua Materna'),('Elemental - A1','Elemental - A1'),('Elemental Superior - A2','Elemental Superior - A2'),('Intermedio - B1','Intermedio - B1'),('Intermedio Superior - B2','Intermedio Superior - B2'),('Avanzado - C1','Avanzado - C1'),('Avanzando Superior - C2','Avanzando Superior - C2')])
    study_center = StringField('Institución de instrucción:')
    submit = SubmitField('POST')   

class ULanguageForm(Form):
    language = SelectField('Lenguaje:',
                                    choices=[('Español','Español'),('Inglés','Inglés'),('Ruso','Ruso'),('Alemán','Alemán'),('Italiano','Italiano'),('Chino Mandarín','Chino Mandarín'),('Quichua','Quichua')])
    level = SelectField('Nivel alcanzado:',
                                    choices=[('Lengua Materna','Lengua Materna'),('Elemental - A1','Elemental - A1'),('Elemental Superior - A2','Elemental Superior - A2'),('Intermedio - B1','Intermedio - B1'),('Intermedio Superior - B2','Intermedio Superior - B2'),('Avanzado - C1','Avanzado - C1'),('Avanzando Superior - C2','Avanzando Superior - C2')])
    study_center = StringField('Institución de instrucción:')
    submit = SubmitField('POST')  

class ReferenceWForm(Form):
    name_rw = StringField('Nombre y Apellido:')
    profession_rw = StringField('Profesión: ')
    company_rw = StringField('Empresa: ')
    position_rw = StringField('Cargo: ')
    number_rw = StringField('Teléfono de Contacto:', render_kw={"placeholder": "(+333) 0999-999-999"})
    mail_rw = StringField('Mail de Contacto: ', render_kw={"placeholder": "ejemplo@asasa.com"})
    submit = SubmitField('POST')   

class UReferenceWForm(Form):
    name_rw = StringField('Nombre y Apellido:')
    profession_rw = StringField('Profesión: ')
    company_rw = StringField('Empresa: ')
    position_rw = StringField('Cargo: ')
    number_rw = StringField('Teléfono de Contacto:', render_kw={"placeholder": "(+333) 0999-999-999"})
    mail_rw = StringField('Mail de Contacto: ', render_kw={"placeholder": "ejemplo@asasa.com"})
    submit = SubmitField('POST')

class ReferencePForm(Form):
    name_rp = StringField('Nombre y Apellido:')
    profession_rp = StringField('Profesión/Ocupación: ')
    relation_rp = SelectField('Relación:',
                                    choices=[('Compañero/a de Estudio','Compañero/a de Estudio'),('Compañero/a Laboral','Compañero/a Laboral'),('Familiar','Familiar')])
    number_rp = StringField('Teléfono de Contacto:', render_kw={"placeholder": "(+333) 0999-999-999"})
    mail_rp = StringField('Mail de Contacto: ', render_kw={"placeholder": "ejemplo@asasa.com"})
    submit = SubmitField('POST')

class UReferencePForm(Form):
    name_rp = StringField('Nombre y Apellido:')
    profession_rp = StringField('Profesión/Ocupación: ')
    relation_rp = SelectField('Relación:',
                                    choices=[('Compañero/a de Estudio','Compañero/a de Estudio'),('Compañero/a Laboral','Compañero/a Laboral'),('Familiar','Familiar')])
    number_rp = StringField('Teléfono de Contacto:', render_kw={"placeholder": "(+333) 0999-999-999"})
    mail_rp = StringField('Mail de Contacto: ', render_kw={"placeholder": "ejemplo@asasa.com"})
    submit = SubmitField('POST')

class FiltroForm(Form):
    carrera = SelectField(label= "Carrera", choices=[('Todas', 'Seleccione una carrera'), ('Ingeniería de Minas', 'Ingeniería de Minas'), ('Ingeniería en Geología', 'Ingeniería en Geología'), ('Ingeniería Ambiental', 'Ingeniería Ambiental'), ('Ingeniería en Petróleos', 'Ingeniería en Petróleos')])
    tipo_u = SelectField(label= "Usuario", choices=[('Todas', 'Seleccione el tipo'),('Estudiante','Estudiante'),('Egresado','Egresado'),('Profesional','Profesional')])
    nivel_i = SelectField(label= "Nivel de Instrucción", choices=[('Todas', 'Seleccione el tipo'),('Primaria','Primaria'),('Secundaria','Secundaria'),('Preparatoria/Bachillerato','Preparatoria/Bachillerato'),('Universitaria/Tecnologia/Licenciatura','Universitaria/Tecnologia/Licenciatura'),('Especialidad','Especialidad'),('Maestria','Maestría'),('Doctorado','Doctorado')])
    area_c = SelectField(label= "Nivel de Instrucción", choices=[('Todas', 'Seleccione área'),('Seguridad Minera','Seguridad Minera'),('Software Técnico','Software Técnico'),('Manejo Ambiental','Manejo Ambiental'),('Legislación Minera','Legislación Minera'),('Cierre de Minas','Cierre de Minas'),('Auditoría Minera','Auditoría Minera'),('Tratamiento de Aguas','Tratamiento de Aguas'),('Optimización de Procesos','Optimización de Procesos'),('Planificación Minera','Planificación Minera'),('Simulación de Procesos','Simulación de Procesos'),('Estimación de Reservas','Estimación de Reservas'),('QA/QC','QA/QC'),('Operaciones Unitarias','Operaciones Unitarias'),('Geología','Geología')])
    area_t = SelectField(label= "Nivel de Instrucción", choices=[('Todas', 'Seleccione área'),('Seguridad Minera','Seguridad Minera'),('Software Técnico','Software Técnico'),('Manejo Ambiental','Manejo Ambiental'),('Legislación Minera','Legislación Minera'),('Cierre de Minas','Cierre de Minas'),('Auditoría Minera','Auditoría Minera'),('Tratamiento de Aguas','Tratamiento de Aguas'),('Optimización de Procesos','Optimización de Procesos'),('Planificación Minera','Planificación Minera'),('Simulación de Procesos','Simulación de Procesos'),('Estimación de Reservas','Estimación de Reservas'),('QA/QC','QA/QC'),('Operaciones Unitarias','Operaciones Unitarias'),('Geología','Geología')])
    idioma_f = SelectField(label= "Nivel de Instrucción", choices=[('Todas', 'Seleccione Idioma'),('Español','Español'),('Inglés','Inglés'),('Ruso','Ruso'),('Alemán','Alemán'),('Italiano','Italiano'),('Chino Mandarín','Chino Mandarín'),('Quichua','Quichua')])
    submit = SubmitField('Filtrar')
