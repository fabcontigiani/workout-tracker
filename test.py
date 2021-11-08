def main():
    import app
    import ejercicio

    WorkoutTracker = app.App()
    # Crear usuario y registrarlo en el sistema
    WorkoutTracker.registrar("Fabrizio", "1234", 96.5)
    # Mostrar todos los usuarios registrados
    WorkoutTracker.mostrar()
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
    # Usuario agrega ejercicios a su entrenamiento del dia de hoy
    user.agregarEjercicio(ejercicio.PesoReps("Press de Banca", 60, 5, 5))
    user.agregarEjercicio(ejercicio.Reps("Dominadas", user.peso, 8, 4))
    user.agregarEjercicio(ejercicio.Tiempo("Trote", 15, True))
    # Usuario muestra los ejercicios realizados el dia de hoy
    user.mostrarFecha()
    # Cerrar sesion de usuario
    WorkoutTracker.cerrarSesion("Fabrizio")
    WorkoutTracker.mostrar()
    # Eliminar usuario
    WorkoutTracker.eliminar("Fabrizio")
    WorkoutTracker.mostrar()


if __name__ == "__main__":
    main()
