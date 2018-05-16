from flask import Flask, request, redirect
from flask import render_template

app = Flask(__name__)


people = {
    1  : {'id': 1, 'name': 'John',   'email': 'Johnjoe@gmail.com',    'phone': '0861234567'},    
    2  : {'id': 2, 'name': 'Olivia', 'email': 'Livtexting.com',       'phone': '0891122334'},
    3  : {'id': 3, 'name': 'Shane',  'email': 'unoriginal@gmail.com', 'phone': '1123581321'},
    
    }
next_id = 4


@app.route("/", methods=['GET', 'POST'])
def add_contact():
    global next_id
    if request.method == "POST":
        
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        id = next_id
        people[id] = {'id': id, 'name': name, 'email': email, 'phone': phone}
        next_id += 1
    return render_template("contact.html", data=people.values())

@app.route("/delete", methods=['POST'])
def delete_contact():
    id_to_delete = int(request.form.get('contact_to_delete'))
    
    del(people[id_to_delete])
    return redirect("/")       


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)