import random
class network:
    def __init__(self):
        self.IDs = []
    def get_new_id(self):
        while True:
            rand_int = random.randint(1000,9999)
            if rand_int not in self.IDs:
                self.IDs.append(rand_int)
                return rand_int
            
class person:
    def __init__(self,first,last,network):
        self.ID = network.get_new_id()
        self.first_name = first
        self.last_name = last
    def __str__(self):
        return f"{self.first_name} {self.last_name}: ({self.ID})"
    
def build_adjacency(data):
    adj_dict = dict()
    for node in data:
        a = node[0]
        b = node[1]
        if a in adj_dict:
            adj_dict[a].append(b)
        else:
            adj_dict[a] = [b]
        if b in adj_dict:
            adj_dict[b].append(a)
        else:
            adj_dict[b] = [a]
    return adj_dict
def display_adj(adj_dict):
    for key,value in adj_dict.items():
        num_friends = len(value)
        print(f"\n{key.ID}: {key.first_name} {key.last_name}, number of friends: {num_friends}")
        for person in value:
            print(person)


if __name__ == '__main__':
    net = network()
    p1 = person("Anita", "Racinez",net)
    p2 = person("Clem", "Jameson",net)
    p3 = person("Lars", "Eriksson",net)
    p4 = person("Jed", "Jones",net)
    data = [(p1, p2), (p2, p3), (p1, p4), (p2, p4)]
    display_adj(build_adjacency(data))