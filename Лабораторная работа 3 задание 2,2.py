# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, argument='|'):
    participants_first_group = participants_first_group.replace(",", argument)
    participants_second_group = participants_second_group.replace(",", argument)
    first_group_list = participants_first_group.split(argument)
    second_group_list = participants_second_group.split(argument)

    common_participants = set(first_group_list) & set(second_group_list)
    sorted_common_participants = sorted(common_participants)

    return sorted_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group)
print(result)
