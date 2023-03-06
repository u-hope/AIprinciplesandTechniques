graph = {
  'Humera' : ['Shire','Gondar'],
  'Shire' : ['Axum', 'Debarke'],
  'Gondar' : ['Metema','Azezo','Debarke','Humera'],
  'Axum' : ['Adwa','Shire'],
  'Debarke' : ['Gondar','Shire'],
  'Metema' : ['Azezo','Gondar'],
  'Azezo' : ['BahirDar','Metema','Gondar'],
  'Adwa' : ['Axum','Adigrat','Mekelle'],
  'BahirDar' : ['FinoteSelam','Injibar','Metekel','Azezo','DebreTabor'],
  'Adigrat' : ['Adwa', 'Mekelle'],
  'Mekelle' : ['Sekota', 'Alamata', 'Adwa', 'Adigrat'],
  'FinoteSelam' : ['DebreMarkos','Injibar','BahirDar'],
  'Injibar' : ['FinoteSelam','BahirDar'],
  'Metekel' : ['BahirDar','Assosa'],
  'DebreTabor' : ['Lalibela','BahirDar'],
  'Sekota' : ['Mekelle', 'Alamata', 'Lalibela'],
  'Alamata' : ['Woldia', 'Sekota', 'Samara', 'Mekelle'],
  'DebreMarkos' : ['FinoteSelam', 'DebreSina'],
  'Assosa' : ['DembiDollo','Metekel'],
  'Lalibela' : ['DebreTabor', 'Woldia', 'Sekota'],
  'Woldia' : ['Dessie', 'Lalibela', 'Alamata', 'Samara'],
  'Samara' : ['GabiRasu', 'Woldia', 'Alamata', 'FantiRasu'],
  'DebreSina' : ['DebreBirhan', 'DebreMarkos', 'Kemise'],
  'DembiDollo': ['Assosa', 'Gimbi', 'Gambella'],
  'Dessie' : ['Kemise', 'Woldia'],
  'GabiRasu' : ['Awash', 'Samara'],
  'FantiRasu' : ['Samara','KilbetRasu'],
  'DebreBirhan': ['DebreSina', 'AddisAbaba'],
  'DebreMarkos': ['FinoteSelam','DebreSina'],
  'Kemise' : ['Dessie','DebreSina'],
  'Awash' : ['GabiRasu','Chiro','Matahara'],
  'KilbetRasu' :[],
  'AddisAbaba':['DebreBirhan','Ambo','Adama'],
  'Chiro' : ['Awash','DireDawa'],
  'Matahara' : ['Adama','Awash'],
  'Ambo': ['Wolkite','Nekemete','AddisAbaba'],
  'Adama':['AddisAbaba','Matahara','Batu','Assella'],
  'DireDawa':['Chiro','Harar'],
  'Wolkite' : ['Ambo','Jimma', 'Worabe'],
  'Nekemete': ['Ambo','Gimbi','Bedelle'],
  'Batu' : ['Adama', 'ButaJirra','Shashemene'],
  'Assella':['Assasa','Adama'],
  'Harar' : ['DireDawa', 'Bablle'],
  'Jimma' : ['Wolkite','Bedelle','Bonga'],
  'Worabe': ['Wolkite','Hossana','ButaJirra'],
  'Gimbi' : ['Nekemete', 'DembiDollo'],
  'Bedelle': ['Nekemete','Jimma', 'Gore'],
  'ButaJirra' :['Worabe','Batu'],
  'Shashemene':['Batu','Hossana','Hawassa','Dodolla'],
  'Assasa' : ['Assella','Dodolla'],
  'Bablle' : ['Harar','Jigjiga'],
  'Bonga' : ['Jimma','Dawaro','Tepi','MezanTeferi'],
  'Hossana' : ['Worabe','Shashemene','WolaitaSodo'],
  'Gore' : ['Bedelle','Tepi', 'Gambella'],
  'Hawassa' : ['Shashemene','Dila'],
  'Dodolla' : ['Shashemene','Assasa','Bale'],
  'Jigjiga' : ['Bablle','DegaHabur'],
  'Dawaro'  : ['Bonga','WolaitaSodo'],
  'Tepi'    : ['Gore','MezanTeferi','Bonga'],
  'MezanTeferi' : ['Tepi', 'Bonga'],
  'WolaitaSodo' : ['Hossana', 'Dawaro', 'ArbaMinch'],
  'Gambella' : ['DembiDollo','Gore'],
  'Dila' : ['Hawassa','BuleHora'],
  'Bale' : ['Dodolla','Liben','Goba','SofOumer'],
  'DegaHabur' : ['Jigjiga', 'KebriDehar'],
  'Dawaro': ['WolaitaSodo','Bonga'],
  'ArbaMinch' : ['Konso','Basketo','WolaitaSodo'],
  'Basketo' : ['Dawaro','ArbaMinch','MezanTeferi','BenchiMaji'],
  'BuleHora' : ['Dila','Yabello'],
  'Liben' :[],
  'Goba':['Bale','SofOumer','Bablle'],
  'SofOumer': ['Bale','Goba','Gode'],
  'KebriDehar': ['DegaHabur','Werder','Gode'],
  'Yabello' : ['BuleHora','Konso','Moyale'],
  'BenchiMaji' : [],
  'Gode' : [],
  'Werder':[],
  'Konso' :['ArbaMinch','Yabello'],
  'Moyale':[]
}

Choose = True

# Start of Breadth First Search

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node, ):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s) 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# #Start of Depth First Search
traversed = set() # Set to keep track of visited nodes.

def dfs(traversed, graph, node):

        if node not in traversed:
            print (node)
            traversed.add(node)
            for neighbour in graph[node]:
                dfs(traversed, graph, neighbour)

if Choose == True:
    print("Depth First Search :")
    dfs(traversed, graph, 'Humera')
else:
    print("Breadth First Search :") 
    bfs(visited, graph, 'Humera')