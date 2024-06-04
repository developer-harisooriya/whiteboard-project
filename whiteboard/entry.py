from tkinter import *
import pymysql as sq

# Initialize main window
root = Tk()
akp = IntVar()
pkp = StringVar()
root.title("White Board Project")
root.geometry('500x300')
root.configure(bg="#f2f3f5")
root.resizable(False, False)

# Establish database connection
c = sq.connect(host='localhost', user="root", password="", database="whiteboard")
y = c.cursor()

def exe():
    ak = akp.get()
    pk = pkp.get()
    p['state'] = 'disabled'
    p['bg'] = 'white'
    p['text'] = 'Submitted'
    print(ak, pk)
    # Use parameterized query to prevent SQL injection
    y.execute('INSERT INTO detials (company_id, project_name) VALUES (%s, %s)', (ak, pk))
    c.commit()

# GUI components
Label(root, text="Company ID:", bg="#f2f3f5").pack()
Entry(root, textvariable=akp, bg="#f2f3f5").pack()

Label(root, text="Project Name:", bg="#f2f3f5").pack()
Entry(root, textvariable=pkp, bg="#f2f3f5").pack()

p = Button(root, text="Submit", bg="red", command=exe)
p.pack()

# Main loop
root.mainloop()

# Close the database connection after the main loop
c.close()
