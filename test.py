def main():
    import app

    WorkoutTracker = app.App()
    # Crear usuario y registrarlo en el sistema
    WorkoutTracker.registrarUsuario("Fabrizio", "1234", 96.5)
    WorkoutTracker.registrarUsuario("Martin", "4321", 74.0)
    # Mostrar todos los usuarios registrados
    WorkoutTracker.mostrarUsuarios()
    # Chequear por usuario ya existente
    WorkoutTracker.registrarUsuario("Martin", "0987", 79.2)
    # Constrasena incorrecta
    user = WorkoutTracker.iniciarSesion("Fabrizio", "otra cosa")
    # No se ingreso, user es None
    WorkoutTracker.mostrarUsuarios()
    print(user is not None)
    # Inicio de sesion de usuario
    user = WorkoutTracker.iniciarSesion("Fabrizio", "1234")
    # Se ingreso, user es el objeto correspondiente al usuario
    WorkoutTracker.mostrarUsuarios()
    print(user is not None)
    # Modificar peso de usuario
    user.peso = 95.8
    WorkoutTracker.mostrarUsuarios()
    # Usuario agrega ejercicios a su entrenamiento del dia de hoy
    user.agregarEjercicio("Press de Banca", peso=60, reps=5, sets=5)
    user.agregarEjercicio("Dominadas", reps=8, sets=4)
    user.agregarEjercicio("Trote", tiempo=15)
    # Usuario intenta agregar un ejercicio invalido
    user.agregarEjercicio("Invalido", peso=True, reps=-3.4, sets="",
                          tiempo=user)
    # Usuario intenta agregar un ejercicio con un entero negativo (o cero)
    user.agregarEjercicio("Negativo", tiempo=-1)
    user.agregarEjercicio("Cero", tiempo=0)
    # Usuario intenta agregar un ejercicio a una fecha invalida
    user.agregarEjercicio("Fecha Invalida", tiempo=1, fecha="Invalido")
    # Usuario muestra los ejercicios realizados el dia de hoy
    user.mostrarFecha()
    # Mostrar volumen de entrenamiendo del dia de hoy
    user.volumenFecha()
    # Usuario muestra los ejercicios realizados en otro dia
    user.mostrarFecha("2020-12-31")
    # Mostrar volumen de entrenamiento de otra fecha no existente en el
    # diccionario
    user.volumenFecha("2020-12-31")
    # Usuario elimina un ejercicio
    user.quitarEjercicio("Trote")
    user.mostrarFecha()
    # Cerrar sesion de usuario
    WorkoutTracker.cerrarSesion("Fabrizio")
    WorkoutTracker.mostrarUsuarios()
    # Usuario no ingresado no puede agregar ejercicios
    user.agregarEjercicio("Plancha", tiempo=1)
    # Usuario no ingresado no puede mostrar ejercicios
    user.mostrarFecha()
    # Usuario no ingresado no puede quitar ejercicios
    user.quitarEjercicio("Dominadas")
    # Eliminar usuario
    WorkoutTracker.eliminarUsuario("Fabrizio")
    WorkoutTracker.mostrarUsuarios()


if __name__ == "__main__":
    main()
