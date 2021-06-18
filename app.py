from flask import Flask, render_template, request
#from bst import BinarySearchTree
#from vpython import *
#bst = BinarySearchTree()
app = Flask(__name__)

#name="Surya"
#age=19

@app.route('/')
def main():
    return render_template('/home.html')

@app.route('/adtinfo')
def adtinf():
    return render_template('/ADTInfo.html')

@app.route('/avlvisual')
def avlvisualisation():
    return render_template('/forms.html')

"""
@app.route('/', methods =["GET", "POST"])
def getValue():
    if request.method == "POST":
        
        insertvalue=request.form['Insertvalue']
        
        a=[1,2,4,5,6,7]
        pos=vector(0,0,0)
        leftstartteta=pi
        rightstartteta=0
        bst.createTree(a,pos,1)
        bst.insertElement(3)
        
        #return "Your value is "+insertvalue
    #return render_template('/forms.html')
"""  

if __name__ == '__main__':
    app.run(debug=True)