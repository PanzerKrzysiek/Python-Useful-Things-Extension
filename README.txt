1. The module_en.py plot:
  1.1. The batch() function:
    Executes the batch command.
    Example: batch("cls") — this command clears the screen in command prompt.
  1.2. The Word() class:
    Generates the undefined word in the consonant-vowel-consonant (etc.) sequence.
    This class must include an integer number passed between quotes.
    The number will be the count of generated word.
    1.2.1. The .get() method:
      Returns the created word.
        1.2.1.1. The .get() method contains a variable that can store two values:
          1.2.1.1.1. The "normal" (default) value — returns the basic form of generated word.
          1.2.1.1.2. The "reversed" value — returns the reversed word.
    Example:
      var1 = Word(5)
      var1.get()
      >>> Ryvop
      var1.get("reversed")
      >>> Povyr
  1.3. The String() class:
    Executes different operations on a string written in brackets.
    1.3.1. The each_letter() method:
      Returns each letter of a string which was typed in brackets.
    1.3.2. The .get() method:
      Returns the string.
      1.3.2.1. The .get() method can contains a number of times of returned string.
    1.3.3. The .get_lenght() method:
      Returns the lenght of a string in number of characters.
    1.3.4. The .letter() method:
      Returns the letter by passed index.
      Must include integer number typed in brackets!
    1.3.5 The .reverse() method:
      Returns the reversed string.
    Example:
      var2 = String("Hello, World!")
      var2.each_letter()
      >>> H
      >>> e
      >>> l
      >>> l
      >>> o
      [...]
      var2.get()
      >>> Hello, World!
      var2.get_lenght()
      >>> 13
      var2.letter(7)
      >>> W
      var2.reverse()
      >>> !dlroW ,olleH
2. Recommended methods of use:
  2.1. Import module to Python interpreter.
  2.2. Import module to your own Python project.
