import csv
import requests
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import IpForm

def ip_lookup(request):
    results = [] # Carga resultados previos SIEMPRE
    if request.method == 'POST':
        form = IpForm(request.POST)
        if form.is_valid():
            ip_list = form.cleaned_data['ip'].splitlines()
            for ip in ip_list:
                url = f"https://ipwhois.app/json/{ip.strip()}"
                try:
                    response = requests.get(url)
                    data = response.json()
                    if data.get("success", True):
                        results = request.session.get('results', []) 
                        results.append(data) 
                        request.session['results'] = results 
                    else:
                        results.append({'ip': ip, 'error': data.get('message', 'Error desconocido')})
                except Exception as e:
                    results.append({'ip': ip, 'error': str(e)})
            # request.session['results'] = results
    else:
        form = IpForm()
    
    print("Resultados actuales:", request.session['results'])
    return render(request, 'core/ip_lookup.html', {'form': form, 'results': results})


def download_csv(request):
    results = request.session.get('results', [])

    if not results:
        return HttpResponse("⚠️ No hay datos para exportar.")

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ips_info.csv"'

    headers = results[0].keys()
    writer = csv.DictWriter(response, fieldnames=headers, delimiter=';')
    writer.writeheader()

    for row in results:
        writer.writerow(row) 

    return response

def limpiar_resultados(request):
    request.session.pop('results', None)  # Elimina resultados de la sesión
    request.session['results'] = []  # Limpia los resultados en la sesión

    return redirect('ip_lookup') 