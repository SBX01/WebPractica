from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Servicio, Reserva, TipoServicio , Calificacion , BlogPost
from django.contrib.auth.decorators import login_required 
from .forms import CustomUserForm, ContactForm
from django.contrib.auth import login, authenticate
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from datetime import datetime
from django.views.generic import DetailView





# Create your views here.

def Home(request):
    #para ver los precios en el home
    valoracion = Calificacion.objects.all()
    serv = Servicio.objects.all()
    #registro de comentario
   
    if request.POST:
       
        nota = Calificacion()
        nota.nombre = request.POST.get("nombreUsuario")
        nota.comentario = request.POST.get("comentario")
        nota.nota = request.POST.get("estrellas")
        nota.save();



    data = {
        'servicio':serv,
        'valoracion' : valoracion
    }

    return render(request, 'core/home.html', data)

   
#@login_required
def Agendar(request): 
    
    tipoSs = TipoServicio.objects.all()
    serv = Servicio.objects.none()
    hoy = date.today().isoformat() # Fecha actual
         
    if request.GET:

        action = request.GET['action']
        if action == 'buscar_TipoServicio':
            data = []
            for i in Servicio.objects.filter(tipo_id=request.GET['id']):
                data.append({'id': i.id , 'name': i.nombre ,'precio': i.precio})
                    
        else:
            data['error'] = 'Ha ocurrido un error'

        print(data)
        return JsonResponse(data, safe=False)
    
        
    #response = JsonResponse(data, safe=False)

    datosRetorno = {
        'servicio':serv,
        'tipo': tipoSs,
        'fecha': hoy        
    }  

    if request.POST:
        
        agenda = Reserva()
        nam = request.POST.get('txtNombre')
        last = request.POST.get('txtApellido')
        #agenda.nombre = /*str(nam)  + str(last) */
        agenda.nombre = nam +' '+ last
        agenda.telefono = request.POST.get('txtTelefono')
        agenda.email = request.POST.get('txtEmail')
        agenda.hora = request.POST.get('txtHora')
        agenda.fecha = request.POST.get('txtFecha')
       
        #saca el servicio
        
        service = Servicio.objects.filter(id= request.POST.get('cbTipoService')).first()
        
        agenda.servi = Servicio(service).pk

        #saca el tipo de servicio

        tipoServ = TipoServicio.objects.filter(id=request.POST.get('cbService')).first()
        agenda.tipo = TipoServicio(tipoServ).pk
        agenda.save()

        #Envio de correo de reserva
        form_nombre = nam +' '+ last
        form_email = request.POST.get('txtEmail')
       
        
        email_from =  settings.EMAIL_HOST_USER
        email_to = [form_email]
        asunto = 'Reserva'
        email_mensaje ='''Gracias por agendar %s 
        dentro de unos minutos sera contactado para agendar la hora'''%(form_nombre)

        send_mail(asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=True)
        
        fecha = datetime.strptime(request.POST.get('txtFecha'), '%Y-%m-%d')
        fechaMail = datetime.strftime(fecha,'%d/%m/%Y')
        #Aviso de reserva
        email_from =  settings.EMAIL_HOST_USER
        email_to =  [settings.EMAIL_HOST_USER]
        asunto = 'Nueva reserva de '+nam
        email_mensaje = '''
        Se ha realizado una nueva reserva.
        Hola, ''' + nam +' '+ last +''' ha hecho una nueva reserva para el dia '''+  fechaMail +'''. 
        se solicita:
        --- ''' + service.nombre + ''' 
        contacte al cliente al numero +56 '''+ request.POST.get('txtTelefono')
        print(type(fechaMail))
        print(fechaMail)
        send_mail(asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=True)

   
    
    return render(request, 'core/agendar.html',datosRetorno)

def Blog(request):
    vistaBlog = BlogPost.objects.all()
    datos = {
        'blogpost':vistaBlog
    }
    
    return render(request, 'core/blog.html', datos)

class VerPost(DetailView):
    template_name = 'core/post.html'
    model = BlogPost
    




