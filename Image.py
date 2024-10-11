from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import hashlib
import random
import os

def load_image(image_path):
    img = Image.open(image_path)
    return np.array(img)

def save_image(image_array, output_path):
    img = Image.fromarray(image_array)
    img.save(output_path)

def generate_key_from_password(password):
    hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
    shift_value = int(hashed[:8], 16) % 256  
    random_seed = int(hashed[8:16], 16)  
    return shift_value, random_seed

def encrypt_image(image_array, shift_value, random_seed):
    np.random.seed(random_seed) 

    encrypted_image = (image_array + shift_value) % 256  
    height, width, channels = encrypted_image.shape
    flattened_image = encrypted_image.reshape(-1, channels)
    np.random.shuffle(flattened_image) 
    encrypted_image = flattened_image.reshape(height, width, channels)
    
    return encrypted_image

def decrypt_image(encrypted_array, shift_value, random_seed):
    np.random.seed(random_seed) 
    height, width, channels = encrypted_array.shape
    flattened_image = encrypted_array.reshape(-1, channels)
    shuffle_indices = np.arange(flattened_image.shape[0])
    np.random.shuffle(shuffle_indices)
    reversed_shuffle_indices = np.argsort(shuffle_indices)
    flattened_image = flattened_image[reversed_shuffle_indices]
    
    decrypted_image = flattened_image.reshape(height, width, channels)
    decrypted_image = (decrypted_image - shift_value) % 256 
    
    return decrypted_image

def process_image(image_path, password, output_encrypted_path, output_decrypted_path, action):
    shift_value, random_seed = generate_key_from_password(password)
    image_array = load_image(image_path)
    
    if action == "encrypt":
        encrypted_image = encrypt_image(image_array, shift_value, random_seed)
        save_image(encrypted_image.astype(np.uint8), output_encrypted_path)
        return encrypted_image
    
    elif action == "decrypt":
        encrypted_image = load_image(image_path)
        decrypted_image = decrypt_image(encrypted_image, shift_value, random_seed)
        save_image(decrypted_image.astype(np.uint8), output_decrypted_path)
        return decrypted_image
        
def load_image_for_display(image_path):
    img = Image.open(image_path)
    img.thumbnail((300, 300)) 
    return ImageTk.PhotoImage(img)
class ImageEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption Tool")
        self.root.geometry("500x400")
        
        # Variables
        self.image_path = None
        self.password = StringVar()
        self.encrypted_image_path = None
        self.create_widgets()

    def create_widgets(self):
        Button(self.root, text="Select Image", command=self.select_image).pack(pady=10)
        self.image_label = Label(self.root)
        self.image_label.pack(pady=10)
        Label(self.root, text="Enter Password:").pack(pady=5)
        Entry(self.root, textvariable=self.password, show="*").pack(pady=5)
        Button(self.root, text="Encrypt Image", command=self.encrypt_image).pack(pady=10)
        Button(self.root, text="Decrypt Image", command=self.select_encrypted_image).pack(pady=10)

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if self.image_path:
            img = load_image_for_display(self.image_path)
            self.image_label.config(image=img)
            self.image_label.image = img  
    
    def encrypt_image(self):
        if not self.image_path or not self.password.get():
            messagebox.showwarning("Input Error", "Please select an image and enter a password.")
            return
        output_encrypted_path = "encrypted_image.png"
        process_image(self.image_path, self.password.get(), output_encrypted_path, None, "encrypt")
        self.encrypted_image_path = output_encrypted_path  
        messagebox.showinfo("Success", f"Image encrypted and saved as {output_encrypted_path}")
    
    def select_encrypted_image(self):
        self.encrypted_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png")])
        if self.encrypted_image_path:
            self.decrypt_image()

    def decrypt_image(self):
        if not self.encrypted_image_path or not self.password.get():
            messagebox.showwarning("Input Error", "Please select an encrypted image and enter a password.")
            return
        output_decrypted_path = "decrypted_image.png"
        process_image(self.encrypted_image_path, self.password.get(), None, output_decrypted_path, "decrypt")
        messagebox.showinfo("Success", f"Image decrypted and saved as {output_decrypted_path}")

if __name__ == "__main__":
    root = Tk()
    app = ImageEncryptionApp(root)
    root.mainloop()
