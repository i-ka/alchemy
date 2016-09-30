from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from AlchemyCommon.models import Element, Category, User, Report
from .forms import ElementForm
from django.http import HttpResponse, Http404
# Create your views here.


@permission_required('AlchemyCommon.can_change_element', login_url='/login/', raise_exception=True)
def index(request):
    users_count = User.objects.count()
    elements_count = Element.objects.count()
    categories_count = Category.objects.count()
    return render(request, 'AlchemyAdmin/admin_menu.html', {
        'users_count': users_count,
        'elements_count': elements_count,
        'categories_count': categories_count
        })

@permission_required('AlchemyCommon.can_change_element', login_url='/login/', raise_exception=True)
def elements_list(request):
    all_elements = Element.objects.all()
    return render(request, 'AlchemyAdmin/elements_list.html', {
            'elements': all_elements,
        })

@permission_required('auth.can_change_user', login_url='/login/', raise_exception=True)
def users_list(request):
    users = User.objects.all()
    return render(request, 'AlchemyAdmin/users_list.html', {'users': users})

@permission_required('auth.can_change_user', login_url='/login/', raise_exception=True)
def set_user_active(request, userId, active):
    user = get_object_or_404(User, pk=userId)
    if active == '0':
        user.is_active = False
    elif active == '1':
        user.is_active = True
    user.save()
    return redirect('/alch-admin/users-list')



@permission_required('AlchemyCommon.can_change_report', raise_exception=True)
def feedback_list(request, filter):
    if filter == 'accepted':
        reports = Report.objects.filter(accepted=True).order_by('-date')
    elif filter == 'rejected':
        reports = Report.objects.filter(accepted=False).order_by('-date')
    elif filter == 'notviewed':
        reports = Report.objects.filter(accepted=None).order_by('-date')
    elif filter == 'all':
        reports = Report.objects.all().order_by('-date')
    else:
        raise Http404()
    return render(request, 'AlchemyAdmin/feedback_list.html', { 'report_list': reports })


@permission_required('AlchemyCommon.can_change_report', raise_exception=True)
def set_report(request, reportId, val):
    rep = get_object_or_404(Report, pk=reportId)
    if val == 'accepted':
        value = True
    elif val == 'rejected':
        value = False
    else:
        raise Http404()
    if value != rep.accepted:
        rep.accepted = value
        rep.save()
    redirect_url = request.GET.get('next', False)
    if redirect_url:
        return redirect(redirect_url)
    else:
        return redirect(reverse('aladmin:feedback-list', args=('all',)))


@permission_required('AlchemyCommon.can_change_report', raise_exception=True)
def report_details(request, reportId):
    report = get_object_or_404(Report, pk=reportId)
    return render(request, 'AlchemyAdmin/report_details.html', {'report': report})


@permission_required('AlchemyCommon.can_delete_element', login_url='/login/', raise_exception=True)
def remove_element(request, el_id):
    element_to_delete = Element.objects.get(pk=el_id)
    conflict_elements = element_to_delete.check_on_delete()
    print(conflict_elements)
    if not conflict_elements:
        element_to_delete.delete()
        return redirect('/alch-admin/elements-list')
    error = True
    return render(request, 'AlchemyAdmin/elements_list.html', {
        'element_to_delete': element_to_delete,
        'error': error,
        'elements': conflict_elements
        })

@permission_required('AlchemyCommon.can_change_element', login_url='/login/', raise_exception=True)
def update_element(request, el_id):
    updated_element = Element.objects.get(pk=el_id)
    if request.method == 'POST':
        form = ElementForm(request.POST, instance=updated_element)
        if form.is_valid():
            form.save()
            return redirect('/alch-admin/elements-list')
    else:
        form = ElementForm(instance=updated_element)
    return render(request, 'AlchemyAdmin/add_element_form.html', {
        'updated_element': updated_element,
        'form': form,
        'update': True
        })

@permission_required('AlchemyCommon.can_add_element', login_url='/login/', raise_exception=True)
def create_element(request):
    if request.method == 'POST':
        form = ElementForm(request.POST)
        if form.is_valid():
            form.save()
            if form.instance.is_essential_element():
                for user in User.objects.all():
                    user.profile.open_elements.add(form.instance)
            return redirect('/alch-admin/elements-list')
    else:
        form = ElementForm()
    return render(request, 'AlchemyAdmin/add_element_form.html', {
        'form': form,
        })

@permission_required('AlchemyCommon.can_add_category', login_url='/login/', raise_exception=True)
def create_category(request):
    name = request.POST.get('name', False)
    if (not name):
        return HttpResponse('failed')
    if (not Category.objects.filter(name=name).exists()):
        new_category = Category(name=name)
        new_category.save()
        return HttpResponse('success')
    else:
        return HttpResponse('failed')