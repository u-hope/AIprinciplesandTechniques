graph = {
  'Humera' :{'Shire':[8,67],'Gondar':[9,56]},
  'Shire' : {'Axum':[2,67], 'Debarke':[7,60]},
  'Gondar' : {'Metema':[7,62],'Azezo':[1,55],'Debarke':[4,60],'Humera':[9,65]},
  'Axum' : {'Adwa':[1,65],'Shire':[2,67]},
  'Debarke' : {'Gondar':[4,56],'Shire':[7,67]},
  'Metema' : {'Azezo':[7,55],'Gondar':[7,56]},
  'Azezo' : {'BahirDar':[7,48],'Metema':[7,62],'Gondar':[1,56]},
  'Adwa' : {'Axum':[1,67],'Adigrat':[4,62],'Mekelle':[7,58]},
  'BahirDar' : {'FinoteSelam':[6,42],'Injibar':[4,44],'Metekel':[11,59],'Azezo':[7,55],'DebreTabor':[4,52]},
  'Adigrat' : {'Adwa':[4,65], 'Mekelle':[4,58]},
  'Mekelle' : {'Sekota':[9,59], 'Alamata':[5,53], 'Adwa':[7,65], 'Adigrat':[4,62]},
  'FinoteSelam' : {'DebreMarkos':[3,39],'Injibar':[2,44],'BahirDar':[6,48]},
  'Injibar' : {'FinoteSelam':[2,42],'BahirDar':[4,48]},
  'Metekel' : {},
  'DebreTabor' : {'Lalibela':[8,57],'BahirDar':[4,48]},
  'Sekota' : {'Mekelle':[9,58], 'Alamata':[6,53], 'Lalibela':[6,57]},
  'Alamata' : {'Woldia':[3,50], 'Sekota':[6,59], 'Samara':[11,42], 'Mekelle':[5,58]},
  'DebreMarkos' : {'FinoteSelam':[3,42], 'DebreSina':[17,33]},
  'Assosa' : {},
  'Lalibela' : {'DebreTabor':[8,52], 'Woldia':[7,50], 'Sekota':[6,59]},
  'Woldia' : {'Dessie':[6,44], 'Lalibela':[7,57], 'Alamata':[3,53], 'Samara':[8,42]},
  'Samara' : {'GabiRasu':[9,32], 'Woldia':[8,50], 'Alamata':[11,53], 'FantiRasu':[7,49]},
  'DebreSina' : {'DebreBirhan':[2,31], 'DebreMarkos':[17,39], 'Kemise':[6,40]},
  'DembiDollo': {'Assosa':[12,51], 'Gimbi':[6,43], 'Gambella':[4,51]},
  'Dessie' : {'Kemise':[4,40], 'Woldia':[6,50]},
  'GabiRasu' : {'Awash':[5,27], 'Samara':[9,42]},
  'FantiRasu' : {'Samara':[7,42],'KilbetRasu':[6,55]},
  'DebreBirhan': {'DebreSina':[2,33], 'AddisAbaba':[5,26]},
  'DebreMarkos': {'FinoteSelam':[3,42],'DebreSina':[17,33]},
  'Kemise' : {'Dessie':[4,44],'DebreSina':[6,33]},
  'Awash' : {'GabiRasu':[5,32],'Chiro':[4,31],'Matahara':[1,26]},
  'KilbetRasu' :{},
  'AddisAbaba':{'DebreBirhan':[5,31],'Ambo':[5,31],'Adama':[3,23]},
  'Chiro' : {'Awash':[4,27],'DireDawa':[8,31]},
  'Matahara' : {'Adama':[3,23],'Awash':[1,27]},
  'Ambo': {'Wolkite':[6,25],'Nekemete':[9,39],'AddisAbaba':[5,26]},
  'Adama':{'AddisAbaba':[3,26],'Matahara':[3,26],'Batu':[4,19],'Assella':[4,22]},
  'DireDawa':{'Chiro':[8,31],'Harar':[4,35]},
  'Wolkite' : {'Ambo':[6,31],'Jimma':[8,33], 'Worabe':[5,22]},
  'Nekemete': {'Ambo':[9,31],'Gimbi':[4,43],'Bedelle':[2,40]},
  'Batu' : {'Adama':[4,23], 'ButaJirra':[2,21],'Shashemene':[3,16]},
  'Assella':{'Assasa':[4,18],'Adama':[4,23]},
  'Harar' : {'DireDawa':[4,31], 'Bablle':[2,37]},
  'Jimma' : {'Wolkite':[8,25],'Bedelle':[7,40],'Bonga':[4,33]},
  'Worabe': {'Wolkite':[5,25],'Hossana':[2,21],'ButaJirra':[2,21]},
  'Gimbi' : {'Nekemete':[4,39], 'DembiDollo':[6,49]},
  'Bedelle': {'Nekemete':[2,39],'Jimma':[7,33], 'Gore':[6,46]},
  'ButaJirra' :{'Worabe':[2,22],'Batu':[2,19]},
  'Shashemene':{'Batu':[3,19],'Hossana':[7,21],'Hawassa':[1,15],'Dodolla':[3,19]},
  'Assasa' : {'Assella':[4,22],'Dodolla':[1,19]},
  'Bablle' : {'Harar':[3,35],'Jigjiga':[3,40]},
  'Bonga' : {'Jimma':[4,33],'Dawaro':[10,23],'Tepi':[8,41],'MezanTeferi':[4,37]},
  'Hossana' : {'Worabe':[2,22],'Shashemene':[7,16],'WolaitaSodo':[4,17]},
  'Gore' : {'Bedelle':[6,40],'Tepi':[9,41], 'Gambella':[5,51]},
  'Hawassa' : {'Shashemene':[1,16],'Dila':[3,12]},
  'Dodolla' : {'Shashemene':[3,16],'Assasa':[1,18],'Robe':[13,22]},
  'Jigjiga' : {'Bablle':[3,37],'DegaHabur':[5,45]},
  'Dawaro'  : {'Bonga':[10,33],'WolaitaSodo':[6,17]},
  'Tepi'    : {'Gore':[9,46],'MezanTeferi':[4,37],'Bonga':[8,33]},
  'MezanTeferi' : {'Tepi':[4,41], 'Bonga':[4,33]},
  'WolaitaSodo' : {'Hossana':[4,21], 'Dawaro':[6,23], 'ArbaMinch':[4,13]},
  'Gambella' : {'DembiDollo':[4,49],'Gore':[5,46]},
  'Dila' : {'Hawassa':[3,15],'BuleHora':[4,8]},
  'Robe' : {'Dodolla':[13,19],'Liben':[11,11],'Goba':[18,40],'SofOumer':[23,45]},
  'DegaHabur' : {'Jigjiga':[5,40], 'KebriDehar':[6,40]},
  'Dawaro': {'WolaitaSodo':[4,17],'Bonga':[10,33]},
  'ArbaMinch' : {'Konso':[4,9],'Basketo':[10,23],'WolaitaSodo':[4,17]},
  'Basketo' : {'ArbaMinch':[10,13],'BenchiMaji':[5,28]},
  'BuleHora' : {'Dila':[4,12],'Yabello':[3,6]},
  'Liben' :{},
  'Goba':{'Robe':[18,22],'SofOumer':[6,45],'Bablle':[28,37]},
  'SofOumer': {'Robe':[23,22],'Goba':[6,40],'Gode':[23,35]},
  'KebriDehar': {'DegaHabur':[6,45],'Werder':[6,46],'Gode':[5,35]},
  'Yabello' : {'BuleHora':[3,8],'Konso':[3,9],'Moyale':[6,0]},
  'BenchiMaji' :{} ,
  'Gode' :{'Dollo':[17,18]},
  'Dollo': {},
  'Werder':{},
  'Konso' :{'ArbaMinch':[4,9],'Yabello':[3,6]},
  'Moyale':{}
}

from queue import PriorityQueue
import heapq

def Astar(startNode, heuristics, graph, goalNode="Bucharest"):
    priorityQueue = queue.PriorityQueue()
    distance = 0
    path = []

    priorityQueue.put((heuristics[startNode] + distance, [startNode, 0]))

    while priorityQueue.empty() == False:
        current = priorityQueue.get()[1]
        path.append(current[0])
        distance += int(current[1])

        if current[0] == goalNode:
            break

        priorityQueue = queue.PriorityQueue()

        for i in graph[current[0]]:
            if i[0] not in path:
                priorityQueue.put((heuristics[i[0]] + int(i[1]) + distance, i))

    return path
    
print(Astar(graph,'AddisAbaba','Moyale'))