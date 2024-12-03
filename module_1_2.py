number_of_completed_homework = 12
number_of_hours_spent = 1.5
course_name = 'Python'
time_for_one_assignment = number_of_hours_spent / number_of_completed_homework
print('Курс: ', course_name, ', всего задач:', number_of_completed_homework,
      ', затрачено часов:', number_of_hours_spent, ', среднее время выполнения',
      time_for_one_assignment, 'часа.')

# Задаём переменные
completed_tasks = 12  # Количество выполненных ДЗ
spent_hours = 1.5  # Количество затраченных часов
course_name = 'Python'  # Название курса

# Объяснение:
# Имена переменных:
# completed_tasks — количество выполненных задач (целое число).
# spent_hours — общее время, затраченное на выполнение задач (число с плавающей точкой).
# course_name — название курса (строка).
# time_per_task — среднее время выполнения одного задания (вычисляется делением spent_hours на completed_tasks).

# Вычисляем время на одно задание
time_per_task = spent_hours / completed_tasks

# Вывод строки с использованием переменных
print('Курс:', course_name, ', всего задач:', completed_tasks, ', затрачено часов:', spent_hours, ', среднее время выполнения', time_per_task, 'часа.')

# Объяснение:
# Вывод строки:
# Используется функция print() для вывода текста.
# Переменные объединяются с текстом через запятые, что автоматически добавляет пробелы между элементами.
# Вывод поддерживает смешение текста и значений переменных.
