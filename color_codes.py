MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

def get_length_major_colors(MAJOR_COLORS =MAJOR_COLORS ):
    return len(MAJOR_COLORS)

def get_length_minor_colors(MINOR_COLORS= MINOR_COLORS):
    return len(MINOR_COLORS)

def get_user_manual(major_colors = MAJOR_COLORS, minor_colors = MINOR_COLORS):
    a,b  = get_length_major_colors() ,get_length_major_colors()
    keys = list(range(1, a*b+1))
    color_pair= []
    for major_color in major_colors:
        for minor_color in minor_colors: 
            color_pair.append( f'{major_color} & {minor_color}')
    user_manual = dict(zip(keys, color_pair))
    return user_manual

def print_user_manual():
    user_manual = get_user_manual()
    for key, value in user_manual.items():
        print(f"\nPair: {key} --> {value}")
