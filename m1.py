from PySimpleGUI  import PySimpleGUI as sg 
#layout
sg.theme('Reddit')
layout = [
[sg.Text('Usuário'), sg.Input(key='usuario', size=(20,1))],
[sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20,1))],
[sg.Checkbox('Salvar o longin?')],
[sg.Button('Entrar')]

]
#windows
janela = sg.Window('Tela de login', layout)
#Ler os Eventos
while True:
    eventos, valores = janela.read()
    if eventos == seg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
     if valores['usuario'] == 'Marcos' and valores['senha'] == '1234':
         print('Bem-vindo')

