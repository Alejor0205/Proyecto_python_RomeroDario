import random #Se importa libreria para el numero ramdon
import json #archivos json
import os #Verificacion de archivos
from tabulate import tabulate 
from datetime import datetime
archvioJson = 'historial.json'
digitosTicket= 6
rango = 50

def limpiarConsola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def enterParaContinuar(mensaje: str = "Enter para continuar..."):
    input(mensaje)

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
        'Tres cifras':'Te toco algo muy suave',
        'Cuatro cifras':'Bueno ya te toco algo mas formalito',
        'Cinco cifras':'Epaaa, te toco el buenoo',
        'Seis cifras':'Ñerda papa le pegaste al gordo!'
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

def hitorialJuegos(result, winners,nombre):
    
    datos = {
        'jugador': nombre,
        'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'ganadores': winners,
        'resultados': result
    }
    historial=[]
    if os.path.exists(archvioJson): # el archivo no puede no existir
        with open (archvioJson, 'r') as file: # leer json 
            try: 
                historial = json.load(file)
            except json.JSONDecodeError:
                historial=[]
    historial.append(datos)
    with open(archvioJson, 'w',encoding= 'utf-8') as file:  #escribir el historial de los ganadores

        json.dump(historial,file,indent=3,) 

def historial():
    if not os.path.exists(archvioJson):
        print ("No hay historial")
        enterParaContinuar()
        return
    with open (archvioJson,'r', encoding= 'utf-8') as file:
        historial = json.load(file)
    for i, juego in enumerate(historial,1):
        print(f'Juego numero {i}')
        print(f'Jugador: {juego.get("jugador", "Desconocido")}')
        print(f'Fecha: {juego.get("fecha", "Desconocida")}')
        print(f'Los numeros ganadores: {juego["ganadores"]}')
        tabla = []
        for ticket, aciertos, coincidenciasPos, premio in juego['resultados']:
            tabla.append([ticket, aciertos, coincidenciasPos, premio])
        print(tabulate(tabla, headers=['Ticket','numeros iguales','Aciertos','Premio'], tablefmt='fancy_grid'))
    enterParaContinuar()

def simularJuegos(juegos):
     
     nombre= input("Indique su nombre:\n ")
     tickets = [generoTicketAuto() for i in range(juegos)]
     winner = numeroGanador()
     resultados = numerosCaidos(tickets, winner)

    # Guardar en historial
     hitorialJuegos(resultados, winner,nombre)

    # Mostrar los números ganadores
     print(f'\n📢 Números ganadores del sorteo:\n{winner}')

    # Mostrar los resultados por ticket
     print("\n📋 Resultado de los tickets simulados:")
     print(tabulate([[j[0],j[1],j[2],j[3]] for j in resultados], headers=['Ticket','numeros iguales','Aciertos','Premio'], tablefmt= 'fancy_grid' ))
     
def salir():
    print('Fue u placer parceroo hasta luego')
    

def menu():
    while True:
        limpiarConsola() 
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
                nombre= input("Indique su nombre:\n ")
                ticket= generoTicket()
                winners = numeroGanador()
                resultados= numerosCaidos([ticket], winners)
                hitorialJuegos(resultados,winners,nombre)
                print(f'\n Numeros ganadores: {winners}')
                print(tabulate([[j[0],j[1],j[2],j[3]] for j in resultados], headers=['Ticket','numeros iguales','Aciertos','Premio'], tablefmt= 'fancy_grid' ))
            
            except Exception as a:
                print(f'Error en el boleto {a}')
                enterParaContinuar()
        elif opcion =='2':
            limpiarConsola()  
            try:
                nombre= input("Indique su nombre:\n ")
                cantidadTicket=int(input('Cuantos boletos automaticos desea comprar?\n'))
                ticket= [generoTicketAuto() for i in range (cantidadTicket)]
                winners = numeroGanador()
                resultados= numerosCaidos(ticket, winners)
                hitorialJuegos(resultados,winners,nombre)
                print(f'\n Numeros ganadores: {winners}')
                print(tabulate([[j[0],j[1],j[2],j[3]] for j in resultados], headers=['Ticket','numeros iguales','Aciertos','Premio'], tablefmt= 'fancy_grid' )) 
            except ValueError:
                print('Errorcito los datos no son validos, digite bien cuantos boletos')
            except Exception as a:
                print(f'Errorcito en los boletos automaticos{a}')
            enterParaContinuar()     
                

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
                print('Errorcito en la simulacion {a}')
            enterParaContinuar()

        elif opcion== '5':
            limpiarConsola()  
            try:
                nombre= input("Indique su nombre:\n ")
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
                        hitorialJuegos(resultados,winners,nombre)
                        print(f'\n Numeros ganadores: {winners}')
                        print(tabulate([[j[0],j[1],j[2],j[3]] for j in resultados], headers=['Ticket','numeros iguales','Aciertos','Premio'], tablefmt= 'fancy_grid' ))
                    elif tipo == 'no':
                        cuantosTicket= int(input('Cuantos boletos desea comprar?\n'))         
                        if cuantosTicket <1:
                            print('Debes compra al menos uno parcerooo')
                            continue
                        tickets = [generoTicketAuto() for i in range(cuantosTicket)]
                        winners = numeroGanador()
                        resultados= numerosCaidos(tickets, winners)
                        hitorialJuegos(resultados,winners,nombre)
                        print(f'\n Numeros ganadores: {winners}')
                        print(tabulate([[j[0],j[1],j[2],j[3]] for j in resultados], headers=['Ticket','numeros iguales','Aciertos','Premio'], tablefmt= 'fancy_grid' ))
                else:
                    print("no pusiste ni 'si', ni 'no', ponlo bien pa")
            except ValueError:
                print('Errorcito alguno de los datos que pusite estan mal parcerooo/a')
            except Exception as a:
                print('Errorcito al jugar {a}')
            enterParaContinuar()
            
        elif opcion == '6':    
            limpiarConsola()  
            salir()
            break

        else:
            print('La opcion no es la correctaaaa')
            enterParaContinuar()
if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        print("Ey mani que es lo que sucede, no interrupa el proceso")
    except Exception as a:
        print(f'Un error lo tiene cualquiera pero aqui si se paso -> {a}')
