import tkinter as tk

class Kalkulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Kalkulator Sederhana")

        # Variabel untuk menyimpan ekspresi
        self.expression = tk.StringVar()

        # Entry untuk menampilkan ekspresi
        entry = tk.Entry(master, textvariable=self.expression, font=('Helvetica', 16), bd=10, insertwidth=4, width=14, justify='right')
        entry.grid(row=0, column=0, columnspan=4)

        # Tombol-tombol kalkulator
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Membuat dan menempatkan tombol-tombol kalkulator
        for (text, row, col) in buttons:
            button = tk.Button(master, text=text, font=('Helvetica', 14), padx=20, pady=20, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col)

    def button_click(self, value):
        # Fungsi untuk menangani klik tombol kalkulator
        if value == 'C':
            # Clear (hapus) ekspresi
            self.expression.set('')
        elif value == '=':
            # Evaluasi ekspresi dan tampilkan hasil
            try:
                result = str(eval(self.expression.get()))
                self.expression.set(result)
            except Exception as e:
                self.expression.set('Error')
        else:
            # Tambahkan nilai tombol yang diklik ke ekspresi
            current_expression = self.expression.get()
            new_expression = current_expression + str(value)
            self.expression.set(new_expression)

def main():
    root = tk.Tk()
    app = Kalkulator(root)
    root.mainloop()

if __name__ == "__main__":
    main()