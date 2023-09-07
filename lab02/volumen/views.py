from django.shortcuts import render
import math

def index(request):
    return render(request, 'volumen/form.html',{
        "tittle" : "Calculo del volumen de un cilindro "
    })

def send(request):
    try:
        radio = float(request.POST['diametro']) / 2
        altura = float(request.POST['altura'])

        volumen = math.pow(radio, 2) * math.pi * altura

        return render(request, 'volumen/result.html', {
            "title": "Volumen del cilindro",
            "volumen": volumen
        })
    except ValueError:
        return render(request, 'volumen/form.html', {
            "error_message": "Asegúrate de que los valores proporcionados sean números válidos."
        })


