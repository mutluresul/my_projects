from flask import Flask # Flask kütüphanesi

app = Flask(__name__) #obje oluşturma

@app.route("/") # / kök dizin
def head(): #decorator etme - ana sayfayı düzenleme
    return "<h1>You are gonna be a good DevOps and AWS Solution Architech</h1>"

@app.route("/second") # url sonuna /second ekle 
def second():
    return "This is the second page"

@app.route("/third/subthird")
def third():
    return "This is the subpath of third path"

@app.route("/forth/<string:id>") #string e atama 
def forth(id):
    return f'Id of this page is {id}'

if __name__=="__main__": # kontrol cümlesi
    app.run(debug=True) # çalıştır (hata ayıklama yap)- port numaraı da atayabiliriz
    

#çalışmayı ctrl + c ile durdurabiliriz.