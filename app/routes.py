from flask import render_template, request, redirect, url_for, flash, current_app as app
from . import db
from .models import Case, Exhibit, User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    total_cases = Case.query.count()
    total_evidence_items = Exhibit.query.count()
    total_users = User.query.count()
    return render_template('dashboard.html', total_cases=total_cases, total_evidence_items=total_evidence_items, total_users=total_users)

@app.route('/cases')
def cases():
    cases = Case.query.all()
    return render_template('cases.html', cases=cases)

@app.route('/add_case', methods=['GET', 'POST'])
def add_case():
    if request.method == 'POST':
        case_file_number = request.form['case_file_number']
        classification = request.form['classification']
        case_suspect = request.form['case_suspect']
        case_location = request.form['case_location']
        case_investigation_lead = request.form['case_investigation_lead']
        case_investigator = request.form['case_investigator']
        forensic_examiner_username = request.form['forensic_examiner_username']
        case_investigator_unit = request.form['case_investigator_unit']
        case_investigator_tel = request.form['case_investigator_tel']
        case_confiscation_date = request.form['case_confiscation_date']
        case_request_description = request.form['case_request_description']
        case_requested_action = request.form['case_requested_action']
        case_crime = request.form['case_crime']
        case_notes = request.form['case_notes']
        
        new_case = Case(
            case_file_number=case_file_number, classification=classification, case_suspect=case_suspect,
            case_location=case_location, case_investigation_lead=case_investigation_lead, case_investigator=case_investigator,
            forensic_examiner_username=forensic_examiner_username, case_investigator_unit=case_investigator_unit,
            case_investigator_tel=case_investigator_tel, case_confiscation_date=case_confiscation_date,
            case_request_description=case_request_description, case_requested_action=case_requested_action,
            case_crime=case_crime, case_notes=case_notes
        )
        
        db.session.add(new_case)
        db.session.commit()
        return redirect(url_for('cases'))
    return render_template('add_case.html')

@app.route('/cases/<case_file_number>', methods=['GET', 'POST'])
def case_detail(case_file_number):
    case = Case.query.filter_by(case_file_number=case_file_number).first_or_404()
    exhibits = Exhibit.query.filter_by(case_file_number=case_file_number).all()
    
    if request.method == 'POST':
        case.case_file_number = request.form['case_file_number']
        case.classification = request.form['classification']
        case.case_suspect = request.form['case_suspect']
        case.case_location = request.form['case_location']
        case.case_investigation_lead = request.form['case_investigation_lead']
        case.case_investigator = request.form['case_investigator']
        case.forensic_examiner_username = request.form['forensic_examiner_username']
        case.case_investigator_unit = request.form['case_investigator_unit']
        case.case_investigator_tel = request.form['case_investigator_tel']
        case.case_confiscation_date = request.form['case_confiscation_date']
        case.case_request_description = request.form['case_request_description']
        case.case_requested_action = request.form['case_requested_action']
        case.case_crime = request.form['case_crime']
        case.case_notes = request.form['case_notes']

        db.session.commit()
        flash('Case updated successfully!', 'success')
        return redirect(url_for('case_detail', case_file_number=case.case_file_number))

    return render_template('case_detail.html', case=case, exhibits=exhibits)

def get_next_exhibit_number(case_file_number):
    last_exhibit = Exhibit.query.filter_by(case_file_number=case_file_number).order_by(Exhibit.id.desc()).first()
    if last_exhibit:
        try:
            last_number = int(last_exhibit.exhibit_ref_number)
            return str(last_number + 1)
        except ValueError:
            return "1"  # Fallback if exhibit_ref_number is not an integer
    else:
        return "1"

@app.route('/cases/<case_file_number>/add_exhibit', methods=['GET', 'POST'], endpoint='add_exhibit_to_case')
def add_exhibit(case_file_number):
    case = Case.query.filter_by(case_file_number=case_file_number).first_or_404()
    next_exhibit_number = get_next_exhibit_number(case_file_number)
    if request.method == 'POST':
        exhibit_ref_number = next_exhibit_number
        external_ref_number = request.form['external_ref_number']
        device_type = request.form['device_type']
        device_manuf = request.form['device_manuf']
        device_model = request.form['device_model']
        device_storage = request.form['device_storage']
        intake_date = request.form['intake_date']
        received_from = request.form['received_from']
        current_location = request.form['current_location']
        is_mobile_dev = 'is_mobile_dev' in request.form
        description_exhibits = request.form['description_exhibits']
        password_pins_exhibit = request.form['password_pins_exhibit']
        exhibit_returned_date = request.form['exhibit_returned_date']
        exhibit_returned_to = request.form['exhibit_returned_to']
        
        new_exhibit = Exhibit(
            case_file_number=case_file_number, exhibit_ref_number=exhibit_ref_number, external_ref_number=external_ref_number,
            device_type=device_type, device_manuf=device_manuf, device_model=device_model, device_storage=device_storage,
            intake_date=intake_date, received_from=received_from, current_location=current_location, is_mobile_dev=is_mobile_dev,
            description_exhibits=description_exhibits, password_pins_exhibit=password_pins_exhibit, exhibit_returned_date=exhibit_returned_date,
            exhibit_returned_to=exhibit_returned_to
        )
        
        db.session.add(new_exhibit)
        db.session.commit()
        flash('Exhibit added successfully!', 'success')
        return redirect(url_for('case_detail', case_file_number=case_file_number))
    return render_template('add_exhibit.html', case=case, next_exhibit_number=next_exhibit_number)

@app.route('/exhibits')
def exhibits():
    exhibits = Exhibit.query.all()
    return render_template('exhibits.html', exhibits=exhibits)

@app.route('/add_exhibit', methods=['GET', 'POST'], endpoint='add_new_exhibit')
def add_exhibit_new():
    next_exhibit_number = 1  # Default value if case_file_number is not provided
    if request.method == 'POST':
        case_file_number = request.form['case_file_number']
        exhibit_ref_number = get_next_exhibit_number(case_file_number)
        external_ref_number = request.form['external_ref_number']
        device_type = request.form['device_type']
        device_manuf = request.form['device_manuf']
        device_model = request.form['device_model']
        device_storage = request.form['device_storage']
        intake_date = request.form['intake_date']
        received_from = request.form['received_from']
        current_location = request.form['current_location']
        is_mobile_dev = 'is_mobile_dev' in request.form
        description_exhibits = request.form['description_exhibits']
        password_pins_exhibit = request.form['password_pins_exhibit']
        exhibit_returned_date = request.form['exhibit_returned_date']
        exhibit_returned_to = request.form['exhibit_returned_to']
        
        new_exhibit = Exhibit(
            case_file_number=case_file_number, exhibit_ref_number=exhibit_ref_number, external_ref_number=external_ref_number,
            device_type=device_type, device_manuf=device_manuf, device_model=device_model, device_storage=device_storage,
            intake_date=intake_date, received_from=received_from, current_location=current_location, is_mobile_dev=is_mobile_dev,
            description_exhibits=description_exhibits, password_pins_exhibit=password_pins_exhibit, exhibit_returned_date=exhibit_returned_date,
            exhibit_returned_to=exhibit_returned_to
        )
        
        db.session.add(new_exhibit)
        db.session.commit()
        flash('Exhibit added successfully!', 'success')
        return redirect(url_for('exhibits'))
    
    return render_template('add_exhibit.html', next_exhibit_number=next_exhibit_number)

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        forensic_examiner_username = request.form['forensic_examiner_username']
        full_name = request.form['full_name']
        title = request.form['title']
        role = request.form['role']
        active_cases = request.form['active_cases']
        completed_cases = request.form['completed_cases']
        password = request.form['password']
        tel_number = request.form['tel_number']
        email = request.form['email']
        
        new_user = User(
            forensic_examiner_username=forensic_examiner_username, full_name=full_name, title=title, role=role,
            active_cases=active_cases, completed_cases=completed_cases, tel_number=tel_number, email=email
        )
        new_user.password = password  # This will hash the password
        
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users'))
    return render_template('add_user.html')

@app.route('/search', methods=['GET'])
def search():
    search_term = request.args.get('search_term', '')
    if search_term:
        case_results = Case.query.filter(
            (Case.case_file_number.contains(search_term)) |
            (Case.classification.contains(search_term)) |
            (Case.case_suspect.contains(search_term)) |
            (Case.case_location.contains(search_term)) |
            (Case.case_investigation_lead.contains(search_term)) |
            (Case.case_investigator.contains(search_term)) |
            (Case.forensic_examiner_username.contains(search_term)) |
            (Case.case_investigator_unit.contains(search_term)) |
            (Case.case_investigator_tel.contains(search_term)) |
            (Case.case_request_description.contains(search_term)) |
            (Case.case_requested_action.contains(search_term)) |
            (Case.case_crime.contains(search_term)) |
            (Case.case_notes.contains(search_term))
        ).all()

        exhibit_results = Exhibit.query.filter(
            (Exhibit.case_file_number.contains(search_term)) |
            (Exhibit.exhibit_ref_number.contains(search_term)) |
            (Exhibit.external_ref_number.contains(search_term)) |
            (Exhibit.device_type.contains(search_term)) |
            (Exhibit.device_manuf.contains(search_term)) |
            (Exhibit.device_model.contains(search_term)) |
            (Exhibit.device_storage.contains(search_term)) |
            (Exhibit.intake_date.contains(search_term)) |
            (Exhibit.received_from.contains(search_term)) |
            (Exhibit.current_location.contains(search_term)) |
            (Exhibit.description_exhibits.contains(search_term)) |
            (Exhibit.password_pins_exhibit.contains(search_term)) |
            (Exhibit.exhibit_returned_date.contains(search_term)) |
            (Exhibit.exhibit_returned_to.contains(search_term))
        ).all()

        results = {
            'cases': case_results,
            'exhibits': exhibit_results
        }
    else:
        results = None

    return render_template('search.html', results=results)
