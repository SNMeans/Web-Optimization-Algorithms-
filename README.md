# Web Optimization Algorithms 
## Introduction
This project involves implementing custom sorting and searching algorithms without relying on built-in Python functions. The focus is on understanding the efficiency of different algorithms, such as iterative sorts and recursive binary search, and their applications in real-world scenarios like database management and web development.
## Technologies Used
- Python 3
* Pytest for testing

## Features
- Iterative Sort: Implemented an  `O(n²)` sorting algorithm. This includes classic techniques like Bubble Sort, which, despite its simplicity, offers substantial learning insights into algorithm optimization.
* Recursive Binary Search: Implemented using recursion, showcasing an `O(log n)` search efficiency, ideal for sorted data arrays.
+ Application in Web Development: Integrated these algorithms into freelance projects to enhance features such as product sorting by popularity and price on e-commerce platforms

## Code Examples
```python
def iterative_sort(arr):
    # Implementation of an O(n^2) iterative sorting algorithm
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```
## How To Install And Run the Project
Clone the repository
```bash
git clone [https://github.com/SNMeans/Web-Optimization-Algorithms-/]
cd [Project-Directory]
```
Install Dependencies
``` bash
pip install pytest
```
Run tests
``` bash
pytest
```

## Real World Applications (Theoretical) 
- E-commerce Sorting Features: Use of sorting algorithms to arrange products by various metrics, enhancing user experience.
* Optimized Search in Databases: Implementing binary search on database queries to reduce the time complexity from  `O(n²)` to `O(log n)`  significantly improving performance.
+ Future Enhancements: Integrating more complex algorithms like quicksort for better efficiency in sorting, and using binary search to refine search features, enabling faster retrieval of user preferences and data.

## Conclusion + Implementation for a Mobile Coffee Shop Website
In addition to the theoretical and technical aspects of sorting and searching algorithms, I have successfully implemented these concepts in a practical, client-driven project. For a mobile coffee shop website, I applied the iterative sorting algorithm to sort coffee products by price and a custom algorithm based on popularity metrics to organize products dynamically on the website.

This implementation was particularly crucial in enhancing user experience, as it allowed customers to easily find and select products based on their preferences and past buyer trends. By integrating these algorithms:

- Sorting by Price: Using the iterative sort algorithm, I enabled the website to display products starting from the lowest to the highest price or vice versa, depending on the user's preference. This is crucial for budget-conscious buyers who are looking for the best deals.
* Sorting by Popularity: By developing a custom algorithm to sort products based on sales data and user ratings, the website now showcases the most popular products prominently, thereby increasing user engagement and potential sales.



