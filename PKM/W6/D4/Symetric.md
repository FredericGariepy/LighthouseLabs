## AES 

To encrypt and decrypt a document using AES on Linux, you can use the `openssl` command-line tool. Below are the steps for encrypting and decrypting a file using AES-256-CBC mode.

### Encrypting a Document

1. **Encrypt the File**:
   Use the `openssl enc` command to encrypt the file. Replace `input.txt` with the name of your file, `output.enc` with your desired encrypted output file name, and `yourpassword` with your encryption password.

   ```bash
   openssl enc -aes-256-cbc -salt -in input.txt -out output.enc -k yourpassword
   ```

   - `-aes-256-cbc`: Specifies AES encryption in CBC mode with a 256-bit key.
   - `-salt`: Adds a salt to the encryption to improve security.
   - `-in input.txt`: Specifies the input file to be encrypted.
   - `-out output.enc`: Specifies the output file for the encrypted data.
   - `-k yourpassword`: Provides the password for encryption.

2. **Verify Encryption**:
   You can check that `output.enc` has been created.

### Decrypting a Document

1. **Decrypt the File**:
   Use the `openssl enc` command to decrypt the file. Replace `output.enc` with your encrypted file, `decrypted.txt` with your desired output file name, and `yourpassword` with your encryption password.

   ```bash
   openssl enc -d -aes-256-cbc -in output.enc -out decrypted.txt -k yourpassword
   ```

   - `-d`: Specifies decryption.
   - `-aes-256-cbc`: Specifies the AES encryption in CBC mode with a 256-bit key.
   - `-in output.enc`: Specifies the encrypted input file.
   - `-out decrypted.txt`: Specifies the output file for the decrypted data.
   - `-k yourpassword`: Provides the password for decryption.

2. **Verify Decryption**:
   Check that `decrypted.txt` matches the original `input.txt` file.

### Notes

- Ensure that `openssl` is installed on your system. You can install it using your package manager (e.g., `sudo apt-get install openssl` on Debian-based systems).
- Use a strong and secure password for encryption. In practice, you might also use a key file or other key management techniques for better security.
- The `-salt` option is recommended to enhance security, as it ensures that the same password generates different ciphertexts.
