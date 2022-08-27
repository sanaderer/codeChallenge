import re

class Valida:
    @staticmethod
    def cpf(cpf: str):
        regex = re.compile(r'(?!(\d)\1+\.?\1+\.?\1+-?\1{2})^\d+\.?\d+\.?\d+-?\d{2}$')
        if regex.findall(cpf):
            return True

        return False

    @staticmethod
    def numero(numero: str):
        regex = re.compile(r'^\(?(\d+)\)?(\d+)-?(\d+)$')
        if regex.findall(numero):
            return True, regex.sub(r'(\1)\2-\3', numero)

        return False

    @staticmethod
    def email(email: str):
        regex = re.compile(r'[\w]+@\w+\.\w+')
        if regex.findall(email):
            return True

        return False

    @staticmethod
    def branco(*args):
        return not all(list(map(lambda x: x.strip(), args)))