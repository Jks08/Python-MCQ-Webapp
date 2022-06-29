from pywebio.input import *
from pywebio.output import *
from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from pywebio.session import *

app = Flask(__name__)

def exam():        
    c = 0
    
    put_html("<h1>Test Quiz</h1>")
    name = input("Enter your Name and click Submit to Start the test", type ="text", validate = validate_name)

    q1 = radio("1. The Python tuple is __ in nature?",['Unchangeable','Immutable','Mutable','All of the above'])
    if q1 =='Immutable':
        c+=1

    q2 = radio("2. Does the python set have duplicate elements?",['No','Yes','Maybe'])
    if q2 =='No':
        c+=1

    q3 = radio("3. Which of the following sorting algorithms can be used to sort a random linked list with minimum time complexity?",['Insertion sort','Quick sort','Heap sort','Merge sort'])
    if q3 =='Merge sort':
        c+=1

    q4 = radio("4. Which python function is used to return length?",['count()','length()','dis()','len()'])
    if q4 == 'len()':
        c+=1

    q5 = radio("5. In Python, how is an empty List defined?",['list[]','list=[]','list=()','list=listName[]'])
    if q5 == 'list=[]':
        c+=1

    if c>3:
    	message = [style(put_html("<h1 style='display:inline;border-bottom:0px'>Congratulations !! </h1>"+ "Score: <b>"+ str(c) + "</b><br><br>") ,'color:green;'),style(put_html("<p>Result : <b>Congratulations! You Passed</b></p>"),'color:green'), put_html("<b>Your test is over</b>")]
    	popup("Result", content=message, size='large', implicit_close=True, closable=True)
    else:
    	message = [style(put_html("<h1 style='display:inline;border-bottom:0px'>Oops! " + "</h1>" + "Score: <b>"+ str(c) + "</b><br><br>"),'color:red'), style(put_html("<p>Result : <b>FAILED</b></p>"), 'color:red') , put_html("<b>Your test is over</b><br><br>"), style(put_link('Retry ↺',""), 'color:red;align-content: center;border-radius: 5px;color:#f9faf8;padding: 5px 100px;text-align:center;align-items : center;background-color: white;\
            background-image: linear-gradient(270deg, #8cf5f5 1%, #0a43f3 100%);')]
    	popup("Result", content=message, size='large', implicit_close=True, closable=True)

def validate_name(name):
	name = name.replace(" ","")
	if(name == "" or not(name.isalpha())):
		return("Only Alphabets allowed!")

app.add_url_rule('/','webio_view',webio_view(exam),methods=['GET','POST','OPTIONS'])

if __name__ == '__main__':
    app.run(debug=True, port= 5000)