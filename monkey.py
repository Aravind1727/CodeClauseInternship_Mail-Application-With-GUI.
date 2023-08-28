import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Application")
        
        self.entry_width = 40  # Width for the Entry widgets
        
        self.from_label = tk.Label(root, text="From:")
        self.from_label.pack(pady=5)
        self.from_entry = tk.Entry(root, width=self.entry_width)
        self.from_entry.pack(pady=5)
        
        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(root, show="*", width=self.entry_width)
        self.password_entry.pack(pady=5)
        
        self.to_label = tk.Label(root, text="To:")
        self.to_label.pack(pady=5)
        self.to_entry = tk.Entry(root, width=self.entry_width)
        self.to_entry.pack(pady=5)
        
        self.subject_label = tk.Label(root, text="Subject:")
        self.subject_label.pack(pady=5)
        self.subject_entry = tk.Entry(root, width=self.entry_width)
        self.subject_entry.pack(pady=5)
        
        self.message_label = tk.Label(root, text="Message:")
        self.message_label.pack(pady=5)
        self.message_text = tk.Text(root, height=10, width=self.entry_width)
        self.message_text.pack(pady=5)
        
        self.send_button = tk.Button(root, text="Send", command=self.send_email)
        self.send_button.pack(pady=10)
        
        self.add_hover_effects()
    
    def add_hover_effects(self):
        entries = [
            self.from_entry,
            self.password_entry,
            self.to_entry,
            self.subject_entry,
        ]
        
        for entry in entries:
            entry.bind("<Enter>", lambda event, e=entry: self.on_enter(event, e))
            entry.bind("<Leave>", lambda event, e=entry: self.on_leave(event, e))
        
    def on_enter(self, event, entry):
        entry.config(bg="lightgray")
        
    def on_leave(self, event, entry):
        entry.config(bg="white")
    
    def send_email(self):
        from_email = self.from_entry.get()
        password = self.password_entry.get()
        to_email = self.to_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", tk.END)
        
        if not from_email or not password or not to_email or not subject or not message:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        
        try:
            smtp_server = "smtp.example.com"  # Update with your SMTP server
            smtp_port = 587
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(from_email, password)
            
            msg = MIMEMultipart()
            msg["From"] = from_email
            msg["To"] = to_email
            msg["Subject"] = subject
            msg.attach(MIMEText(message, "plain"))
            
            server.sendmail(from_email, to_email, msg.as_string())
            server.quit()
            
            messagebox.showinfo("Success", "Email sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    email_app = EmailApp(root)
    root.mainloop()
