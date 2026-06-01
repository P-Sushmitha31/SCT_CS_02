

from PIL import Image   
import numpy as np      

def encrypt_image(image_path, key):
    print("Opening image...")
    img = Image.open(image_path)
    pixels = np.array(img)

    print(f"Encrypting with key: {key} ...")
    encrypted = (pixels.astype(int) + key) % 256
    result = Image.fromarray(encrypted.astype(np.uint8))
    result.save("encrypted.png")
    print("Done! Encrypted image saved as: encrypted.png")

def decrypt_image(image_path, key):
    print("Opening encrypted image...")
    img = Image.open(image_path)

    pixels = np.array(img)

    print(f"Decrypting with key: {key} ...")
    decrypted = (pixels.astype(int) - key) % 256
    result = Image.fromarray(decrypted.astype(np.uint8))
    result.save("decrypted.png")
    print("Done! Decrypted image saved as: decrypted.png")
 
print("=" * 40)
print("   IMAGE ENCRYPTION TOOL")
print("   SkillCraft Technology - Task 02")
print("   Method: Math (Add / Subtract)")
print("=" * 40)

print("\nWhat do you want to do?")
print("1. Encrypt an image")
print("2. Decrypt an image")

choice = input("\nEnter 1 or 2: ")

image_file = input("Enter image file name (example: photo.png): ")
key = int(input("Enter a secret key number (example: 42): "))

print()

if choice == "1":
    encrypt_image(image_file, key)
elif choice == "2":
    decrypt_image(image_file, key)
else:
    print("Invalid choice! Please enter 1 or 2.")

print("\nCheck your folder for the output image!")