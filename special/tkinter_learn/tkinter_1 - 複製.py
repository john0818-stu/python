import tkinter as tk

window = tk.Tk()

window.title("title")

#設定視窗大小為 300x100(長*寬)，視窗（左上角）在螢幕上的座標位置為 (250, 150)
window.geometry("500x200+250+150")

ent = tk.Entry( window , show='*' )
ent.pack()

def password() :
    
    var = ent.get()
    text.insert( 'insert' , var )
    
def insert_end() :
    
    var = ent.get()
    text.insert( 2.2 , var )

bn1 = tk.Button( window , text = 'password' , command = password , width = 12 , height = 2 )
bn1.pack()


bu2 = tk.Button( window , text = 'insert' , command = insert_end  , width = 12 , height = 2 )
bu2.pack()

text = tk.Text( window , height = 2 )
text.pack()

window.mainloop()
