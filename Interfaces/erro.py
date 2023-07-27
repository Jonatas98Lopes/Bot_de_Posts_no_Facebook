import PySimpleGUI as sg


class Erro:

    def __init__(self, mensagem, titulo):
        
        sg.theme('Dark Blue 10')

        layout = [
            [sg.Text(mensagem, font=('Helvetica', 14), text_color=('white'))],

            [sg.Text('Por favor, verifique seus dados e tente novamente.', 
                    font=('Helvetica', 14), text_color=('white'))],
            [sg.Column(
                layout=[
                    [sg.Button('OK?', button_color=('white', '#0E8EF2'), 
                    font=('Helvetica', 14), size=(5, 1))]
                ],
                justification='center',  
                element_justification='center'  
            )]]

        janela = sg.Window(titulo, font='_ 14', size=(550,130))\
        .layout(layout)

	
        self.button, self.values = janela.Read() 
        janela.close()

