number = 13.5055
"""
Using column justification and how it looks when numbers are included
"""
print("Text string".ljust(15),"|","{}".rjust(15,"*").format(number))

print("Text stringA".ljust(15),"|","{:.2f}".rjust(15,"*").format(number))

print("Text stringBB".ljust(15),"|","{:.2f}".rjust(15,"*").format(1/3))

"""
Using column justification and how it looks when numbers are included
and column width is adjusted
"""
print("Text string".ljust(15),"|","{}".rjust(10).format(number))

print("Text stringA".ljust(15),"|","{:.2f}".rjust(14).format(number))

print("Text stringBB".ljust(15),"|","{:.2f}".rjust(15).format(1/3))

"""
Using column justification for text,
and format for numbers
"""
print("Text string".ljust(15),"|","{:10}".format(number))

print("Text string".ljust(15),"|","{:10.2f}".format(number))

print("Text stringA".ljust(15),"|","{:10.2f}".format(number))

print("Text stringBB".ljust(15),"|","{:10.2f}".format(1/3))
