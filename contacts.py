from flask import Flask, request
from flask import render_template

app = Flask(__name__)


people = {
    'John'   : {'name': 'John',   'email': 'Johnjoe@gmail.com',    'phone': '0861234567'},    
    'Olivia' : {'name': 'Olivia', 'email': 'Livtexting.com',       'phone': '0891122334'},
    'Shane'  : {'name': 'Shane',  'email': 'unoriginal@gmail.com', 'phone': '1123581321'},
    'Frank'  : {'name': 'Frank',  'email': 'sinatra@hotmail.com',  'phone': '248163264128'}
    }



@app.route("/", methods=['GET', 'POST'])
def add_contact():
    if request.method == "POST":
        
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        # people.append({'name': name, 'email': email, 'phone': phone})
        people[name] = {'name': name, 'email': email, 'phone': phone}
    
    return render_template("contact.html", data=people.values())

@app.route("/delete", methods=['POST'])
def delete_contact():
    name_to_delete = request.form.get('contact_to_delete')
    
    del(people[name_to_delete])
            
    return render_template("contact.html", data=people.values())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)