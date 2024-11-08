from django.shortcuts import render
from .models import Division,Office,Employee,Position,Supplier,Classification,Unit_list,Fund_cluster,Stock

# Create your views here.
def main(request):
    return render(request,'myapp/main.html')

def division(request):
    division = Division.objects.all()

    if request.method == "POST":
        if "div_add" in request.POST:
           division_name = request.POST.get("division_name")
           Division.objects.create(
               division_name = division_name
           )

        elif "div_update" in request.POST:
           id = request.POST.get("id")
           division_name = request.POST.get("division_name")

           update_division = Division.objects.get(id=id)
           update_division.division_name = division_name
           update_division.save()
        
        elif "div_delete" in request.POST:
            id = request.POST.get("id")
            Division.objects.get(id=id).delete()

           
    context = {"division_list":division}
    return render(request,'myapp/division.html',context)

def office(request):
    office = Office.objects.all()
    division = Division.objects.all()

    if request.method == "POST":
        if "office_add" in request.POST:
           office_name = request.POST.get("office_name")
           office_code = request.POST.get("office_code")
           division_name = request.POST.get("division_name")
           Office.objects.create(
               office_name = office_name,
               division_id = division_name,
               office_code = office_code
           )

        elif "office_update" in request.POST:
           id = request.POST.get("id")
           office_name = request.POST.get("office_name")
           office_code = request.POST.get("office_code")
           division_name = request.POST.get("division_name")

           update_office = Office.objects.get(id=id)
           update_office.office_name = office_name
           update_office.office_code = office_code
           update_office.division_id = division_name
           update_office.save()
        
        elif "office_delete" in request.POST:
            id = request.POST.get("id")
            Office.objects.get(id=id).delete()

           
    context = {"office_list":office,"division_list":division}
    return render(request,'myapp/office.html',context)

def employee(request):
    division = Division.objects.all()
    office = Office.objects.all()
    employee = Employee.objects.all()
    position = Position.objects.all()

    if request.method == "POST":    
        if "employee_add" in request.POST:
            employee_name = request.POST.get("employee_name")
            office_id = request.POST.get("office_name")
            position_id = request.POST.get("position_name")

            Employee.objects.create(
                employee_name = employee_name,
                office_id = office_id,
                position_id = position_id
            )
        elif "employee_update" in request.POST:
            id = request.POST.get("id")
            employee_name = request.POST.get("employee_name")
            office_id = request.POST.get("office_name")
            position_id = request.POST.get("position_name")

            update_employee = Employee.objects.get(id=id)
            update_employee.employee_name = employee_name
            update_employee.office_id = office_id
            update_employee.position_id = position_id
            update_employee.save()

        elif "employee_delete" in request.POST:
            id  = request.POST.get("id")
            Employee.objects.get(id=id).delete()

    context = {"office_list":office,"division_list":division,"employee_list":employee,"position_list":position}
    return render(request,'myapp/employee.html',context)

def position(request):
    position = Position.objects.all()

    if request.method == "POST":
        if "position_add" in request.POST:
           position_name = request.POST.get("position_name")
           Position.objects.create(
               position_name = position_name
           )

        elif "position_update" in request.POST:
           id = request.POST.get("id")
           position_name = request.POST.get("position_name")

           update_position = Position.objects.get(id=id)
           update_position.position_name = position_name
           update_position.save()
        
        elif "position_delete" in request.POST:
            id = request.POST.get("id")
            Position.objects.get(id=id).delete()

           
    context = {"position_list":position}
    return render(request,'myapp/position.html',context)

def supplier(request):
    supplier = Supplier.objects.all()

    if request.method == "POST":
        if "supplier_add" in request.POST:
           supplier_name = request.POST.get("supplier_name")
           Supplier.objects.create(
               supplier_name = supplier_name
           )

        elif "supplier_update" in request.POST:
           id = request.POST.get("id")
           supplier_name = request.POST.get("supplier_name")

           update_supplier = Supplier.objects.get(id=id)
           update_supplier.supplier_name = supplier_name
           update_supplier.save()
        
        elif "supplier_delete" in request.POST:
            id = request.POST.get("id")
            Supplier.objects.get(id=id).delete()

           
    context = {"supplier_list":supplier}
    return render(request,'myapp/supplier.html',context)

def classification(request):
    classification = Classification.objects.all()

    if request.method == "POST":
        if "classification_add" in request.POST:
           class_name = request.POST.get("classification_name")
           Classification.objects.create(
               class_name = class_name
           )

        elif "classification_update" in request.POST:
           id = request.POST.get("id")
           class_name = request.POST.get("classification_name")

           update_classification = Classification.objects.get(id=id)
           update_classification.class_name = class_name
           update_classification.save()
        
        elif "classification_delete" in request.POST:
            id = request.POST.get("id")
            Classification.objects.get(id=id).delete()

           
    context = {"classification_list":classification}
    return render(request,'myapp/classification.html',context)


def unit(request):
    unit = Unit_list.objects.all()

    if request.method == "POST":
        if "unit_add" in request.POST:
           unit_measure = request.POST.get("unit_name")
           Unit_list.objects.create(
               unit_measure = unit_measure
           )

        elif "unit_update" in request.POST:
           id = request.POST.get("id")
           unit_measure = request.POST.get("unit_name")

           update_unit = Unit_list.objects.get(id=id)
           update_unit.unit_measure = unit_measure
           update_unit.save()
        
        elif "unit_delete" in request.POST:
            id = request.POST.get("id")
            Unit_list.objects.get(id=id).delete()

           
    context = {"unit_list":unit}
    return render(request,'myapp/unit.html',context)

def fund(request):
    fund = Fund_cluster.objects.all()

    if request.method == "POST":
        if "fund_add" in request.POST:
           fund_name = request.POST.get("fund_name")
           fund_code = request.POST.get("fund_code")
           Fund_cluster.objects.create(
               fund_name = fund_name,
               fund_code = fund_code
           )

        elif "fund_update" in request.POST:
           id = request.POST.get("id")
           fund_name = request.POST.get("fund_name")
           fund_code = request.POST.get("fund_code")

           update_fund = Fund_cluster.objects.get(id=id)
           update_fund.fund_name = fund_name
           update_fund.fund_code = fund_code
           update_fund.save()
        
        elif "fund_delete" in request.POST:
            id = request.POST.get("id")
            Fund_cluster.objects.get(id=id).delete()

           
    context = {"fund_list":fund}
    return render(request,'myapp/fund.html',context)

#last code
def stock(request):
    stock = Stock.objects.all()
    unit = Unit_list.objects.all()

    if request.method == "POST":    
        if "stock_add" in request.POST:
            stock_num = request.POST.get("stock_num")
            stock_name = request.POST.get("stock_name")
            unit_id = request.POST.get("unit_measure")
            stock_qty = request.POST.get("stock_qty")
            unit_cost = request.POST.get("unit_cost")

            Stock.objects.create(
                stock_num = stock_num,
                stock_name = stock_name,
                unit_id = unit_id,
                stock_qty = stock_qty,
                unit_cost = unit_cost
            )

        elif "stock_update" in request.POST:
            id = request.POST.get("id")
            stock_num = request.POST.get("stock_num")
            stock_name = request.POST.get("stock_name")
            unit_id = request.POST.get("unit_measure")
            stock_qty = request.POST.get("stock_qty")
            unit_cost = request.POST.get("unit_cost")

            update_stock = Stock.objects.get(id=id)
            update_stock.stock_num = stock_num
            update_stock.stock_name = stock_name
            update_stock.unit_id = unit_id
            update_stock.stock_qty = stock_qty
            update_stock.unit_cost = unit_cost
            update_stock.save()

        elif "stock_delete" in request.POST:
            id  = request.POST.get("id")
            Stock.objects.get(id=id).delete()

    context = {"stock_list":stock,"unit_list":unit}
    return render(request,'myapp/stock.html',context)