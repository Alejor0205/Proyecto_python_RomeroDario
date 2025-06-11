import random #Se importa libreria para el numero ramdon
import json #archivos json
import os #Verificacion de archivos
from tabulate import tabulate 

archvioJson = 'historial.json'
digitosTicket= 6
rango = 50

def limpiarConsola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def generoTicket():
    ticket = set() # evitar duplicados
    print(f'ingrese los {digitosTicket} nuermos unicos entre 1 y {rango}:')
    while len(ticket) < digitosTicket:
        try:
            numero= int(input(f'Numero {len(ticket)+1}:')) # funcion para pedir numeros ordenados empezando de Numero 1 en posicion 0
            if numero > 0 and numero < rango:
                ticket.add(numero)
            elif numero in ticket:
                print('Numero repetido')
            else:
                print('Numero invalido')
        except ValueError:
            print('Ingresa solo numeros')
    return sorted(ticket)    # retorna de una forma ordenada

def generoTicketAuto():
            
    return sorted(random.sample(range(1,rango),digitosTicket)) #sample hace que los numeros sean unicos sin repetirse

def numeroGanador():    
    
    numGanador = sorted(random.sample(range(1, rango),digitosTicket))
    return numGanador

def premiacion(acierto):
    premios = {
        'Tres cifras':'Premio pequeño',
        'Cuatro cifras':'Premio medianooo',
        'Cinco cifras':'Premio grandeeeeeee',
        'Seis cifras':'Premio mayooooooooooor!'
    }
    return premios.get(acierto,'Pailaaaa, no tienes premios') #buscador de cual es el premio 

def numerosCaidos(tickets, winners ):
    resultados=[]
    coincidenciasPos = 0
    for ticket in tickets:
        coincidenciasPos = sum(1 for i in range(len(ticket)) if ticket[i] == winners[i])
        cuantosCaidos = len(set(ticket) & set(winners))
        resultados.append((ticket, cuantosCaidos,coincidenciasPos, premiacion(cuantosCaidos)))
    return resultados

def hitorialJuegos(result, winners):
    datos={
        'ganadores':winners,
        'reesultados': result
    }
    historial=[]
    if os.path.exists(archvioJson): # el archivo no puede no existir
        with open (archvioJson, 'r') as file: # leer json 
            try: 
                historial = json.load(file)
            except json.JSONDecodeError:
                historial=[]
    historial.append(datos)
    with open(archvioJson, 'w') as file:  #escribir el historial de los ganadores
        json.dump(historial,file,indent=3) 

def historial():
    if not os.path.exists(archvioJson):
        print ("No hay historial")
        return
    with open (archvioJson,'r') as file:
        historial = json.load(file)
    for i, juego in enumerate(historial,1):
        print(f'Juego numero {i}')
        print(f'Los numeros ganadores: {juego["ganadores"]}')
        tabla = []
        for ticket, premio, acierto in juego['resultados']:
            tabla.append([ticket,acierto,premio])
        print(tabulate(tabla, headers=['Ticket','numeros iguales','Aciertos','Premio'], tablefmt='fancy_grid'))

def estadisticas(estadistica):
    
    tabla=[]
    for frecuencia, acierto in sorted(estadistica.items()):
        premio = premiacion(acierto)
        tabla.append([acierto,frecuencia,premio])
    print()
    print("Las estaditicas de la simulacion son:")
    print()
    print(tabulate(tabla,headers=['Acierto','Frecuencia','Premio'],tablefmt='fancy_grid'))

def simularJuegos(juegos):
     estadistica = {i: 0 for i in range(7)}
     for i in range(juegos):
         ticket = generoTicketAuto()
         winner= numeroGanador()
         acierto = numerosCaidos(ticket,winner)
         estadistica [acierto] +=1
     estadisticas(estadistica)
def salir():
    print('Fue u placer parceroo hasta luego')
    

def menu():
    while True:
        
        print('''

             =======loteria don alejoooo========
             1. Compra boleto
             2. Compra boleto automatico
             3. Ver el historial de los juegos
             4. simular múltiples juegos automáticos
             5. jugar 
             6. salir  
              ''')
        opcion = input('Ingrese la opcion que desea\n')
         
        if opcion =='1':
            limpiarConsola()  
            try:
                ticket= generoTicket()
                winners = numeroGanador()
                resultados= numerosCaidos([ticket], winners)
                hitorialJuegos(resultados,winners)
                print(f'\n Numeros ganadores: {winners}')
                print(tabulate([[j[0],j[1],j[2],j[3]] for j in resultados], headers=['Ticket','numeros iguales','Aciertos','Premio'], tablefmt= 'fancy_grid' ))
            
            except Exception as a:
                print(f'Error en el boleto {a}')
        elif opcion =='2':
            limpiarConsola()  
            try:
                cantidadTicket=int(input('Cuantos boletos automaticos desea comprar?\n'))
                ticket= [generoTicketAuto() for _ in range (cantidadTicket)]
                winners = numeroGanador()
                resultados= numerosCaidos(ticket, winners)
                hitorialJuegos(resultados,winners)
                print(f'\n Numeros ganadores: {winners}')
                print(tabulate([[j[0],j[1],j[2],j[3]] for j in resultados], headers=['Ticket','numeros iguales','Aciertos','Premio'], tablefmt= 'fancy_grid' )) 
            except ValueError:
                print('Errorcito los datos no son validos, digite bien cuantos boletos')
            except Exception as a:
                print(f'Errorcito en los boletos automaticos{a}') 
                
             

        elif opcion == '3':
            limpiarConsola()  
            historial()
            

        elif opcion == '4':
            limpiarConsola()  
            try:
                simulaciones = int(input('Cuantas simulaciones quieres hacer\n')) 
                simularJuegos(simulaciones)
            except ValueError:
                print('Errorcito digite bien las simulaciones')
            except Exception as a:
                print('Errorcito en la simulacion {e}')

        elif opcion== '5':
            limpiarConsola()  
            try:
                tipo = input('Quieres elegir los numeros del ticket tu? (si/no)\n').strip().lower()
               
                tickets=[]
                if tipo =="si" or tipo=="no":
                    if tipo == 'si': 
                        cuantosTicket= int(input('Cuantos boletos desea comprar?\n'))         
                        if cuantosTicket <1:
                            print('Debes compra al menos uno parcerooo')
                            continue
                        for i in range(cuantosTicket):
                         print(f'\n Ticket {i+1}:')
                        tickets.append(generoTicket())
                        winners = numeroGanador()
                        resultados= numerosCaidos(tickets, winners)
                        hitorialJuegos(resultados,winners)
                        print(f'\n Numeros ganadores: {winners}')
                        print(tabulate([[j[0],j[1],j[2]] for j in resultados], headers=['Ticket','Aciertos','Premio'], tablefmt= 'fancy_grid' ))
                    elif tipo == 'no':
                        cuantosTicket= int(input('Cuantos boletos desea comprar?\n'))         
                        if cuantosTicket <1:
                            print('Debes compra al menos uno parcerooo')
                            continue
                        tickets = [generoTicketAuto() for _ in range(cuantosTicket)]
                        winners = numeroGanador()
                        resultados= numerosCaidos(tickets, winners)
                        hitorialJuegos(resultados,winners)
                        print(f'\n Numeros ganadores: {winners}')
                        print(tabulate([[j[0],j[1],j[2]] for j in resultados], headers=['Ticket','Aciertos','Premio'], tablefmt= 'fancy_grid' ))
                else:
                    print("no pusiste ni 'si', ni 'no', ponlo bien pa")
            except ValueError:
                print('Errorcito algun de los datos que pusite estan mal parcerooo/a')
            except Exception as a:
                print('Errorcito al jugar {a}')

        elif opcion == '6':    
            limpiarConsola()  
            salir()
            break

        else:
            print('La opcion no es la correctaaaa')

if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        print("Programa Interrumpido por el usuario")
    except Exception as a:
        print(f'Error inesperado {a}')
