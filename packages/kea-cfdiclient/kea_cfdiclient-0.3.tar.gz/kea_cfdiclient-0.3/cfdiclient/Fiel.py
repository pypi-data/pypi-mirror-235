import base64
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1
from Crypto.PublicKey import RSA
from cryptography.x509 import load_der_x509_certificate
from cryptography.hazmat.primitives import serialization

class Fiel:
    def __init__(self, cer_der, key_der, passphrase):
        self.__importar_cer__(cer_der)
        self.__importar_key__(key_der, passphrase)

    def __importar_cer__(self, cer_der):
        # Load the DER certificate
        self.cer = load_der_x509_certificate(cer_der)

    def __importar_key__(self, key_der, passphrase):
        try:
            # Import the private key using PKCS#8 format and the provided passphrase
            self.key = RSA.import_key(key_der, passphrase=passphrase)
        except ValueError:
            raise ValueError('Wrong key password')

    def firmar_sha1(self, texto):
        # Sign with SHA1
        h = SHA1.new(texto)
        signature = pkcs1_15.new(self.key).sign(h)
        # Convert the signature to base64
        b64_firma = base64.b64encode(signature)
        return b64_firma

    def cer_to_base64(self):
        # Serialize the certificate to DER format and convert it to base64
        cer_der = self.cer.public_bytes(encoding=serialization.Encoding.DER)
        return base64.b64encode(cer_der)

    def cer_issuer(self):
        # Extract issuer components
        components = self.cer.issuer
        # Generate the issuer string
        return u','.join(['{key}={value}'.format(key=key, value=value) for key, value in components])

    def cer_serial_number(self):
        # Get the serial number of the certificate
        serial = self.cer.serial_number
        # Convert the serial number to a string
        return str(serial)
