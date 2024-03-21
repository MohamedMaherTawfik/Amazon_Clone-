from .models import Company

def Get_Company_data(request):
    data=Company.objects.last()
    return{'company_data':data}