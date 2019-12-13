def sqInRect(height, width, first=True):
    if height == width:
        return None if first else [height]

    if height > width:
        r, height = width, height - width
    else:
        r, width = height, width - height

    return [r] + (sqInRect(height, width, False) or [])
