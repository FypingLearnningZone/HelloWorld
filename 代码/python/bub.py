def bubble_sort(a):
    for i in range(len(a)):
        for j in range(i + 1,len(a)):
            if a[i] > a[j]:
                a[i],a[j] = a[j],a[i]
    return a

l = list(range(10))
a = bubble_sort(l[::-1])