from rich import print
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario
from pessoa import Pessoa

a1 = Aluno("José", 17, "Informática", "T01")
a1.fazer_aniversario()
a1.fazer_matricula()

p1 = Professor("Samuel", 37,"Biologia", "Mestrado")
p1.fazer_aniversario()
p1.inic_aula()

f1 = Funcionario("Claudia", 28, "Secretária", "Secretaria")
f1.fazer_aniversario()
f1.bater_ponto()