Sender
1. hash document
2. encrypt hash with private key
3. Pair document with signature and public key
4. Send

Receiver
1. Get sender public key from CA certificate.
2. Use sender public key to decrypt signature into the expected file hash
4. Compare the expected and resulting hashes.
5. Success if match.

__This works only because of trust in CAs__ \
https://en.wikipedia.org/wiki/Certificate_authority \
__CA compromise__ \
See also: Supply chain attack



