from django.shortcuts import redirect

def cliente_activo(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.session.get('cliente_id'):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return _wrapped_view_func

