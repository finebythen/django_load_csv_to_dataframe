from django.shortcuts import render
import pandas as pd
import json


def main(request):
    df = None
    context = {}

    if request.method == 'POST' and request.FILES['myFile']:
        myFile = request.FILES['myFile']

        try:
            df = pd.read_csv(myFile, sep=';')
            json_raw = df.to_json(orient='records')
            json_df = json.loads(json_raw)
            context = {'json_df': json_df}
        except FileNotFoundError:
            pass

    return render(request, 'app_csv_to_dataframe/main.html', context)
