

# there are two types of XPath:
# 1. Absolute XPath: This is the full path to the element starting from the root of the document.
# It begins with a single slash (/) and follows the hierarchy of elements in the HTML document. 
# Example: /html/body/div[1]/div[2]/div[1]/input

# 2. Relative XPath: This is a more flexible way to locate elements.
# It starts with a double slash (//) and can be used to find elements anywhere in the document.
# It allows you to use various attributes and functions to identify elements.
# Example: //input[@id='username'] or //input[contains(@class, 'login')] or //button[text()='Login']
# Example of Absolute XPath: