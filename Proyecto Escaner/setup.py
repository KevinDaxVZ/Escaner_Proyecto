import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    'packages': [
        'tkinter', 'face_recognition', 'PIL', 'pathlib',
        'cv2', 'numpy', 'pygame', 'locale',
        'pandas', 'openpyxl'
    ],
    'include_files': [
        'Sonidos', 'Empleados', 'Imagenes_del_programa', 'Registro_de_asistencia'
    ]
}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'  # Si tu programa es una aplicación de GUI

setup(
    name='Proyecto_Escaner',
    version='1.0',
    description='Descripción de tu programa',
    options={'build_exe': build_exe_options},
    executables=[Executable('Proyecto_Escaner.py', base=base)]
)

