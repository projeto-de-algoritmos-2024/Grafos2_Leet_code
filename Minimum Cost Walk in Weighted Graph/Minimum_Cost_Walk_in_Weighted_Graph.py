class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        def encontrar(no: int) -> int:
            if no == pai[no]: 
                return no
            pai[no] = encontrar(pai[no])
            return pai[no]
        
        def unir(u: int, v: int, peso: int) -> int:
            x, y = encontrar(u), encontrar(v)
            peso_max[y] &= peso_max[x] & peso
            pai[x] = y
        
        def encontrar_peso(consulta: list) -> int:
            origem, destino = consulta
            if origem == destino: 
                return 0
            if encontrar(origem) != encontrar(destino): 
                return -1
            return peso_max[encontrar(origem)]
        
        pai = list(range(n))
        resposta = []
        peso_max = [(1<<31) - 1] * n
        
        for edge in edges:
            unir(*edge)
        
        return list(map(encontrar_peso, queries))

        for edge in edges:
            unir(*edge)
        
        return list(map(encontrar_peso, queries))

peso_max = [(1<<31) - 1] * 10
