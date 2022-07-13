from spellchecker import SpellChecker
import re
from django.shortcuts import render
from .forms import FormularioPrincipal
from .models import Revisor
import string
import secrets

num = 1000 # define the length of the random string

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

            resultado = []
            lista1 = []
            lista2 = []
            desconocidas = []

            spell = SpellChecker(language=None, case_sensitive=False)  # lenguaje ninguno, distinguir entre mayusculas y minusculas
            spell.word_frequency.load_text_file('textprueba.txt')

            usuario = guarani.texto
            minuscula = usuario.lower()

            dashpattern = re.compile("(\w+)?- (\w+)")
            # replaces non-char
            sentmarker = re.compile('[»\,\:;!()”–"¿¡?-]')

            text = dashpattern.sub(r"\1\2", minuscula)

            text = sentmarker.sub('', text)
            text = text.replace("’", "'")
            text = text.replace("´", "'")
            text = text.replace(".", " ")
            text = text.replace("ä", "ã")
            text = text.replace("â", "ã")
            text = text.replace("ā", "ã")
            text = text.replace("à", "á")
            text = text.replace("è", "é")
            text = text.replace("ê", "ẽ")
            text = text.replace("ē", "ẽ")
            text = text.replace("ë", "ẽ")
            text = text.replace("ï", "ĩ")
            text = text.replace("î", "ĩ")
            text = text.replace("ī", "ĩ")
            text = text.replace("ì", "í")
            text = text.replace("ö", "õ")
            text = text.replace("ō", "õ")
            text = text.replace("ô", "õ")
            text = text.replace("ò", "ó")
            text = text.replace("ū", "ũ")
            text = text.replace("ü", "ũ")
            text = text.replace("û", "ũ")
            text = text.replace("ù", "ú")
            text = text.replace("ÿ", "ỹ")
            text = text.replace("ĝ", "g̃")
            text = text.replace("§", "g̃")
            limpio = text.split()
            #print("limpio recibe",limpio)
            palabraincorrecta = spell.unknown(limpio)  # traer lo que no está en el corpus/diccionario
            print("las palabras equivocadas son: ", palabraincorrecta)  # la tipo set

            if len(palabraincorrecta) == 0:
                print("Todo está bien escrito")
                res = 'Todo esta bien escrito'
                return render(request, "principal.html", {"message": res, "form": formulario})

            for palabra in palabraincorrecta:
                if palabra != spell.correction(palabra):

                    candi = spell.candidates(
                        palabra)  # Devuelve un conjunto de posibles candidatos para la palabra mal escrita

                    lista1.append(palabra)
                    lista2.append(list(candi))
                    print('la nueva lista es', lista2)
                    resultado = list(zip(lista1, lista2))
                    print("el serultado es", resultado)

                else:
                    desconocidas.append(palabra)
                    # print("**************desconocidas",desconocidas,type(desconocidas))
                    if len(desconocidas) == 0:
                        desconocidas = ' '

            if len(resultado) == 0:
                resultado = ' '
            res = 'Resultados '

            guarani.save()

            return render(request, "principal.html", {"message": res, "resultado": resultado, "desconocidas": desconocidas, "form": formulario})

    else:
        formulario = FormularioPrincipal()

    return render(request, "principal.html", {"form":formulario})

