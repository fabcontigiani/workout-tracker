def main():
    import app
    import ejercicio

    WorkoutTracker = app.App()
    # Crear usuario y registrarlo en el sistema
    WorkoutTracker.registrar("Fabrizio", "1234", 96.5)
    WorkoutTracker.registrar("Martin", "4321", 74.0)
    # Mostrar todos los usuarios registrados
    WorkoutTracker.mostrar()
    # Chequear por usuario ya existente
    WorkoutTracker.registrar("Martin", "0987", 79.2)
    # Constrasena incorrecta
    user = WorkoutTracker.iniciarSesion("Fabrizio", "otra cosa")
    # No se ingreso, user es None
    WorkoutTracker.mostrar()
    print(user is not None)
    # Inicio de sesion de usuario
    user = WorkoutTracker.iniciarSesion("Fabrizio", "1234")
    # Se ingreso, user es el objeto correspondiente al usuario
    WorkoutTracker.mostrar()
    print(user is not None)
    # Modificar peso de usuario
    user.peso = 95.8
    WorkoutTracker.mostrar()
    # Usuario agrega ejercicios a su entrenamiento del dia de hoy
    user.agregarEjercicio(ejercicio.PesoReps("Press de Banca", 60, 5, 5))
    user.agregarEjercicio(ejercicio.Reps("Dominadas", user.peso, 8, 4))
    user.agregarEjercicio(ejercicio.Tiempo("Trote", 15, True))
    # Usuario muestra los ejercicios realizados el dia de hoy
    user.mostrarFecha()
    # Usuario muestra los ejercicios realizados en otro dia
    user.mostrarFecha("2020-12-31")
    # Usuario elimina un ejercicio
    user.quitarEjercicio("Trote")
    user.mostrarFecha()
    # Cerrar sesion de usuario
    WorkoutTracker.cerrarSesion("Fabrizio")
    WorkoutTracker.mostrar()
    # Usuario no ingresado no puede agregar ejercicios
    user.agregarEjercicio(ejercicio.Tiempo("Plancha", 1, False))
    # Usuario no ingresado no puede mostrar ejercicios
    user.mostrarFecha()
    # Usuario no ingresado no puede quitar ejercicios
    user.quitarEjercicio("Dominadas")
    # Eliminar usuario
    WorkoutTracker.eliminar("Fabrizio")
    WorkoutTracker.mostrar()


if __name__ == "__main__":
    main()
