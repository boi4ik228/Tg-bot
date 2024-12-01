import sqlite3


def get_act(data, obj):
    p = [4, 4, 4, 4]
    if data[1] == '1': p[0] = 1
    if data[1] == '2': p[1] = 1
    if data[1] == '3': p[2] = 1
    if data[1] == '4': p[3] = 1
    connection = sqlite3.connect('Hant_project_2024_01.db')
    cursor = connection.cursor()
    if obj != '0':
        cursor.execute(
            f'SELECT id, article, short_description, link, key_to_act FROM document_database '
            f'WHERE key_to_area = {int(data[0])} AND (for_p1 = {p[0]} OR for_p2 = {p[1]} OR for_p3 = {p[2]} OR for_p4 = {p[3]}) AND key_to_object = {obj}'
        )
    else:
        cursor.execute(
            f'SELECT id, article, short_description, link, key_to_act FROM document_database '
            f'WHERE key_to_area = {int(data[0])} AND (for_p1 = {p[0]} OR for_p2 = {p[1]} OR for_p3 = {p[2]} OR for_p4 = {p[3]})'
        )
    acts = cursor.fetchall()
    connection.close()
    acts_right = list()
    for w in acts:
        acts_right.append(((str(w[1]).capitalize(), w[2], w[3]), get_edited(w[0])))
    return acts_right


def get_edited(id):
    connection = sqlite3.connect('Hant_project_2024_01.db')
    cursor = connection.cursor()
    cursor.execute(
        f'SELECT article, short_description, link FROM document_database '
        f'WHERE edits = {id}'
    )
    edited = cursor.fetchall()
    edited_right = list()
    for w in edited:
        edited_right.append((str(w[0]).capitalize(), w[1], w[2]))
    return edited_right
