def importe_total(request):
    total = 0
    if request.user.is_authenticated:

        #if 'carro' in request.session:
        for key, value in request.session['carro'].items():
            total = total +(float(value['creditos'])*value['cantidad'])

    else:
        total="Debes Iniciar Sesión"

    return {'importe_total':total} 