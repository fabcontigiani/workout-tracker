def main():
    import app

    WorkoutTracker = app.App()
    WorkoutTracker.registrar("Fabrizio", "1234", 96.5)
    WorkoutTracker.mostrar()
    WorkoutTracker.iniciarSesion("Fabrizio", "otra cosa")
    WorkoutTracker.mostrar()
    WorkoutTracker.iniciarSesion("Fabrizio", "1234")
    WorkoutTracker.mostrar()
    WorkoutTracker.cerrarSesion("Fabrizio")
    WorkoutTracker.mostrar()
    WorkoutTracker.eliminar("Fabrizio")
    WorkoutTracker.mostrar()


if __name__ == "__main__":
    main()
