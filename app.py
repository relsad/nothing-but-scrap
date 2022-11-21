from operator import and_
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:zscaqres26@127.0.0.1:4044/test'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mqrqedppgmgere:d9d5281de967edd4af63a8df206f0354ad87e3b63d63a3612d386c0f9903c252@ec2-176-34-215-248.eu-west-1.compute.amazonaws.com:5432/d4fcjq00ak9rrf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

Base = automap_base()
   
Base.prepare(db.engine, reflect = True)

 
### Classes for Tables ###
DT       = Base.classes.DiseaseType
Country  = Base.classes.Country
Disease  = Base.classes.Disease
Discover = Base.classes.Discover
Users    = Base.classes.Users
PS       = Base.classes.PublicServant
Doctor   = Base.classes.Doctor
Record   = Base.classes.Record



### default route
@app.route('/')
def index():
    return render_template('index.html')
        

@app.route('/create')
def create():
    return render_template('create.html')    

@app.route('/create_DT', methods = ["POST"])
def create_DT():
    inputDTid          = request.form['DT_id']
    inputDTdesctiption = request.form['DT_description']
    new_DT = DT(id = inputDTid, description = inputDTdesctiption)
    try:
        db.session.add(new_DT)
        db.session.commit()
    except: 
        print("error!")
    # print(inputDTid, inputDTdesctiption)
    return redirect('/create')

@app.route('/create_Country', methods = ["POST"])
def create_Country():
    inputCcname          = request.form['C_cname']
    inputCpopulation     = request.form['C_population']
    new_Country = Country(cname = inputCcname, population = inputCpopulation)
    try: 
        db.session.add(new_Country)
        db.session.commit()
    except: 
        print("error!")
    # print(inputCcname, inputCpopulation)
    return redirect('/create')

@app.route('/create_Disease', methods = ["POST"])
def create_Disease():
    inputDiseaseCode        = request.form['Disease_code']
    inputDiseasePathogen    = request.form['Disease_pathogen']
    inputDiseaseDescription = request.form['Disease_description']
    inputDiseaseId          = request.form['Disease_id']
    new_Disease = Disease(disease_code = inputDiseaseCode, pathogen = inputDiseasePathogen, description = inputDiseaseDescription, id = inputDiseaseId)
    try:
        db.session.add(new_Disease)
        db.session.commit()
    except: 
        print("error!")
    # print(inputDiseaseCode, inputDiseasePathogen, inputDiseaseDescription, inputDiseaseId)
    return redirect('/create')

@app.route('/create_Discover', methods = ["POST"])
def create_Discover():
    inputDiscoverCname        = request.form['Discover_cname']
    inputDiscoverDiseaseCode  = request.form['Discover_disease_code']
    inputDiscoverDate         = request.form['Discover_date']
    new_Discover = Discover(cname = inputDiscoverCname, disease_code = inputDiscoverDiseaseCode, first_enc_date = inputDiscoverDate)
    try:
        db.session.add(new_Discover)
        db.session.commit()
    except: 
        print("error!")
    # print(inputDiscoverCname, inputDiscoverDiseaseCode, inputDiscoverDate)
    return redirect('/create')

@app.route('/create_Users', methods = ["POST"])
def create_Users():
    # email name surname salary phone cname
    inputUemail     = request.form['U_email']
    inputUname      = request.form['U_name']
    inputUsurname   = request.form['U_surname']
    inputUsalary    = request.form['U_salary']
    inputUphone     = request.form['U_phone']
    inputUcname     = request.form['U_cname']
    new_U = Users(email = inputUemail, name = inputUname, surname = inputUsurname, salary = inputUsalary, phone = inputUphone, cname = inputUcname)
    try:
        db.session.add(new_U)
        db.session.commit()
    except: 
        print("error!")
    # print(inputUemail, inputUname, inputUsurname, inputUsalary, inputUsalary, inputUphone, inputUcname)
    return redirect('/create')

@app.route('/create_PS', methods = ["POST"])
def create_PS():
    inputPSemail          = request.form['PS_email']
    inputPSdepartment     = request.form['PS_department']
    new_PS = PS(email = inputPSemail, department = inputPSdepartment)
    try:
        db.session.add(new_PS)
        db.session.commit()
    except: 
        print("error!")
    # print(inputPSemail, inputPSdepartment)
    return redirect('/create')

@app.route('/create_Doctor', methods = ["POST"])
def create_Doctor():
    inputDemail          = request.form['Doctor_email']
    inputDdegree         = request.form['Doctor_degree']
    new_Doc = Doctor(email = inputDemail, degree = inputDdegree)
    try:
        db.session.add(new_Doc)
        db.session.commit()
    except: 
        print("error!")
    # print(inputDemail, inputDdegree)
    return redirect('/create')

@app.route('/create_Record', methods = ["POST"])
def create_Record():
    # email cname discode death patient
    inputRemail       = request.form['Record_email']
    inputRcname       = request.form['Record_cname']
    inputRdiseasecode = request.form['Record_disease_code']
    inputRdeath       = request.form['Record_deaths']
    inputRpatient     = request.form['Record_patients']
    
    new_Rec = Record(email = inputRemail, cname = inputRcname, disease_code = inputRdiseasecode, total_deaths = inputRdeath, total_patients = inputRpatient)
    try:
        db.session.add(new_Rec)
        db.session.commit()
    except: 
        print("error!")
    # print(inputRemail, inputRcname, inputRdiseasecode, inputRdeath, inputRpatient)
    return redirect('/create')

@app.route('/read', methods = ['GET', 'POST'])
def read():
    return render_template('read.html')

@app.route('/read_table', methods = ['GET', 'POST'])
def read_table():
    table  = request.form['table_name']
    DThead = ("integer", "description")
    Chead  = ("country name", "population")
    Dhead  = ("disease code", "pathogen", "description", "id")
    DCVhead= ("country name", "disease code", "first enc date")
    Uhead  = ("email", "name", "surname", "salary", "phone", "country name")
    PShead = ("email", "department")
    DOChead= ("email", "degree")
    Rhead  = ("email", "country name", "disease code", "deaths", "patients")
    
    if   (table == "DT"):
        head = DThead
        data = db.session.query(DT).all()
        cols = tuple(Base.metadata.tables['DiseaseType'].columns.keys())
    elif (table == "Country"):
        head = Chead
        data = db.session.query(Country).all()
        cols = tuple(Base.metadata.tables['Country'].columns.keys())
    elif (table == "Disease"):
        head = Dhead
        data = db.session.query(Disease).all()
        cols = tuple(Base.metadata.tables['Disease'].columns.keys())
    elif (table == "Discover"):
        head = DCVhead
        data = db.session.query(Discover).all()
        cols = tuple(Base.metadata.tables['Discover'].columns.keys())
    elif (table == "Users"):
        head = Uhead
        data = db.session.query(Users).all()
        cols = tuple(Base.metadata.tables['Users'].columns.keys())
    elif (table == "PS"):
        head = PShead
        data = db.session.query(PS).all()
        cols = tuple(Base.metadata.tables['PublicServant'].columns.keys())
    elif (table == "Doctor"):
        head = DOChead
        data = db.session.query(Doctor).all()
        cols = tuple(Base.metadata.tables['Doctor'].columns.keys())
    else :
        head = Rhead
        data = db.session.query(Record).all()
        cols = tuple(Base.metadata.tables['Record'].columns.keys())


    return render_template('table.html', qdata = data, headings = head, colnames = cols)

@app.route('/update', methods = ['GET', 'POST'])
def update():
    return render_template('update.html')

@app.route('/update_DT', methods = ["POST"])
def update_DT():
    inputDTid          = request.form['DT_id']
    inputDTdesctiption = request.form['DT_description']
    try:
        db.session.query(DT).filter(DT.id == inputDTid).update({'description':inputDTdesctiption})
        db.session.commit()
    except: 
        print("error!")

    return redirect('/update')

@app.route('/update_Country', methods = ["POST"])
def update_Country():
    inputCcname          = request.form['C_cname']
    inputCpopulation     = request.form['C_population']
    try:
        db.session.query(Country).filter(Country.cname == inputCcname).update({'population': inputCpopulation})
        db.session.commit()
    except: 
        print("error!")

    return redirect('/update')

@app.route('/update_Disease', methods = ["POST"])
def update_Disease():
    inputDiseaseCode        = request.form['Disease_code']
    inputDiseaseAttribute   = request.form['Disease_col']
    inputDiseaseNew         = request.form['Disease_newVal']
    try:
        db.session.query(Disease).filter(Disease.disease_code == inputDiseaseCode).update({inputDiseaseAttribute:inputDiseaseNew})
        db.session.commit()
    except: 
        print("error!")

    return redirect('/update')

@app.route('/update_Discover', methods = ["POST"])
def update_Discover():
    inputDiscoverCname        = request.form['Discover_cname']
    inputDiscoverDiseaseCode  = request.form['Discover_disease_code']
    inputDiscoverDate         = request.form['Discover_date']
    try:
        db.session.query(Discover).filter(and_(Discover.disease_code == inputDiscoverCname,
                                           Discover.disease_code == inputDiscoverDiseaseCode)).update({'first_enc_date':inputDiscoverDate})
        db.session.commit()
    except: 
        print("error!")
    return redirect('/update')

@app.route('/update_Users', methods = ["POST"])
def update_Users():
    inputUemail     = request.form['U_email']
    inputUcol      = request.form['U_col']
    inputUnew     = str(request.form['U_newVal'])
    try:
        db.session.query(Users).filter(Users.email == inputUemail).update({inputUcol:inputUnew})
        db.session.commit()
    except: 
        print("error!")
    return redirect('/update')

@app.route('/update_PS', methods = ["POST"])
def update_PS():
    inputPSemail          = request.form['PS_email']
    inputPSdepartment     = request.form['PS_department']
    try:
        db.session.query(PS).filter(PS.email == inputPSemail).update({'department':inputPSdepartment})
        db.session.commit()
    except: 
        print("error!")
    return redirect('/update')

@app.route('/update_Doctor', methods = ["POST"])
def update_Doctor():
    inputDemail          = request.form['Doctor_email']
    inputDdegree         = request.form['Doctor_degree']
    try:
        db.session.query(Doctor).filter(Doctor.email == inputDemail).update({'degree':inputDdegree})
        db.session.commit()
    except: 
        print("error!")
    return redirect('/update')

@app.route('/update_Record', methods = ["POST"])
def update_Record():
    inputRemail       = request.form['Record_email']
    inputRcname       = request.form['Record_cname']
    inputRdiseasecode = request.form['Record_disease_code']
    inputRcol         = request.form['Record_col']
    inputRnew         = request.form['Record_newVal']
    try:
        db.session.query(Record).filter(and_(Users.disease_code == inputRdiseasecode,
                                         and_(Users.email == inputRemail,
                                              Users.cname == inputRcname))).update({inputRcol:inputRnew})
        db.session.commit()
    except: 
        print("error!")
    return redirect('/update')

@app.route('/delete', methods = ['GET', 'POST'])
def delete():
    return render_template('delete.html')

@app.route('/delete_DT', methods = ["POST"])
def delete_DT():
    inputDTid          = request.form['DT_id']
    try:
        db.session.query(DT).filter(DT.id == inputDTid).delete()
        db.session.commit()
    except: 
        print("error!")
    return redirect('/delete')

@app.route('/delete_Country', methods = ["POST"])
def delete_Country():
    inputCcname          = request.form['C_cname']
    try:
        db.session.query(Country).filter(Country.cname == inputCcname).delete()
        db.session.commit()
    except: 
        print("error!")
    return redirect('/delete')

@app.route('/delete_Disease', methods = ["POST"])
def delete_Disease():
    inputDiseaseCode        = request.form['Disease_code']
    try:
        db.session.query(Disease).filter(Disease.disease_code == inputDiseaseCode).delete()
        db.session.commit()
    except: 
        print("error!")
    return redirect('/delete')

@app.route('/delete_Discover', methods = ["POST"])
def delete_Discover():
    inputDiscoverCname        = request.form['Discover_cname']
    inputDiscoverDiseaseCode  = request.form['Discover_disease_code']
    try:
        db.session.query(Discover).filter(and_(Discover.disease_code == inputDiscoverCname,
                                           Discover.disease_code == inputDiscoverDiseaseCode)).delete()
        db.session.commit()
    except: 
        print("error!")
    return redirect('/delete')

@app.route('/delete_Users', methods = ["POST"])
def delete_Users():
    inputUemail     = request.form['U_email']
    try:
        db.session.query(Users).filter(Users.email == inputUemail).delete()
        db.session.commit()
    except: 
        print("error!")
    return redirect('/delete')

@app.route('/delete_PS', methods = ["POST"])
def delete_PS():
    inputPSemail          = request.form['PS_email']
    try:
        db.session.query(PS).filter(PS.email == inputPSemail).delete()
        db.session.commit()
    except: 
        print("error!")
    return redirect('/delete')

@app.route('/delete_Doctor', methods = ["POST"])
def delete_Doctor():
    inputDemail          = request.form['Doctor_email']
    try:
        db.session.query(Doctor).filter(Doctor.email == inputDemail).delete()
        db.session.commit()
    except: 
        print("error!")
    return redirect('/delete')

@app.route('/delete_Record', methods = ["POST"])
def delete_Record():
    inputRemail       = request.form['Record_email']
    inputRcname       = request.form['Record_cname']
    inputRdiseasecode = request.form['Record_disease_code']
    try:
        db.session.query(Record).filter(and_(Users.disease_code == inputRdiseasecode,
                                         and_(Users.email == inputRemail,
                                              Users.cname == inputRcname))).delete()
        db.session.commit()
    except: 
        print("error!")
    return redirect('/delete')

if __name__ == '__main__':
    app.run()