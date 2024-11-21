# 0157CY221126
# Shiksha Jaiswal

from random import *

users={}

questions={
    'py':[
        {"q":"Which of the following is the correct extension of a Python file?", "options":[".python",".pl",".py",".p"], "ans":".py"},  
        {"q":"Which keyword is used for function in Python?", "options":["define","function","define","def"], "ans":"def"},
        {"q":"What is the output of print(type([]))", "options":["<class 'list'>","<class 'tuple'>","<class 'set'>","<class 'dict'>"], "ans":"<class 'list'>"},
        {"q":"What is the output of print(2**3)?", "options":['6', '8', '9', '12'], "ans":'8'},
        {"q":"Which of the following functions can be used to find the length of a string in Python?", "options":["len()","length()","size()","count()"], "ans":"len()"},
        {"q":"Which of the following is NOT a valid Python data type", "options":["List","Tuple","Class","Stack"], "ans":"Stack"},
        {"q":"Which function is used to convert a string into a list of words in Python", "options":["split()","join()","replace()","cut()"], "ans":"split()"},
        {"q":"What will be the output of : print(bool(0))", "options":["True","False","Error","None"], "ans":"False"},
        {"q":"What does the following expression evaluate to in Python : not True", "options":["True","False","Error","None"], "ans":"False"},
        {"q":"Which of the following statements is used to stop a loop in Python?", "options":["exit","break","quit","stop"], "ans":"break"},
        {"q":"Which of the following is a mutable data type in Python?", "options":["Tuple","List","String","Integer"], "ans":"List"},
        {"q":"Which of the following methods can be used to combine two lists in Python?", "options":["append()","extend()","merge()","insert()"], "ans":"extend()"},
        {"q":"Which of the following methods removes an element from a list by value in Python?", "options":["remove()","pop()","delete()","discard()"], "ans":"remove()"},
        {"q":"What is the output of the following code?", "options":["3.33","3","4","3.0"], "ans":"3"},
        {"q":"What will be the output of the following code : print(2**2**3) ", "options":["16","64","256","512"], "ans":"256"},
        {"q":"Which of the following is used to delete a variable in Python?", "options":["del","remove","discard","pop"], "ans":"del"},
        {"q":"Which of the following methods can be used to add an element to the end of a list?", "options":["add()","insert()","append()","update()"], "ans":"append()"},
        {"q":"Which of the following functions is used to return the maximum value from a list in Python?", "options":["max()","min()","len()","sum()"], "ans":"max()"},
        {"q":"Which of the following methods can be used to create a shallow copy of a list?", "options":["copy()","deepcopy()","duplicate()","clone()"], "ans":"copy()"},
        {"q":"Which of the following can be used to find the type of an object in Python?", "options":["object_type()","typeof()","type()","gettype()"], "ans":"type()"}      
    ],

    'html':[
        {"q":"Which HTML tag is used to create a hyperlink?", "options":["<link>", "<a>", "<href>", "<hyperlink>"], "ans":"<a>"},
        {"q": "Which HTML tag is used to define an image?", "options": ["<img>", "<src>", "<picture>", "<image>"], "ans": "<img>"},
        {"q":"Which HTML element is used to specify a footer for a document?", "options":["<footer>", "<bottom>", "<foot>", "<footersection>"], "ans":"<footer>"},
        {"q":"What is the correct HTML tag for inserting a line break?", "options": ["<br>", "<break>", "<lb>", "<hr>"], "ans":"<br>"},
        {"q":"Which tag is used to define the largest heading?", "options": ["<h1>", "<h6>", "<heading>", "<head>"], "ans":"<h1>"},
        {"q":"What is the correct HTML for creating an ordered list?", "options": ["<ul>", "<ol>", "<list>", "<order>"], "ans":"<ol>"},
        {"q":"What is the correct HTML for creating a checkbox?", "options": ["<input type='checkbox'>", "<check>", "<checkbox>", "<input type='check'>"], "ans":"<input type='checkbox'>"},
        {"q":"How can you create a numbered list in HTML?", "options": ["<dl>", "<ul>", "<ol>", "<li>"], "ans":"<ol>"},
        {"q":"Which attribute specifies an alternate text for an image, if the image cannot be displayed?", "options": ["alt", "title", "src", "href"], "ans":"alt"},
        {"q":"What is the correct way to open a link in a new tab?", "options": ["<a href='url' target='_blank'>", "<a href='url' new_tab='true'>", "<a href='url' new='yes'>", "<a href='url' target='new'>"], "ans":"<a href='url' target='_blank'>"},
        {"q":"Which HTML element is used to define the title of a document?", "options": ["<meta>", "<title>", "<header>", "<head>"], "ans":"<title>"},
        {"q":"Which HTML tag is used to make text bold?", "options": ["<bold>", "<b>", "<strong>", "<em>"], "ans":"<b>"},
        {"q":"Which tag is used to define a table row in HTML?", "options": ["<tr>", "<td>", "<th>", "<row>"], "ans":"<tr>"},
        {"q":"Which HTML tags are used to create a drop-down list?", "options": ["<select>", "<list>", "<dropdown>", "<input>"], "ans":"<select>"},
        {"q":"Which tag is used to define a table header in HTML?", "options": ["<th>", "<tr>", "<td>", "<header>"], "ans":"<th>"},
        {"q":"Which attribute is used to specify the URL of the linked document in an anchor tag?", "options": ["href", "src", "link", "url"], "ans":"href"},
        {"q":"Which tag is used to create a section within an HTML document?", "options": ["<div>", "<section>", "<header>", "<article>"], "ans":"<section>"},
        {"q":"What is the correct syntax for creating a radio button in HTML?", "options": ["<input type='radio'>", "<radio>", "<input type='button'>", "<input type='option'>"], "ans":"<input type='radio'>"},
        {"q":"Which HTML element is used to embed videos in a web page?", "options": ["<video>", "<media>", "<embed>", "<source>"], "ans":"<video>"},
        {"q":"Which HTML element is used to group multiple form elements together?", "options": ["<fieldset>", "<form>", "<legend>", "<group>"], "ans":"<fieldset>"}     
    ],

    'cpp':[
        {"q":"Which of the following is the correct syntax to declare a pointer in C++?", "options":["int *ptr;", "int ptr*;", "*int ptr;", "ptr int*;"], "ans":"int *ptr;"},
        {"q":"Which C++ keyword is used to define a constant?", "options":["constant", "const", "define", "static"], "ans":"const"},
        {"q":"Which operator is used to access the members of a structure through a pointer in C++?", "options":["->", ".", "::", "&"], "ans":"->"},
        {"q":"Which of the following is a correct comment in C++?", "options":["// Comment", "/* Comment", "# Comment", "<!-- Comment -->"], "ans":"// Comment"},
        {"q":"Which of the following is used to define a class in C++?", "options":["class", "struct", "object", "template"], "ans":"class"},
        {"q":"What is the size of a double in C++?", "options":["4 bytes", "8 bytes", "16 bytes", "depends on the compiler"], "ans":"8 bytes"},
        {"q":"Which of the following is the correct syntax to create an object in C++?", "options":["ClassName object;", "object ClassName;", "ClassName = object;", "ClassName::object;"], "ans":"ClassName object;"},
        {"q":"Which C++ keyword is used to allocate memory dynamically?", "options":["malloc", "alloc", "new", "create"], "ans":"new"},
        {"q":"Which of the following is the correct way to declare a constructor in C++?", "options":["ClassName();", "void ClassName();", "constructor ClassName();", "function ClassName();"], "ans":"ClassName();"},
        {"q":"Which of the following access specifiers is the most restrictive in C++?", "options":["private", "protected", "public", "internal"], "ans":"private"},
        {"q":"Which of the following is used to terminate a loop in C++?", "options":["break", "continue", "exit", "stop"], "ans":"break"},
        {"q":"Which function is used to write formatted output to the console in C++?", "options":["cout", "printf", "cin", "puts"], "ans":"cout"},
        {"q":"Which of the following is used to define a function outside of a class in C++?", "options":["::", ".", "->", "&"], "ans":"::"},
        {"q":"Which of the following data types stores a single character in C++?", "options":["char", "string", "int", "float"], "ans":"char"},
        {"q":"Which of the following C++ containers automatically grows in size?", "options":["vector", "array", "queue", "stack"], "ans":"vector"},
        {"q":"Which C++ keyword is used to prevent a class from being inherited?", "options":["final", "const", "protected", "sealed"], "ans":"final"},
        {"q":"Which of the following is used to handle exceptions in C++?", "options":["try-catch", "if-else", "throw-catch", "catch-finally"], "ans":"try-catch"},
        {"q":"Which of the following allows a class to inherit the properties of another class in C++?", "options":["Inheritance", "Abstraction", "Polymorphism", "Encapsulation"], "ans":"Inheritance"},
        {"q":"Which operator is used to check if two values are equal in C++?", "options":["==", "=", "=>", "<="], "ans":"=="},
        {"q":"Which of the following is not a C++ keyword?", "options":["private", "this", "struct", "integer"], "ans":"integer"}
    
    ]
}

def pswd_check(password):
    lower =0; upper=0; digit=0; special=0
    length=len(password)
    for s in password:
        if s.isalpha():
            if s.isupper():
                upper+=1
            elif s.islower():
                lower+=1
        elif s.isdigit():
            digit+=1
        else:
            if s not in ['@','#','%']:
                special+=1

    if length>8 and length<20 and digit and lower and upper and special:
        return True
    else:
        return False


def login():
    print("Login")
    id=input("Enter your User ID : ")
    if id not in users:
        print("User not Registered")
        return False
    pswd=input("Enter your Password : ")
    if users[id]==pswd:
        print("You have Logged In !!!!")
        return True
    

def register():
    print("Register")
    user_id=input("Create a Username : ")
    if user_id in users:
        print("User already exists! You need to Login")
    else:       
        password=input("Create your Password : ")
        if pswd_check(password):
            users[user_id] = password
            print("User Registered Successfully !!!!")
            main()
        else:
            print("Password Not Strong !!!! Make a strong Password")
            register()


def choose_topic():
    topic=input("Chosse the topic for the Quiz - 1.Python  2.HTML  3.C++ : ")
    if int(topic)==1:
        take_quiz('py')
    elif int(topic)==2:
        take_quiz('html')
    elif int(topic)==3:
        take_quiz('cpp')
    else:
        print("Invalid Option Choosen.")


def take_quiz(topic):
    print(f"{topic.upper()} Quiz")
    selected_questions =sample(questions[topic], 5)  
    score = 0
    
    for i, q in enumerate(selected_questions):
        print(f"\nQ{i+1}. {q['q']}")
        for j, opt in enumerate(q['options']):
            print(f"{j+1}. {opt}")
        answer = input("Enter the option number: ")
        correct_option = q['options'].index(q['ans']) + 1
        
        if answer == str(correct_option):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct Answer : {correct_option}.{q['ans']}")
    
    print(f"\nYour score: {score}/5")
    b=input("Do you want to give the test again - \n1.Yes \n2.No")
    if int(b)==1:
        choose_topic()
    elif int(b)==2:
        return
    else:
        print("Invalid Option Selected")
        return
     

def main():
    print("QUIZ")
    a=input("1.Login \n2.Register \n3.Exit \n")
   
    if int(a)==1:
        if login():
            choose_topic()
        else:
            main()

    elif int(a)==2:
        register()

    elif int(a)==3:
        return

    else:
        print("Invalid Input")
        main()
    

main()





