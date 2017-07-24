import random
import math


def random_points_irregular(xsize,ysize,number_points):
    return [ (random.randint(1,xsize-2),random.randint(1,ysize-2)) for i in range(number_points) ]

def random_graph_irregular(xsize,ysize,number_points,extra_connection_prob=0):
    points = [ (int(xsize/2), 1)] + random_points_irregular(xsize,ysize,number_points) 
    return random_graph_make_connections(xsize,ysize,points,extra_connection_prob)

def random_point_regular(xsize,ysize,x_number_points,y_number_points,deviation=1):
    # Puts points i x,y square grid, with deviation (0 to 1) allowed from square center
    xcellsize = float(xsize)/x_number_points
    ycellsize = float(ysize)/y_number_points
    devmin = max(0,0.5-deviation/2)
    devmax = min(1,0.5+deviation/2)
    return [ (random.randint(int((i+devmin)*xcellsize),int((i+devmax)*xcellsize)),random.randint(int((j+devmin)*ycellsize),int((j+devmax)*ycellsize))) \
                for i in range(x_number_points) for j in range(y_number_points) ]


def random_graph_regular(xsize,ysize,x_number_points,y_number_points,deviation=1,extra_connection_prob=0):
    points = [ (int(xsize/2), 1)] + random_point_regular(xsize,ysize,x_number_points,y_number_points,deviation) 
    return random_graph_make_connections(xsize,ysize,points,extra_connection_prob)
    
    
def random_graph_make_connections(xsize,ysize,points,extra_connection_prob):
    connections = list()
    connected_points = [ points[0] ]
    unconnected_points = list(points[1:])
    while unconnected_points:
        best_from_1 = 0
        best_from_2 = 0
        best_to = 0
        best_dist = float('inf')
        for i in range(len(unconnected_points)):
            best_from_1_i = 0
            best_from_2_i = 0            
            best_dist_1_i = float('inf')
            best_dist_2_i = float('inf')        
            xi, yi = unconnected_points[i]
            for j in range(len(connected_points)):
                xj, yj = connected_points[j]
                dist = float(abs(xi-xj)+abs(yi-yj))
                if dist < best_dist_1_i:
                    best_dist_2_i = best_dist_1_i
                    best_from_2_i = best_from_1_i
                    best_dist_1_i = dist
                    best_from_1_i = j
                elif dist < best_dist_2_i:
                    best_dist_2_i = dist
                    best_from_2_i = j
            if best_dist_1_i < best_dist:
                best_dist = best_dist_1_i
                best_from_1 = best_from_1_i
                best_from_2 = best_from_2_i
                best_to = i
        connections.append( ( unconnected_points[best_to], connected_points[best_from_1]) )
        if len(connected_points) > 1 and random.random() < extra_connection_prob:
            connections.append( ( unconnected_points[best_to], connected_points[best_from_2]) )
        connected_points.append(unconnected_points[best_to])
        del unconnected_points[best_to]
    return points, connections

def initial_grid(xsize,ysize,background,foregrounds):
    grid =  [ [ background for x in range(xsize) ] for y in range(ysize) ]
    for f in foregrounds:
        x,y,radius = random.randint(1,xsize-2),random.randint(1,ysize-2),random.randint(1,int((xsize+ysize)/8))        
        for x1 in range(max(0,x-radius),min(xsize,x+radius+1)):
            for y1 in range(max(0,y-radius),min(ysize,y+radius+1)):
                if math.sqrt((x1-x)**2+(y1-y)**2) <= radius:
                    grid[y1][x1] = f
    return grid

def print_grid(grid):
    for l in grid:
        for c in l:
            print(c,end='')
        print()
        

def pack_grid(grid):
    packed_grid = list()
    for l in grid:
        packed_line = ""
        for c in l:
            packed_line += c
        packed_grid.append(packed_line)
    return packed_grid

            
def add_graph_to_grid(points,connections,grid,terrain,pointterrain=False):
    if not pointterrain:
        pointterrain = terrain
    conn_coord_list = list()
    for c in connections:
        p1, p2 = c
        x1,y1 = p1
        x2,y2 = p2
        dx = int(math.copysign(1,x2-x1))
        dy = int(math.copysign(1,y2-y1))
        conn_coordinates = list()
        if random.random() < 0.5:
            for x in range(x1,x2+dx,dx):
                grid[y1][x] = terrain
                conn_coordinates.append((x,y1))
            for y in range(y1,y2+dy,dy):
                grid[y][x2] = terrain
                conn_coordinates.append((x2,y))
        else:
            for y in range(y1,y2+dy,dy):
                grid[y][x1] = terrain
                conn_coordinates.append((x1,y))
            for x in range(x1,x2+dx,dx):
                grid[y2][x] = terrain
                conn_coordinates.append((x,y2))
        conn_coord_list.append(conn_coordinates)
    for p in points:
        x,y = p
        grid[y][x] = pointterrain
    return grid,conn_coord_list

def make_square_rooms(points,grid,terrain,minsize,maxsize,free=' '):
    xmax = len(grid[0])
    ymax = len(grid)
    room_coordinates = list()
    for p in points:
        room_coordinates.append(list())
        xp,yp = p
        r = random.randint(minsize,maxsize)
        for x in range(xp-r,xp+r+1):
            for y in range(yp-r,yp+r+1):
                if 1 <= x <=xmax-2 and 1 <= y <=ymax-2 and grid[y][x] in free: 
                    grid[y][x] = terrain
                    room_coordinates[-1].append((x,y))
    return grid, room_coordinates
            
def make_round_rooms(points,grid,terrain,minsize,maxsize,free=' '):
    xmax = len(grid[0])
    ymax = len(grid)
    room_coordinates = list()
    for p in points:
        room_coordinates.append(list())
        xp,yp = p
        r = random.randint(minsize,maxsize)
        for x in range(xp-r,xp+r+1):
            for y in range(yp-r,yp+r+1):
                if 1 <= x <=xmax-2 and 1 <= y <=ymax-2 and math.sqrt((xp-x)**2+(yp-y)**2) <= r and grid[y][x] in free: 
                    grid[y][x] = terrain
                    room_coordinates[-1].append((x,y))
    return grid, room_coordinates

def every_nth_element(l,n,offset=0):
    l2 = list()
    for i in range(offset,len(l),n):
        l2.append(l[i])
    return l2


def make_square_rooms_with_walls(points,grid,terrain,wall,minsize,maxsize,free=' '):
    xmax = len(grid[0])
    ymax = len(grid)
    room_coordinates = list()
    for p in points:
        room_coordinates.append(list())
        xp,yp = p
        h = random.randint(minsize,maxsize)
        w = random.randint(minsize,maxsize)
        for x in range(xp-w,xp+w+1):
            for y in range(yp-h,yp+h+1):
                if 1 <= x <=xmax-2 and 1 <= y <=ymax-2 and grid[y][x] in free:
                    if x == max(0,xp-w) or x == min(xmax-1,xp+w) or y == max(0,yp-h) or y == min(ymax-1,yp+h):
                        grid[y][x] = wall
                    else:
                        grid[y][x] = terrain
                        room_coordinates[-1].append((x,y))
    return grid, room_coordinates

def add_obstacle_to_room(room_coordinates,grid,element,terrain):
    if len(room_coordinates) > 0:
        tries = 0
        xmax = len(grid[0])
        ymax = len(grid)
        while tries < 99:
            i = random.randint(0,len(room_coordinates)-1)
            x,y = room_coordinates[i]
            if 1 <= x <=xmax-2 and 1 <= y <=ymax-2 and grid[y][x] in terrain and not bottleneck(grid,x,y,terrain):
                grid[y][x] = element
                return grid, (x,y)
            tries +=1
    return grid, False

def bottleneck(grid,x,y,terrain):
    # Used to identify cells that should not be blocked
    # Compute connected components for the 8 cells surrounding a given cell (x,y)
    cells = list()
    components = list()
    for x1 in range(x-1,x+2):
        for y1 in range(y-1,y+2):
            if grid[y1][x1] not in terrain:
                cells.append((x1,y1))
    while cells:
        # Start a component with a singe cell
        components.append([cells[0]])
        del cells[0]
        found = True
        while found:
            found = False
            for i in range(len(cells)):
                x1,y1 = cells[i]
                # Check if cell is connected to any cell in last component
                for j in range(len(components[-1])):
                    x2,y2 = components[-1][j]
                    if -1 <= x1-x2 <= 1 and -1 <= y1-y2 <= 1:
                        found = True
                        components[-1].append(cells[i])
                        del cells[i]
                        break
                if found:
                    break
    if len(components) > 1:
        return True
    else:
        return False
                

def get_centers_of_regular_graph(points,x_number_points,y_number_points):
    centers = list()
    for i in range(x_number_points-1):
        for j in range(y_number_points-1):
            x_center = int((points[i*y_number_points+j][0]+points[(i+1)*y_number_points+j][0]+\
                       points[i*y_number_points+j+1][0]+points[(i+1)*y_number_points+j+1][0])/4)
            y_center = int((points[i*y_number_points+j][1]+points[(i+1)*y_number_points+j][1]+\
                       points[i*y_number_points+j+1][1]+points[(i+1)*y_number_points+j+1][1])/4)
            centers.append([(x_center,y_center),points[i*x_number_points+j],points[(i+1)*x_number_points+j],
                            points[i*x_number_points+j+1],points[(i+1)*x_number_points+j+1]])
    return centers
  

def add_items_near_connection(connection_coordinates,grid,number,elements,free=' '):
    count = 0
    failed = 0
    while count < number and failed < 10:
        i = random.randint(0,len(connection_coordinates)-1)
        x,y = connection_coordinates[i]
        el = random.choice(elements).split(' ')
        xsize = len(el[0])
        ysize = len(el)
        directions = list([(-1*xsize,0),(0,-1*ysize),(1,0),(0,1)])
        random.shuffle(directions)
        blocked = True
        for dir in directions:
            dx, dy = dir
            blocked = free_area(grid,x+dx,y+dy,x+dx+xsize-1,y+dy+ysize-1)
            if not blocked:
                place_in_area(grid,x+dx,y+dy,el)
                count += 1
                break
        if blocked:
            failed += 1
    return grid
        

def free_area(grid,x1,y1,x2,y2,free=' '):
    xmax = len(grid[0])
    ymax = len(grid)
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if not (0 <= i < xmax and 0 <= j < ymax and grid[j][i] in free):
                return True
    return False

def place_in_area(grid,x,y,el):
    if type(el) == str:
        el=el.split(' ')
    xsize = len(el[0])
    ysize = len(el)    
    for i in range(xsize):
        for j in range(ysize):
            grid[y+j][x+i] = el[j][i]
    
    
        
# Test
g = initial_grid(25,25," ", "")
p,c  = random_graph_regular(25,25,2,2,0.5,1)
g,ccl = add_graph_to_grid(p,c,g,'.','*')
#g, rcl_round = make_round_rooms(every_nth_element(p,2,0),g,'r',1,2,'.')
#g, rcl_square = make_square_rooms(every_nth_element(p,2,1),g,'s',1,2,'.')
random.shuffle(p)
g, rcl = make_square_rooms_with_walls(p,g,'.','#',2,6)

print(25*"-")
print_grid(g)
print(25*"-")


g = initial_grid(25,25," ", "")
p,c  = random_graph_regular(25,25,4,3,0.5,0.5)
g,ccl = add_graph_to_grid(p,c,g,'.','*')
#g, rcl_round = make_round_rooms(every_nth_element(p,2,0),g,'r',1,2,'.')
#g, rcl_square = make_square_rooms(every_nth_element(p,2,1),g,'s',1,2,'.')
p2 = random_points_irregular(25,25,8)
g, rcl = make_round_rooms(p[0:2],g,'A',2,4,' ')
g, rcl = make_round_rooms(p[2:4],g,'B',2,6,' ')
g, rcl = make_round_rooms(p[4:6],g,'C',4,8,' ')
g, rcl = make_round_rooms(p[6:8],g,'D',4,10,' ')

print(25*"-")
print_grid(g)
print(25*"-")

g = initial_grid(25,25," ", "")
p,c  = random_graph_regular(25,25,10,10,0.5,0.3)
g,ccl = add_graph_to_grid(p,c,g,'.','*')
# centers = get_centers_of_regular_graph(p[1:],4,5)  # Do not inlcuee first point, not part of grid
##for r in centers:
##    x,y = r[0]
##    g[y][x]="x" 

for cc in ccl:
    g = add_items_near_connection(cc,g,2,['A', 'BC','DD DD',' '])
	
print(25*"-")
print_grid(g)
print(25*"-")

#for r in rcl_round:
#    g,pos = add_obstacle_to_room(r,g,"O","r")
#for r in rcl_square:
#    g,pos = add_obstacle_to_room(r,g,"O","s")
    
# print_grid(g)
              
#print(bottleneck(["   ","X X", "XXX"], 1, 1, " "))
#print(bottleneck(["   ","X X", "X X"], 1, 1, " "))
#print(bottleneck(["   ","   ", "   "], 1, 1, " "))


            


    
