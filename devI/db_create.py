from manage import *
import contextlib, io
from django.utils.dateparse import parse_date
from datetime import date


saida = io.StringIO()

with contextlib.redirect_stdout(saida):
    main()


from relacionamentos.models import *
 
Matricula.objects.all().delete()
Passaporte.objects.all().delete()
Aluno.objects.all().delete()
Disciplina.objects.all().delete()
Pessoa.objects.all().delete()

thiago =  Pessoa(nome='Thiago', data_nascimento=parse_date('1990-01-20'), cpf='12345678911')
lucas = Pessoa(nome='Lucas', data_nascimento=parse_date('1992-02-02'), cpf='12345678912')
leonardo = Pessoa(nome='Leonardo', data_nascimento=parse_date('1994-03-03'), cpf='12345678913')
leonidas = Pessoa(nome='Leonidas', data_nascimento=parse_date('1996-04-04'), cpf='12345678914')
miles = Pessoa(nome='Miles', data_nascimento=parse_date('1998-05-05'), cpf='12345678915')

lista_pessoas = [thiago, lucas, leonardo, leonidas, miles]

for pessoa in lista_pessoas:
    pessoa.full_clean()  
    pessoa.save()

passaporte_thiago = Passaporte(numero='A1234567', emissao=date.today(), vencimento=parse_date('2028-01-01'), pessoa=thiago)
passaporte_lucas = Passaporte(numero='B1234567', emissao=date.today(), vencimento=parse_date('2029-02-01'), pessoa=lucas)
passaporte_leonardo = Passaporte(numero='C1234567', emissao=date.today(), vencimento=parse_date('2027-03-01'), pessoa=leonardo) 
passaporte_leonidas = Passaporte(numero='D1234567', emissao=date.today(), vencimento=parse_date('2028-04-01'), pessoa=leonidas)
passaporte_miles = Passaporte(numero='E1234567', emissao=date.today(), vencimento=parse_date('2031-05-01'), pessoa=miles)

lista_passaportes = [passaporte_thiago, passaporte_lucas, passaporte_leonardo, passaporte_leonidas, passaporte_miles]

for passaporte in lista_passaportes:
    passaporte.full_clean()  
    passaporte.save()

disciplina1 = Disciplina(nome='Desenvolvimento 1',sigla='DevI',semestre=4,ementa='Berimbau') 
disciplina2 = Disciplina(nome='Desenvolvimento 2',sigla='DevII',semestre=6,ementa='Cavaquinho')
disciplina3 = Disciplina(nome='Desenvolvimento 3',sigla='Dev3',semestre=8,ementa='Pandeiro')
disciplina4 = Disciplina(nome='Desenvolvimento 4',sigla='DevIV',semestre=10,ementa='Agogô')  
disciplina5 = Disciplina(nome='Desenvolvimento 5',sigla='DevV',semestre=1,ementa='Reco-reco')

lista_disciplinas = [disciplina1, disciplina2, disciplina3, disciplina4, disciplina5]

for disciplina in lista_disciplinas:
    disciplina.full_clean()  
    disciplina.save()


aluno1 = Aluno(nome='rauls', data_nascimento=parse_date('1991-01-20'), cpf='12345678000',email='leandro@gmail.com',cod='2021000001')
aluno2 = Aluno(nome='mayas', data_nascimento=parse_date('1992-02-02'), cpf='12345678001',email='lucas@gmail.com',cod='2021000002')
aluno3 = Aluno(nome='vitor', data_nascimento=parse_date('1993-03-03'), cpf='12345678002',email='leo@gmai.com',cod='2021000003')
aluno4 = Aluno(nome='pedro', data_nascimento=parse_date('1994-04-04'), cpf='12345678003',email='leonidas@gmail.com',cod='2021000004')
aluno5 = Aluno(nome='marcia', data_nascimento=parse_date('1995-05-05'), cpf='12345678004',email='miles@gmail.com',cod='2021000005')

lista_alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]

for aluno in lista_alunos:
    aluno.full_clean()  
    aluno.save()

matricula1 = Matricula(data_matricula=parse_date('2021-01-01'),nota=8.5,frequencia=90.0,status='Aprovado',aluno=aluno1,disciplina=disciplina1)
matricula2 = Matricula(data_matricula=parse_date('2021-02-01'),nota=6.0,frequencia=20.0,status='Reprovado',aluno=aluno2,disciplina=disciplina2)
matricula3 = Matricula(data_matricula=parse_date('2021-03-01'),nota=7.0,frequencia=70.0,status='Reprovado',aluno=aluno3,disciplina=disciplina3) 
matricula4 = Matricula(data_matricula=parse_date('2021-04-01'),nota=9.0,frequencia=95.0,status='Aprovado',aluno=aluno4,disciplina=disciplina4)
matricula5 = Matricula(data_matricula=parse_date('2021-05-01'),nota=5.0,frequencia=60.0,status='Reprovado',aluno=aluno5,disciplina=disciplina5)

lista_matriculas = [matricula1, matricula2, matricula3, matricula4, matricula5]

for matricula in lista_matriculas:
    matricula.full_clean()  
    matricula.save()

