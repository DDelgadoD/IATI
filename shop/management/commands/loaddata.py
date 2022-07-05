import json
import os
from django.core.management.commands import loaddata
from shop.models import Product, Cap, Shirt


def new_record(record):
    if record['model'] == 'shop.product':
        return not Product.objects.filter(pk=record['pk']).exists()
    elif record['model'] == 'shop.cap':
        return not Cap.objects.filter(pk=record['pk']).exists()
    elif record['model'] == 'shop.shirt':
        return not Shirt.objects.filter(pk=record['pk']).exists()
    else:
        return True


class Command(loaddata.Command):
    def handle(self, *args, **options):
        args = list(args)
        file_name = args[0]

        with open(file_name) as json_file:
            json_list = json.load(json_file)

        json_list_new = list(filter(new_record, json_list))
        if not json_list_new:
            print("All data are already previously loaded")
            return

        # Write the updated JSON file because only accepts json from file
        file_dir_and_name, file_ext = os.path.splitext(file_name)
        file_temp = f"{file_dir_and_name}_temp{file_ext}"
        with open(file_temp, 'w') as json_file_temp:
            json.dump(json_list_new, json_file_temp)

        # json with only new records to regular loaddata.py from django
        args[0] = file_temp
        super().handle(*args, **options)
        os.remove(file_temp)
