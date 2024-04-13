import mysql.connector

class Cajero:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cajero"
        )

    def __del__(self):
        self.conexion.close()



    def check_numero(self):
        numero = input('Ingrese su número telefónico: ')
        if len(numero) == 10 :
            return True
            
        

        

    def check_cliente(self, dni, password):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM clientes WHERE dni = %s AND password = %s", (dni, password))
        cliente = cursor.fetchone()
        cursor.close()
        return cliente

    def check_password(self, password):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM clientes WHERE password = %s LIMIT 1", (password,))
        cliente = cursor.fetchone()
        cursor.close()
        return cliente

    def search_saldo(self, cliente_id):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT saldo FROM clientes WHERE id = %s", (cliente_id,))
        saldo = cursor.fetchone()[0]
        cursor.close()
        return saldo
    
    def update_saldo(self, cliente_id, nuevo_saldo):
        cursor = self.conexion.cursor()
        cursor.execute("UPDATE clientes SET saldo = %s WHERE id = %s", (nuevo_saldo, cliente_id))
        self.conexion.commit()
        cursor.close()

    def update_saldo_tarjeta(self, cliente_id, nuevo_saldo):
        cursor = self.conexion.cursor()
        cursor.execute("UPDATE clientes SET creditcard_saldo = %s WHERE id = %s", (nuevo_saldo, cliente_id))
        self.conexion.commit()
        cursor.close()

    def search_saldo_tarjeta(self, cliente_id):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT creditcard_saldo FROM clientes WHERE id = %s", (cliente_id,))
        saldo = cursor.fetchone()[0]
        cursor.close()
        return saldo
    
    def avances(self, valor, cliente_id):
        cursor = self.conexion.cursor()
        cursor.execute("UPDATE clientes SET creditcard_saldo = creditcard_saldo - %s WHERE id = %s", (valor, cliente_id))
        cursor.execute("UPDATE clientes SET saldo = saldo + %s WHERE id = %s", (valor, cliente_id))
        self.conexion.commit()
        cursor.close()

    def transfer(self, valor, cliente_id):
        cursor = self.conexion.cursor()
        cursor.execute("UPDATE clientes SET saldo_tarjeta = saldo_tarjeta - %s WHERE id = %s", (valor, cliente_id))
        cursor.execute("UPDATE clientes SET saldo = saldo + %s WHERE id = %s", (valor, cliente_id))
        self.conexion.commit()
        cursor.close()

    def retiros(self, cliente_id):
        saldo_actual = self.search_saldo_tarjeta(cliente_id)
        print("Su saldo actual tarjeta es:", saldo_actual)
        print("\nSeleccione el monto:")
        print("1. 20.000")
        print("2. 50.000")
        print("3. 100.000")
        print("4. 200.000")
        print("5. 500.000")
        print("6. 300.000")
        print("7. 1.000.000")
        print('8. valor personalizado')

        opc_monto = int(input('Seleccione el monto a retirar: '))
        monto_dis = {
                    1: 20000,
                    2: 50000,
                    3: 100000,
                    4: 200000,
                    5: 500000,
                    6: 300000,
                    7: 1000000
                }

        if opc_monto in monto_dis:
            monto = monto_dis[opc_monto]
            password = input("Ingrese la password con la cual inicio sesión: ")
            cliente = self.check_password(password)

            if cliente:
                if saldo_actual >= monto:
                    nuevo_saldo = saldo_actual - monto
                    self.update_saldo_tarjeta(cliente_id, nuevo_saldo)
                    print('Retiro exitoso. Nuevo saldo:', nuevo_saldo)
                else:
                    print("Saldo insuficiente. Su saldo actual es:", saldo_actual)
            else:
                print('password incorrecta')
        elif opc_monto == 8:
            monto_personalizado = int(input('Ingrese el monto a retirar: '))

            if monto_personalizado % 10000 == 0 and monto_personalizado > 0:
                password = input("Ingrese la password con la cual inicio sesión: ")
                cliente = self.check_password(password)  # Corregido aquí
                if cliente: 
                    if saldo_actual >= monto_personalizado:
                        nuevo_saldo = saldo_actual - monto_personalizado
                        self.update_saldo_tarjeta(cliente_id, nuevo_saldo)
                        print('Retiro exitoso. Nuevo saldo:', nuevo_saldo)
                    else:
                        print("Saldo insuficiente. Su saldo actual es:", saldo_actual)
                else:
                    print('password incorrecta')
            else:
                print("error debe ser mayor a 10k")
        else:
            print("Opción inválida")

    def servicios(self, cliente_id):

       
        
            print('Elige el método de pago')
            print('1. Saldo')
            print('2. Salir')

            opces = {
                1: 'saldo',
                2: 'salir'     
            }
            opc_elegida = int(input('ingresa : '))
            if opc_elegida in opces:
                if opces[opc_elegida] == 'saldo':
                    saldo_actual = self.search_saldo(cliente_id)
                    monto = int(input('Ingrese el valor a pagar: '))
                    password = input("Ingrese la password con la cual inició sesión: ")
                    cliente = self.check_password(password)
                    if cliente:
                        if saldo_actual >= monto:
                            nuevo_saldo = saldo_actual - monto
                            self.update_saldo(cliente_id, nuevo_saldo)
                            print('El servicio ha sido pagado, su saldo es de: ', nuevo_saldo)
                        else:
                            print("Saldo insuficiente. Su saldo actual es:", saldo_actual)
                    else:
                        print('password incorrecta')        
        
     
            

    




    def retiros2(self, cliente_id):
       # if self.msj("nequi"):
            
            if self.check_numero()  :
                
                
                
                print("\nSeleccione el monto:")
                print("1. 20.000")
                print("2. 50.000")
                print("3. 100.000")
                print("4. 200.000")
                print("5. 500.000")
                print("6. 300.000")
                print("7. 1.000.000")
                print('8. valor personalizado')

                opc_monto = int(input('Seleccione el monto a retirar: '))
                monto_dis = {
                    1: 20000,
                    2: 50000,
                    3: 100000,
                    4: 200000,
                    5: 500000,
                    6: 300000,
                    7: 1000000
                }

                if opc_monto in monto_dis:
                    monto = monto_dis[opc_monto]
                 
                    print('\nIngrese el codigo de 6 digitos: ')
                   
                    retirar_codigo = input('Ingrese el código: ')
                    if len(retirar_codigo) == 6:
                        saldo_actual = self.search_saldo(cliente_id)
                        if saldo_actual >= monto:
                            nuevo_saldo = saldo_actual - monto
                            self.update_saldo(cliente_id, nuevo_saldo)
                            print('Retiro exitoso. Nuevo saldo:', nuevo_saldo)
                        else:
                            print("Saldo insuficiente")
                    else:
                        print('Código inválido')
                elif opc_monto == 8:
                    monto_personalizado = int(input('Ingrese el monto a retirar: '))
                    if monto_personalizado % 10000 == 0 and monto_personalizado > 0:
                       
                        print('\nIngrese el codigo de 6 digitos: ')
                  
                        retirar_codigo = input('Ingrese el código: ')
                        if len(retirar_codigo) == 6:
                            saldo_actual = self.search_saldo(cliente_id)
                            if saldo_actual >= monto_personalizado:
                                nuevo_saldo = saldo_actual - monto_personalizado
                                self.update_saldo(cliente_id, nuevo_saldo)
                                print('Retiro exitoso. Nuevo saldo:', nuevo_saldo)
                            else:
                                print("Saldo insuficiente")
                        else:
                            print('Código inválido')
                    else:
                        print("error debe ser mayor a 10k")
                else:
                    print("Opción inválida")
            else:
                print('Número inválido')

    def retirar_efectivo(self, cliente_id):
        print("\nSeleccione el tipo de cuenta:")
        print("1. Cuenta de ahorros")
        print("2. Cuenta corriente")
        print("3. Nequi")
        print("4. Bancolombia a la mano")
        tipo_account = int(input("Seleccione el tipo de cuenta: "))
        if tipo_account == 1:
            self.retiros(cliente_id)
        elif tipo_account == 2:
            self.retiros(cliente_id)
        elif tipo_account == 3:
            self.retiros2(cliente_id)
        elif tipo_account == 4:
            
            self.retiros2(cliente_id)
            
                
        else:
            print("Opción inválida")

            

    def avance2(self, cliente_id):
     valor = int(input("Ingrese el valor de su avance: "))
     if valor % 10000 == 0 and valor > 0:
         print("Realizando avance en efectivo...")
         self.avances(valor, cliente_id)
         print("saldo es de:", cajero.search_saldo(cliente_id))
         print("tarjeta saldo:", cajero.search_saldo_tarjeta(cliente_id))
     else:
         print('error debe ser mayor a 10k')

 

    def realizar_transferencia(self, cliente_id):
        print("Realizando transferencia...")
        # Aquí puedes implementar la lógica para realizar transferencias
        print("\nSeleccione el tipo de cuenta:")
        print("1. Cuenta Bancolombia")
        print("2. Cuenta inscrita")
        print("3. Cuenta no inscrtia")
        tipo_account = int(input("Seleccione el tipo de cuenta: "))
        valor = int(input("Ingrese el valor : "))
        # Aquí puedes implementar la lógica para cada tipo de cuenta
        if tipo_account == 1:
                if valor % 10000 == 0 and valor > 0:
                    print("\nRealizando transferencia en efectivo...")
                    print
                    self.avances(valor, cliente_id)
                    cliente = cajero.check_cliente(dni, password)
                    cliente_id = cliente[0] 
                    print("Bienvenido,", cliente[1], cliente[2])
                    print("saldo es de:", cajero.search_saldo(cliente_id))
                   
                else:
                    print('error debe ser mayor a 10k')
               
        elif tipo_account == 2:
            pass
        elif tipo_account == 3:
             pass
        else:
            print("Opción inválida")
            

    def pagar_servicio(self, cliente_id):
        print("Pagando servicio...")
        # Aquí puedes implementar la lógica para pagar servicios
        
        #cursor.execute("SELECT id, nombre FROM servicios")
        
        print("\nSeleccione el tipo de servicio:")
        print("agua")
        print("luz")
        print("gas")
        tipo_account = int(input("Seleccione el tipo de cuenta: "))
        
        # Aquí puedes implementar la lógica para cada tipo de cuenta
        if tipo_account == 1:
            self.servicios(cliente_id)
            pass
        elif tipo_account == 2:
            self.servicios(cliente_id)
        elif tipo_account == 3:
            self.servicios(cliente_id)
        elif tipo_account == 4:
            self.servicios(cliente_id)
     
        else:
            print("Opción inválida")

    def cambiar_(self, cliente_id):
        nueva_clave = input("Ingrese la nueva clave: ")
        cursor = self.conexion.cursor()
        cursor.execute("UPDATE clientes SET clave = %s WHERE id = %s", (nueva_clave, cliente_id))
        self.conexion.commit()
        cursor.close()
        print("password cambiada exitosamente")

# Ejemplo de uso del cajero automático
cajero = Cajero()

# Solicitar información de cliente
dni = input("Ingrese su número de cédula: ")
password = input("Ingrese su password: ")

cliente = cajero.check_cliente(dni, password)

if cliente:
    cliente_id = cliente[0]  # Suponiendo que el ID del cliente es el primer campo en la tabla

    print("Bienvenido")

    while True:
    
        print("\nSeleccione una opción:")
    
        print("1. Consultar saldo")
        
        print("2. Retirar efectivo")
       
        print("3. Realizar avance en efectivo")
       
        print("4. Realizar transferencia")
       
        print("5. Pagar servicio")
   
        print("6. Cambiar password principal")
       
        print("7. Salir")
    
        opc = int(input("Elige la opción: "))

        if opc == 1:
            print("saldo es de:", cajero.search_saldo(cliente_id))
            print("tarjeta saldo:", cajero.search_saldo_tarjeta(cliente_id))
        elif opc == 2:
            cajero.retirar_efectivo(cliente_id)
        elif opc == 3:
            cajero.avance2(cliente_id)
        elif opc == 4:
            cajero.realizar_transferencia(cliente_id)
        elif opc == 5:
            cajero.pagar_servicio(cliente_id)
        elif opc == 6:
            cajero.cambiar_clave(cliente_id)
        elif opc == 7:
            print("Gracias")
            break
        else:
            print("Opción inválida")
else:
    print("Número de dni o password incorrectos")