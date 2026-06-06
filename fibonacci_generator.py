import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# ---------------- FIBONACCI ---------------- #

def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# ---------------- GENERATE + SHOW ---------------- #

def generate():
    try:
        n = int(entry.get())

        if n <= 0:
            messagebox.showwarning("Warning", "Enter positive number")
            return

        fib = fibonacci(n)

        # Text output
        output.delete("1.0", tk.END)
        output.insert(tk.END, "FIBONACCI SERIES\n" + "="*50 + "\n\n")
        output.insert(tk.END, str(fib))

        # Stats
        total = sum(fib)
        largest = max(fib)
        even = len([x for x in fib if x % 2 == 0])
        odd = len(fib) - even

        stats_label.config(text=f"""
Count  : {len(fib)}
Sum    : {total}
Max    : {largest}
Even   : {even}
Odd    : {odd}
""")

    except:
        messagebox.showerror("Error", "Invalid input")


# ---------------- GRAPH ---------------- #

def show_graph():
    try:
        n = int(entry.get())

        if n <= 0:
            return

        fib = fibonacci(n)

        plt.figure(figsize=(8, 5))
        plt.plot(range(n), fib, marker="o", color="blue")

        plt.title("Fibonacci Series Graph")
        plt.xlabel("Index")
        plt.ylabel("Value")
        plt.grid(True)

        plt.show()

    except:
        messagebox.showerror("Error", "Invalid input")


# ---------------- CLEAR ---------------- #

def clear():
    entry.delete(0, tk.END)
    output.delete("1.0", tk.END)
    stats_label.config(text="-")


# ---------------- UI ---------------- #

root = tk.Tk()
root.title("Fibonacci Generator")
root.geometry("900x600")
root.configure(bg="#1E1E2F")

# Title
tk.Label(root, text="FIBONACCI GENERATOR",
         font=("Segoe UI", 18, "bold"),
         fg="#00D4FF", bg="#1E1E2F").pack(pady=10)

# Input
frame = tk.Frame(root, bg="#1E1E2F")
frame.pack()

tk.Label(frame, text="Enter Number:",
         fg="white", bg="#1E1E2F").grid(row=0, column=0)

entry = tk.Entry(frame, font=("Segoe UI", 14))
entry.grid(row=0, column=1, padx=10)

# Buttons
btn_frame = tk.Frame(root, bg="#1E1E2F")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Generate", command=generate,
          bg="#00D4FF", width=12).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Show Graph", command=show_graph,
          bg="#90EE90", width=12).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Clear", command=clear,
          bg="#FF4444", width=12).grid(row=0, column=2, padx=5)

# Output
output = tk.Text(root, height=10, bg="#2A2A40", fg="white")
output.pack(fill="both", expand=True, padx=10, pady=10)

# Stats
stats_label = tk.Label(root, text="-",
                       fg="white", bg="#1E1E2F",
                       font=("Segoe UI", 11))
stats_label.pack(pady=10)

footer = tk.Label(
    root,
    text="Developed by Sri Poorani | Fibonacci Generator",
    bg="#111122",
    fg="gray",
    font=("Segoe UI", 9)
)
footer.pack(side="bottom", fill="x")
root.mainloop()