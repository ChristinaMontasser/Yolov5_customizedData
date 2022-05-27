import numpy as np

def txtData( Ptxt, Ttxt):
    data = [Ttxt, Ptxt]
    point = [0, 0]
    orderPair=[]
    if(not(np.any(Ptxt))):
        area1, area2 =0 ,0
        return orderPair, area1, area2
    for i in range(2):
        current =data[i]
        
        point[0]= ((current[0]-(current[2]/2)), (current[1]-(current[3]/2)))
        point[1]= ((current[0]+(current[2]/2)), (current[1]+(current[3]/2)))
        # point[2]= ((current[0]+(current[2]/2)), (current[1]-(current[3]/2)))
        # point[3]= ((current[0]-(current[2]/2)), (current[1]+(current[3]/2)))
        orderPair.append(point)
        point = [0, 0]
    #print(orderPair[0])
    area1 = (data[0][2]*data[0][3])
    area2 = (data[1][2]*data[1][3])
    return orderPair, area1, area2



def areaInter(orderPair):
    if(len(orderPair)==0):
        area_Inter=0
        return area_Inter
    x_inter1= max(orderPair[0][0][0], orderPair[1][0][0])
    y_inter1= max(orderPair[0][0][1], orderPair[1][0][1])

    x_inter2= min(orderPair[0][1][0], orderPair[1][1][0])
    y_inter2= min(orderPair[0][1][1], orderPair[1][1][1])
    
    width_inter= x_inter2- x_inter1
    height_inter=  y_inter2 -y_inter1
    # #(width_inter, height_inter)
    area_Inter =(width_inter * height_inter)
    return area_Inter

def IOU (area1, area2, area_Inter ):
    if(area_Inter==0):
        return 0
    area_union=(area1 + area2) -area_Inter
    IOU  =area_Inter/area_union
    return (IOU if IOU>0 else  0)


Pxywh1 = [0.4775,0.51625,0.73,0.5025]
Txywh1 = [0.507055,0.528219,0.804233,0.527337]
orderPair, area1, area2 =txtData(Pxywh1, Txywh1)
area_Inter = areaInter(orderPair)
print( IOU(area1, area2, area_Inter))

Pxywh2 = [0.52875,0.53,0.6625,0.345]
Txywh2 = [0.520282,0.545855,0.816578,0.340388] 
orderPair, area1, area2 =txtData(Pxywh2, Txywh2)
area_Inter = areaInter(orderPair)
print( IOU(area1, area2, area_Inter))

Pxywh3 = [0.56125,0.4275,0.5125,0.45]
Txywh3 = [0.546737,0.410935,0.502646,0.391534]
orderPair, area1, area2 =txtData(Pxywh3, Txywh3)
area_Inter = areaInter(orderPair)
print( IOU(area1, area2, area_Inter))

Pxywh4 = [0.465,0.36625,0.3,0.4225]
Txywh4 = [0.458554,0.353616,0.340388,0.417989] 
orderPair, area1, area2 =txtData(Pxywh4, Txywh4)
area_Inter = areaInter(orderPair)
print( IOU(area1, area2, area_Inter))

Pxywh5 = [0.83125,0.36625,0.3375,0.3475]
Txywh5 = [0.819665,0.313933,0.360670,0.557319] 
orderPair, area1, area2 =txtData(Pxywh5, Txywh5)
area_Inter = areaInter(orderPair)
print( IOU(area1, area2, area_Inter))

Pxywh6 = [0, 0, 0, 0]
Txywh6= [0.136243,0.340388,0.272486,0.627866] 
orderPair, area1, area2 =txtData(Pxywh6, Txywh6)
area_Inter = areaInter(orderPair)
print( IOU(area1, area2, area_Inter))

Pxywh7 = [0.28375, 0.51125, 0.3875, 0.3425]
Txywh7 = [0.270559, 0.511513, 0.445724, 0.332237] 
orderPair, area1, area2 =txtData(Pxywh7, Txywh7)
area_Inter = areaInter(orderPair)
print( IOU(area1, area2, area_Inter))

Pxywh8 = [0.76375, 0.41125, 0.2075, 0.1475]
Txywh8 = [0.763158, 0.409539, 0.213816, 0.128289]
orderPair, area1, area2 =txtData(Pxywh8, Txywh8)
area_Inter = areaInter(orderPair)
print( IOU(area1, area2, area_Inter)) 

Pxywh9 = [0, 0, 0, 0]
Txywh9 = [0.620066, 0.564967, 0.154605, 0.149671] 
orderPair, area1, area2 =txtData(Pxywh9, Txywh9)
area_Inter = areaInter(orderPair)
print( IOU(area1, area2, area_Inter))


Pxywh12= [0, 0, 0, 0]
Txywh12= [0.513228,0.303351,0.463845,0.335097]
orderPair, area1, area2 =txtData(Pxywh12, Txywh12)
area_Inter = areaInter(orderPair)
print( IOU(area1, area2, area_Inter)) 

Pxywh13= [0, 0, 0, 0]
Txywh13= [0.510582,0.753086,0.977072,0.493827]
orderPair, area1, area2 =txtData(Pxywh13, Txywh13)
area_Inter = areaInter(orderPair)
print( IOU(area1, area2, area_Inter))

Pxywh14= [0.52,0.33875,0.505,0.3025]
Txywh14= [0.531746,0.328042,0.557319,0.320988]
orderPair, area1, area2 =txtData(Pxywh14, Txywh14)
area_Inter = areaInter(orderPair)
print( IOU(area1, area2, area_Inter))

Pxywh15= [0.7275,0.29375,0.41,0.2725]
Txywh15= [0.709877,0.309524,0.412698,0.287478]
orderPair, area1, area2 =txtData(Pxywh15, Txywh15)
area_Inter = areaInter(orderPair)
print( IOU(area1, area2, area_Inter))

Pxywh16= [0.39125,0.58375,0.5125,0.2775]
Txywh16= [0.425164,0.605263,0.570724,0.348684]
orderPair, area1, area2 =txtData(Pxywh16, Txywh16)
area_Inter = areaInter(orderPair)
print( IOU(area1, area2, area_Inter))

Pxywh17= [0, 0, 0, 0]
Txywh17= [0.519400, 0.492945, 0.582011, 0.326279]
orderPair, area1, area2 =txtData(Pxywh17, Txywh17)
area_Inter = areaInter(orderPair)
print( IOU(area1, area2, area_Inter))

Pxywh18= [0.575, 0.47875, 0.795, 0.7775]
Txywh18= [0.542328, 0.493827, 0.902998, 0.867725]
orderPair, area1, area2 =txtData(Pxywh18, Txywh18)
area_Inter = areaInter(orderPair)
print( IOU(area1, area2, area_Inter))




