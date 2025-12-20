import base64
import datetime
from typing import cast

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID

from api import get_problem, submit_solution


PROBLEM = "tales_of_ssl"
problem = get_problem(PROBLEM)

private_key = problem["private_key"]
domain = problem["required_data"]["domain"]
serial_number = int(problem["required_data"]["serial_number"], 0)
country = problem["required_data"]["country"]

countries = {"Tokelau Islands": "TK", "Cocos Islands": "CC"}


subject = issuer = x509.Name(
    [
        x509.NameAttribute(NameOID.COUNTRY_NAME, countries[country]),
        x509.NameAttribute(NameOID.COMMON_NAME, domain),
    ]
)

key = serialization.load_der_private_key(base64.b64decode(private_key), password=None)
signing_key = cast(rsa.RSAPrivateKey, key)

cert = (
    x509.CertificateBuilder()
    .public_key(signing_key.public_key())
    .subject_name(subject)
    .issuer_name(issuer)
    .serial_number(serial_number)
    .add_extension(
        x509.SubjectAlternativeName([x509.DNSName(domain)]),
        critical=False,
    )
    .not_valid_before(datetime.datetime.now(datetime.timezone.utc))
    .not_valid_after(
        datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=30)
    )
    .sign(signing_key, hashes.SHA256())
)

der_cert = cert.public_bytes(serialization.Encoding.DER)

solution = {"certificate": base64.b64encode(der_cert).decode("ascii")}
result = submit_solution(PROBLEM, solution)
print(result)
