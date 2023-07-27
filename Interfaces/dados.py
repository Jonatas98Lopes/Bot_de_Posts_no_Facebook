import PySimpleGUI as sg


class UserData:

    def __init__(self):
        
        sg.theme('Dark Blue 10')

        layout = [
            [sg.Text('Digite seu nome de usuário no Facebook:', 
                    font=('Helvetica', 14), text_color=('white'))],

            [sg.Input(size=(70,5), background_color='white', 
                    key='user_name', font=('Helvetica', 12))],

            [sg.Text('Digite sua senha:', font=('Helvetica', 14), text_color=('white'))],
            [sg.Input(password_char='*',size=(70,5), background_color='white',
                    key='password', font=('Helvetica', 12))],

            [sg.Text('Digite o que deseja publicar:', font=('Helvetica', 14), 
                    text_color=('white'))],
            [sg.Multiline(size=(70, 5), background_color='white', key='post', 
                    font=('Helvetica', 12))],

            [sg.Button('Enviar', button_color=('white', '#0E8EF2'), font=('Helvetica', 14)), 
             sg.Button('Cancelar', button_color=('red', 'white'), font=('Helvetica', 14))]
            
        ]

        janela = sg.Window('Dados do Usuário:', font='_ 14', size=(500,300)).layout(layout)

	
        self.button, self.values = janela.Read() 
        janela.close()

