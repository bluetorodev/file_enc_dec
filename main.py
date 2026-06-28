import os
from io import BytesIO
from cryptography.fernet import Fernet
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse

app = FastAPI(title="File Encryption API", version="1.0")

KEY_PATH = "secret.key"


def get_or_create_key(key_path=KEY_PATH):
    """Loads the key if it exists, otherwise creates a new one."""
    if os.path.exists(key_path):
        print(f"Loading existing key from {key_path}")
        with open(key_path, "rb") as key_file:
            return key_file.read()
    else:
        print(f"No key found. Generating a new key at {key_path}...")
        key = Fernet.generate_key()
        with open(key_path, "wb") as key_file:
            key_file.write(key)
        return key


# Initialize and cache the key at application startup
SECRET_KEY = get_or_create_key()
fernet = Fernet(SECRET_KEY)


@app.post("/encrypt/", summary="Encrypt an uploaded file")
async def encrypt_file(file: UploadFile = File(...)):
    try:
        # Read file contents into memory
        file_content = await file.read()

        # Encrypt data
        encrypted_content = fernet.encrypt(file_content)

        # Split the filename into name and extension (e.g., 'data' and '.txt')
        name, ext = os.path.splitext(file.filename)

        # Reconstruct as filename.enc.extension (e.g., 'data.enc.txt')
        # If there's no extension, it defaults to 'filename.enc'
        output_filename = f"{name}.enc{ext}" if ext else f"{name}.enc"

        # Stream the encrypted bytes back to the user
        return StreamingResponse(
            BytesIO(encrypted_content),
            media_type="application/octet-stream",
            headers={
                "Content-Disposition": f'attachment; filename="{output_filename}"'
            },
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Encryption failed: {str(e)}"
        )


@app.post("/decrypt/", summary="Decrypt a previously encrypted file")
async def decrypt_file(file: UploadFile = File(...)):
    try:
        # Read file contents into memory
        encrypted_content = await file.read()

        # Decrypt data
        decrypted_content = fernet.decrypt(encrypted_content)

        orig_filename = file.filename

        # Clean up `.enc` from the filename string if it's there
        # Handles cases like 'report.enc.pdf' -> 'report.pdf'
        if ".enc" in orig_filename:
            orig_filename = orig_filename.replace(".enc", "")

        # Split the cleaned filename into name and extension
        name, ext = os.path.splitext(orig_filename)

        # Reconstruct as filename.dec.extension
        output_filename = f"{name}.dec{ext}" if ext else f"{name}.dec"

        # Stream the decrypted bytes back to the user
        return StreamingResponse(
            BytesIO(decrypted_content),
            media_type="application/octet-stream",
            headers={
                "Content-Disposition": f'attachment; filename="{output_filename}"'
            },
        )
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Decryption failed. The key might be wrong or the file is corrupted.",
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)