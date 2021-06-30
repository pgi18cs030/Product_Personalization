from django.shortcuts import render
from django.http import HttpResponse
import pickle
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import json
from sklearn.preprocessing import StandardScaler

# Create your views here.
def index(request):
    return render(request,'index.html')

def cloths(request):
    context = {'data1': ['ARBO', 'TEE_BUD', 'Lev', 'SATDEVANGIKHADIBHAND', 'Purple_Sta',
                         'Scott_Internation', 'AXMA', 'Tees_Collecti', 'Bindass_Bo',
                         'dream_o', 'FancyW', 'Sherr', 'R', 'KPS_Clothi', 'GANTI',
                         'Black_Bull_Design_Stud', 'Welwe', 'REAZ', 'Fuel_Clothi', 'ShreeR',
                         'Sketch_Vib', 'Bumm', 'Fesn', 'Ravil', 'NEVER_LO', 'CLOTH',
                         'Royalty_Retail_And_Expo', 'Fresh_Fe', 'MODERN_CR', 'INTER_CREATI',
                         'G'],
               'data2': ['T10_Spor', 'York', 'Lucky_Rog', 'GYMBROTHE', 'Fila', 'Keo',
                         'Szto', 'NEBRAS', 'SayItLo', 'KAY_D', 'ATHL', 'Byford_by_Pantaloo',
                         'Mohr', 'AS_Tre', 'Flyer'],
               'data3' :['LDHSA', 'Marca_Disa', 'Vector', 'Bone', 'limited_colou', 'TeeMoo',
                         'MR_FASHI', 'Steenb', 'Asa', 'The_HOLLAND', 'FASHION_WOU',
                         'US_POLO_Associati', 'A_J_Styl', 'CANTAB'],
               'data4' :[x for x in range(500,5000,10)]
                }
    return render(request,'cloths.html',context)


def footwear(request):
    context = {'data1': ['ZACK_Fo', 'Mett', 'DISCOUNT_OUTL', 'allan_pet', 'MagMatri',
                         'SEVN', 'LIVST', 'saltla', 'Man', 'Cots', 'adidas_Origina',
                         'Crocks_Cl', 'BlackSN', 'Lafant', 'RodZ', 'PROLI', 'Lucky_Bi',
                         'MASH_UNLIMIT'],
               'data2': ['Uber_Urb', 'Fairdea', 'REEBOK_CLASSI', 'Footprin', 'BlueSha',
                         'ModeWa', 'RRENTERPRI', 'EverLa', 'Truemo', 'SORA', 'GLO',
                         'Jai_Textil', 'Bonnevil', 'Jagdish_Garmen'],
               'data3': ['Mo', 'Solid_Styl', 'HUMBE', 'HaltonHil', 'East_I',
                          'JACK_AND_HAR', 'Pol', 'The_Arch', 'SUR', 'V', 'Clo', 'Inspi',
                          'ABC_ANY_BUDY_CLE', 'TOM_BU'],
               'data4': [x for x in range(500, 5000, 10)]
               }
    return render(request, 'footwear.html', context)

def cosmetic(request):
    context = {'data1': ['VOXA', 'ATTIITU', 'Mylifestylebazz', 'Amp', 'Black_Beat', 'K',
                         'CA', 'ECKO_Unl', 'Cher', 'rockha'],
               'data2': ['chawla_fashi', 'M7_By_Metrona', 'Adam_Park', 'Sharar', 'VARTe',
                         'Paridhanlok_Onli', 'Styleska', 'FOOT_F', 'Wab', 'FLEXIM'],
               'data3': ['Urban_D', 'yellowvib', 'Mountain_colou', 'RELIEF_ZO', 'PIX',
                         'NETT'],
               'data5': ['FOREVER_YOU', 'CupidSto', 'Rose_We', 'Xi', 'Mah', 'REF', 'Onei'],

               'data4': [x for x in range(500, 5000, 10)]
               }
    return render(request, 'cosmetic.html', context)

def bags(request):
    context = {'data1': ['Oka', 'Wildst', 'True_Bl', 'vims_rai', 'Shoef', 'Simon_Rob',
                         'US_Polo_As', 'US_POLO_ASS', 'Breakboun'],
               'data2': ['Gracew', 'REEB', 'Free_Authori', 'Dudli', 'Pu', 'A', 'PixF'],
               'data4': [x for x in range(500, 5000, 10)]
               }
    return render(request, 'bags.html', context)

def prediction(data):
    dataset = pd.read_csv('user_product_attraction.csv')
    features = dataset[['Sub_category', 'Brand', 'Price', 'Quantity']]
    labels = dataset[['Offer']]
    labels = np.array(labels, dtype='int64').ravel()
    encoder = ColumnTransformer([('encoder', OneHotEncoder(), [0, 1])], remainder='passthrough')
    features = encoder.fit_transform(features)
    features = features.toarray()
    temp1 = features[:, 1:12]
    temp2 = features[:, 13:]
    features = np.concatenate((temp1, temp2), axis=1)
    features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    features_train = scaler.fit_transform(features_train)

    pred_df=encoder.transform(data)
    pred_df = pred_df.toarray()
    temp1 = pred_df[:, 1:12]
    temp2 = pred_df[:, 13:]
    pred_df = np.concatenate((temp1, temp2), axis=1)
    pred_df=scaler.transform(pred_df)
    print(pred_df.dtype)

    model_reg = pickle.load(open('user_offer_attraction.pkl', 'rb'))
    result=model_reg.predict(pred_df)
    return result



def result(request):
    if request.method =='POST':
        l3 = []
        l1 = []
        l2 = []
        out = request.POST.get('optradio')
        print(out)
        brand = request.POST.getlist('brand')
        for i in range(0,len(brand)):
            l3.append(out)
        print(brand)

        a = request.POST.getlist('price')
        for row in a:
            if int(row) !=0:
                l1.append(int(row))
        print(l1)
        quantity=request.POST.getlist('quantity')

        for row in quantity:
            if row !='':
                l2.append(int(row))
        print(l2)
        df=pd.DataFrame()
        df['Sub_category']=l3
        df['Brand']=brand
        df['Price']=l1
        df['Quantity']=l2
        print(df)
        print(df.dtypes)
        output=prediction(df)
        df['Offer']=np.round(output).astype(int)
        df=df.sort_values("Offer", ascending=False)
        json_records = df.reset_index().to_json(orient='records')
        data = []
        data = json.loads(json_records)
        context = {'d': data}
    return render(request,'result.html',context)
