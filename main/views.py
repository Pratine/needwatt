from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render
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
        tension = request.POST['tension_selection_combo']
        cicle = request.POST['cicle_selection_combo']
        price_p_month = request.POST["value_p_month"]

        # For BTN
        if tension == "1":
            hired_power = request.POST["hired-power"]

            # For simple
            if cicle == "1":
                save = simulations.simulation_btn_simple(float(hired_power),
                                                         float(price_p_month))

                '''message = get_template("email_btn.html").render(Context({
                    'name': simulation_name,
                    'cicle_selection_combo': cicle,
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
                mail.send()'''

                return render(request, 'simulation.html', {'simulation_name': simulation_name})

            # For Bi-Hor
            elif cicle == "2":
                save = simulations.simulation_btn_bi_hor(float(hired_power),
                                                         float(price_p_month))

                '''message = get_template("email_btn.html").render(Context({
                    'name': simulation_name,
                    'cicle_selection_combo': cicle,
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
                mail.send()'''

                return render(request, 'simulation.html', {'simulation_name': simulation_name})

            # For Tri-Hor
            elif cicle == "3":
                save = simulations.simulation_btn_tri_hor(float(hired_power),
                                                          float(price_p_month))

                '''message = get_template("email_btn.html").render(Context({
                    'name': simulation_name,
                    'cicle_selection_combo': cicle,
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
                mail.send()'''

                return render(request, 'simulation.html', {'simulation_name': simulation_name})

        # For BTE
        elif tension == "2":

            tarrif_pontas = request.POST['input_tarrif_pontas']
            tarrif_cheias = request.POST['input_tarrif_cheias']
            tarrif_vazio_normal = request.POST['tarrif_vazio_normal']
            tarrif_super_vazio = request.POST['tarrif_vazio_normal']
            network = request.POST['network']

            # With Networks
            if network == "0":
                save = simulations.simulation_bte_with_network(float(tarrif_pontas),
                                                               float(tarrif_cheias),
                                                               float(tarrif_vazio_normal),
                                                               float(tarrif_super_vazio),
                                                               float(price_p_month))

                '''message = get_template("email_bte.html").render(Context({
                    'name': simulation_name,
                    'cicle_selection_combo': cicle,
                    'save_percentage': save,
                }))

                mail = EmailMessage(
                    subject="Simulação energética da NeedWatt",
                    body=message,
                    from_email='noreply@needwatt.com',
                    to=simulation_email,
                )
                mail.content_subtype = "html"
                mail.send()'''

                return render(request, 'simulation.html', {'simulation_name': simulation_name})

            # Without Networks
            if network == "1":
                save = simulations.simulation_bte_without_network(float(tarrif_pontas),
                                                                  float(tarrif_cheias),
                                                                  float(tarrif_vazio_normal),
                                                                  float(tarrif_super_vazio),
                                                                  float(price_p_month))

                '''message = get_template("email_bte.html").render(Context({
                    'name': simulation_name,
                    'cicle_selection_combo': cicle,
                    'save_percentage': save,
                }))

                mail = EmailMessage(
                    subject="Simulação energética da NeedWatt",
                    body=message,
                    from_email='noreply@needwatt.com',
                    to=simulation_email,
                )
                mail.content_subtype = "html"
                mail.send()'''

                return render(request, 'simulation.html', {'simulation_name': simulation_name})

        # For MT
        elif tension == "3":

            tarrif_pontas = request.POST['input_tarrif_pontas']
            tarrif_cheias = request.POST['input_tarrif_cheias']
            tarrif_vazio_normal = request.POST['tarrif_vazio_normal']
            tarrif_super_vazio = request.POST['tarrif_vazio_normal']
            network = request.POST['network']

            # With Networks
            if network == "0":
                save = simulations.simulation_mt_with_network(float(tarrif_pontas),
                                                              float(tarrif_cheias),
                                                              float(tarrif_vazio_normal),
                                                              float(tarrif_super_vazio),
                                                              float(price_p_month))

                '''message = get_template("email_bte.html").render(Context({
                    'name': simulation_name,
                    'cicle_selection_combo': cicle,
                    'save_percentage': save,
                }))

                mail = EmailMessage(
                    subject="Simulação energética da NeedWatt",
                    body=message,
                    from_email='noreply@needwatt.com',
                    to=simulation_email,
                )
                mail.content_subtype = "html"
                mail.send()'''

                return render(request, 'simulation.html', {'simulation_name': simulation_name})

            # Without Networks
            if network == "1":
                save = simulations.simulation_mt_without_network(float(tarrif_pontas),
                                                                 float(tarrif_cheias),
                                                                 float(tarrif_vazio_normal),
                                                                 float(tarrif_super_vazio),
                                                                 float(price_p_month))

                '''message = get_template("email_bte.html").render(Context({
                    'name': simulation_name,
                    'cicle_selection_combo': cicle,
                    'save_percentage': save,
                }))

                mail = EmailMessage(
                    subject="Simulação energética da NeedWatt",
                    body=message,
                    from_email='noreply@needwatt.com',
                    to=simulation_email,
                )
                mail.content_subtype = "html"
                mail.send()'''

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
