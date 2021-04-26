from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context

# Create your views here.
from django.template.loader import render_to_string, get_template
from . import simulations


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name,
            message,
            message_email,
            ['geral@needwatt.com'],
            fail_silently=True,
        )
        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})


def simulation(request):
    if request.method == "POST":
        simulation_name = request.POST['simulation-name']
        simulation_email = request.POST['simulation-email']
        tension = request.POST['tension']
        hired_power = request.POST["hired-power"]
        cicle = request.POST['cicle']

        if tension == "btn":
            day_start = request.POST["day-start"]
            day_end = request.POST["day-end"]
            n_days = day_end - day_start
            price_p_month = request.POST["price-p-month"]

            if cicle == "simple":
                save = simulations.simulation_btn_simple(hired_power,
                                                         n_days,
                                                         price_p_month)
                message = get_template("email_btn.html").render(Context({
                    'name': simulation_name,
                    'cicle': cicle,
                    'hired_power': hired_power,
                    'save_percentage': save,
                }))
                mail = EmailMessage(
                    subject="Simulação energética da NeedWatt",
                    body=message,
                    from_email='noreply@needwatt.com',
                    to=simulation_email,
                )
                mail.content_subtype = "html"
                mail.send()

                return render(request, 'simulation.html', {'simulation_name': simulation_name})

            elif cicle == "bi_hor":
                save = simulations.simulation_btn_bi_hor(hired_power,
                                                         n_days,
                                                         price_p_month)
                message = get_template("email_btn.html").render(Context({
                    'name': simulation_name,
                    'cicle': cicle,
                    'hired_power': hired_power,
                    'save_percentage': save,
                }))
                mail = EmailMessage(
                    subject="Simulação energética da NeedWatt",
                    body=message,
                    from_email='noreply@needwatt.com',
                    to=simulation_email,
                )
                mail.content_subtype = "html"
                mail.send()

                return render(request, 'simulation.html', {'simulation_name': simulation_name})

            elif cicle == "tri_hor":
                save = simulations.simulation_btn_tri_hor(hired_power,
                                                          n_days,
                                                          price_p_month)
                message = get_template("email_btn.html").render(Context({
                    'name': simulation_name,
                    'cicle': cicle,
                    'hired_power': hired_power,
                    'save_percentage': save,
                }))
                mail = EmailMessage(
                    subject="Simulação energética da NeedWatt",
                    body=message,
                    from_email='noreply@needwatt.com',
                    to=simulation_email,
                )
                mail.content_subtype = "html"
                mail.send()

                return render(request, 'simulation.html', {'simulation_name': simulation_name})

        elif tension == "bte":
            tarrif_pontas = request.POST['tarrif-pontas']
            tarrif_cheias = request.POST['tarrif-cheias']
            tarrif_vazio_normal = request.POST['tarrif-vazio_normal']
            tarrif_super_vazio = request.POST['tarrif-super-vazio']
            price_p_month = request.POST['price-p-month']

            save = simulations.simulation_bte(tarrif_pontas,
                                              tarrif_cheias,
                                              tarrif_vazio_normal,
                                              tarrif_super_vazio,
                                              price_p_month)

            message = get_template("email_bte.html").render(Context({
                'name': simulation_name,
                'cicle': cicle,
                'hired_power': hired_power,
                'tarrif_ponta': tarrif_pontas,
                'tarrif_cheia': tarrif_cheias,
                'tarrif_vazio_normal': tarrif_vazio_normal,
                'tarrif_super_vazio': tarrif_super_vazio,
                'save_percentage': save,
            }))

            mail = EmailMessage(
                subject="Simulação energética da NeedWatt",
                body=message,
                from_email='noreply@needwatt.com',
                to=simulation_email,
            )
            mail.content_subtype = "html"
            mail.send()

            return render(request, 'simulation.html', {'simulation_name': simulation_name})

        elif tension == "mt":
            tarrif_pontas = request.POST['tarrif-pontas']
            tarrif_cheias = request.POST['tarrif-cheias']
            tarrif_vazio_normal = request.POST['tarrif-vazio_normal']
            tarrif_super_vazio = request.POST['tarrif-super-vazio']
            price_p_month = request.POST['price-p-month']

            save = simulations.simulation_mt(tarrif_pontas,
                                             tarrif_cheias,
                                             tarrif_vazio_normal,
                                             tarrif_super_vazio,
                                             price_p_month)

            message = get_template("email_mt.html").render(Context({
                'name': simulation_name,
                'cicle': cicle,
                'hired_power': hired_power,
                'tarrif_ponta': tarrif_pontas,
                'tarrif_cheia': tarrif_cheias,
                'tarrif_vazio_normal': tarrif_vazio_normal,
                'tarrif_super_vazio': tarrif_super_vazio,
                'save_percentage': save,
            }))

            mail = EmailMessage(
                subject="Simulação energética da NeedWatt",
                body=message,
                from_email='noreply@needwatt.com',
                to=simulation_email,
            )
            mail.content_subtype = "html"
            mail.send()

            return render(request, 'simulation.html', {'simulation_name': simulation_name})

    else:
        return render(request, 'simulation.html', {})


def about(request):
    return render(request, 'about.html', {})


def service(request):
    return render(request, 'service.html', {})


# Views related with the many services that NeedWatt offer

# Start

def merca_lib_ener(request):
    return render(request, 'merca_lib_ener.html', {})


def bater_conde(request):
    return render(request, 'bater_conde.html', {})


def autit_cert_ener(request):
    return render(request, 'autit_cert_ener.html', {})


def carrega_viatu_eletric(request):
    return render(request, 'carrega_viatu_eletric.html', {})


def ilumina_led(request):
    return render(request, 'ilumina_led.html', {})


def autoconsumo_foto(request):
    return render(request, 'autoconsumo_foto.html', {})


def sistem_monito_energ(request):
    return render(request, 'sistem_monito_energ.html', {})

# End
