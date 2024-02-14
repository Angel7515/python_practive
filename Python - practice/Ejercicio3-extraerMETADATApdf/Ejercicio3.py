import PyPDF2

pdf = open("Ejercicio3-extraerMETADATApdf/Policy Reforms and Sust Intensification in Africa.pdf","rb")

reader = PyPDF2.PdfReader(pdf)

meta = reader.metadata

print(meta)