import tkinter as tk

calculation = ""

def add_to_calculationss(symbol):
    global calculation
    calculation += str(symbol)
    text_results.delete(1.0, "end")
    text_results.insert(1.0, calculation)

def evaluate_calculations():
    global calculation
    try: 
        result = str(eval(calculation))
        text_results.delete(1.0, "end")
        text_results.insert(1.0, calculation)    
    except:
        clear_field()
        text_results.insert(1.0, "Error")
    

def clear_field():
    global calculation
    calculation = ""
    text_results.insert(1.0, "end")

root = tk.Tk()
root.geometry("300x275")
text_results = tk.Text(root, height=2, width=16, font=("arial", 24))
text_results.grid(columnspan=5)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculationss(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculations(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculations(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculations(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculations(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculations(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculations(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculations(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculations(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculations(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculations(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculations(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculations(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculations(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculations(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculations(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculations(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculations("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculations("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)

btn_multiply = tk.Button(root, text="*", command=lambda: add_to_calculations("*"), width=5, font=("Arial", 14))
btn_multiply.grid(row=4, column=4)

btn_divide = tk.Button(root, text="/", command=lambda: add_to_calculations("/"), width=5, font=("Arial", 14))
btn_divide.grid(row=5, column=4)

btn_open_parenthesis = tk.Button(root, text="(", command=lambda: add_to_calculations("("), width=5, font=("Arial", 14))
btn_open_parenthesis.grid(row=5, column=1)

btn_close_parenthesis = tk.Button(root, text=")", command=lambda: add_to_calculations(")"), width=5, font=("Arial", 14))
btn_close_parenthesis.grid(row=5, column=3)

btn_equals = tk.Button(root, text="=", command=evaluate_calculations, width=11, font=("Arial", 14))
btn_equals.grid(row=6, column=3)

btn_clear = tk.Button(root, text="C", command=clear_field, width=5, font=("Arial", 14))
btn_clear.grid(row=6, column=1)





root.mainloop()