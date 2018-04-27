from datetime import date


def generate_query_data(all_data):
    query = """
            INSERT daily_temperature_90_00
            (
            min,
            max,
            state,
            country,
            date
            )
            VALUES {0}
            """
    string_values = __format_query_values(all_data)
    with open("tests/data/result_query.sql", "w+") as file:
        file.write(query.format(string_values))
    return query.format(string_values)


def __format_query_values(all_data: list):
    data_list_values = list()
    for result in all_data:
        values = list()
        values.append(result['celsius_min'])
        values.append(result['celsius_max'])
        values.append(result['state'])
        values.append(result['country'])
        values.append(__to_date(
            int(result['da']), int(result['mo']),
            int(result['year']))
        )
        data_list_values.append(values)

    values_string = ",".join(
        [
            '(' + ",".join(
                [
                    "'" + str(y) + "'" if y or y == 0.0 else "NULL"
                    for y in x
                ]
            ) + ')'
            for x in data_list_values
        ])
#    with open("tests/data/query_values.txt", "w+") as file:
#        file.write(values_string)
    return values_string


def __to_date(day: int, month: int, year: int):
    if type(day) is int and type(month) is int and type(year) is int:
        return str(date(year, month, day))
    else:
        return "0000-00-00"