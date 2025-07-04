from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Case(db.Model):
    __tablename__ = 'cases'
    case_file_number = db.Column(db.String, primary_key=True)
    classification = db.Column(db.String)
    case_suspect = db.Column(db.String)
    case_location = db.Column(db.String)
    case_investigation_lead = db.Column(db.String)
    case_investigator = db.Column(db.String)
    forensic_examiner_username = db.Column(db.String, db.ForeignKey('users.forensic_examiner_username'))
    case_investigator_unit = db.Column(db.String)
    case_investigator_tel = db.Column(db.String)
    case_confiscation_date = db.Column(db.String)
    case_request_description = db.Column(db.String)
    case_requested_action = db.Column(db.String)
    case_crime = db.Column(db.String)
    case_notes = db.Column(db.String)
    exhibits = db.relationship('Exhibit', backref='case', lazy=True)

class Exhibit(db.Model):
    __tablename__ = 'exhibits'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    case_file_number = db.Column(db.String, db.ForeignKey('cases.case_file_number'), nullable=False)
    exhibit_ref_number = db.Column(db.String)
    external_ref_number = db.Column(db.String)
    device_type = db.Column(db.String)
    device_manuf = db.Column(db.String)
    device_model = db.Column(db.String)
    device_storage = db.Column(db.String)
    intake_date = db.Column(db.String)
    received_from = db.Column(db.String)
    current_location = db.Column(db.String)
    is_mobile_dev = db.Column(db.Boolean)
    description_exhibits = db.Column(db.String)
    password_pins_exhibit = db.Column(db.String)
    exhibit_returned_date = db.Column(db.String)
    exhibit_returned_to = db.Column(db.String)

class User(db.Model):
    __tablename__ = 'users'
    forensic_examiner_username = db.Column(db.String, primary_key=True)
    full_name = db.Column(db.String)
    title = db.Column(db.String)
    role = db.Column(db.String)
    active_cases = db.Column(db.Integer)
    completed_cases = db.Column(db.Integer)
    password_hash = db.Column(db.String)
    tel_number = db.Column(db.String)
    email = db.Column(db.String)
    cases = db.relationship('Case', backref='examiner', lazy=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
