class Solution:
    def canFinish(self, n, prerequisites):
        grafo1 = [[] for _ in range(n)]
        grafo2 = [[] for _ in range(n)]
        visitado = [False] * n
        finalizar = [0] * n
        tempo = [0]  

        for aresta in prerequisites:
            de_no, para_no = aresta
            if de_no == para_no:
                return False
            grafo1[de_no].append(para_no)
            grafo2[para_no].append(de_no)

        ordens = list(range(n))
        
        for i in range(n):
            if not visitado[i]:
                self.dfs(grafo1, i, finalizar, tempo, visitado)

        ordens.sort(key=lambda x: finalizar[x], reverse=True)

        scc = 0
        tempo[0] = 0
        visitado = [False] * n
        
        for id in ordens:
            if not visitado[id]:
                self.dfs(grafo2, id, finalizar, tempo, visitado)
                scc += 1

        return scc > 0

    def dfs(self, grafo, id, finalizar, tempo, visitado):
        tempo[0] += 1
        visitado[id] = True
        for vizinho in grafo[id]:
            if not visitado[vizinho]:
                self.dfs(grafo, finalizar, vizinho, tempo, visitado)
                tempo[0] += 1
        tempo[0] += 1
        finalizar[id] = tempo[0]

