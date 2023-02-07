from django.shortcuts import render

def dashboard(
    request,
    template_name="dashboard.html", **kwargs
):
    context = {}
    return render(request, template_name=template_name, context=context)