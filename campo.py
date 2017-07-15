import urllib2
from bs4 import BeautifulSoup
from itertools import combinations

class PKF():

    url = None
    page = None
    parser = None

    def __init__(self, url):
        self.url = url
        self.page = urllib2.urlopen(self.url)
        self.parser = BeautifulSoup(self.page, 'html.parser')

    def obtener_tabla(self, css_class):
        return self.parser.find_all('table', attrs={'class': css_class})

    def obtener_font(self,tabla, css_class):
        return

    def tablas_venta_directa(self):
        header = 'Promedio Ventas Directas'
        tablas = self.obtener_tabla('tab1')
        return [i for i in tablas if header in str(i)]

    def tabla_precio(self):
        tablas_cabecera = self.tablas_venta_directa()
        tablas_clase_2 = self.obtener_tabla('tab2')

        combinacion = combinations(tablas_cabecera + tablas_clase_2, 2)

        return [(i,j) for i, j in combinacion if i.parent == j.parent]

    def precio_bruto(self, tabla):
        div = (tabla.find('div', attrs={'class': 'promedio'}))
        return div.text

    def mes(self, tabla):
        font = tabla.find('font', attrs={'class': 'storycat'})
        return font.text

    def listado(self):
        for i in pkf.tabla_precio():
            print self.mes(i[0]), self.precio_bruto(i[1])

if __name__ == '__main__':

    pkf = PKF('http://www.pkfsrl.com.ar/modules.php?name=News&new_topic=2&pagenum=3')

    pkf.listado()

    pkf = PKF('http://www.pkfsrl.com.ar/modules.php?name=News&new_topic=2&pagenum=2')

    pkf.listado()

    pkf = PKF('http://www.pkfsrl.com.ar/modules.php?name=News&new_topic=2&pagenum=1')

    pkf.listado()

    #print pkf.tabla_precio()


'''
x = soup.find_all('div', attrs={'class': 'promedio'})

x = soup.find_all('table')

#print (x)
if __name__ == '__main__':
    for i in x:
        y = (i.find_all('table', attrs={'class': 'tab2'}))
        for j in y:
            print((j.find_all('table')))

'''