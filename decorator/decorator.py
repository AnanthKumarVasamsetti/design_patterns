"""
Decorator: This structural design pattern allows additional behaviours (or) responsibilities to be dynamically
           attached to an object, through the use of aggregation to combine behaviours at runtime.

Example: In the following example a simple text gets rendered into different styles during runtime.
"""

class TextTag:
    def __init__(self, text):
        self.text = text
    
    def render(self):
        return self.text

class BoldText(TextTag):
    def __init__(self, wrapper):
        self.wrapper = wrapper
    
    def render(self):
        return '<b>{}</b>'.format(self.wrapper.render())

class ItalicText(TextTag):
    def __init__(self, wrapper):
        self.wrapper = wrapper
    
    def render(self):
        return '<i>{}</i>'.format(self.wrapper.render())


if __name__ == "__main__":
    simple_text = TextTag("Hello world")
    italic_text = ItalicText(simple_text)
    bold_text = BoldText(simple_text)
    special_text = ItalicText(BoldText(simple_text))

    print(simple_text.render())
    print(italic_text.render())
    print(bold_text.render())
    print(special_text.render())