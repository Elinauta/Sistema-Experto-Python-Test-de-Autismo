from experta import *
import os
import time
borrarPantalla = lambda: os.system ("cls")
#------------------------------------------------------------
class InteresesObsesivos(Fact):
    """ Leyendo tus sintomas """   
class RespuestaSentimientos(Fact):
    """ Leyendo tus sintomas """
class ActSolitarias(Fact):
    """ Leyendo tus sintomas """   
class Rutinas(Fact):
    """ Leyendo tus sintomas """
class ResistenciaCambios(Fact):
    """ Leyendo tus sintomas """
class ContactoCorp(Fact):
    """ Leyendo tus sintomas """
class Torpeza(Fact):
    """ Leyendo tus sintomas """
class EntonacionRasa(Fact):
    """ Leyendo tus sintomas """
#-------------Rasgos(8) de autismo leve--------------------
class ImitacionSocial(Fact):
    """ Leyendo tus sintomas """
class EntenderGestos(Fact):
    """ Leyendo tus sintomas """
class Hipersensibilidad(Fact):
    """ Leyendo tus sintomas """
class Entorno(Fact):
    """ Leyendo tus sintomas """
class InvacionEspacio(Fact):
    """ Leyendo tus sintomas """
#--------------Rasgos(5) de autismo moderado----------------
class LenguajeHablado(Fact):
    """ Leyendo tus sintomas """  
class RespuestaNombre(Fact):
    """ Leyendo tus sintomas """
class RepiteFrases(Fact):
    """ Leyendo tus sintomas """   
class ComunicacionNoVerbal(Fact):
    """ Leyendo tus sintomas """
class DesinteresTerceros(Fact):
    """ Leyendo tus sintomas """
class Mirada(Fact):
    """ Leyendo tus sintomas """
class RespuestaDolor(Fact):
    """ Leyendo tus sintomas """
class MovExtranos(Fact):
    """ Leyendo tus sintomas """
class PercepcionPeligro(Fact):
    """ Leyendo tus sintomas """
class Rabietas(Fact):
    """ Leyendo tus sintomas """
#------------------Rasgos(10) de autismo alto---------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------

class AUTISMO(KnowledgeEngine):
  contador=0 #para respuestas positivas
  contador2=0 #para respuestas negativas
#------------------------------------------------------------------rasgos para autismo leve----------------------------------------------------------------
#Rasgo1---------------------------------------------------------------------------------------------------------------------------------------------------
  @Rule(InteresesObsesivos(intereses_obesisvos = '1'))           
  def autismoLeve1(self):
    self.contador=self.contador + 1
    self.declare(RespuestaSentimientos(respuesta_sentimientos = input("Escaso reconocimiento o respuesta a los sentimientos  \n1) Si \n2) No \n ")))
    print()     
  @Rule(InteresesObsesivos(intereses_obesisvos = '2'))              
  def Neurotipico1(self):
    self.contador2=self.contador2 + 1
    self.declare(RespuestaSentimientos(respuesta_sentimientos = input("Escaso reconocimiento o respuesta a los sentimientos  \n1) Si \n2) No \n ")))
    print()            
#Rasgo2--------------------------------------------------------------------------------------------------------------------------------------------------
  @Rule(RespuestaSentimientos(respuesta_sentimientos = '1'))  
  def autismoLeve2(self):
    self.contador=self.contador + 1
    self.declare(ActSolitarias(act_solitarias = input("Prefiere actividades solitarias  \n1) Si \n2) No \n ")))
    print()    
  @Rule(RespuestaSentimientos(respuesta_sentimientos = '2'))  
  def Neurotipico2(self):
    self.contador2=self.contador2 + 1
    self.declare(ActSolitarias(act_solitarias = input("Prefiere actividades solitarias  \n1) Si \n2) No \n ")))
    print()  
#Rasgo3---------------------------------------------------------------------------------------------------------
  @Rule(ActSolitarias(act_solitarias = '1'))  
  def autismoLeve3(self):
    self.contador=self.contador + 1
    self.declare(Rutinas(rutinas = input("Insistencia en rutinas y rituales  \n1) Si \n2) No \n ")))
    print() 
  @Rule(ActSolitarias(act_solitarias = '2'))  
  def Neurotipico3(self):
    self.contador2=self.contador2 + 1
    self.declare(Rutinas(rutinas = input("Insistencia en rutinas y rituales  \n1) Si \n2) No \n ")))
    print() 
#Rasgo4----------------------------------------------------------------------------------------------------------
  @Rule(Rutinas(rutinas = '1'))  
  def autismoLeve4(self):
    self.contador=self.contador + 1
    self.declare(ContactoCorp(contacto_corp = input("Evitan el contacto corporal  \n1) Si \n2) No \n ")))
    print() 
  @Rule(Rutinas(rutinas = '2'))  
  def Neurotipico4(self):
    self.contador2=self.contador2 + 1
    self.declare(ContactoCorp(contacto_corp = input("Evitan el contacto corporal  \n1) Si \n2) No \n ")))
    print() 
#Rasgo5----------------------------------------------------------------------------------------------------------
  @Rule(ContactoCorp(contacto_corp = '1'))  
  def autismoLeve5(self):
    self.contador=self.contador + 1
    self.declare(Torpeza(torpeza = input("Exhibe torpeza o falta de destreza  \n1) Si \n2) No \n ")))
    print() 
  @Rule(ContactoCorp(contacto_corp = '2'))  
  def Neurotipico5(self):
    self.contador2=self.contador2 + 1
    self.declare(Torpeza(torpeza = input("Exhibe torpeza o falta de destreza  \n1) Si \n2) No \n ")))
    print() 
#Rasgo6----------------------------------------------------------------------------------------------------------
  @Rule(Torpeza(torpeza = '1'))  
  def autismoLeve6(self):
    self.contador=self.contador + 1
    self.declare(EntonacionRasa(entonacion = input("Entonacion anormal  \n1) Si \n2) No \n ")))
    print() 
  @Rule(Torpeza(torpeza = '2'))  
  def Neurotipico6(self):
    self.contador2=self.contador2 + 1
    self.declare(EntonacionRasa(entonacion= input("Entonacion anormal  \n1) Si \n2) No \n ")))
    print() 
#Rasgo7----------------------------------------------------------------------------------------------------------
  @Rule(EntonacionRasa(entonacion = '1'))  
  def autismoLeve7(self):
    self.contador=self.contador + 1
    self.declare(ResistenciaCambios(cambios = input("Resistencia a los cambios  \n1) Si \n2) No \n ")))
    print() 
  @Rule(EntonacionRasa(entonacion = '2'))  
  def Neurotipico7(self):
    self.contador2=self.contador2 + 1
    self.declare(ResistenciaCambios(cambios = input("Resistencia a los cambios  \n1) Si \n2) No \n ")))
    print()     
#Rasgo8----------------------------------------------------------------------------------------------------------
  @Rule(ResistenciaCambios(cambios = '1'))  
  def autismoLeve8(self):
    self.contador=self.contador + 1
    if(self.contador > self.contador2):   
      self.declare(ImitacionSocial(imitacion_social = input("Ausencia de juegos de representación o imitación de algun personaje  \n1) Si \n2) No \n ")))
      print()
    else:
      borrarPantalla()
      print("No se muestran razgos de autismo en tus resultados.")
      print("Te recomendamos igualmente consultar con un especialista para descartalo al 100%")
      time.sleep(3)
      input("Presiona ENTER para salir...")            
  @Rule(ResistenciaCambios(cambios = '2'))  
  def Neurotipico8(self):
    self.contador2=self.contador2 + 1
    if(self.contador >= self.contador2):   
      self.declare(ImitacionSocial(imitacion_social = input("Ausencia de juegos de representación o imitación de algun personaje  \n1) Si \n2) No \n ")))
    else:
      borrarPantalla()
      print("No se muestran razgos de autismo en tus resultados.")
      print("Te recomendamos igualmente consultar con un especialista para descartalo al 100%")
      time.sleep(3)
      input("Presiona ENTER para salir...")  
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------rasgos para autismo moderado-----------------------------------------------------------------------------
#Rasgo9--------------------------------------------------------------------------------------------------------------------------------------------------------
  @Rule(ImitacionSocial(imitacion_social = '1'))              
  def autismoModerado1(self):
    self.contador=self.contador + 2
    self.declare(EntenderGestos(entender_gestos = input("Dificultad para entender gestos, complicidades o palabras  \n1) Si \n2) No \n ")))
    print()     
  @Rule(ImitacionSocial(imitacion_social = '2'))              
  def autismoLeve9(self):
    self.contador2=self.contador2 + 2
    self.declare(EntenderGestos(entender_gestos = input("Dificultad para entender gestos, complicidades o palabras  \n1) Si \n2) No \n ")))
    print()    
#Rasgo10-----------------------------------------------------------------------------------------------------------------------------------------
  @Rule(EntenderGestos(entender_gestos = '1'))              
  def autismoModerado2(self):
    self.contador=self.contador + 2
    self.declare(Hipersensibilidad(hiper_sensibilidad = input("Hipersensibilidad a los sonidos, tacto y ciertas texturas  \n1) Si \n2) No \n ")))
    print()           
  @Rule(EntenderGestos(entender_gestos = '2'))              
  def autismoLeve10(self):
    self.contador2=self.contador2 + 2
    self.declare(Hipersensibilidad(hiper_sensibilidad = input("Hipersensibilidad a los sonidos, tacto y ciertas texturas  \n1) Si \n2) No \n ")))
    print()   
#Rasgo11-----------------------------------------------------------------------------------------------------------------------------------------
  @Rule(Hipersensibilidad(hiper_sensibilidad = '1'))              
  def autismoModerado3(self):
    self.contador=self.contador + 2
    self.declare(Entorno(entorno = input("No reacciona ante lo que ocurre a su alrededor  \n1) Si \n2) No \n ")))
    print()       
  @Rule(Hipersensibilidad(hiper_sensibilidad = '2'))              
  def autismoLeve11(self):
    self.contador2=self.contador2 + 2
    self.declare(Entorno(entorno = input("No reacciona ante lo que ocurre a su alrededor  \n1) Si \n2) No \n ")))
    print()   
#Rasgo12------------------------------------------------------------------------------------------------------------------------------------------
  @Rule(Entorno(entorno = '1'))              
  def autismoModerado4(self):
    self.contador=self.contador + 2
    self.declare(InvacionEspacio(invasion_espacio = input("Tiene reacciones extremas ante la invasión de su espacio  \n1) Si \n2) No \n ")))
    print()   
  @Rule(Entorno(entorno = '2'))              
  def autismoLeve12(self):
    self.contador2=self.contador2 + 2
    self.declare(InvacionEspacio(invasion_espacio = input("Tiene reacciones extremas ante la invasión de su espacio  \n1) Si \n2) No \n ")))
    print()   
#Rasgo13----------------------------------------------------------------------------------------------------------------------------------------
  @Rule(InvacionEspacio(invasion_espacio = '1'))              
  def autismoModerado5(self):
    self.contador=self.contador + 2
    if(self.contador >= self.contador2):   
      self.declare(LenguajeHablado(lenguaje_hablado = input("Tiene un desarrollo deficiente del lenguaje hablado \n1) Si \n2) No \n ")))
    else:   
      borrarPantalla()          
      print("De acuerdo con las respuestas obtenidas el niño/adolescente prestenta:")
      print("Transtorno del espectro autista de nivel LEVE")
      print("\nEl puntaje final fue de ",self.contador)
      print("\n\n                 ----------------TRATAMIENTO---------------                           ")
      print("Te recomendamos hacer un diagnostico a prfundidad, \nya que al presentar un nivel de autismo leve pueden pasar desapercibidos varios rasgos \nque definan si el niño/adolescente se encuentra dentro del espectro autista, como lo es el Asperger.")
      time.sleep(3)
      input("\nPresiona para salir...")      
  @Rule(InvacionEspacio(invasion_espacio = '2'))              
  def autismoLeve13(self):
    self.contador2=self.contador2 + 2
    if(self.contador >= self.contador2):   
      self.declare(LenguajeHablado(lenguaje_hablado = input("Tiene un desarrollo deficiente del lenguaje hablado \n1) Si \n2) No \n ")))
    else:
      borrarPantalla()          
      print("De acuerdo con las respuestas obtenidas el niño/adolescente prestenta:")
      print("Transtorno del espectro autista de nivel LEVE")
      print("\nEl puntaje final fue de ",self.contador)
      print("\n\n                 ----------------TRATAMIENTO---------------                           ")
      print("Te recomendamos hacer un diagnostico a prfundidad, \nya que al presentar un nivel de autismo leve pueden pasar desapercibidos varios rasgos \nque definan si el niño/adolescente se encuentra dentro del espectro autista, como lo es el Asperger.")
      time.sleep(3)
      input("\nPresiona para salir...")     
#-----------------------------------------------------------------------------------------------------------------------------------------------  
#--------------------------------------------------------rasgos para autismo alto-----------------------------------------------------------
#Rasgo14-----------------------------------------------------------------------------------------------------------------------------------------
  @Rule(LenguajeHablado(lenguaje_hablado = '1'))              
  def autismoAlto1(self):
    self.contador=self.contador + 3
    self.declare(RespuestaNombre(respuesta_nombre = input("No responde cuando se le llama por su nombre \n1) Si \n2) No \n ")))
    print()
  @Rule(LenguajeHablado(lenguaje_hablado = '2'))
  def autismoModerado6(self):
    self.contador2=self.contador2 + 3
    self.declare(RespuestaNombre(respuesta_nombre = input("No responde cuando se le llama por su nombre \n1) Si \n2) No \n ")))
    print()
#Rasgo15----------------------------------------------------------------------------------------------------------------------------------
  @Rule(RespuestaNombre(respuesta_nombre = '1'))              
  def autismoAlto2(self):
    self.contador=self.contador + 3
    self.declare(RepiteFrases(repite_frases = input("Repite frases o palabras \n1) Si \n2) No \n ")))
    print()
  @Rule(RespuestaNombre(respuesta_nombre = '2'))              
  def autismoModerado7(self):
    self.contador2=self.contador2 + 3
    self.declare(RepiteFrases(repite_frases = input("Repite frases o palabras \n1) Si \n2) No \n ")))
    print()
#Rasgo16-----------------------------------------------------------------------------------------------------------------------------
  @Rule(RepiteFrases(repite_frases = '1'))              
  def autismoAlto3(self):
    self.contador=self.contador + 3
    self.declare(ComunicacionNoVerbal(cno_verbal = input("Dificultad para expresarse de manera no verbal \n1) Si \n2) No \n ")))
    print()
  @Rule(RepiteFrases(repite_frases = '2'))              
  def autismoModerado8(self):
    self.contador2=self.contador2 + 3
    self.declare(ComunicacionNoVerbal(cno_verbal = input("Dificultad para expresarse de manera no verbal \n1) Si \n2) No \n ")))
    print()
#Rasgo17----------------------------------------------------------------------------------------------------------------------------
  @Rule(ComunicacionNoVerbal(cno_verbal = '1'))              
  def autismoAlto4(self):
    self.contador=self.contador + 3
    self.declare(DesinteresTerceros(desinteres_terceros = input("No muestra interes por otras personas \n1) Si \n2) No \n ")))
    print()
  @Rule(ComunicacionNoVerbal(cno_verbal = '2'))              
  def autismoModerado9(self):
    self.contador2=self.contador2 + 3
    self.declare(DesinteresTerceros(desinteres_terceros = input("No muestra interes por otras personas \n1) Si \n2) No \n ")))
    print()  
#Rasgo18---------------------------------------------------------------------------------------------------------------------------------------------------------
  @Rule(DesinteresTerceros(desinteres_terceros = '1'))              
  def autismoAlto5(self):
    self.contador=self.contador + 3
    self.declare(Mirada(mirada = input("Escasa utilizacion social de la mirada \n1) Si \n2) No \n ")))
  @Rule(DesinteresTerceros(desinteres_terceros = '2'))              
  def autismoModerado10(self):
    self.contador2=self.contador2 + 3
    self.declare(Mirada(mirada = input("Escasa utilizacion social de la mirada \n1) Si \n2) No \n ")))
#Rasgo19---------------------------------------------------------------------------------------------------------------------------------------------------------
  @Rule(Mirada(mirada = '1'))              
  def autismoAlto6(self):
    self.contador=self.contador + 3
    self.declare(RespuestaDolor(dolor = input("Respuesta inusual al dolor \n1) Si \n2) No \n ")))
  @Rule(Mirada(mirada = '2'))              
  def autismoModerado11(self):
    self.contador2=self.contador2 + 3
    self.declare(RespuestaDolor(dolor = input("Respuesta inusual al dolor \n1) Si \n2) No \n ")))
#Rasgo20---------------------------------------------------------------------------------------------------------------------------------------------------------
  @Rule(RespuestaDolor(dolor = '1'))              
  def autismoAlto7(self):
    self.contador=self.contador + 3
    self.declare(MovExtranos(mov_extranos = input("Movimientos extraños \n1) Si \n2) No \n ")))
  @Rule(RespuestaDolor(dolor = '2'))              
  def autismoModerado12(self):
    self.contador2=self.contador2 + 3
    self.declare(MovExtranos(mov_extranos = input("Movimientos extraños \n1) Si \n2) No \n ")))
#Rasgo21---------------------------------------------------------------------------------------------------------------------------------------------------------
  @Rule(MovExtranos(mov_extranos = '1'))              
  def autismoAlto8(self):
    self.contador=self.contador + 3
    self.declare(PercepcionPeligro(peligro = input("No percibe el peligro \n1) Si \n2) No \n ")))
  @Rule(MovExtranos(mov_extranos = '2'))              
  def autismoModerado13(self):
    self.contador2=self.contador2 + 3
    self.declare(PercepcionPeligro(peligro = input("No percibe el peligro \n1) Si \n2) No \n ")))
#Rasgo22---------------------------------------------------------------------------------------------------------------------------------------------------------
  @Rule(PercepcionPeligro(peligro = '1'))              
  def autismoAlto9(self):
    self.contador=self.contador + 3
    self.declare(Rabietas(rabietas = input("Con frecuencia hay rabietas y berinches \n1) Si \n2) No \n ")))
  @Rule(PercepcionPeligro(peligro = '2'))              
  def autismoModerado14(self):
    self.contador2=self.contador2 + 3
    self.declare(Rabietas(rabietas = input("Con frecuencia hay rabietas y berinches \n1) Si \n2) No \n ")))
#Rasgo23---------------------------------------------------------------------------------------------------------------------------------------------------------
  @Rule(Rabietas(rabietas = '1'))              
  def autismoAlto10(self):
    self.contador=self.contador + 3
    if(self.contador > self.contador2):   
      borrarPantalla()  
      print("De acuerdo con las respuestas obtenidas el niño/adolescente prestenta:")
      print("Transtorno del espectro autista de nivel ALTO")
      print("\nEl puntaje final fue de",self.contador)
      print("\n\n                 ----------------TRATAMIENTO---------------                           ")
      print("Se sugiere comenzar lo mas pronto posible con:")
      print("\n --> Intervencion Psicologica")
      print("Tratar las emociones y sentimientos asociados")
      print("\n --> Habilidades sociales")
      print("Medio de sesiones de juego y actuaciones en las que el niño/adolescente participa activamente.")
      print("Comunicacion verbal y contacto visual")
      print("\n --> Comunicacion")
      print("Terapias del habla y lenguaje")
      print("\n --> Conducta")
      print("Terapias conductuales")
      print("\n --> Juegos")
      print("Los juegos educativos pueden mejorar el dia de los niños/adolescentes autistas.")
      time.sleep(3)
      input("\nPresiona ENTER para salir...")
    else:
      borrarPantalla()  
      print("De acuerdo con las respuestas obtenidas el niño/adolescente prestenta:")
      print("Transtorno del espectro autista de nivel MODERADO")
      print("\nEl puntaje final fue de",self.contador)
      print("\n\n                ----------------TRATAMIENTO---------------                           ")
      print("Se sugiere comenzar lo mas pronto posible con:")
      print("\n --> Intervencion Psicologica")
      print("Tratar las emociones y sentimientos asociados")
      print("\n --> Habilidades sociales")
      print("Medio de sesiones de juego y actuaciones en las que el niño/adolescente participa activamente.")
      print("Terapias conductuales")
      print("\n --> Juegos")
      print("Los juegos educativos pueden mejorar el dia de los niños/adolescentes autistas.")
      time.sleep(3)
      input("\nPresiona ENTER para salir...")     
  @Rule(Rabietas(rabietas = '2'))              
  def autismoModerado15(self):
    self.contador2=self.contador2 + 3
    if(self.contador > self.contador2):   
      borrarPantalla()  
      print("De acuerdo con las respuestas obtenidas el niño/adolescente prestenta:")
      print("Transtorno del espectro autista de nivel ALTO")
      print("\nEl puntaje final fue de",self.contador)
      print("\n\n                 ----------------TRATAMIENTO---------------                           ")
      print("Se sugiere comenzar lo mas pronto posible con:")
      print("\n --> Intervencion Psicologica")
      print("Tratar las emociones y sentimientos asociados")
      print("\n --> Habilidades sociales")
      print("Medio de sesiones de juego y actuaciones en las que el niño/adolescente participa activamente.")
      print("Comunicacion verbal y contacto visual")
      print("\n --> Comunicacion")
      print("Terapias del habla y lenguaje")
      print("\n --> Conducta")
      print("Terapias conductuales")
      print("\n --> Juegos")
      print("Los juegos educativos pueden mejorar el dia de los niños/adolescentes autistas.")
      time.sleep(3)
      input("\nPresiona ENTER para salir...")
    else:
      borrarPantalla()  
      print("De acuerdo con las respuestas obtenidas el niño/adolescente prestenta:")
      print("Transtorno del espectro autista de nivel MODERADO")
      print("\nEl puntaje final fue de",self.contador)
      print("\n\n                ----------------TRATAMIENTO---------------                           ")
      print("Se sugiere comenzar lo mas pronto posible con:")
      print("\n --> Intervencion Psicologica")
      print("Tratar las emociones y sentimientos asociados")
      print("\n --> Habilidades sociales")
      print("Medio de sesiones de juego y actuaciones en las que el niño/adolescente participa activamente.")
      print("Terapias conductuales")
      print("\n --> Juegos")
      print("Los juegos educativos pueden mejorar el dia de los niños/adolescentes autistas.")
      time.sleep(3)
      input("\nPresiona ENTER para salir...")           
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

engine = AUTISMO()
engine.reset()

borrarPantalla()
print("                             ---- TEST DEL ESPECTRO AUTISTA EN NIÑOS MAYORES A 3 AÑOS ----   ")
print("\n\nEl espectro del autismo abarca una gama de condiciones de desarrollo neurológico, todas ellas apuntando a la presencia de trastornos como el autismo clásico, el síndrome de Asperger o el síndrome de Rett.")
print("\nSin embargo, hay una variación considerable en el tipo y la gravedad de los síntomas.\n")
print("\nEl objetivo de este test es para el Diagnóstico y Tratamiento de Trastornos del Espectro Autista (TEA) en niños y adolescentes basado en reglas, que permita dar un diagnostico confiable y posteriormente un profesinal brinde un tratamiento que nos ayude a mejorar sus capacidades comunicativas y de interacción social.\n")
time.sleep(3)
input("\n\n\nPresiona ENTER para empezar el test...")
borrarPantalla()
print("¿En qué lugar del espectro del autismo se encuentra tu hijo?") 
print("\nPara cada una de las siguientes afirmaciones, marca (1) SI representa al niño/adolescente ó (2) cunado NO lo represente")
time.sleep(3)
pregunta1 = input("\n\nTiene intereses obsesivos  \n1) Si \n2) No \n ")
print()

engine.declare((InteresesObsesivos(intereses_obesisvos = pregunta1)))
engine.run()
