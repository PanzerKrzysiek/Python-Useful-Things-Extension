1. Requirements: Python.
 
2. The module.py plot:
  2.1. The batch() function:
    Executes the batch commands from Windows Command Prompt.
    Example: batch("cls") — this command clears the screen in command prompt.
  2.2. The Word() class:
    Generates the undefined word in the consonant-vowel-consonant (etc.) sequence.
    This class must include an integer number passed between quotes.
    The number will be the count of generated word.
    2.2.1. The __repr__(self) method:
      Returns the generated word by printing the name of class Word().
      Example:
        var1 = Word(5)
        print(var1)
        >>> Tefop
    2.2.2. The __len__(self) method:
      Returns the lenght of the generated word.
        var1 = Word(5)
        print(len(var1))
        >>> 5
    2.2.3. The .get() method:
      Returns the created word.
      2.2.3.1. The .get() method contains a variable that can store the following values:
        2.2.3.1.1. The "normal" (default) value — returns the basic form of generated word.
        2.2.3.1.2. The "reversed" value — returns the reversed word.
        2.2.3.1.3. The "lenght" value — returns the lenght of the word.
        2.2.3.1.4. The "capitalized" value — returns the capitalized form of generated word.
        2.2.3.1.5. The "lowered" value — returns the lowered form of generated word.
        2.2.3.1.6. The "uppered" value — returns the uppered form of generated word.
    Example:
      var1 = Word(5)
      var1.get()
      >>> Ryvop
      var1.get("reversed")
      >>> Povyr
  2.3. The String() class:
    Executes different operations on a string written in brackets.
    2.3.1. The each_letter() method:
      Returns each letter of a string which was typed in brackets.
    2.3.2. The .get() method:
      Returns the string.
      1.3.2.1. The .get() method can contains a number of times of returned string.
    2.3.3. The .get_lenght() method:
      Returns the lenght of a string in number of characters.
    2.3.4. The .letter() method:
      Returns the letter by passed index.
      Must include integer number typed in brackets!
    2.3.5 The .reverse() method:
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
3. Recommended methods of use:
  3.1. Import module to Python interpreter:
    3.1.1. Open command prompt in the module.py directory.
    3.1.2. Type "python" in command prompt.
    3.1.3. Type "from module import *" in command prompt.
  3.2. Import module to Your own Python Project:
    3.2.1. Copy the module.py file to Your own Python Project directory.
    3.2.1. Type "from module import *" in Your own Python Project.
