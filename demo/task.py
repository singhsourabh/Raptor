from bs4 import BeautifulSoup
import re
import requests


def crawl_one_view(url):

    r = requests.get(url)
    try:
        soup = BeautifulSoup(r.content, 'lxml')
        base = soup.find(id="pnlContent")
        x = base.contents[3]
        details = dict()
        for detail in x.findAll("tr", {"class": "highlight"}):
            info = detail.findAll("span")
            for i in range(0, len(info), 2):
                details[info[i].text.strip()] = info[i+1].text.strip()

        result = []
        y = base.contents[5]
        sem = y.contents[3].td.findAll("div", recursive=False)
        attr = ['Sem', 'Result', 'Marks', 'COP', 'IsAUCPassed', 'Division']
        for i in sem:
            z = i.table.tr.td.findAll("span")
            temp = dict()
            text = z[0].find(
                "b", text=re.compile('Session')).next_sibling.strip()
            temp['Session'] = text[:text.find("(")]
            temp['SessionType'] = text[text.find("(")+1:text.find(")")]
            for count, id_name in enumerate(attr):
                if id_name == 'COP' and z[count+1].text.strip() != '':
                    if z[count+1].find("b", text=re.compile('COP')).next_sibling:
                        temp[id_name] = list(filter(
                            None, (z[count+1].find("b", text=re.compile('COP')).next_sibling.strip().split(','))))
                    else:
                        temp[id_name] = ''
                elif id_name == 'IsAUCPassed' and z[count+1].text.strip() != '':
                    temp[id_name] = z[count+1].find(
                        "b", text=re.compile('AUC Status')).next_sibling.strip()
                elif id_name == 'Division' and z[count+1].text.strip() != '':
                    temp[id_name] = z[count+1].find(
                        "b", text=re.compile('Division')).next_sibling.strip()
                elif id_name == 'Sem' or id_name == 'Marks':
                    temp[id_name] = list(
                        filter(None, re.split('[,/]', z[count+1].text.strip())))
                else:
                    temp[id_name] = z[count+1].text.strip()
            result.append(temp)

        return {'details': details, 'result': result}
    except:
        return 'Invalid data provided'
