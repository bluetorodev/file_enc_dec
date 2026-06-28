# 🔒 File Encryption & Decryption App

A simple and secure **Streamlit** web application that allows users to encrypt and decrypt files using the **Fernet** symmetric encryption scheme from the **Cryptography** library.

## ✨ Features

* 🔐 Encrypt any file with a single click
* 🔓 Decrypt previously encrypted files
* 📥 Download encrypted and decrypted files instantly
* 🔑 Automatically generates and stores a secret encryption key (`secret.key`)
* 🖥️ Simple and intuitive Streamlit interface

---

## 🛠️ Technologies Used

* Python 3.x
* Streamlit
* Cryptography (Fernet)
* OS Module

---

## 📂 Project Structure

```
File-Crypter/
│
├── app.py              # Main Streamlit application
├── secret.key          # Automatically generated encryption key
├── requirements.txt    # Project dependencies
└── README.md
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/file-crypter.git
cd file-crypter
```

### 2. Create a virtual environment (Optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit server with:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 🔐 How It Works

### Encryption

1. Select **Encrypt File**.
2. Upload any file.
3. The application encrypts the file using a Fernet key.
4. Download the encrypted file.

Example:

```
document.pdf
      ↓
document.enc.pdf
```

---

### Decryption

1. Select **Decrypt File**.
2. Upload an encrypted file.
3. The application decrypts it using the same `secret.key`.
4. Download the decrypted file.

Example:

```
document.enc.pdf
        ↓
document.dec.pdf
```

---

## 🔑 Secret Key

On the first run, the application automatically creates a file named:

```
secret.key
```

This key is required for both encryption and decryption.

> **Important:** If the `secret.key` file is lost or replaced, previously encrypted files cannot be decrypted.

---

## 📄 Supported Files

The application works with any file type, including:

* PDF
* Images
* Word Documents
* Excel Files
* ZIP Archives
* Text Files
* Audio Files
* Video Files

---

## ⚠️ Notes

* Keep your `secret.key` file secure.
* Do not share your encryption key publicly.
* Always back up your key before deploying or moving the application.

---

## 📋 Requirements

Example `requirements.txt`:

```text
streamlit
cryptography
```

---

## 🚀 Future Improvements

* Password-based encryption
* User-generated encryption keys
* Multiple key management
* Drag-and-drop support
* Batch file encryption
* Progress indicators
* Cloud storage integration

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed as a simple and secure file encryption application using Python, Streamlit, and the Cryptography library.
