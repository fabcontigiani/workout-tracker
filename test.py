def main():
    import app

    WorkoutTracker = app.App()
    WorkoutTracker.registrar("Fabrizio", "1234", 96.5)
    WorkoutTracker.mostrar()
    WorkoutTracker.ingresar("Fabrizio", "1234")
    WorkoutTracker.mostrar()
    WorkoutTracker.eliminar("Fabrizio")
    WorkoutTracker.mostrar()


if __name__ == "__main__":
    main()
