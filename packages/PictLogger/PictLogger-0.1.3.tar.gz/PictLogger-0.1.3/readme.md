## PictLogger

A simple logger writen in c++
For now, works only on Linux, X86_64
I`m trying to compile it for Windows, maybe it will be 

You can see all sources at https://github.com/ilyadudelzak/pictlogger

## How to use

To save files you need to create the "logs" folder near your main program

## Simple example:
```python
import pictlogger

pictlogger.start(True)

pictlogger.log("Testing", "Hello, World!")

pictlogger.close(0)
```
It prints and saves to the file:
```
Fri Oct 13 15:34:48 2023 Pictlogger: Started
Fri Oct 13 15:34:48 2023 PictLogger: Version: 0.0.1
Fri Oct 13 15:34:48 2023 Python: PictLogger Imported Successfully
Fri Oct 13 15:34:48 2023 Testing: Hello, World!
Fri Oct 13 15:34:48 2023 PictLogger: Exit with exit code: 0 (Success)
```

## Example with exception

```python
import pictlogger

pictlogger.start(True)

pictlogger.log("Testing", "Hello, World!")

try:
    n = int(input())
    pictlogger.log("Testing", "User entered number " + str(n));
    pictlogger.close(0)
    
except Exception as e:
    pictlogger.log("Exception", str(e))
    pictlogger.close(1)
```
it will print
```
Fri Oct 13 16:10:19 2023 Pictlogger: Started PictLogger
Fri Oct 13 16:10:19 2023 PictLogger: Version: 0.0.1
Fri Oct 13 16:10:19 2023 Python: PictLogger Imported Successfully
Fri Oct 13 16:10:19 2023 Testing: Hello, World!
1234
Fri Oct 13 16:10:21 2023 Testing: User entered number 1234
Fri Oct 13 16:10:21 2023 PictLogger: Exit with exit code: 0 (Success)
```
Or
```
Fri Oct 13 16:10:37 2023 Pictlogger: Started PictLogger
Fri Oct 13 16:10:37 2023 PictLogger: Version: 0.0.1
Fri Oct 13 16:10:37 2023 Python: PictLogger Imported Successfully
Fri Oct 13 16:10:37 2023 Testing: Hello, World!
kitten
Fri Oct 13 16:10:41 2023 Exception: invalid literal for int() with base 10: 'kitten'
Fri Oct 13 16:10:41 2023 PictLogger: Exit with exit code: 1 (Error)

```

## Documentation

## start(print)
Starts library, opens the file.

print is True or False

If it is true, library will print all logs to the screen.

If if is false, it will not print logs, but save all to the file, like before.

## log(sender, text)
It will save log string to file and print it, if you setted print to true.

sender is string, thal prints before text.
text is string, that prints after text, it contains main sense of the log.

## close(code)
Closes output and saves files
Call at end of program

code is number, that is an exit code of your program.
Library will print it after exit message
