import os
import shutil
#Antes de ejecutar el programa Cree las carpetas: Documentos, Imagenes, Videos,
# Programas y Comprimidos en la carpeta descargas.
#Ruta de la carpeta descargas, cambiar Usuario por el Usuario correspondiente
ruta_descargas = "C:\\Users\\Usuario\\Downloads\\"
# Extensiones por las que se filtra
ext_texto = ['.docx','.txt','.doc','.pdf', '.pptx','.xlsx', '.epub', '.ppt', '.pps','.csv','.xlm','.xls','.docx']
ext_foto = ['.JPG','.gbr', '.gif','.ico','.jpeg','.jpg','.png','.psd', '.svg', '.bmp', '.xcf','.ai', '.eps']
ext_video = ['.mov','.mp4','.avi','.mpeg','.m1v','.webm', '.mkv','.mpeg-2']
ext_programas = ['.exe','.deb','.apk','.bat','.msi']
ext_comprimidos = ['.tar', '.tar.gz','.rar','.zip','.tgz', '.7z']
move = False

#Funcion que mueve y ordena los Archivos por Carpeta
def ordenar (archivo,ext,move, Carpetas):
    if ext in ext_texto:
        shutil.move(ruta_descargas + archivo, ruta_descargas + 'Documentos')
        move = True
    if ext in ext_foto:
        shutil.move(ruta_descargas + archivo, ruta_descargas + 'Imagenes')
        move = True
    if ext in ext_video:
        shutil.move(ruta_descargas + archivo, ruta_descargas + 'Videos')
        move = True
    if ext in ext_programas:
        shutil.move(ruta_descargas + archivo, ruta_descargas + 'Programas')
        move = True
    if ext in ext_comprimidos:
        shutil.move(ruta_descargas + archivo, ruta_descargas + 'Comprimidos')
        move = True
    if move == False and ext != '':
        shutil.move(ruta_descargas + archivo, ruta_descargas + 'Varios')
        move = True

#Funcion que va revisando archivo por archivo
def main():
    for archivo in os.listdir(ruta_descargas):
        nombre_archivo, ext = os.path.splitext(archivo)
        ordenar (archivo, ext,move)
main()
print('Archivos Ordenados exitosamente')