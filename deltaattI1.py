from Bio import SeqIO
import glob
import re

# Secuencia a buscar de fragmentos variables del sitio attI1
secuencia_buscar = "AAAACAAAGtt"
patron = re.compile(secuencia_buscar, re.IGNORECASE)  # Ignorar diferencias de case

# Diccionario para guardar resultados: {nombre_archivo: conteo}
archivos_con_secuencia = {}

# Buscar en todos los archivos FASTA del directorio actual
for fasta_file in glob.glob("/content/*.fasta"):
    conteo = 0
    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = str(record.seq)
        # Contar todas las ocurrencias de la secuencia en esta entrada
        conteo += len(patron.findall(seq))

    if conteo >= 2:  # Solo guardar si aparece 2+ veces
        archivos_con_secuencia[fasta_file] = conteo

# Mostrar resultados
if archivos_con_secuencia:
    print("Archivos con la secuencia 'AAAACAAAGtt' 2+ veces:")
    for archivo, conteo in archivos_con_secuencia.items():
        print(f"- {archivo}: {conteo} repeticiones")
else:
    print("No se encontraron archivos con la secuencia 2+ veces.")