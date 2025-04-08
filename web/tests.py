from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class PruebasPaginaInicio(SimpleTestCase):
    def test_url_existe_en_ubicacion_correcta(self):
        respuesta = self.client.get('/')
        self.assertEqual(respuesta.status_code, 200)

    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertEqual(respuesta.status_code, 200)

        

class PruebasPaginaNosotros(SimpleTestCase):
    def test_url_existe_en_ubicacion_correcta(self):
        respuesta = self.client.get('/nosotros/')
        self.assertEqual(respuesta.status_code, 200)

    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse('nosotros'))
        self.assertEqual(respuesta.status_code, 200)
