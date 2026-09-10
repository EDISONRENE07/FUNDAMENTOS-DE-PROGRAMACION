sistema_activo = True
tiene_permiso = True

if sistema_activo == True:
    if tiene_permiso == True:
        print("Accion ejecutada")
    else:
        print ("Permiso denegado")
else:
    print ("Sistema inactivo")