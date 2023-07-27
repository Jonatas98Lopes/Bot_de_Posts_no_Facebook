import PySimpleGUI as sg


class Fim:

    def __init__(self):
        
        sg.theme('Dark Blue 10')

        layout = [
            [sg.Text('Programa finalizado. Seu post foi publicado com sucesso.', 
                    font=('Helvetica', 14), text_color=('white'))],

            [sg.Column(
                layout=[
                    [sg.Button('OK?', button_color=('white', '#0E8EF2'), 
                    font=('Helvetica', 14), size=(5, 1))]
                ],
                justification='center',  
                element_justification='center'  
            )]]

        janela = sg.Window('Programa encerrado:', font='_ 14', size=(550,100))\
        .layout(layout)

	
        self.button, self.values = janela.Read() 
        janela.close()
