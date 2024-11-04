#Web VPython 3.2

scene.autoscale = True
scene.camera.pos=vec(0,0,10**9)
scene.forward=vec(0,0,-1)
const_G = 6.674 * (10**(-11))
t = 86400/4 #const

#mass
sun = 1.9 * (10**30)
mercury = 0.33010 * (10**24)
venus = 4.867 * (10**24)
earth = 5.972 * (10**24)
mars = 6.39 * (10**23)
jupiter = 1.898 * (10**27)
saturn = 5.683 * (10**26)
uranus = 8.681 * (10**25)
neptune = 1.024 * (10**26)
pluto = 1.31 * (10**22)

#initial velocity
v0_sun = 0
v0_mercury = 47 *(10**3) #m/s
v0_venus = 35.021 *(10**3)
v0_earth = 29.784 *(10**3)
v0_mars = 24.08 *(10**3)
v0_jupiter = 59.5 *(10**3)
v0_saturn = 9.68 * (10**3)
v0_uranus = 6.835 * (10**3)
v0_neptune = 5.45 * (10**3)
v0_pluto = 4.66 * (10**3)

#radius
r_sun = 0
r_mercury = 60.83 * (10**9) #m
r_venus = 108.73 * (10**9)
r_earth = 149.72 * (10**9)
r_mars = 226.41 * (10**9)
r_jupiter = 484 * (10**9)
r_saturn = 1.4438 * (10**12)
r_uranus = 2.9262 * (10**12)
r_neptune = 4.4717 * (10**12)
r_pluto = 5.9 * (10**12)

#sizes of the bodies
'''
planets are too small
d_sun = 1.4 * 10**9 #m
d_mercury = 4.879 *10**6
d_venus = 1.2104 * 10**7
d_earth = 1.2756 * 10**7
d_mars = 6.794 * 10**6
d_jupiter = 1.42800 * 10**8
d_saturn = 1.20500 * 10**8
d_uranus = 5.1118 * 10**7
d_neptune = 4.9528 * 10**7
d_pluto = 2.377 * 10**6
'''
d_sun = 10 * (10**10) #m
d_mercury = 2.5 *(10**10)
d_venus = 2.5 * (10**10)
d_earth = 2.5 * (10**10)
d_mars = 2.5 * (10**10)
d_jupiter = 5 * (10**10)
d_saturn = 5 * (10**10)
d_uranus = 5 * (10**10)
d_neptune = 5 * (10**10)
d_pluto = 5 * (10**10)


m = [sun,mercury,venus,earth,mars,jupiter,saturn,uranus,neptune,pluto]
vx = [0,0,0,0,0,0,0,0,0,0]
vy = [v0_sun,v0_mercury,v0_venus,v0_earth,v0_mars,v0_jupiter,v0_saturn,v0_uranus,v0_neptune,v0_pluto]
ry = [0,0,0,0,0,0,0,0,0,0]
rx = [r_sun,r_mercury,r_venus,r_earth,r_mars,r_jupiter,r_saturn,r_uranus,r_neptune,r_pluto]
v = [0,0,0,0,0,0,0,0,0,0]
r = [0,0,0,0,0,0,0,0,0,0]
d = [d_sun,d_mercury,d_venus,d_earth,d_mars,d_jupiter,d_saturn,d_uranus,d_neptune,d_pluto]

def force(index_i,index_j,m1,m2,r_xi,r_yi,r_xj,r_yj):
    const_G = 6.674 * (10**(-11))
    f = 0.0
    r_x = r_xi - r_xj
    r_y = r_yi - r_yj
    r_vec = (r_x**2 + r_y**2)**0.5
    f = (const_G * m1 * m2) / r_vec**2
    theta = degrees(atan2(r_y,r_x))
    #*(180/3.14)
    f_x = f * cos(theta)
    f_y = f * sin(theta)
    #print("f ",f_x,index_i,index_j)
    #print("f ",f_y,index_i,index_j)
    return f_x,f_y


rx_post = []
ry_post = []
vx_post = []
vy_post = []
Spheres = []
S_arrows = []

for i in range(6):
    rx_post.append(rx[i])
    ry_post.append(0)
    vx_post.append(0)
    vy_post.append(vy[i])

all_col = [color.red,color.green,color.blue,color.cyan]
scene.camera.pos=vec(0,0,2*ry[0])
Spheres = [6]
print("HERE1")
for k in range(6):
    print("HERE2")
    #scene.camera.pos=vec(0,0,2*ry[k])
    #scene.forward=vec(0,0,-1)
    sleep(1)
    Spheres[k] = sphere(make_trail=True, pos=vec(rx[k], ry[k], 0),radius = (d[k])/2.0,color=all_col[k%4])
    Spheres[k].visible = True
    #scene.pause()
    scene.autoscale = True
scene.pause()
print("HERE3")
for n in range(365*4):
    #print("HERE4")
    #sleep(1)
    for i in range(0,6):
        for j in range(i+1,6):
            #print("HERE ",i,j)
            
            #scene.pause()
            f_x,f_y = force(i,j,m[i],m[j],rx[i],ry[i],rx[j],ry[j])
            u_x = vx[j]
            a_x = f_x / m[j]
            rx_init = rx[j]
            #if(rx_post[j] < ((u_x*t + 0.5*a_x*t**2) + rx[j]) ):
            if(j==i+1 and i==0):
                rx_post[j] = (rx[j] + ((u_x*t + 0.5*a_x*t**2) + rx[j]))/2
                #print("rx1",rx_post[j],i,j)
            else:
                rx_post[j] = (rx_post[j] + ((u_x*t + 0.5*a_x*t**2) + rx[j]))/2 
                #print("rx",rx_post[j],i,j)
            u_y = vy[j]
            a_y = f_y / m[j]
            ry_init = ry[j]
            #if((ry_post[j] <  ((u_y*t + 0.5*a_y*t**2) + ry[j]) ):
            if(j==i+1 and i==0):
                ry_post[j] = (ry[j] + ((u_y*t + 0.5*a_y*t**2) + ry[j]))/2
                #print("ry1",ry_post[j],i,j)
            else:
                ry_post[j] = (ry_post[j] + ((u_y*t + 0.5*a_y*t**2) + ry[j]))/2
                #print("ry",ry_post[j],i,j)
            #Spheres[j].visible = False
            vx_post[j] = (rx_post[j]-rx_init)/t
            #print(vx_post[j],i,j)
            vy_post[j] = (ry_post[j]-ry_init)/t
            #print(vy_post[j],i,j)
        #scene.pause()
            
    
    sleep(0.00001)
    #scene.pause()
    for j in range(1,6):        
        Spheres[j].pos =vec(rx_post[j] , ry_post[j], 0)
        #Spheres[j].visible = True
          
        rx[j] = rx_post[j]
        ry[j] = ry_post[j]
        vx[j] = vx_post[j]
        vy[j] = vy_post[j]
    #print(rx)
    #print(ry)
    #print(vx)
   #print(vy)

        
    #if(n=300):
        #scene.autoscale = True 
    #print("HERE4")
        #scene.pause()
print("HERE4")

    
