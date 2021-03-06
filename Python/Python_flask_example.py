from flask import Flask, render_template
from flask import jsonify, make_response
from flask import request
from flask import json
from flask import Response
from flask_cors import CORS
from flask import current_app
import pandas as pd
app = Flask(__name__)
cors = CORS(app)
data = ([
        { "name": "Nina Dobrev", "date": "on 09 Aug 1978", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTIBeGwc_hxfUV5WLGoXIj9Q6OLnraLPid2k7si6nUgczVW23qc" },
        { "name": "Mark Lind", "date": "on 28 Feb 2020", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSob3wey6wikjtqCra5wPLb286NKa48rIaFuiPYMzJy00xmN_ta" },
        { "name": "Meek", "date": "on 28 Feb 2020", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR4ZquZ9WBSNSuWlUwtYXR1a2Xrb-1V8TeCKA8evcQSCOxiw5yD" },
        { "name": "Shia LeBeouf", "date": "on 28 Feb 2020", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQOgYVUE73-k4ESk4wwux1H1625Vs8TwjfUeGCff96PeJbL-2OL" }])
persondata_df = pd.DataFrame(data)

vehicledata = ([
        { "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRykCjSTepqOInxuZeFdC_t1Tuq4PeGTWqR4DUFUCSdnd-fboRZ","detailtitle":"Toyota Corolla,2004 Model","licenseplate":"9XBR691","linkedpeople":"Lindsay Lohan,Nina Dobrev,Meek Mill","linkedrecords":"Rec0001-Felony - Assault"},
        { "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTPovBxL-atK0_t3yDTpv_WULCeZGCQzjGGTfw_eiQkZzXJrQuv", "detailtitle":"Toyota Corolla,2006 Model","licenseplate":"9XBR671","linkedpeople":"Lindsay Lohan,Nina Dobrev,Meek Mill","linkedrecords":"Rec0015-Felony - Assault"},
        { "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSSk6mWyNHtRA_aIw3xNam7Zk2yp_szXf76ja-KXTLacqrIecrP", "detailtitle":"Toyota Corolla,2015 Model","licenseplate":"9XBR453","linkedpeople":"Lindsay Lohan,Nina Dobrev,Meek Mill","linkedrecords":"Rec0006-Felony - Assault"}])
vehicledata_df = pd.DataFrame(vehicledata)

addressdata = ([
        { "name": "Bruno Mars","img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSxypH2VAi6VsPtkdE-7dwuVaXGAn0IdHG9SkUf1b2EBzSt76cY","addressname":"478 St Loius Street,Concord,","state":"CA - 47965","linkedpeople":"Lindsay Lohan,Nina Dobrev,Meek Mill","linkedrecords":"Rec0001-Felony - Assault"},
        { "name": "Bruno Mars","img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ5SL9ewoC4wUW9c8iJbs1ze8HlwYlqDlzo1fpbjMStkkgr3ZEV","addressname":"448 St Robert Street,Concord,","state":"CA - 47945","linkedpeople":"Lindsay Lohan,Nina Dobrev,Meek Mill","linkedrecords":"Rec0001-Felony - Assault"},
        { "name": "Bruno Mars","img": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQF9E9_mO1FhML45-f4ZuaA8nROCWWl7TnkYjMG96IkYGGJdg7X", "addressname":"474 St Peter Street,Concord,","state":"CA - 47865","linkedpeople":"Lindsay Lohan,Nina Dobrev,Meek Mill","linkedrecords":"Rec0001-Felony - Assault"}])
addressdata_df = pd.DataFrame(addressdata)

@app.route("/persondata", methods=['GET', 'POST'], endpoint='func1')
def func1(): 
    return (persondata_df.to_json(orient='records').replace('\\', ''))

@app.route("/vehicledata", methods=['GET', 'POST'], endpoint='func2')
def func2(): 
    return (vehicledata_df.to_json(orient='records').replace('\\', ''))
@app.route("/addressdata", methods=['GET', 'POST'], endpoint='func3')
def func3(): 
    return (addressdata_df.to_json(orient='records').replace('\\', ''))
if __name__ == '__main__':
    #app.run(debug=True, port=3000)
    app.run()
    #app.run(debug=True, host='172.20.10.5', port=3000)
    