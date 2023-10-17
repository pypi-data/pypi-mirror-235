import wcwidth

def printBox(singleLineString):
    singleLineString = str(singleLineString)
    localStringLength = len(singleLineString)
    localTop = '═'*localStringLength
    print('\n '+localTop+'\n '+singleLineString+'\n '+localTop+'\n') # '\n╔'+ +'╗\n' '\n╚'+ +'╝' '║'+

def get_display_width(string):
    total_width = 0
    for char in string:
        width = wcwidth.wcwidth(char)
        if width == -1:
            width = 0
        total_width += width
    return total_width

def printBoxThin(singleLineString):
    singleLineString = str(singleLineString)
    localStringLength = get_display_width(singleLineString)
    new_input = ""
    spaces = 0

    for i, letter in enumerate(singleLineString):
        width = wcwidth.wcwidth(letter)
        if width == -1:
            width = 0

        if letter == ' ':
            spaces += 1
            if spaces == 9:
                new_input += '\n'
                spaces = 0
            else:
                new_input += letter
        elif letter == '\n':
            new_input += ' '
            spaces += 1
            if spaces == 9:
                new_input += '\n'
                spaces = 0
        else:
            new_input += letter

    localStringArray = new_input.split('\n')
    maxLineLength = max(get_display_width(line) for line in localStringArray)
    bht = ''

    for index, line in enumerate(localStringArray):
        fillLength = maxLineLength - get_display_width(line)
        filler = ' ' * fillLength
        line = ' │' + line + filler + '│\n'
        bht += line

    localTop = '─' * maxLineLength
    if get_display_width(localTop) > maxLineLength:
        localTop = localTop.replace('─', '', get_display_width(localTop) - maxLineLength)

    print('\n ┌' + localTop + '┐\n' + bht + '┌┴' + localTop + '┘')