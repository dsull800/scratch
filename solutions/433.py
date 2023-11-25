class Solution:
    def __init__(self):
        self.string_bank = {}

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def string_compare(string1, string2):
            count = 0
            for s_ind, (s_1, s_2) in enumerate(zip(string1, string2)):
                if s_1 != s_2:
                    count += 1
                    if count > 1:
                        return False
            return True

        if endGene not in bank:
            return -1

        genes = list(set([startGene] + bank))
        for id_gene, gene in enumerate(genes[:-1]):
            for gene_comp in genes[id_gene + 1:]:
                if string_compare(gene, gene_comp):
                    self.string_bank[gene] = self.string_bank.get(gene, []) + [gene_comp]
                    self.string_bank[gene_comp] = self.string_bank.get(gene_comp, []) + [gene]

        # if len(self.string_bank.get(endGene, [])) == 0:
        #     return -1

        visited = set()
        frontier = deque(self.string_bank[startGene])
        frontier.appendleft('move')
        moves = 1
        while frontier:
            current_gene = frontier.pop()
            if current_gene == 'move':
                moves += 1
                if frontier:
                    frontier.appendleft('move')
                continue
            if current_gene == endGene:
                return moves
            frontier.extendleft([gene for gene in self.string_bank[current_gene] if gene not in visited])
            visited = visited.union(set(self.string_bank[current_gene]))

        return -1

