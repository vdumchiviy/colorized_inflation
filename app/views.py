from django.shortcuts import render
from django.conf import settings
import csv


def inflation_view(request):
    template_name = 'app/inflation.html'
    context = {}

    # чтение csv-файла и заполнение контекста
    csv.register_dialect('inflation_csv', delimiter=";")
    with open(settings.STATISTIC_FILE, mode="r", encoding="utf-8") as f:
        data_file = list(csv.reader(f, 'inflation_csv'))
    # row_number = 0
    # for data in data_file:
    #     row_data = list()
    #     row_data[row_number] = data[0]
    # context[row_number] = data[0]
    context = {"inflation_data": data_file}
    print(context)
    return render(request, template_name,
                  context)
