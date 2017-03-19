num = int(raw_input("Escribe el numero a factorizar: "))
multiplicador = num - int(1)
while multiplicador > int(1):
    resultado = multiplicador * num
    num = resultado 
    multiplicador = multiplicador - int(1)
print "Aqui tienes el resultado: ", resultado
