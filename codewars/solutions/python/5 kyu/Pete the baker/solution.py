def cakes(recipe, available):
    return min(available[k] // recipe[k] for k in recipe) if set(recipe).issubset(available) else 0
