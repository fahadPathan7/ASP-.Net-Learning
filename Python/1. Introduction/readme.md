# <div align='center'> 🔰 Introduction to Python </div>

## 📌 Table of Contents
- [ 🔰 Introduction to Python ](#--introduction-to-python-)
  - [📌 Table of Contents](#-table-of-contents)
  - [❓ What is Python?](#-what-is-python)
  - [📚 Features of Python](#-features-of-python)
  - [🖨️ Printing something](#️-printing-something)
<hr>

<br><br>

## ❓ What is Python?
- Python is a high-level, interpreted, interactive and object-oriented scripting language.
- Python is designed to be highly readable.
- It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages.

<br><br>

## 📚 Features of Python
- **Easy-to-learn:** Python has few keywords, simple structure, and a clearly defined syntax. This allows the student to pick up the language quickly.
- **Easy-to-read:** Python code is more clearly defined and visible to the eyes.
- **Easy-to-maintain:** Python's source code is fairly easy to maintain.
- **A broad standard library:** Python's bulk of the library is very portable and cross-platform compatible on UNIX, Windows, and Macintosh.
- **Dynamically typed:** Python is dynamically typed. We don't have to declare the type of variables.
- **Interpreted:** Python is processed at runtime by the interpreter. We do not need to compile program before executing it. This is similar to PERL and PHP.
- **Garbage Collection:** Python has an automatic garbage collection. Memory management is done internally and the user does not have to worry about memory management.
- **Asynchronous:** Python is asynchronous, meaning that it can do multiple things at once. It can be achieved by using the `asyncio` module.
    ```python
    import asyncio

    async def main():
        print('Hello')
        await asyncio.sleep(1)
        print('World')

    asyncio.run(main())
    ```
    it will print `Hello` and then after 1 second it will print `World`.

<br><br>

## 🖨️ Printing something
- To print something in Python, we use the `print()` function.

    ```python
    print("Hello, World!")
    ```

    Output:
    ```
    Hello, World!
    ```


