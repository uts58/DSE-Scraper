import requests

if __name__ == '__main__':
    temp = list()
    data = dict()
    res = requests.get('https://www.dsebd.org/latest_share_price_all.php', timeout=(5, 5))
    text = res.text.split('''<tr bgcolor='#EFEFEF'>''')[1:]
    for items in text:
        sanitizedText = items.replace('''<td align='right'>''', '').replace("""</font>""", '').replace('''<td align='center'>''', '').replace('''</tr>''', '').replace("""<td> <a href='""", '').replace("""</a>""", '').split('</td>')[:-1]
        data[sanitizedText[1].split("""' target='_top' class='ab1'>""")[1]] = {
            'id': sanitizedText[0],
            'url': 'https://www.dsebd.org/' + sanitizedText[1].split("""' target='_top' class='ab1'>""")[0],
            'ltp': sanitizedText[2],
            'high': sanitizedText[3],
            'low': sanitizedText[4],
            'closeep': sanitizedText[5],
            'ycp': sanitizedText[6],
            'change': sanitizedText[7].split("""'>""")[1],
            'trade': sanitizedText[8],
            'value (mn)': sanitizedText[9],
            'volume': sanitizedText[10].replace(',', '')
        }

print(data)
