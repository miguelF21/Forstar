from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse




def index(request):
          return render(request,'index.html')
      
      
      
def cuerpo(request):
    return render(request,'cuerpo.html') 




def pruebas(request, nombre,edad):
    
    nomb_usuario=nombre+"perez";
    
    
    return HttpResponse(f"""<h1>Pagiana de prueba<h1>
                        
                            <h2>Mi nombre es: {nomb_usuario} y tengo {edad} años <h2>""")
    
    