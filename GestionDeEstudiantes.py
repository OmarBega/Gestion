# student_management.py

students_db = {}

def add_student(name, age, student_id, grade):
    if student_id in students_db:
        print("❌ Ya existe un estudiante con este ID.")
        return
    if not (0.0 <= grade <= 5.0):
        print("❌ La nota debe estar entre 0.0 y 5.0.")
        return
    if age <= 0 or not isinstance(age, int):
        print("❌ La edad debe ser un número entero positivo.")
        return
    students_db[student_id] = {"nombre": name, "edad": age, "nota": grade}
    print("✅ Estudiante agregado exitosamente.")

def search_by_id(student_id):
    student = students_db.get(student_id)
    if student:
        print(f"👤 Estudiante encontrado: {student}")
    else:
        print("❌ No se encontró ningún estudiante con ese ID.")

def search_by_name(name_part):
    results = [
        (sid, data) for sid, data in students_db.items()
        if name_part.lower() in data["nombre"].lower()
    ]
    if results:
        for sid, data in results:
            print(f"📌 ID: {sid}, Datos: {data}")
    else:
        print("❌ No se encontraron estudiantes con ese nombre.")

def update_student(student_id):
    if student_id not in students_db:
        print("❌ Estudiante no encontrado.")
        return
    print("Introduce los nuevos valores o presiona Enter para omitir:")
    new_age_input = input("Nueva edad: ").strip()
    new_grade_input = input("Nueva nota: ").strip()

    if new_age_input:
        try:
            new_age = int(new_age_input)
            if new_age > 0:
                students_db[student_id]["edad"] = new_age
            else:
                print("❌ La edad debe ser positiva.")
        except:
            print("❌ Edad inválida.")
    if new_grade_input:
        try:
            new_grade = float(new_grade_input)
            if 0.0 <= new_grade <= 5.0:
                students_db[student_id]["nota"] = new_grade
            else:
                print("❌ La nota debe estar entre 0.0 y 5.0.")
        except:
            print("❌ Nota inválida.")
    print("✅ Estudiante actualizado exitosamente.")

def delete_student(student_id):
    if student_id in students_db:
        del students_db[student_id]
        print("✅ Estudiante eliminado exitosamente.")
    else:
        print("❌ Estudiante no encontrado.")

def average_grade():
    if not students_db:
        print("⚠️ No hay estudiantes registrados.")
        return
    avg = sum(s["nota"] for s in students_db.values()) / len(students_db)
    print(f"📊 Promedio de notas: {avg:.2f}")

def list_students_below(threshold=3.0):
    try:
        threshold = float(threshold)
    except:
        print("❌ Umbral inválido.")
        return
    low_scores = [(sid, data) for sid, data in students_db.items() if data["nota"] < threshold]
    if low_scores:
        print(f"📉 Estudiantes con nota menor a {threshold}:")
        for sid, data in low_scores:
            print(f"ID: {sid}, Datos: {data}")
    else:
        print(f"✅ No hay estudiantes con nota menor a {threshold}.")

def preload_students():
    add_student("Alice Smith", 20, "S001", 4.2)
    add_student("Bob Johnson", 22, "S002", 2.8)
    add_student("Carla Reyes", 19, "S003", 3.9)
    add_student("David Lee", 21, "S004", 2.4)
    add_student("Eva Brown", 23, "S005", 4.7)

def display_menu():
    print("\n===== Sistema de Gestión de Estudiantes =====")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante por ID")
    print("3. Buscar estudiante por nombre")
    print("4. Actualizar información del estudiante")
    print("5. Eliminar estudiante")
    print("6. Calcular promedio de notas")
    print("7. Listar estudiantes con nota baja")
    print("8. Mostrar todos los estudiantes")
    print("9. Salir")

def show_all_students():
    if not students_db:
        print("⚠️ No hay estudiantes disponibles.")
    else:
        for sid, data in students_db.items():
            print(f"ID: {sid}, Datos: {data}")

def main():
    preload_students()
    while True:
        display_menu()
        choice = input("Selecciona una opción (1-9): ").strip()

        if choice == "1":
            name = input("Nombre completo: ").strip()
            try:
                age = int(input("Edad: ").strip())
                student_id = input("ID del estudiante: ").strip()
                grade = float(input("Nota: ").strip())
                add_student(name, age, student_id, grade)
            except ValueError:
                print("❌ Entrada inválida. Intenta de nuevo.")
        elif choice == "2":
            sid = input("ID del estudiante: ").strip()
            search_by_id(sid)
        elif choice == "3":
            name = input("Introduce el nombre o parte del nombre: ").strip()
            search_by_name(name)
        elif choice == "4":
            sid = input("ID del estudiante: ").strip()
            update_student(sid)
        elif choice == "5":
            sid = input("ID del estudiante: ").strip()
            delete_student(sid)
        elif choice == "6":
            average_grade()
        elif choice == "7":
            th = input("Umbral (por defecto es 3.0): ").strip()
            list_students_below(th if th else 3.0)
        elif choice == "8":
            show_all_students()
        elif choice == "9":
            print("👋 Saliendo del sistema... ¡Hasta pronto!")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
