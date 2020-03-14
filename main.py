import requests

if __name__ == '__main__':
    temp = list()
    res = requests.get('https://www.dsebd.org/latest_share_price_all.php')
    a = res.text.split('</table>')[0].replace('''<td align='right'>''', '').replace('''<td align='center'>''', '').replace('''</tr>''', '').split('''<tr bgcolor='#EFEFEF'>''')[1:]
    # for items in a:
    #     temp.append(items.split('</td>')[:-1])
    #     # print(items)
    print(a[0].split('</td>')[1].replace("""""<td> <a href='""", ''))
    print(a[0].split('</td>')[:-1])
