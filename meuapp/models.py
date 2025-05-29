from django.db import models

class Consulta(models.Model):
    cnpj = models.CharField(max_length=14, unique=True)
    razao_social = models.CharField(max_length=255)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.razao_social} - {self.cnpj}"


    class Pessoa(models.Model):
        nome = models.CharField(max_length=100)
        dt_nascimento = models.DateField()
        idade = models.IntegerField(null=True)
        email = models.EmailField(null=True)
        sexo_choices = [
            ('M', 'Masculino'),
            ('F', 'Feminino'),
            ('O', 'Outro'),
        ]
        sexo = models.CharField(max_length=1, choices=sexo_choices, null=True)
        telefone = models.CharField(max_length=15, null=True)
        cidade = models.CharField(max_length=100, null=True)
        estado = models.CharField(max_length=1, null=True)

        def __str__(self):
            return self.nome