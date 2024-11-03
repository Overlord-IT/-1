def find_common_participants(participants_first_group, participants_second_group, separator=','):
    first_group_list = participants_first_group.split(separator)
    second_group_list = participants_second_group.split(separator)
    common_participants = sorted(list(set(first_group_list) & set(second_group_list)))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

intersection_participants_first_group = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(intersection_participants_first_group)


participants_first_group = "Иванов;Петров;Сидоров"
participants_second_group = "Петров;Сидоров;Смирнов"

intersection_participants_first_group = find_common_participants(participants_first_group, participants_second_group, separator=";")
print(intersection_participants_first_group)


