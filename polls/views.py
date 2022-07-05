from nltk.tokenize.toktok import ToktokTokenizer
from spellchecker import SpellChecker
import time
from django.shortcuts import render
from .forms import FormularioPrincipal
from .models import Revisor
import string
import secrets
num = 256 # define the length of the random string

# Create your views here.
def registro(request):
    if request.method == "POST":
        formulario = FormularioPrincipal(request.POST)

        if formulario.is_valid():
            infFormulario = formulario.cleaned_data
            stringRandom = res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))
            guarani = Revisor(
                texto = infFormulario['texto'],
            )

            print(guarani.texto)
            toktok = ToktokTokenizer()
            # spell = SpellChecker()
            spell = SpellChecker(language=None,
                                 case_sensitive=False)  # lenguaje ninguno, distinguir entre mayusculas y minusculas
            corpus = spell.word_frequency.load_text_file('textprueba.txt')

            def separa_palabras(lista_tokens):
                lista_palabras = []
                for token in lista_tokens:
                    if token.isalpha():
                        lista_palabras.append(token)
                return lista_palabras

            palabras_separadas = toktok.tokenize(corpus)
            lista_palabras = separa_palabras(palabras_separadas)
            palabra = []
            palabra = separa_palabras(palabras_separadas)
            usuario = guarani.texto
            minuscula = usuario.lower()
            limpio = minuscula.split()
            palabraincorrecta = spell.unknown(limpio)  # traer lo que no está en el corpus/diccionario
            print("las palabras equivocadas son: ", palabraincorrecta)  # la palabra equivocada
            if len(palabraincorrecta) == 0:
                print("Todo está bien escrito")

            for palabra in palabraincorrecta:
                inicio = time.time()
             #cor = spell.correction(palabra)  # Devuelve el resultado más probable para la palabra mal escrita

              #  print("La mejor ortografía para '{}' es '{}'".format(palabra, cor))

                print("otra posible palabra candidata es: ")
                resultado=spell.candidates(palabra)
                res="salio ok"
                print("Palabra equivocada: '{}' Candidatos: '{}'".format(palabra, spell.candidates(palabra)))  # Devuelve un conjunto de posibles candidatos para la palabra mal escrita
                fin = time.time()
               # print(fin - inicio)
            guarani.save()
            return render(request, "principal.html",{"message":res,"resultado":resultado, "form":formulario})

    else:
        formulario = FormularioPrincipal()

    return render(request, "principal.html", {"form":formulario})
