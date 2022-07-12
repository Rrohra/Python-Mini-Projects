import folium
import pandas
a=pandas.read_csv("Volcanoes_USA.txt")
#a["LAT"]=a["LAT"].map(str)+","+a["LON"].map(str)
#a=a.drop("LON",axis=1)
'''var=open("yolo.html", "r")   #ignored because iframe chal nahi raha.
var2 = var.read()
iframe = folium.IFrame(html=var2, width=500, height=300)
popup = folium.Toolkit(iframe, max_width=2650)'''
def color_producer(e):
    if  e< 1000:
        return "green"
    elif e < 2000:
        return "orange"
    else :
        return "red"

map = folium.Map(location=[19.179180,72.972580],zoom_start=6, tiles="Mapbox Control Room")
fga = folium.FeatureGroup(name="first layer")
for i in range(1, len(a)):
    x=a.loc[i,'LAT'].astype(float)  #a.loc[i,[]] is of type numpy.64 hence it has to be coverted to required type.
    y =a.loc[i,'LON'].astype(float)  #get the required vslues
    z=a.loc[i,'ELEV'].astype(str) #same

    fga.add_child(folium.CircleMarker(location=[x, y], popup=z, fill_color=color_producer(float(z)), color= "black"))
    #alternate script
#lat = list(data["LAt"])
#lon = list(data["LOn"])
#elev = list(data["ELEV"])
#for lt,ln,el in zip(lat, lon, elev):
 #   fg.add_child(folium.MArker(locxation=[lt, ln], popup =el.astype(str) )
fgb = folium.FeatureGroup(name="population")
fgb.add_child(folium.GeoJson(data=open("115 world.json","r", encoding="utf-8-sig").read(),
                            style_function=lambda x: {"fillColor": "yellow" if x["properties"]["POP2005"]<10000000
                                                      else "orange" if 10000000 <= x["properties"]["POP2005"]
                                                                       < 2000000 else "red"}))
map.add_child(fga)
map.add_child(fgb)
map.add_child(folium.LayerControl())
map.save("yolo1.html")
print("done")
