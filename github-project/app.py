from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    job_text = request.form['job_description']
    vect_text = vectorizer.transform([job_text])
    prediction = model.predict(vect_text)
    result = "Fake Job Posting ❌" if prediction[0] == 1 else "Real Job Posting ✅"
    return render_template("index.html", prediction=result)

# ✅ Step 2: Add this route
@app.route('/company', methods=['POST'])
def company_info():
    name = request.form.get("company_name", "").strip().lower()

    # Company database
    company_db = {
        "tcs": {
            "name": "Tata Consultancy Services",
            "website": "https://www.tcs.com",
            "locations": "India, USA, UK, Europe",
            "hiring": "Online Assessment → Technical Interview → HR Interview"
        },
        "infosys": {
            "name": "Infosys Limited",
            "website": "https://www.infosys.com",
            "locations": "India, USA, Europe, Australia",
            "hiring": "Aptitude Test → Technical Interview → HR Round"
        },
        "wipro": {
            "name": "Wipro Ltd.",
            "website": "https://www.wipro.com",
            "locations": "India, USA, Canada",
            "hiring": "Online Test (Aptitude + Coding) → Technical Round → HR Interview"
        },
        "google": {
            "name": "Google LLC",
            "website": "https://careers.google.com",
            "locations": "Global (USA, India, UK, Europe, etc.)",
            "hiring": "Online Application → Phone Screening → Technical Interviews → Hiring Committee"
        },
"accenture": {
    "name": "Accenture",
    "website": "https://www.accenture.com",
    "locations": "India, USA, UK, Australia, Europe",
    "hiring": "Online Assessment → Technical Interview → HR Interview"
},
"capgemini": {
    "name": "Capgemini",
    "website": "https://www.capgemini.com",
    "locations": "India, France, USA, UK, Germany",
    "hiring": "Written Test → Group Discussion → Technical + HR Interview"
},
"cognizant": {
    "name": "Cognizant Technology Solutions",
    "website": "https://www.cognizant.com",
    "locations": "India, USA, Europe",
    "hiring": "Aptitude Test → Technical Interview → HR Interview"
},
"hcl": {
    "name": "HCL Technologies",
    "website": "https://www.hcltech.com",
    "locations": "India, USA, Canada, Europe",
    "hiring": "Online Test → Technical Interview → HR Round"
},
"ibm": {
    "name": "IBM",
    "website": "https://www.ibm.com",
    "locations": "Global",
    "hiring": "Cognitive Ability Games → Technical Interviews → HR Interview"
},
"mindtree": {
    "name": "Mindtree",
    "website": "https://www.ltimindtree.com",
    "locations": "India, USA, Europe",
    "hiring": "Aptitude Test → Coding Test → Technical + HR Interview"
},
"oracle": {
    "name": "Oracle",
    "website": "https://www.oracle.com",
    "locations": "USA, India, UK, Australia",
    "hiring": "Online Coding Round → Technical Interviews → Managerial + HR Round"
},
"zoho": {
    "name": "Zoho Corporation",
    "website": "https://www.zoho.com",
    "locations": "India, USA",
    "hiring": "Written Round → Programming + Debugging → Technical + HR Interviews"
},
"techmahindra": {
    "name": "Tech Mahindra",
    "website": "https://www.techmahindra.com",
    "locations": "India, UK, USA, Europe",
    "hiring": "Online Test → Technical Round → HR Round"
},
"lti": {
    "name": "L&T Infotech (LTI)",
    "website": "https://www.lntinfotech.com",
    "locations": "India, USA, Europe",
    "hiring": "Online Test → Technical Interview → HR Interview"
}

    }

    # Get data or fallback
    data = company_db.get(name, {
        "name": "Not Found",
        "website": "N/A",
        "locations": "N/A",
        "hiring": "No data available"
    })

    return render_template("index.html", company_info=data)

if __name__ == "__main__":
    app.run(debug=True)
