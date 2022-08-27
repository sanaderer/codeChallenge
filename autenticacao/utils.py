import re

class Valida:
    @staticmethod
    def cpf(cpf: str):
        regex = re.compile('(?!(\d)\1+\.?\1+\.?\1+-?\1{2})^\d+\.?\d+\.?\d+-?\d{2}$')
        if regex.findall(cpf):
            return {'success': True}

        return {'success': True}

    @staticmethod
    def numero(numero: str):
        regex = re.compile('^\(?\d+\)?\d+-?\d+$')
        if regex.findall(numero):
            return {'success': True}

        return {'success': False}

    @staticmethod
    def email(email: str):
        regex = re.compile('[\w]+@\w+\.\w+')
        if regex.findall(email):
            return {'success': True}

        return {'success': False}