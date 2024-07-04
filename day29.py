import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menampilkan pesan
def show_message():
    messagebox.showinfo("Pesan", "Selamat datang di Program Grafis Sederhana!")

# Membuat jendela utama
root = tk.Tk()
root.title("Program Grafis Sederhana")

# Membuat tombol
button = tk.Button(root, text="Klik untuk Pesan", command=show_message)
button.pack(pady=20)

# Menjalankan main loop untuk menampilkan jendela
root.mainloop()
