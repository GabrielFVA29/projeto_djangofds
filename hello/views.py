from simulador.views import inicio


def index(request):
    """Página inicial do site: abre direto a tela de abertura do simulador (T1)."""
    return inicio(request)
