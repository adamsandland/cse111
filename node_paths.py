possible_routes = []

list_of_route_data = []

def make_route_data(node, edges ,paths, connections):
# The function takes in a node name (string), edge (number), path(string), and connections (list of strings)
    route = [node, edges, paths, connections]
    possible_routes.append(route)

def analyze_routes():
    for i in possible_routes:
        for con_num in possible_routes[i][3]:
            #get the connection name data
            possible_routes[i][3][con_num]
            list_of_route_data[i] = 
