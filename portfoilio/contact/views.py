from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your message has been sent")
            return redirect('contact:contact')
        else:
            messages.error("Please fix the error below")
    else:
        form = ContactForm()

    context = {
        'form':form,
    }
    return render(request, 'contact/contact_form.html', context)