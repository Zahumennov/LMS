
def format_list(lst, base_link):
    response = ''
    for entry in lst:
        link = f"<a href='{base_link}{entry.id}'>UPDATE</a>"
        response += f'{link} {entry} <br>'
    return response if response else 'Empty results'
