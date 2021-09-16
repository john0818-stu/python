import tkinter as tk

window = tk.Tk()

window.title("title")

#設定視窗大小為 300x100(長*寬)，視窗（左上角）在螢幕上的座標位置為 (250, 150)
window.geometry("400x400+250+150")

var = tk.StringVar()

lal = tk.Label( window , textvariable=var , bg = "red" , width = 15 , height = 2  )
lal.place( x = 100 , y = 50 )

on_hit = False 
def hit() :
    
    global on_hit

    if on_hit == False :
        on_hit = True 
        var.set('you hit me')
        
    else :
        on_hit = False
        var.set('')

    
but = tk.Button( window , text = "button" , width = 15 , height = 2 , command = hit )
but.place( x = 100 , y = 200 )

window.mainloop()
