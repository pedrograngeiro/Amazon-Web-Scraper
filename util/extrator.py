def pegar_texto_id(soup, element_id):
    element = soup.find(id=element_id)
    if element:
        coringa = element.get_text(strip=True)
        return print(coringa)

    else:
        return "Elemento não encontrado"

def pegar_texto_classe(soup, element_class):
    element = soup.find(class_=element_class)
    if element:
        coringa = element.get_text(strip=True)
        return print(coringa)

    else:
        return "Elemento não encontrado"