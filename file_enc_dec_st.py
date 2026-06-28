import os
from io import BytesIO
import streamlit as st
from cryptography.fernet import Fernet

# Set up page configuration
st.set_page_config(
    page_title="File Crypter", page_icon="🔒", layout="centered"
)


def get_or_create_key(key_path="secret.key"):
    """Loads the key if it exists, otherwise creates a new one."""
    if os.path.exists(key_path):
        with open(key_path, "rb") as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open(key_path, "wb") as key_file:
            key_file.write(key)
        return key


# Initialize the cipher suite
SECRET_KEY = get_or_create_key()
fernet = Fernet(SECRET_KEY)

# UI Elements
st.title("🔒 File Encryption & Decryption")
st.write(
    "Upload a file to securely encrypt or decrypt it instantly using AES-128 (Fernet)."
)

# App mode selection
mode = st.radio("Choose Operation:", ["Encrypt File", "Decrypt File"])

st.divider()

if mode == "Encrypt File":
    st.subheader("📁 Encrypt a File")
    uploaded_file = st.file_uploader(
        "Choose a file to encrypt", key="encrypt_upload"
    )

    if uploaded_file is not None:
        file_bytes = uploaded_file.read()

        try:
            # Process encryption
            encrypted_bytes = fernet.encrypt(file_bytes)

            # Build filename: filename.enc.extension
            name, ext = os.path.splitext(uploaded_file.name)
            output_filename = f"{name}.enc{ext}" if ext else f"{name}.enc"

            st.success(f"File encrypted successfully as `{output_filename}`!")

            # Download button
            st.download_button(
                label="📥 Download Encrypted File",
                data=encrypted_bytes,
                file_name=output_filename,
                mime="application/octet-stream",
            )
        except Exception as e:
            st.error(f"Encryption failed: {e}")

else:
    st.subheader("🔓 Decrypt a File")
    uploaded_file = st.file_uploader(
        "Choose a file to decrypt", key="decrypt_upload"
    )

    if uploaded_file is not None:
        file_bytes = uploaded_file.read()

        try:
            # Process decryption
            decrypted_bytes = fernet.decrypt(file_bytes)

            orig_filename = uploaded_file.name
            # Strip out .enc if it exists in the name string
            if ".enc" in orig_filename:
                orig_filename = orig_filename.replace(".enc", "")

            # Build filename: filename.dec.extension
            name, ext = os.path.splitext(orig_filename)
            output_filename = f"{name}.dec{ext}" if ext else f"{name}.dec"

            st.success(f"File decrypted successfully as `{output_filename}`!")

            # Download button
            st.download_button(
                label="📥 Download Decrypted File",
                data=decrypted_bytes,
                file_name=output_filename,
                mime="application/octet-stream",
            )
        except Exception:
            st.error(
                "Decryption failed! The file may be corrupted or the secret key does not match."
            )