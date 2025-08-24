# User Input and Output in C++

## Generic skeleton of a C++ program:

```cpp
#include<iostream>

int main() {
    // Your code here
    return 0;
}
```

## Output in C++

```cpp
#include<iostream>

int main() {
    std::cout << "Hey, Aniruddha!";
    return 0;
}
```
This will print "Hey, Aniruddha!" on the console.

The `std` indicates that the `cout` function (from the iostream library) is a part of the standard namespace.

Use `\n` to add a new line. Low level operation, directly moves the cursor to the beginning of the next line in the output.

`endl` also inserts a newline character and flush the output buffer as well. Hence slower (can become costly if dealing with a large amount of text).


The `namespace std` can be used at the beginning of the signal to the compiler that all names being used are from the standard namespace. Cleans up your code. However, can be tricky for large codebases (naming conflicts!).

## Input in C++

```cpp
#include<iostream>

int main() {
    int x, y;

    std::cin >> x >> y;
    std::cout << "The value received as the first input is: " << x << std::endl;
    std::cout << "The value received as the second input is: " << y << std::endl;
    return 0;
}
```

Output:
```
~/Documents/code » g++ user-input-output.cpp -o user-input-output && user-input-output
10 20
The value received as the first input is: 10
The value received as the second input is: 20
```


> [!NOTE]
> `bits/stdc++.h` header is a shortcut that includes a vast number of standard C++ libraries. time-saving approach.


