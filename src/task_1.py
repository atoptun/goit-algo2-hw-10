from dataclasses import dataclass
from typing import Optional
from copy import deepcopy

# Визначення класу Teacher
@dataclass
class Teacher:
    first_name: str
    last_name: str
    age: int
    email: str
    can_teach_subjects: set[str]
    assigned_subjects: set[str]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.age} років, email: {self.email}"


def create_schedule(subjects: set[str], teachers: list[Teacher]) -> Optional[list[Teacher]]:
    temp_subjects = set(subjects)
    temp_teachers = list(deepcopy(teachers))
    result_teachers = []

    while temp_subjects:
        can_teach = list(filter(lambda teacher: teacher.can_teach_subjects & temp_subjects, temp_teachers))
        if not can_teach:
            return None
        
        can_teach.sort(key=lambda t: (-len(t.can_teach_subjects & temp_subjects), t.age))
        best_teacher = can_teach[0]
        best_cover = best_teacher.can_teach_subjects & temp_subjects

        best_teacher.assigned_subjects = best_cover
        result_teachers.append(best_teacher)

        temp_subjects -= best_cover
        temp_teachers.remove(best_teacher)

    return result_teachers


def print_schedule(schedule: Optional[list[Teacher]]) -> None:
    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"  {teacher}")
            print(f"    Викладає предмети: {', '.join(teacher.assigned_subjects)}")
    else:
        print("  Неможливо покрити всі предмети наявними викладачами.")


def test():
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {"Математика", "Фізика"}, set()),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}, set()),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {"Інформатика", "Математика"}, set()),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}, set()),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {"Фізика", "Інформатика"}, set()),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}, set()),
    ]
    print(f"Список викладачів:")
    for teacher in teachers:
        print(f"  {teacher}")
        print(f"    Може викладати: {', '.join(teacher.can_teach_subjects)}")
    print("-" * 50)

    print("\nTest 1: Successful schedule creation")
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    print(f"Предмети: {", ".join(subjects)}")
    schedule = create_schedule(subjects, teachers)
    print_schedule(schedule)
    print("-" * 50)

    print("\nTest 2: Unsuccessful schedule creation")
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія', 'Географія'}
    print(f"Предмети: {", ".join(subjects)}")
    schedule = create_schedule(subjects, teachers)
    print_schedule(schedule)
    print("-" * 50)


if __name__ == '__main__':
    test()
