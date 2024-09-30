from django.db import models

class Visitante(models.Model):
    
    STATUS_VISITANTE = [
        ('AGUARDANDO','Aguardando Autorização'),
        ('EM_VISITA', 'Em Visita'),
        ('FINALIZADO','Visita Finalizada')
    ]
    
    status =  models.CharField( verbose_name='status', max_length=10,choices=STATUS_VISITANTE, default='AGUARDANDO')
    nome_completo = models.CharField( verbose_name='Nome completo', max_length=200)
    cpf = models.CharField(verbose_name='CPF', max_length=11)
    telefone = models.CharField(verbose_name='Telefone', max_length=11)
    data_nascimento = models.DateField(verbose_name='Data de Nascimento', auto_now=False, auto_now_add=False)
    numero_casa = models.PositiveSmallIntegerField(verbose_name='Número da casa a ser visitada')
    placa_veiculo = models.CharField(verbose_name='Placa do Carro', max_length=7, blank=True, null=True)
    horario_chegada = models.DateTimeField(verbose_name='Horario de chegada na portaria', auto_now_add=True)
    horario_autorizacao = models.DateTimeField(verbose_name='Horario da autorização de entrada', auto_now_add=False, blank=True, null= True)
    horario_saida = models.DateTimeField(verbose_name='Horario de saida do condominio', auto_now_add=False, blank=True, null=True)
    morador_responsavel =  models.CharField( verbose_name='Nome do morador responsavel',max_length=200,blank=False)
    registrado_por = models.ForeignKey('porteiros.Porteiro', verbose_name='Porteiro responsavel pelo registro', on_delete=models.PROTECT)
    
    def get_horario_chegada(self):
        if self.horario_chegada:
            return self.horario_chegada
        
    def get_horario_saida(self):
        if self.horario_saida:
            return self.horario_saida
        
    def get_horario_autorizacao(self):
        if self.horario_autorizacao:
            return self.horario_autorizacao
        
    def get_morador_responsavel(self):
        if self.morador_responsavel:
            return self.morador_responsavel
        
    def get_placa_veiculo(self):
        if self.placa_veiculo:
            return self.placa_veiculo
    
    def get_cpf(self):
        if self.cpf:
            cpf = str(self.cpf)
            
            cpf_parte_um = cpf[0:3]
            cpf_parte_dois = cpf[3:6]
            cpf_parte_tres = cpf[6:9]
            cpf_parte_quatro = cpf[9:]
            
            cpf_formatado = f'{cpf_parte_um}.{cpf_parte_dois}.{cpf_parte_tres}-{cpf_parte_quatro}'
            return cpf_formatado
            
    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = 'visitante'
        
    def __str__(self):
        return self.nome_completo