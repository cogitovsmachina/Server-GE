from django.http import HttpResponse# Create your views here.
from gala_endeavor_2011.models import *
from django.http import Http404, HttpResponseBadRequest
from django.utils import simplejson
from decimal import *

def index(request):
	return HttpResponse("Indice subasta. Gala Endeavor 2012")

def creaUsuario(request):
	
	if request.method == 'GET':
		return HttpResponse("")

	usuario 	=request.POST.get('usuario', False )
	nombre 		=request.POST.get('nombre', False )
	mesa 		=request.POST.get('mesa', False )

	if usuario == False or nombre == False or mesa == False:
		return HttpResponseBadRequest("Bad Request")

	usuario = Usuarios (user = usuario.strip().lower(), nombre = nombre.strip(), mesa = int(mesa))
	usuario.save(force_insert=True)

	return HttpResponse("OK")

def pujaProducto(request):
	
	if request.method == 'GET':
		return HttpResponse("Why are you entering through your browser??")
	
	usuario 	=request.POST.get('usuario', False ).strip()
	producto 	=request.POST.get('producto', False ).strip()
	precio 		=request.POST.get('precio', False ).strip()

		
	if usuario == False or producto == False or precio == False:
		return HttpResponseBadRequest("Bad Request")

	usuario = Usuarios.objects.get(user = usuario)
	producto = Productos.objects.get(id_prod = int(producto))


	user_offer = Decimal(precio)
	server_offer = Decimal(producto.costo_actual)

	if user_offer <= server_offer:
		print("Error: La oferta enviada por el usuario es menor que la existente en el servidor.")
		return HttpResponseBadRequest("Bad Request")


	producto.costo_actual = precio
	producto.last_bidder = usuario
	producto.save()
		
	Pujas (producto = producto, usuario = usuario, precio_actual = precio).save()
	
	
		
		
	return HttpResponse ("OK")


def pullProducto (request):

	productos = Productos.objects.all()
	
	alive = Alive.objects.get(pk=1)

	data = simplejson.dumps( {	'alive' : alive.alive,
																		'productos':[{	'id_producto': o.id_prod,\
																										'usuario' : iif (o.last_bidder_id=="user", None , o.last_bidder_id),\
																										'precio': str(o.costo_actual),
																		}
																		for o in productos]} )

	
	return HttpResponse (data)


def iif(conditional, true =True, false =False):
		if conditional:
			return true
		else:
			return false


def testForm (request):
	
	data = """ <html>
	<body>

	<form method="post" action="http://127.0.0.1:8000/endeavor/creaUsuario/" >
	Usuario: <input type="text" name="usuario" />
	Nombre: <input type="text" name="nombre" />
	Mesa: <input type="text" name="mesa" />
	<input type="submit" />
	</form>

	</body>
	</html>"""
	
	return HttpResponse( data )

	
	
