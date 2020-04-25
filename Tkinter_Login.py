from Tkinter import *
import os

# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()


# Designing window for login 

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

# Implementing event on register button

def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

# Implementing event on login button 

def login_sucess():
    import random
    import time

    class Game:
        def __init__(self, canvas): # Added method.
            self.canvas=canvas
        def game_loop(self):  # Removed canvas parameter.
            if hit_bottom==True:
                self.draw_text(self.canvas,300,200,text)  # Added self.canvas arg
        def draw_text(self,canvas,x,y,text,size='40'):
            font=('Helvetica',size)
            return self.canvas.create_text(x,y,text=text,font=font)

    class Ball:
        def __init__(self,canvas,bat,color):
            self.canvas=canvas
            self.bat=bat
            self.id=canvas.create_oval(30,30,50,50,fill=color)
            self.canvas.move(self.id,100,200)
            starting_position=[-3,-2,-1,1,2,3]
            random.shuffle(starting_position)
            self.x = starting_position[0]
            self.y = -3
            self.canvas_height=self.canvas.winfo_height()
            self.canvas_width=self.canvas.winfo_width()
            self.hit_bottom=False 


        def hit_bat(self,pos):
            bat_pos=self.canvas.coords(self.bat.id)
            if pos[2] >=bat_pos[0] and pos[0] <=bat_pos[2]:
                if pos[3]>=bat_pos[1] and pos[3] <= bat_pos[3]:
                    return True
            return False

        def draw(self):
            self.canvas.move(self.id,self.x,self.y)
            pos=self.canvas.coords(self.id)
            if pos[1] <=0:
                self.y=6
            if pos[3] >=self.canvas_height:
                self.hit_bottom = True


            if self.hit_bat(pos) ==True:
                self.y=-6
            if pos[0] <=0:
                self.x=6
            if pos[2]>=self.canvas_width:
                self.x=-6



    class Pongbat():
        def __init__(self,canvas,color):
            self.canvas=canvas
            self.id=canvas.create_rectangle(0,0,100,10,fill=color)
            self.canvas.move(self.id,200,300)
            self.x=0
            self.canvas_width=self.canvas.winfo_width()
            self.canvas.bind_all('',self.left_turn)
            self.canvas.bind_all('',self.right_turn)


        def draw(self):
            self.canvas.move(self.id,self.x,0)
            pos=self.canvas.coords(self.id)
            if pos[0]<=0:
                self.x=0
            if pos[2]>=self.canvas_width:
                self.x=0

        def left_turn(self,evt):
            self.x=-10

        def right_turn(self,evt):
            self.x=10

    def main():
        tk=Tk()
        tk.title("My 21st Century Pong Game")
        tk.resizable(0,0)
        tk.wm_attributes("-topmost",1)
        canvas=Canvas(tk,bg="white",width=500,height=400,bd=0,highlightthickness=0)
        canvas.pack()
        tk.update()

        bat1=Pongbat(canvas,'red')
        ball1=Ball(canvas,bat1, 'green')

        while 1:
            if ball1.hit_bottom ==False: 
                ball1.draw()
                bat1.draw()
                tk.update()  # Allow screen to be updated (moved here after draw calls).
            else:
                draw1=Game(canvas)  # Added argument for new __init__() method.
                draw1.draw_text(canvas,250,200,'Game Over')  # Added canvas arg.
                tk.update()  # Allow screen to be updated.
                canvas.after(3000)  # Added. Pause for a few seconds.
                return  # Terminate.

#        time.sleep(0.02)  # Although you can do so, it is best not to call sleep() in tkinter app.
            canvas.after(2)  # Use universal 'after()` method instead. Time in millisecs.
    main()
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir("/Users/wastella/Basic_Tkinter")
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

# Designing popup for login success


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()
