from django.shortcuts import render

def index(request):
    return render(request, 'calculadora/form.html',{"tittle":"Calculator"})

def send(request):
    result = 0
    number1 = int(request.POST['number1'])
    number2 = int(request.POST['number2'])
    
    if(request.POST['operation'] == 'suma'):
        result = number1 + number2      
    elif request.POST['operation'] == 'resta':
        result = number1 - number2
    elif request.POST['operation'] == 'multiplicacion':
        result = number1 * number2
    elif request.POST['operation'] == 'division':
        result = number1 / number2

    return render(request, 'calculadora/result.html', {
        "number1" : request.POST['number1'],
        "number2" : request.POST['number2'],
        "operation" : request.POST['operation'],
        "result" : result,
        "tittle" : "Result",
    })
