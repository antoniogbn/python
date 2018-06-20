
#DEFINICAO DAS CLASSES
class Lampada(object):

	def __init__(self, t, p, a = False):
		self.potencia = p
		self.tecnologia = t
		self._acesa = a
		self._funcionando = True

	def __str__(self):
		saida = 'Lampada Tipo : %s  - Potencia : %s watts - Acesa : %s\n' % \
		(self.tecnologia, self.potencia, self._acesa)
		#saida = saida + super(Lampada, self).__str__()
		return saida

	#get
	@property
	def acesa(self):
		#print("Dentro do metodo acesa!")
		return self._acesa

	#set
	@acesa.setter
	def acesa(self, valor):
		#print("Dentro do metodo set de acesa!")
		if (self._funcionando):
			self._acesa = valor

class Luminaria(object):
	def __init__(self):
		self.lampadas = []
		self.acesa = False
	
	def __str__(self):
		saida = '%s \n' % \
		(self.lampadas)
		return saida

	def adicionaLampada(self, t, p, a = False):
		self.lampadas.append(Lampada( t, p, a = False))
		
	def Acende(self, acende):
		self.acesa = acende
		for x in range(len(self.lampadas)):
				self.lampadas[x].acesa = acende
				
	def Status(self):
		print ('Luminaria Acesa : %s\n' % (self.acesa))
		for x in range(len(self.lampadas)):
			print(self.lampadas[x])

#SCRIPT
#CRIA A LUMINARIA
Lumi1 = Luminaria()

print("\nNova Execucao")
print("\n*")
print("\n*")
print("\n*")
print("\n*")
#ADICIONA AS LAMPADAS A LUMINARIA
Lumi1.adicionaLampada("Led",60)
Lumi1.adicionaLampada("Led",50)
Lumi1.adicionaLampada("Fluorescente",100)
Lumi1.adicionaLampada("Fluorescente",120)

# MOSTRA STATUS DA LUMINARIA
Lumi1.Status()

# ACENDE AS LAMPADAS
print("\n*")
print("\nAcende Luminaria")
Lumi1.Acende(True)
# MOSTRA STATUS DA LUMINARIA
print("\n*")
Lumi1.Status()

# ACENDE AS LAMPADAS
print("\n*")
print("\nApaga Luminaria")
Lumi1.Acende(False)

# MOSTRA STATUS DA LUMINARIA
print("\n*")
Lumi1.Status()
