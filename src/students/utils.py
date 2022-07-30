
def format_list(lst):
    response = ''
    for entry in lst:
        link = f"<a href='/students/update/{entry.id}'>UPDATE</a>"
        response += f'{link} {entry} <br>'
    return response if response else 'Empty results'
