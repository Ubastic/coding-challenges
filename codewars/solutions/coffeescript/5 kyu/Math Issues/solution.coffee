Math.round = (number) -> parseInt(number) + (number % 1 >= 0.5)
Math.ceil  = (number) -> parseInt(number) + (number % 1 != 0)
Math.floor = (number) -> parseInt(number)