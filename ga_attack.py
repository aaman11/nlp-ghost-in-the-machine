import random

def mutate_with_llm(gemini_generate_fn, paragraph):
    prompt = f"""Rewrite this paragraph to change the rhythm of the sentences while keeping the vocabulary mostly similar.
Introduce a subtle grammatical inconsistency or a rare archaic word.
Keep the meaning broadly the same.

Paragraph:
{paragraph}
"""
    return gemini_generate_fn(prompt)

def genetic_optimize(initial_population, score_fn, mutate_fn, generations=5, elite_k=3):
    population = list(initial_population)
    history = []

    for gen in range(generations):
        scored = [(txt, score_fn(txt)) for txt in population]
        scored.sort(key=lambda x: x[1], reverse=True)
        elites = [t for t, s in scored[:elite_k]]
        history.append({
            "generation": gen,
            "best_score": scored[0][1],
            "avg_score": sum(s for _, s in scored) / len(scored)
        })

        next_pop = elites[:]
        while len(next_pop) < len(population):
            parent = random.choice(elites)
            child = mutate_fn(parent)
            next_pop.append(child)
        population = next_pop

    return population, history
