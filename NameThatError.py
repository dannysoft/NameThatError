import random as rnd
questionCount = 0
questionScore = 0
askMeAnother = True
while askMeAnother:
    print("\n"*12)
    print("You have answered {0} questions so far and scored {1}/{0}. ".format(questionCount,questionScore))
    print("\n"*2)
    try:
        possErrorNum = 0    #key access into dictionary possErrors.
        otherErrorNum = 0   #other possible keys.
        errorAnswer = ""    #Error name questioned about.
        #Built-in exceptions that are usually raised in Python:
        possErrors = {
        1:'ArithmeticError',
        2:'AssertionError',
        3:'AttributeError',
        4:'EOFError',
        5:'Exception',
        6:'FloatingPointError',
        7:'GeneratorExit',
        8:'ImportError',
        9:'IndentationError',
        10:'IndexError',
        11:'KeyboardInterrupt',
        12:'KeyError',
        13:'LookupError',
        14:'MemoryError',
        15:'NameError',
        16:'NotImplementedError',
        17:'OSError',
        18:'OverflowError',
        19:'ReferenceError',
        20:'RuntimeError',
        21:'StopIteration',
        22:'SyntaxError',
        23:'SystemError',
        24:'SystemExit',
        25:'TabError',
        26:'TypeError',
        27:'UnboundLocalError',
        28:'UnicodeDecodeError',
        29:'UnicodeEncodeError',
        30:'UnicodeError',
        31:'UnicodeTranslateError',
        32:'ValueError',
        33:'ZeroDivisionError'
        }
        possErrorNum = rnd.randint(1,33)        #randomly chosen error to raise
        errorAnswer = possErrors[possErrorNum]  #error name
        lstpossErrorNums = [possErrorNum]       #error possible answers list A,B,C or D
        
        #create a list object containing 1 answer index and 3 other indexes
        threeOtherErrors = 0
        while threeOtherErrors < 3:
            otherErrorNum = rnd.randint(1,33)
            if otherErrorNum not in lstpossErrorNums:
                lstpossErrorNums.append(otherErrorNum)
                threeOtherErrors += 1
            #end if
        #end while
        lstpossErrorNums.sort()
        ansPos = lstpossErrorNums.index(possErrorNum)
        answerLetters = ["A","B","C","D"]
        answerLetter = answerLetters[ansPos] #Actual answer letter from multiple choice question.

        if possErrorNum == 1:  raise ArithmeticError
        if possErrorNum == 2:  raise AssertionError
        if possErrorNum == 3:  raise AttributeError
        if possErrorNum == 4:  raise EOFError
        if possErrorNum == 5:  raise Exception
        if possErrorNum == 6:  raise FloatingPointError
        if possErrorNum == 7:  raise GeneratorExit
        if possErrorNum == 8:  raise ImportError
        if possErrorNum == 9:  raise IndentationError
        if possErrorNum == 10:  raise IndexError
        if possErrorNum == 11:  raise KeyboardInterrupt
        if possErrorNum == 12:  raise KeyError
        if possErrorNum == 13:  raise LookupError
        if possErrorNum == 14:  raise MemoryError
        if possErrorNum == 15:  raise NameError
        if possErrorNum == 16:  raise NotImplementedError
        if possErrorNum == 17:  raise OSError
        if possErrorNum == 18:  raise OverflowError
        if possErrorNum == 19:  raise ReferenceError
        if possErrorNum == 20:  raise RuntimeError
        if possErrorNum == 21:  raise StopIteration
        if possErrorNum == 22:  raise SyntaxError
        if possErrorNum == 23:  raise SystemError
        if possErrorNum == 24:  raise SystemExit
        if possErrorNum == 25:  raise TabError
        if possErrorNum == 26:  raise TypeError
        if possErrorNum == 27:  raise UnboundLocalError
        if possErrorNum == 28:  raise UnicodeDecodeError
        if possErrorNum == 29:  raise UnicodeEncodeError
        if possErrorNum == 30:  raise UnicodeError
        if possErrorNum == 31:  raise UnicodeTranslateError
        if possErrorNum == 32:  raise ValueError
        if possErrorNum == 33:  raise ZeroDivisionError


    except ArithmeticError:  print('Raised when an error occurs in numeric calculations', end = '') 
    except AssertionError:  print('Raised when an assert statement fails', end = '') 
    except AttributeError:  print('Raised when attribute reference or assignment fails', end = '') 
    except EOFError:  print('Raised when the input() method hits an "end of file" condition (EOF)', end = '') 
    except FloatingPointError:  print('Raised when a floating point calculation fails', end = '') 
    except GeneratorExit:  print('Raised when a generator is closed (with the close() method)', end = '') 
    except ImportError:  print('Raised when an imported module does not exist', end = '') 
    except IndentationError:  print('Raised when indendation is not correct', end = '') 
    except IndexError:  print('Raised when an index of a sequence does not exist', end = '') 
    except KeyboardInterrupt:  print('Raised when the user presses Ctrl+c, Ctrl+z or Delete', end = '') 
    except KeyError:  print('Raised when a key does not exist in a dictionary', end = '') 
    except LookupError:  print('Raised when errors raised cant be found', end = '') 
    except MemoryError:  print('Raised when a program runs out of memory', end = '') 
    except NameError:  print('Raised when a variable does not exist', end = '') 
    except NotImplementedError:  print('Raised when an abstract method requires an inherited class to override the method', end = '') 
    except OSError:  print('Raised when a system related operation causes an error', end = '') 
    except OverflowError:  print('Raised when the result of a numeric calculation is too large', end = '') 
    except ReferenceError:  print('Raised when a weak reference object does not exist', end = '') 
    except RuntimeError:  print('Raised when an error occurs that do not belong to any specific expections', end = '') 
    except StopIteration:  print('Raised when the next() method of an iterator has no further values', end = '') 
    except SyntaxError:  print('Raised when a syntax error occurs', end = '') 
    except SystemError:  print('Raised when a system error occurs', end = '') 
    except SystemExit:  print('Raised when the sys.exit() function is called', end = '') 
    except TabError:  print('Raised when indentation consists of tabs or spaces', end = '') 
    except TypeError:  print('Raised when two different types are combined', end = '') 
    except UnboundLocalError:  print('Raised when a local variable is referenced before assignment', end = '') 
    except UnicodeDecodeError:  print('Raised when a unicode decoding problem occurs', end = '') 
    except UnicodeEncodeError:  print('Raised when a unicode encoding problem occurs', end = '') 
    except UnicodeError:  print('Raised when a unicode problem occurs', end = '') 
    except UnicodeTranslateError:  print('Raised when a unicode translation problem occurs', end = '') 
    except ValueError:  print('Raised when there is a wrong value in a specified data type', end = '') 
    except ZeroDivisionError:  print('Raised when the second operator in a division is zero', end = '')
    except Exception:  print('Base class for all exceptions', end = '')
    finally:
        questionCount += 1
        qText = '''

        From the description above.
        What error was raised?
        Choose one of the following 4 options...
        
        A) {1}
        B) {2}
        C) {3}
        D) {4}
        '''
        print(qText.format(errorAnswer,
                           possErrors[lstpossErrorNums[0]],
                           possErrors[lstpossErrorNums[1]],
                           possErrors[lstpossErrorNums[2]],
                           possErrors[lstpossErrorNums[3]]))
        yourAnswer = input("Which error is being described? A,B,C or D: ")
        if yourAnswer.upper() == answerLetter.upper():
            print("CORRECT! Well done :-)")
            questionScore += 1
        else:
            print("Wrong! Keep trying :-(.")
            print("Learning point, actual answer is: ",errorAnswer)
        #end if

    another = input("\n\nY or y for another: ").upper()          
    askMeAnother = (another == "Y")
print("\n")
print("You have answered {0} questions and scored {1}/{0}. ".format(questionCount,questionScore))
print("\n")
