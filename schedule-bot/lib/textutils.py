from re import findall


def put_links_in_anchors(text):
    link_regex = r'http[s]?://\S*'
    matches = findall(link_regex, text)
    for m in matches:
        template = f'<a href="{m}">{m}</a>'
        text = text.replace(m, template)

    return text
