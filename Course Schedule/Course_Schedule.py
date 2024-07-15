class Solution:
    def canFinish(self, n, prerequisites):
        grafo1 = [[] for _ in range(n)]
        grafo2 = [[] for _ in range(n)]
        visitado = [False] * n
        finalizado = [0] * n
        tempo = [0]  # Use uma lista para passar por referência

        for edge in prerequisites:
            de_no, para_no = edge
            if de_no == para_no:
                return False
            grafo1[de_no].append(para_no)
            grafo2[para_no].append(de_no)

        for i in range(n):
            if not visitado[i]:
                self.dfs(grafo1, i, visitado, finalizado, tempo)

        ordens = list(range(n))
        ordens.sort(key=lambda x: finalizado[x], reverse=True)

        cfc = 0
        tempo[0] = 0
        visitado = [False] * n
        for id in ordens:
            if not visitado[id]:
                self.dfs(grafo2, id, visitado, finalizado, tempo)
                cfc += 1

        return cfc == n

    def dfs(self, grafo, id, visitado, finalizado, tempo):
        tempo[0] += 1
        visitado[id] = True
        for vizinho in grafo[id]:
            if not visitado[vizinho]:
                self.dfs(grafo, vizinho, visitado, finalizado, tempo)
        tempo[0] += 1
        finalizado[id] = tempo[0]
