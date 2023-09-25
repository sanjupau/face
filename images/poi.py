from itertools import combinations

def generate_candidates(itemset, k):
    """
    Generate candidate itemsets of size k from a given itemset
    """
    candidates = []
    for i in range(len(itemset)):
        for j in range(i+1, len(itemset)):
            # Join the two itemsets if the first k-2 items are the same
            if itemset[i][:k-2] == itemset[j][:k-2]:
                candidate = tuple(set(itemset[i]) | set(itemset[j]))
                # Prune the candidate if any subset of size k-1 is not in the itemset
                if all([subset in itemset for subset in combinations(candidate, k-1)]):
                    candidates.append(candidate)
    return candidates