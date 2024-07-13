# parallel-processing-pyqt: Parallel Processing From PyQt6

## Introduction
I created this concept application to *hopefully* help others and to garner constructive feedback as to how it might be improved.

## The Problem
- PyQt applications have a main thread of execution: **the GUI thread**.
- Typically, anything called directly from PyQt (object method calls, scripts, etc.) is run on the GUI thread.
- This results in everything running **synchronously**, one task at a time - which can be impractical for sophisticated applications.
- PyQt does offer **multithreading**, which allows for subprograms to be run, in thread(s), separate to the GUI thread.
  - This can often be all that is required, and if that is all you need, this application can still help you with that!
  - Simply adjust the *thread_worker* module so it no longer instantiates *ParallelSupervisor*.
- If **multiprocessing** is required, however, things get even more complicated.
  - multithreading and multiprocessing need to be combined.

## This Solution
- This solution demonstrates combining multithreading (with PyQt [QThread](https://doc.qt.io/qt-6/qthread.html)) with multiprocessing, via [RAY](https://www.ray.io/).
  - I chose RAY because I find it easier to work with, and the principles of how to communicate between multiprocessing and PyQt are the same regardless of the library you use.
- **Please note**: This is definitely **not** a demonstration of how to do multiprocessing - that's a big topic, out of the scope of this.
- This solution also employs the [Model-View-ViewModel](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel) design pattern, because:
  1. I think it's good practice, and I'm trying to use it more.
  2. It actually lent itself, very nicely, to this particular problem.

## Reference Sources
- [Doing python multiprocessing The Right Way](https://medium.com/@sampsa.riikonen/doing-python-multiprocessing-the-right-way-a54c1880e300)
- [Use PyQt's QThread to Prevent Freezing GUIs](https://realpython.com/python-pyqt-qthread/)
- [Model–view–viewmodel](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel)
- [Model-View-ViewModel (MVVM)](https://learn.microsoft.com/en-us/dotnet/architecture/maui/mvvm)