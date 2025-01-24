from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Найти узлы без исходящих ребер (конечные узлы)
        safety_set = {i for i, lst in enumerate(graph) if not lst}
        
        # Проверяем остальные узлы
        def is_safe(node):
            visited.add(node)  # Отмечаем узел как посещенный
            for neighbor in graph[node]:
                if neighbor not in safety_set:  # Если сосед не безопасен
                    if neighbor in visited or not is_safe(neighbor):
                        return False
            safety_set.add(node)  # Узел безопасен, добавляем его в множество
            return True
        
        visited = set()
        for i in range(len(graph)):
            if i not in safety_set and i not in visited:
                is_safe(i)
        
        # Возвращаем отсортированный список всех безопасных узлов
        return sorted(safety_set)
