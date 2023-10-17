import requests
from bs4 import BeautifulSoup
from helps import *


class Portal:
    def __init__(self):
        #inicializamos las variables necesarias
        self.data_login = None
        self.csrf = None
        self.soup = None
        self.url_main = 'https://www.portal.nauta.cu/'
        self.url_login = 'https://www.portal.nauta.cu/user/login/es-es'
        self.url_captcha = 'https://www.portal.nauta.cu/captcha/?'
        self.headers = {
            "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64; rv: 117.0.1)"
        }
        self.session = requests.Session()

    def verify_connection(self):
        #verificamos si hay una conexion estable con la web, si es asi pasamos la respuesta por BeautifulSoup para buscar datos
        try:
            response = self.session.get(self.url_login, headers=self.headers, timeout=4)
            if response.status_code == 200:
                self.soup = BeautifulSoup(response.content, 'html.parser')
                return True
            else:
                return False
        except Exception as e1:
            print(f'Error: {e1}')

    def get_captcha(self):
        #obtenemos el numero captcha necesario para iniciar sesion
        try:
            with open('captcha.png', 'wb') as captcha_imagen:
                captcha_img = self.session.get(self.url_captcha, headers=self.headers)
                for c in captcha_img:
                    captcha_imagen.write(c)
                print('La imagen del respectivo numero CAPTCHA de esta\nsesion ah sido guardada en el directorio de este archivo con exito')
        except Exception as e2:
            print(f'Error al intentar obtener el captcha: {e2}')
            return False

    def login_net(self, username, password, captcha_number):
        #buscamos el token csrf
        self.csrf = self.soup.find('input', {'name': 'csrf'}).get('value')
        data_login = {
            'csrf': self.csrf,
            'login_user': username,
            'password_user': password,
            'captcha': captcha_number,
            'btn_submit': ''
        }
        try:
            #intentamos iniciar sesion
            self.data_login = self.session.post(self.url_login, headers=self.headers, data=data_login)
            #variables de error para identificarlos
            error_captcha = 'El código Captcha no coincide con el valor introducido'
            error_usuario = 'Usuario desconocido o contraseña incorrecta'
            #si encontramos el mensaje de error de captcha en la respuesta devolvemos el error
            if error_captcha in self.data_login.text:
                #print('Error en el captcha')
                return 'captcha_error'
            #si encontramos el mensaje de error de credenciales en la respuesta deviolvemos el error
            elif error_usuario in self.data_login.text:
                #print('Error en el usuario o la contrasena')
                return 'credentials_error'
            else:
                return True
        #otros errores fuera de lo comun serian una excepcion y aqui devolvemos false
        except Exception as e3:
            print(f'Error al establecer conexion para iniciar sesion: {e3}')
            return False

    def recargar(self, codigo_recarga):
        try:
            datos_para_recargar = {
                'csrf': self.csrf,
                'recharge_code': codigo_recarga,
                'btn_submit': ''
            }

            recarga_response = self.session.post('https://www.portal.nauta.cu/useraaa/recharge_account', headers=self.headers, data=datos_para_recargar)
            if 'El código de recarga es incorrecto' in recarga_response.text:
                return 'error_codigo'
            elif recarga_response.status_code == 200:
                return True
            else:
                return 'recarga_error'

        except Exception as error:
            print(error)
            return False

    def info_cuenta(self):
        try:
            soup = BeautifulSoup(self.data_login.content, 'html.parser')
            fecha_bloqueo = soup.find_all('h5')

            datos = []

            for tag in fecha_bloqueo:
                if 'Fecha de bloqueo' in tag.text:
                    fecha_de_bloqueo = tag.find_next('p').text.strip()
                    datos.append(fecha_de_bloqueo)
                elif 'Fecha de eliminación' in tag.text:
                    fecha_de_eliminacion = tag.find_next('p').text.strip()
                    datos.append(fecha_de_eliminacion)
                elif 'Tipo de cuenta' in tag.text:
                    tipo_de_cuenta = tag.find_next('p').text.strip()
                    datos.append(tipo_de_cuenta)
                elif 'Tipo de servicio' in tag.text:
                    tipo_de_servicio = tag.find_next('p').text.strip()
                    datos.append(tipo_de_servicio)
                elif 'Saldo disponible' in tag.text:
                    saldo_disponible = tag.find_next('p').text.strip()
                    datos.append(saldo_disponible)
                elif 'Tiempo disponible de la cuenta' in tag.text:
                    tiempo_disponible_en_cuenta = tag.find_next('p').text.strip()
                    datos.append(tiempo_disponible_en_cuenta)
                elif 'Cuenta de correo' in tag.text:
                    cuenta_de_correo = tag.find_next('p').text.strip()
                    datos.append(cuenta_de_correo)
                else:
                    pass
            del datos[7:10]
            return datos
        except Exception as error:
            print(error)
            return False

    def info_enlace(self):
        try:
            soup = BeautifulSoup(self.data_login.content, 'html.parser')
            fecha_bloqueo = soup.find_all('h5')

            datos_enlace = []

            for tag in fecha_bloqueo:
                if 'Oferta' in tag.text:
                    oferta = tag.find_next('p').text.strip()
                    datos_enlace.append(oferta)
                elif 'Cuota mensual' in tag.text:
                    cuota_mensual = tag.find_next('p').text.strip()
                    datos_enlace.append(cuota_mensual)
                elif 'Velocidad de bajada' in tag.text:
                    velocidad_bajada = tag.find_next('p').text.strip()
                    datos_enlace.append(velocidad_bajada)
                elif 'Velocidad de subida' in tag.text:
                    velocidad_subida = tag.find_next('p').text.strip()
                    datos_enlace.append(velocidad_subida)
                elif 'Teléfono' in tag.text:
                    telefono = tag.find_next('p').text.strip()
                    datos_enlace.append(telefono)
                elif 'Identificador del enlace' in tag.text:
                    identificador_enlace = tag.find_next('p').text.strip()
                    datos_enlace.append(identificador_enlace)
                elif 'Estado del enlace' in tag.text:
                    estado_enlace = tag.find_next('p').text.strip()
                    datos_enlace.append(estado_enlace)
                elif 'Fecha de activación' in tag.text:
                    fecha_activacion = tag.find_next('p').text.strip()
                    datos_enlace.append(fecha_activacion)
                elif 'Fecha de bloqueo' in tag.text:
                    fecha_bloqueo = tag.find_next('p').text.strip()
                    datos_enlace.append(fecha_bloqueo)
                elif 'Fecha de eliminación' in tag.text:
                    fecha_eliminacion = tag.find_next('p').text.strip()
                    datos_enlace.append(fecha_eliminacion)
                elif 'Fondo de cuota' in tag.text:
                    fondo_cuota = tag.find_next('p').text.strip()
                    datos_enlace.append(fondo_cuota)
                elif 'Bono' in tag.text:
                    bono = tag.find_next('p').text.strip()
                    datos_enlace.append(bono)
                elif 'Deuda' in tag.text:
                    deuda = tag.find_next('p').text.strip()
                    datos_enlace.append(deuda)
                else:
                    pass
            del datos_enlace[0:2]
            return datos_enlace
        except Exception as error:
            print(error)
            return False


if __name__ == '__main__':
    portal = Portal()
    control = False
    while portal.verify_connection():
        username1 = input('Usuario: ')
        password2 = input('Password: ')
        portal.get_captcha()
        captcha = input('Captcha: ')

        sesion = portal.login_net(username1, password2, captcha)
        if sesion == 'captcha_error':
            print('Error, el codigo captcha no coincide con el de la imagen')
        elif sesion == 'credentials_error':
            print('Error, usuario o contrasena incorrectos')
        elif not sesion:
            print('Error inesperado del lado del servidor del Portal Nauta.\ncerrando....')
            break
        else:
            print('\nInicio de sesion correcto')
            print(f'{portal.info_enlace()}\n{portal.info_cuenta()}')
            control = True
            break
    while control:
        print('Bienvenido al PortalNauta, que accion deseas realizar: ')
        print('''
        1-Recargar cuenta nauta''')
        tupla_num = [1]
        longitud = len(tupla_num)

        control_maximo = int(input('Elige el respectivo numero para realizar su respectiva operacion: '))

        if insertar_numero(control_maximo, 'realizar su respectiva accion'):
            codigo = int(input('Codigo de recarga: '))
            con = len_recarga(codigo)
            if con:
                res = portal.recargar(codigo)
                if res == 'error_codigo':
                    print('error el codigo de recarga es incorrecto')
            elif con == 'menor_12':
                print('Escribe un numero entre 12 y 16 caracteres, saliendo de la opcion...')
            elif con == 'mayor_16':
                print('Escribe un numero entre 12 y 16 caracteres, saliendo de la opcion...')
            else:
                print('Escribe algo valido, para la proxima')

