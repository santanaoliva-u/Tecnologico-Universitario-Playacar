import pyperclip  # Asegúrate de instalar esta librería con `pip install pyperclip`
import random
# Lista de títulos ampliados
titulos = [
    "💈 ¡Transforma tu Estilo con Nosotros!",
    "🪒 ¡Renueva Tu Imagen Profesionalmente!",
    "💇‍♂️ ¡La Mejor Experiencia en Cortes Masculinos!",
    "🌟 ¡Destaca con un Corte a la Altura de Tu Estilo!",
    "🪒 ¡Cortes Exclusivos para Hombres Únicos!",
    "💇‍♂️ Estilo y Elegancia al Alcance de Tu Mano",
    "💈 ¡Vuelve a Sentirte como Nuevo con Nosotros!",
    "🪒 La Perfección en Cada Corte",
    "🌟 Cortes Personalizados para Cada Estilo",
    "🪒 El Arte del Cuidado Masculino",
    "💇‍♂️ ¡El Corte Que Siempre Has Querido Está Aquí!",
    "💈 Tu Estilo, Nuestro Compromiso",
    "🪒 ¡Eleva tu Imagen con Cortes Únicos!",
    "🌟 Lo Mejor para Tu Estilo Personal",
    "💇‍♂️ ¡Descubre tu Nuevo Look con los Expertos!",
    "💈 ¡Atrévete a Cambiar tu Imagen Hoy Mismo!",
    "🪒 Cortes que Hablan por Ti",
    "🌟 Tu Look Perfecto Te Está Esperando",
    "🪒 ¡Haz que Tu Estilo Destaque!",
    "💇‍♂️ Cortes y Estilo sin Compromisos",
    "💈 Haz que tu Corte Hable de Ti",
    "🪒 La Imagen que Mereces",
    "🌟 ¡Transformamos Tu Look en Cada Visita!",
    "💇‍♂️ Cortes Únicos Para Personalidades Únicas",
    "🪒 El Cuidado Profesional que Tu Imagen Necesita"
]

# Lista de servicios mejorados sin descripciones
servicios = [
    "✔️ Cortes modernos y clásicos.",
    "✔️ Diseño y perfilado de barba.",
    "✔️ Tratamientos premium.",
    "✔️ Cortes personalizados para todos los estilos.",
    "✔️ Diseño único para cada cliente.",
    "✔️ Estilizado y acabado con productos de alta calidad.",
    "✔️ Asesoría en estilo personal.",
    "✔️ Afeitado profesional con navaja.",
    "✔️ Corrección de corte y retoque.",
    "✔️ Servicios para eventos especiales."
]

# Información adicional
ubicacion = "📍 Ubicación: 77724, Guadalupana, Playa del Carmen, México."
correo = "📧 Correo: santanabarberoprofesional@gmail.com"
telefono = "📞 Contáctame: 984 187 0157"
precios_link = "👉 Menú de precios: https://drive.google.com/file/d/1__XEFjZ-7ZO0uEx3jOsbJijsowFFb7UW/view"
catalogo_link = "👉 Catálogo de cortes: https://drive.google.com/file/d/1-Ryuki1rlEuo5TlElQ5VB_mOgOnctMfC/view"
sitio_web = "🌐 Visítanos en: https://santanabarberoprofesional.com"

# Hashtags SEO mejorados
hashtags = (
    "#BarberoPlayaDelCarmen #CortesDeCabello #EstiloProfesional #BarberShopPlaya #CortesParaHombres "
    "#CortesMasculinos #CortesDeCabelloPlayaDelCarmen #EstiloPersonal #LookPerfecto #CuidadoMasculino "
    "#CorteDeCabello #BarbaPerfecta #CorteDeCabelloPlaya #BarberíaPlayaDelCarmen #CorteDeBarba "
    "#EstiloMasculino #TransformaTuImagen #CortesDeEstilo #BarberosProfesionales #CortesDeModa "
    "#CorteDeCabelloConEstilo #BarberíaDeCalidad #CorteDeCabelloPremium #CortePersonalizado #CorteDeCabelloÚnico"
)

# Función para generar el post con todos los servicios
def generar_post():
    titulo = random.choice(titulos)
    
    # Generar el listado de todos los servicios
    lista_servicios = "\n".join(servicios)
    
    post = (
        f"{titulo}\n\n"
        f"{lista_servicios}\n\n"
        f"{ubicacion}\n"
        f"{correo}\n"
        f"{telefono}\n"
        f"{precios_link}\n"
        f"{catalogo_link}\n"
        f"{sitio_web}\n\n"
        "🌟 ¡Transformemos tu imagen hoy mismo!\n"
        f"{hashtags}"
    )
    return post

# Generar y copiar el post al portapapeles
post_generado = generar_post()
pyperclip.copy(post_generado)  # Copia el post generado al portapapeles
print("Post generado y copiado al portapapeles:")
print(post_generado)

