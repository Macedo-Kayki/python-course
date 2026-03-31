import re

padrao_email = re.compile(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')

def validar_email(email):
    return bool(padrao_email.match(email))

if __name__ == "__main__":
    exemplos_emails = [
        "usuario@email.com",
        "nome+tag@email.com",
        "a@b.co",
        "usuario@email.co.uk",
        "@email.com",
        "usuario@.com",
        "usuario@email",
        "usu ario@email.com",
    ]
    for email in exemplos_emails:
        if validar_email(email):
            print(f"{email} é um endereço de e-mail válido.")
        else:
            print(f"{email} não é um endereço de e-mail válido.")