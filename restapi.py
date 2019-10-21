import os

counter=0
for year in range(2004,2005):
    for day in range(9,10,8):
        day="{0:03}".format(day)
        os.system('curl -u admin:geoserver -XPOST -H "Content-type: application/json" -d @import.json "http://localhost:8080/geoserver/rest/imports"')

        os.system('curl -u admin:geoserver -F name=idsi -F filedata=@/home/pratik/pratik/Drought/IDSI/%s/idsi%s%s.tif "http://localhost:8080/geoserver/rest/imports/%s/tasks"'%(year,year,day,counter))

        os.system('curl -u url -u admin:geoserver -XPOST "http://localhost:8080/geoserver/rest/imports/%s"'%(counter))

        os.system('curl -u admin:geoserver -XPUT -H "Content-type: text/xml" -d "<layer><defaultStyle><name>raster</name></defaultStyle><enabled>true</enabled></layer>" http://localhost:8080/geoserver/rest/layers/idsi:idsi%s%s'%(year,day))
        counter+=1
