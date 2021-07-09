
from flask import Flask,url_for,redirect,render_template,request
import pickle
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/buy')
def buy():
    return 'Congratulations!! Your client will buy the insurace.'

@app.route('/notbuy')        
def notbuy():
    return 'Unfortunately, Your client will not take the insurance.'

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/submit',methods=['GET','POST'])
def submit():
    
    if request.method == 'POST':
        
        Policy_Sales_Channel = float(request.form['Policy_Sales_Channel'])
        Vehicle_Age = str(request.form['Vehicle_Age'])
        Age = float(request.form['Age'])
        Region_Code = float(request.form['Region_Code'])
        Vintage = float(request.form['Vintage'])
        Gender = str(request.form['Gender'])
        Driving_License = str(request.form['Driving_License'])
        Previously_Insured = str(request.form['Previously_Insured'])
        Vehicle_Damage = str(request.form['Vehicle_Damage'])
        
        Vehicle_Age_dict = {'1-2 Year':3,'< 1 Year':2,'> 2 Years':1}
        Vehicle_Damage_dict = {'Yes':1,'No':0}
        Gender_dict = {'Male':1,'Female':0}
        Driving_License_dict = {'Yes':1,'No':0}
        Previously_Insured_dict = {'Yes':1,'No':0}
        
        Vehicle_Age = Vehicle_Age_dict[Vehicle_Age]
        Previously_Insured = Previously_Insured_dict[Previously_Insured]
        Vehicle_Damage_Yes = Vehicle_Damage_dict[Vehicle_Damage]
        Male = Gender_dict[Gender]
        Driving_License = Driving_License_dict[Driving_License]
        
        y = model.predict([[Policy_Sales_Channel + Vehicle_Age, Age + Driving_License,
       Male + Vintage, Vehicle_Age + Vintage, Region_Code * Vehicle_Age,
       Policy_Sales_Channel + Region_Code,
       Previously_Insured + Region_Code, Driving_License + Region_Code,
       Age * Vintage, Driving_License * Vintage, Region_Code + Vintage,
       Male + Region_Code, Driving_License + Policy_Sales_Channel,
       Policy_Sales_Channel + Previously_Insured, Age * Vehicle_Damage_Yes,
       Male * Vehicle_Age, Vehicle_Age * Vintage,
       Age + Previously_Insured, Age * Region_Code,
       Age * Driving_License, Policy_Sales_Channel * Vintage,
       Age + Policy_Sales_Channel, Age + Vehicle_Damage_Yes, Age * Male,
       Vehicle_Damage_Yes + Vintage, Vehicle_Age * Vehicle_Damage_Yes,
       Driving_License * Policy_Sales_Channel,
       Previously_Insured + Vintage, Driving_License * Region_Code,
       Policy_Sales_Channel * Vehicle_Age, Driving_License + Vintage,
       Age + Male, Age * Policy_Sales_Channel, Region_Code + Vehicle_Age,
       Male + Policy_Sales_Channel, Age + Vehicle_Age, Age + Vintage,
       Region_Code + Vehicle_Damage_Yes, Age * Vehicle_Age,
       Policy_Sales_Channel + Vehicle_Damage_Yes]])
        
        if y==1:
            
            return redirect(url_for('buy'))
            
        else:
            
            return redirect(url_for('notbuy'))
        
        
if __name__ == '__main__':
    app.run(debug=True)
    
            
        
        






