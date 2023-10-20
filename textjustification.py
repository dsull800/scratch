class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output_ind = 0
        word_store = []
        output = []
        max_width = maxWidth
        for word in words:
            if output_ind + len(word) + len(word_store) > max_width:
                spaces = max_width - (output_ind + len(word_store) - 1)
                spacing = ceil(spaces/(len(word_store) - 1)) if len(word_store) > 1 else spaces
                print(spacing)
                print(spaces)
                word_output = ""
                for index, word_s in enumerate(word_store):
                    if index < len(word_store) - 1:
                        word_output = word_output + word_s + ' ' + ' ' * max(0,min(spaces, spacing))
                        spaces = spaces - spacing
                    else:
                        word_output = word_output + word_s + ' ' * max(0,min(spaces, spacing))

                output.append(word_output)
                word_store = [word]
                print(word_store)
                output_ind = len(word)
            else:
                output_ind = output_ind + len(word)
                word_store.append(word)

        spaces = max_width - (output_ind + len(word_store) - 1)
        # spacing = ceil(spaces/(len(words) - 1)) if len(word_store) > 1 else spaces
        word_output = ""
        for index, word in enumerate(word_store):
            if index < len(word_store) - 1:
                word_output = word_output + word + ' '
            else:
                word_output = word_output + word + ' ' * spaces
        output.append(word_output)
        return output