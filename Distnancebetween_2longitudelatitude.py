from math import sin,cos,radians,tan,acos


print("Enter starting and ending latitudes/longitudes below when prompted:---")
start_latitude = radians(float(input("Enter starting latitude")))
end_latitude = radians(float(input("Enter ending latitude")))
start_longitude = radians(float(input("Enter starting longitude")))
end_longitude = radians(float(input("Enter ennding latitude")))

distance= 6371.01 *  acos(sin(start_latitude)*sin(end_latitude) + cos(start_latitude)*cos(end_latitude)*cos(start_longitude - end_longitude))
print("The distance between two points is %.2fkm." %distance)