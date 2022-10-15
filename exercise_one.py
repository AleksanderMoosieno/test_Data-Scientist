groups: dict[int, int] = dict()


def is_good_id(person_id: int) -> bool:
    if not isinstance(person_id, int):
        return False
    cnt: int = 0
    while person_id > 0:
        person_id = int(person_id / 10)
        cnt += 1
    return (cnt >= 5 and cnt <= 7)


def get_id_sum(person_id: int) -> int:
    group_number: int = 0
    figure: int = 0
    while person_id > 0:
        figure = person_id % 10
        person_id = int(person_id / 10)
        group_number += figure
    return group_number


def add_group_member(group_number: int, members_number: int = 1) -> bool:
    members_cnt: int = groups.get(group_number, 0)
    members_cnt += members_number
    groups[group_number] = members_cnt
    return True


def add_person(person_id: int) -> bool:
    if not is_good_id(person_id=person_id):
        return False

    group_number: int = get_id_sum(person_id=person_id)

    return add_group_member(group_number=group_number)


def add_people(n_first_id: int, n_customers: int) -> bool:
    if not is_good_id(n_first_id):
        return False

    group_number: int = get_id_sum(person_id=n_first_id)
    return add_group_member(
        group_number=group_number,
        members_number=n_customers
    )


def view_group() -> None:
    k: int
    v: int
    for k, v in groups.items():
        print(f"Группа {k} с количеством людей {v}")


def test_func_one(n_customers: int) -> None:
    _: int
    for _ in range(n_customers):
        id: int = int(input("Введите ID клиента: "))
        add_person(id)
    view_group()


def test_func_two(n: int) -> None:
    _: int
    for _ in range(n):
        n_first_id: int = int(input("Введите ID: "))
        n_customers: int = int(input("Введите кол-во клиентов: "))
        add_people(n_first_id=n_first_id, n_customers=n_customers)
    view_group()


test_func_one(5)
test_func_two(7)
