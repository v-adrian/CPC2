import webbrowser as wb

message = '''
<!DOCTYPE html>
<html>
    <title>Exercise #5 </title>

    <head> 
        <h1>Welcome to my first HTML Program using Python!</h1> 
    </head>

    <body> 
        <h2>Vonn Adrian C. Jutar- A121</h2>
        <p>Thank you!</p> 
    </body>
</html>
'''

f = open('Exercise #5.html', 'w')
f.write(message)
f.close()

wb.open_new_tab('Exercise #5.html')
