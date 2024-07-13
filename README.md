# parallel-processing-pyqt: Parallel Processing From PyQt6

## Introduction
I created this concept application to *hopefully* help others and to garner constructive feedback as to how it might be improved.

## The Problem
- PyQt applications have a main thread of execution: **the GUI thread**.
- Typically, anything called directly from PyQt (object method calls, scripts, etc.) is run on the GUI thread.
- This results in everything running **synchronously**, one task at a time - which can be impractical for sophisticated applications.
- PyQt does offer **multithreading**, which allows for subprograms to be run in thread(s) separate to the GUI thread.
  - This can often be all that is required, and this is a great primer: [Use PyQt's QThread to Prevent Freezing GUIs](https://realpython.com/python-pyqt-qthread/)
- If you require **multiprocessing**, however, things get even more complicated.

## This Solution
[TODO]

## Reference Sources
- [Doing python multiprocessing The Right Way](https://medium.com/@sampsa.riikonen/doing-python-multiprocessing-the-right-way-a54c1880e300)
- [Use PyQt's QThread to Prevent Freezing GUIs](https://realpython.com/python-pyqt-qthread/)
- [Model–view–viewmodel](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel)
- [Model-View-ViewModel (MVVM)](https://learn.microsoft.com/en-us/dotnet/architecture/maui/mvvm)