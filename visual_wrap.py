from PIL import ImageFont

def visual_split(text, font, width, response_type='list'):
    font = font
    words = text.split()
    
    word_lengths = [(word, font.getsize(word)[0]) for word in words]
    space_length = font.getsize(' ')[0]
    
    lines = ['']
    line_length = 0
    
    for word, length in word_lengths:

        if line_length+length <= width:
            lines[-1] = '{line}{word} '.format(line=lines[-1], word=word)
            line_length += length + space_length
        else:
            lines.append('{word} '.format(word=word))
            line_length = length + space_length
    
    if response_type == 'list':
        return [line.strip() for line in lines]
    elif response_type == 'str':
        return '\n'.join(line.strip() for line in lines)
    else:
        raise ValueError('Invalid response type. Valid values are "list" and "str".')
    
    
    
# Demonstrate Usage
if __name__ == '__main__':
    
    #Example Usage
    text = "This is a long piece of text, so we\'ll see how it splits."
    font = ImageFont.truetype("fonts/verdanab.ttf", 16)
    width = 200
    
    print(text)
    wrapped_text = visual_split(text, font, width)
    print(wrapped_text)
    
    # Illustrate how different letter widths affect line length
    text = 'iii iii iii iii iii iii iii iii iii iii iii iiw iiw iiw iiw iiw iiw iiw iiw iiw iiw www www www www www www www www www www'
    width = 50
    print(text)
    wrapped_text = visual_split(text, font, width)
    print(wrapped_text)