import tkinter

window = tkinter.Tk()
window.title("BMI")
window.minsize(width=250, height=250)
window.config(bg="light blue")
window.config(pady=40)

label = tkinter.Label(text="Lütfen Kilonuzu girin", font=('Arial', 13, "normal"))
label.config(bg="light blue")
label.pack()

entry = tkinter.Entry(window)
entry.pack()

label2 = tkinter.Label(text="Lütfen boyunuzu girin", font=('Arial', 13, "normal"))
label2.config(bg="light blue")
label2.pack()

entry2 = tkinter.Entry(window)
entry2.pack()

result_label = tkinter.Label(text="", font=('Arial', 13, "normal"))
result_label.config(bg="light blue")
result_label.pack()

def bmi_calculate():
    try:
        weight = float(entry.get())
        height = float(entry2.get())
        bmi = weight / (height ** 2)
        result_label.config(text=f"BMI: {bmi:.2f}")
        bmi_value(bmi)
    except ValueError:
        result_label.config(text="Lütfen sayıları doğru girin.")

def bmi_value(bmi):
    if bmi < 18.5:
        result_label.config(text="Zayıf")
    elif 18.5 <= bmi < 25:
        result_label.config(text="Normal")
    elif 25 <= bmi < 30:
        result_label.config(text="Kilolu")
    elif 30 <= bmi < 40:
        result_label.config(text="Obezite")
    elif bmi >= 40:
        result_label.config(text="Yüksek Obezite")

button = tkinter.Button(text="Hesapla", command=bmi_calculate)
button.pack()

window.mainloop()

