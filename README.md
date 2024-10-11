## Image Encryption Tool
This is a Python-based image encryption and decryption tool built with Tkinter. It allows users to encrypt and decrypt image files using pixel manipulation and a password-based key generation method. The password ensures an additional layer of security, as it is used to generate the key for pixel shifting and pixel swapping.

## Features
- Encrypt Images: Encrypts images by shifting pixel values and randomly shuffling pixels using a key derived from a password.
- Decrypt Images: Decrypts encrypted images back to their original form by reversing the pixel shifts and swaps.
- Password Protection: Uses a password to generate a deterministic key for encryption and decryption.
- Image Formats Supported: .jpg, .jpeg, .png

## Prerequisites
Before running the application, make sure you have Python 3 installed, and install the required libraries.

Required Libraries:
- Tkinter (usually comes bundled with Python)
- Pillow (for image processing)
- NumPy (for pixel manipulation)
## Installation of Dependencies
You can install the necessary dependencies by running the following command:

```bash
pip install Pillow numpy
```
## How to Run
Clone or download the repository to your local machine.
Navigate to the project directory.
Run the Python script:
```bash
python image_encryption_tkinter.py
```
## How to Use
- Encrypting an Image
Launch the application.
Click the "Select Image" button to choose an image file from your computer.
Enter a password in the "Enter Password" field.
Click the "Encrypt Image" button to encrypt the selected image. The encrypted image will be saved as encrypted_image.png in the current working directory.
- Decrypting an Image
Launch the application.
Click the "Decrypt Image" button to select an encrypted image file (.png format).
Enter the same password used during encryption in the "Enter Password" field.
Click the "Decrypt Image" button to decrypt the image. The decrypted image will be saved as decrypted_image.png in the current working directory.

## Project Logic
Key Generation: The encryption key is derived from the user-provided password using the SHA-256 hashing algorithm. The key determines how much the pixel values are shifted and the random seed for pixel shuffling.
- Encryption:
The pixel values (RGB) of the image are shifted by the derived key.
The pixels are then shuffled randomly using a deterministic shuffle based on the password.
- Decryption:
The pixels are unshuffled back to their original order using the same password-based shuffle.
The pixel values are reversed by applying the negative shift from the derived key.
Important Notes
The password used during encryption must be the same when decrypting the image.
Only .png files can be decrypted since the encryption process outputs .png images.
Be careful not to lose the password, as it is critical for decrypting the image!
