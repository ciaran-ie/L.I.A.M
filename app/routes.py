from flask import render_template, request, redirect, url_for, flash
from app import db
from app.models import Case

@app.route('/add_case', methods=['GET', 'POST'])
def add_case():
    if request.method == 'POST':
        case_name = request.form['case_name']
        case_file_number = request.form['case_file_number']
        case_crime = request.form['case_crime']
        classification = request.form['classification']
        case_suspect = request.form['case_suspect']
        case_investigation_lead = request.form['case_investigation_lead']
        case_investigator = request.form['case_investigator']
        case_investigator_tel = request.form['case_investigator_tel']
        case_investigator_unit = request.form['case_investigator_unit']
        case_confiscation_date = request.form['case_confiscation_date']
        case_request_description = request.form['case_request_description']
        case_requested_action = request.form['case_requested_action']
        examiners_notes = request.form['examiners_notes']
        case_contains_mob_dev = bool(request.form.get('case_contains_mob_dev', False))
        case_urgency = request.form['case_urgency']
        case_urg_justification = request.form['case_urg_justification']

        new_case = Case(
            name=case_name,
            file_number=case_file_number,
            crime=case_crime,
            classification=classification,
            suspect=case_suspect,
            investigation_lead=case_investigation_lead,
            investigator=case_investigator,
            investigator_tel=case_investigator_tel,
            investigator_unit=case_investigator_unit,
            confiscation_date=case_confiscation_date,
            request_description=case_request_description,
            requested_action=case_requested_action,
            examiners_notes=examiners_notes,
            contains_mob_dev=case_contains_mob_dev,
            urgency=case_urgency,
            urg_justification=case_urg_justification
        )
        db.session.add(new_case)
        db.session.commit()
        flash('Case added successfully')
        return redirect(url_for('index'))
    return render_template('add_case.html')
