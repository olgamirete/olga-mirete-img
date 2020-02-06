from PIL import ImageFont

def get_wrapped_text(text, PIL_font, max_width):
        
        # Returns a list where each item is a line of text that does not exceed
        # the max_width. If there should be any single word that is bigger than
        # the max_width argument, it will be shown in an individual line, even
        # though it exceeds the max_width.

        lines = []
        
        # Split the line by spaces to get a list of words.
        words = text.split(' ')
        i = 0
        # Append every word to a line while its width is shorter than the image
        # width
        while i < len(words):
            
            line = ''
            
            new_line = words[i]

            while i < len(words):
                new_line = line + ' ' + words[i]
                if PIL_font.getsize(new_line)[0] <= max_width:
                    line = new_line
                    i += 1
            
            if line == '':
                line = words[i]
                i += 1
            else:
                line = line[1:]
            
            lines.append(line)

        return lines