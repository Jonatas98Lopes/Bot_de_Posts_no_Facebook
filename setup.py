# ESTE ARQUIVO DEVE SER USADO PARA GERAR O EXECUTÁVEL DO PROGRAMA.


from cx_Freeze import setup, Executable


settings = Executable(
    script='app.py',
    icon='assets\\facebook.ico',
)

setup(
    name='Bot de Postagem no Facebook',
    version='1.0',
    description='Com este software, você pode automatizar o processo de postagem no seu Facebook',
    author='Jonatas Lopes de Sousa',
    options= {'build_exe': {
        'include_msvcr': True
    }},
    executables=[settings]
    )