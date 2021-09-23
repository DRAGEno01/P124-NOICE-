from flask import Flask,jsonify,request

app=Flask(__name__)

List=[
{
'id':1,
'Name':'Daniel',
'Contact':'123456789',
'done':False

},
{
'id':2,
'Name':'Bob',
'Contact':'987654321',
'done':False

}

]
@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/add-data",methods=["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Plaese provide the data"
        },400)

    contact={
        'id':tasks[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact',""),
        'done':False

    }
    List.append(contact)
    return jsonify({
        "status":"success",
        "message":"Contact added successfully"
    })

@app.route("/get-data")
def get_data():
    return jsonify({
        "data":List
    })

if (__name__ == "__main__"):
    app.run(debug=True)