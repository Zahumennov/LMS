
def format_list(lst):
    response = ''
    for entry in lst:
        response += '<br>' + str(entry)
    return response if response else 'Empty results'
