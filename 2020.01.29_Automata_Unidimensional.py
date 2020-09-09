# -*- coding: utf-8 -*-
"""

@author: Fernan Alonso Villa

Los autómatas celulares (AC) son sistemas computacionales abstractos discretos
que han sido útiles tanto como modelos generales de complejidad 
como representaciones más específicas de dinámicas no lineales. Son aplicados 
en una gran variedad de campos científicos, como:
    - Analizadores sintácticos y semánticos
    - Motores de cómputo
    - Simuladores de sistemas de cómputo discretos
    - Modelos conceptuales para estudiar la formación de patrones y la complejidad
    - Como modelos originales de física fundamental.
    - Representación Fractal

 Para Más detalles de los AC consultar: 
     https://plato.stanford.edu/entries/cellular-automata/

Los AC son habitualmente espaciales y temporalmente discretos. Están compuestos
 por un conjunto finito o numerable de unidades simples y homogéneas,
 tradicionalmente llamados átomos, células o celdas. En cada unidad de tiempo, 
 las celdas crean una instancia de un conjunto finito de estados. 
 
Los AC Evolucionan en paralelo en pasos de tiempo discretos,  siguiendo las 
 funciones de actualización de estado o reglas de transición 
 dinámicas. La actualización de un estado de celda se obtiene tomando en 
 cuenta los estados  de las celdas en su vecindario local; entonces, no hay 
 acciones a distancia!.
 
Los AC son abstractos, es decir, pueden especificarse en términos puramente 
 matemáticos e implementarse en estructuras físicas. 

Además, los AC son sistemas computacionales, considerando que pueden calcular 
 funciones y resolver problemas algorítmicos. A pesar de funcionar de manera 
 diferente a los dispositivos tradicionales de tipo máquina de Turing,
 CA con reglas adecuadas puede emular una máquina universal de Turing y,
 por lo tanto, procesar, dada la Tesis de Turing, cualquier cosa computable.
 
 Para más detalles de Máquinas de Turing consultar:
     https://en.wikipedia.org/wiki/Turing_machine

"""
def automata_celular():
    '''
    Implementación de un Autómata Celular UNIDIMENSIONAL, aplica una regla
    al estado inicial de un sistema de 32 celulas e imprime su evolución
    
    Estado Inicial, también conocido como clase inicial: 
        La lista denominada 'sistema' representa el estado del 
        sistema de 32 celdas (átomos o células) en esta Lista Verdadero es 1 (^) y 
        Falso es 0 (_)
    
    La regla de transformación: El estado de la celda actual es Verdadero (^)
    si y sólo si el estado del la celda izquierda o derecha del renglón 
    anterior es Verdadero (^) nunca ambos, en otro caso el estado de la 
    celda es Falso (_).
    Por ejemplo, 
        - 010 produce 101
        - 100 produce 010
        - 001 produce 010
        - 011 produce 111
        - 111 produce 101
        
    Esta es conocida como la 'Hat Rule', para más detalle
    sobre esta regla consultar https://plato.stanford.edu/entries/cellular-automata/
    
    Existen otras reglas famosas:
        https://en.wikipedia.org/wiki/Rule_110
        https://en.wikipedia.org/wiki/Rule_30
        https://en.wikipedia.org/wiki/Rule_90
    
    La siguiente es la evolución de la regla en cada paso, con base en el patrón
    inicial. Este es el patrón evolutivo resultante de la regla.
    
    Paso 00: ________________^_______________
    Paso 01: _______________^_^______________
    Paso 02: ______________^___^_____________
    Paso 03: _____________^_^_^_^____________
    Paso 04: ____________^_______^___________
    Paso 05: ___________^_^_____^_^__________
    Paso 06: __________^___^___^___^_________
    Paso 07: _________^_^_^_^_^_^_^_^________
    Paso 08: ________^_______________^_______
    Paso 09: _______^_^_____________^_^______
    Paso 10: ______^___^___________^___^_____
    Paso 11: _____^_^_^_^_________^_^_^_^____
    Paso 12: ____^_______^_______^_______^___
    Paso 13: ___^_^_____^_^_____^_^_____^_^__
    Paso 14: __^___^___^___^___^___^___^___^_
    Paso 15: _^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^
    
    Nótese que en el patrón inicial solo hay un Verdadero en la posición 17
    '''
    sistema = [ 0,0,0,0,0,0,0,0,0,0, 
            0,0,0,0,0,0,1,0,0,0,
            0,0,0,0,0,0,0,0,0,0, 0,0]
    

    '''
        diccionariocionario para mapear los valores de las celdas a símbolos
    '''
    diccionario = {0:'_', 1:'^'}

    '''
        Se imprime la primera línea, o paso = 0
        Nótese como en una sola línea se usa el diccionario aplicado al sistema
                diccionario[e] for e in sistema_nuevo
        Luego entre [] se arma esta lista así
                [diccionario[e] for e in sistema_nuevo]
        Con la función join se concatenan los elementos de la lista
                ''.join([])
        '' esto evita tener que crear una variable para acceder a las funciones
        de tipo texto
        
    '''
    print(''.join( [diccionario[e] for e in sistema]))
    
    '''
        Ahora los siguientes 15 pasos. Ver que paso es menor que 16
    '''
    paso = 1
    while(paso < 16):
        sistema_nuevo = []
        '''
            Se itera entre la posición 0 y la 32 y almacena el estado de la 
            celda actual en la lista de sistema_nuevo
        '''
        for i in range(0,32):
            '''
                Para la celda correspondiente, verifica el estado de los 
                vecinos
            '''
            if i > 0 and i < 31:
                if sistema[i-1] == sistema[i+1]:
                    sistema_nuevo.append(0)
                else:
                    sistema_nuevo.append(1)

            # Para el caso del primer elemento
            elif(i == 0):
                if sistema[1] == 1:
                    sistema_nuevo.append(1)
                else:
                    sistema_nuevo.append(0)

            # Para el caso del último elemento
            elif(i == 31):
                if sistema[30] == 1:
                    sistema_nuevo.append(1)
                else:
                    sistema_nuevo.append(0)

        '''
            Se actualizan los estados del sistema
            [:] tomar todos los elementos de la lista, sin esto funciona igual
        '''
        sistema = sistema_nuevo[:]
        
        '''
            Se imprime el estado actualizado del sistema
        '''
        print  (''.join( [diccionario[e] for e in sistema]))

        # incrementa el paso o iterador
        paso += 1

    
'''
    Función Principal
'''
if __name__ == '__main__':
    automata_celular()