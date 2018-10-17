
if __name__ == '__main__':
    bullet_number = 0  # To track current bullet number
    sub_bullet_num = None # To track sub bullet number of current Bullet
    nested_level_count_dict = {} # To track sub bullet nested count
    for line in sys.stdin:
       if line.startswith('* '):
            bullet_number += 1
            line = line.replace('*', str(bullet_number) + " ")
            sub_bullet_num = None
            nested_level_count_dict = {}
        elif line.startswith('**'):
            sub_str = line[0: line.index(" ")+1]  # Get the substring from start to till we get first space
            star_count = sub_str.count('*')
            if star_count in nested_level_count_dict:
                # increase sub bullet num if it repeats
                nested_level_count_dict[star_count] = nested_level_count_dict.get(star_count) + 1
            else:
                nested_level_count_dict[star_count] = 1
 
            # Calculate the sub bullet no based on the repetition of stars
            if nested_level_count_dict.get(star_count) == 1:
                sub_bullet_num = str(bullet_number) + "."
            else:
                sub_bullet_num = str(bullet_number) + "." + str(nested_level_count_dict.get(star_count)) + "."
                star_count -= 1
            sub_bullet_num_str = sub_bullet_num + ".".join([str(1) for i in range(1, star_count)])
 
            # replace stars with sub bullet number
            last_star_index = sub_str.rindex('* ')
            line = sub_bullet_num_str + " " + line[last_star_index+1:]
        elif line.startswith(". "):
            line = line.replace('. ', '- ')
 
        sys.stdout.write(line)
 
# Working with following command
# cat input.txt | python parse_file.py > output.txt

"""
Sample Output:

1  This is an outline

- It's not a very good outline

.. I've seen better

.. I've seen worse

... I saw a really bad one back in 2008

2  This is the second numbered item in the outline

- This is sub text that spans multiple lines

This should be included with the previous line

And this line too

.. That is more sub text

3  Numbers

- Some text

3.1  Lots

- Some more text

- And some more

3.1.1  And lots

- One

.. Two

... Three

3.1.1.1  Of numbers

- Another line

3.2.  Less Numbers

- Text

3.2.1  More Numbers

- Blah

4  One number again

- The last line
"""
